#!/usr/bin/env python3

#
# Copyright (C) 2022 by Yuri Astrakhan <YuriAstrakhan@gmail.com>.
# This code is licensed under the MIT license.
# The _make_iterencode() code is based on the Python JSON library's code.
#
# See https://github.com/nyurik/fatul for new versions and upgrade instructions.
#
# This utility converts Factorio blueprints to an alternative JSON representation
# that uses relative coordinates instead of entity_number values, and uses (x,y) sort.
# This minimizes changes between blueprint versions.

import argparse
import base64
import json
import re
import sys
import textwrap
import zlib
import hashlib
from dataclasses import dataclass
from itertools import groupby
from pathlib import Path
from traceback import format_exception
from typing import List, Any, Literal, NewType, Tuple, Dict, get_args, Union, Optional

try:
    # Optionally allow clipboard access
    import pyperclip
except ImportError:
    pyperclip = None

# Larger entities are more likely to stay in the same place, so boost their score penalty
ENTITY_SCORES = {
    "assembling-machine-1": 2,
    "assembling-machine-2": 2,
    "assembling-machine-3": 2,
    "beacon": 3,
    "centrifuge": 3,
    "chemical-plant": 3,
    "electric-furnace": 3,
    "lab": 3,
    "nuclear-reactor": 5,
    "oil-refinery": 5,
    "railway": 2,
    "roboport": 4,
    "rocket-silo": 9,
    "steam-engine": 4,
    "steam-turbine": 4,
    "steel-furnace": 2,
    "stone-furnace": 2,
    "substation": 2,
}

MAX_LINE_LENGTH = 100
COORD_MULTIPLIER = 16
SORT_ORDER = {
    "name": "0",
    "item": "1",
    "label": "2",
    "description": "3",
    "_simple": "8",  # other keys with simple values
    "_complex": "9",  # other keys with list and dict values
}
COMPLEX_TYPES = {dict, list}
NUMBER_TYPES = (int, float)
SPECIAL_REF_TYPES = {"locomotives", "wires", "stock_connections"}
IdsMode = Literal["refs", "mixed", "keep"]
SortMode = Literal["all", "entities", "keys", "none"]
Position = NewType("Position", Tuple[int, int])
EID = NewType("EID", int)
HistogramKey = NewType("HistogramKey", Union[int, Tuple[int, str]])
Histogram = NewType("Histogram", List[Tuple[HistogramKey, int]])


def main():
    # Top level
    parser = argparse.ArgumentParser(
        description="This tool helps to manage Factorio blueprints.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Decode
    decoder = subparsers.add_parser(
        "decode", aliases=["d"], formatter_class=argparse.RawTextHelpFormatter,
        help="Decode a blueprint from clipboard, a file, or stdin")
    decoder.set_defaults(func=decode_cmd)
    decoder.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    decoder.add_argument("--ids", choices=get_args(IdsMode), default="refs",
                         help=textwrap.dedent("""\
                         How to process the entity_number and entity_id values - '%(default)s' by default
                            * refs  - convert entity_id values to relative references.
                                      Set neighbours to the delta x,y relative to the current entity.
                                      Set schedules.locomotives to the absolute x,y of their position.
                                      Set schedules.wires to the absolute x,y of their entity position.
                                      Set schedules.stock_connections to the absolute x,y of their entity position.
                                      The original entity_id and entity_number values will be removed.
                            * mixed - Same as refs, but do not delete original entity_id values.
                            * keep  - Do not convert entity_id values."""))
    decoder.add_argument("--sort", choices=get_args(SortMode), default="all",
                         help=textwrap.dedent("""\
                         Order keys and entities in the output. (default = '%(default)s').
                            * all      - apply all sorting rules.
                            * entities - sort entities by their position, trying to keep nearby entities together.
                            * keys     - sort object keys alphabetically, moving 'name' to the top.
                            * none     - do not sort."""))
    decoder.add_argument("--pretty", "-p", dest="compact", default=True, action="store_false",
                         help="Use standard JSON formatting instead of compact")
    decoder.add_argument("--no-shift", dest="normalize_shift", default=True, action="store_false",
                         help="Do not change entity positions. If not set, FaTul will attempt to normalize x,y values.")
    decoder.add_argument("--no-index-merge", dest="merge_index", default=True, action="store_false",
                         help="If the output file already exists and contains a book index, and the current data "
                              "does not, do not copy old index to the new file")
    decoder.add_argument("--no-shift-merge", dest="merge_shift", default=True, action="store_false",
                         help="If the output file already exists, do not try to shift the new entities "
                              "to fit the location of the old ones")
    decoder.add_argument("--shift-x", dest="shift_x", type=int, help="Override shift_x value")
    decoder.add_argument("--shift-y", dest="shift_y", type=int, help="Override shift_y value")
    decoder.add_argument("destination", type=Path,
                         help="The destination file or directory to write to. "
                              "Use '-' to write to STDOUT as a single formatted JSON.")
    decoder.add_argument("source", type=Path, nargs="?",
                         help="Optional source file with the Factorio blueprint string. "
                              "Uses clipboard if not specified. Use '-' to read from STDIN.")

    # Dump
    dumper = subparsers.add_parser(
        "dump", formatter_class=argparse.RawTextHelpFormatter,
        help="Decode a blueprint from clipboard, a file, or stdin without any additional processing. "
             "This is identical to   decode --ids=keep --sort=none")
    dumper.set_defaults(func=dump_cmd)
    dumper.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    dumper.add_argument("--pretty", "-p", dest="compact", default=True, action="store_false",
                        help="Use standard JSON formatting instead of compact")
    dumper.add_argument("--sort", "-s", dest="sort", default=False, action="store_true",
                        help="Sort output by keys")
    dumper.add_argument("destination", type=Path,
                        help="The destination file or directory to write to. "
                             "Use '-' to write to STDOUT as a single formatted JSON.")
    dumper.add_argument("source", type=Path, nargs="?",
                        help="Optional source file with the Factorio blueprint string. "
                             "Uses clipboard if not specified. Use '-' to read from STDIN.")

    # Encode
    encoder = subparsers.add_parser(
        "encode", aliases=["e"],
        help="Encode a blueprint from a file, directory, or stdin")
    encoder.set_defaults(func=encode_cmd)
    encoder.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    encoder.add_argument("source", type=Path,
                         help="A JSON file or a directory with JSON files to encode. Only *.json files are processed.")
    encoder.add_argument("destination", type=Path, nargs="?",
                         help="The destination file to write to. By default, the result "
                              "is copied to clipboard. Use '-' to write to STDOUT.")

    args = parser.parse_args()
    if args is None:
        parser.print_help(file=sys.stderr)
    else:
        try:
            args.func(args)
        except Exception as ex:
            message = str(ex)
            if args.verbose or message == "":
                message += "\n\n" + "".join(format_exception(type(ex), ex, ex.__traceback__))
            parser.error(message)


def dump_cmd(args: argparse.Namespace):
    decode(args.source, args.destination, args.verbose, args.compact, sort_mode='keys' if args.sort else 'none')


def decode_cmd(args: argparse.Namespace):
    decode(args.source, args.destination, args.verbose, args.compact, args.sort, args.ids,
           args.normalize_shift, args.merge_index, args.merge_shift, args.shift_x, args.shift_y)


def decode(source: Path, destination: Path, verbose: bool, compact: bool,
           sort_mode: SortMode = "none", ids_mode: IdsMode = "keep", normalize_shift=False, merge_index=False,
           merge_shift=False, override_shift_x: int = None, override_shift_y: int = None) -> None:
    if source is None:
        assert_clipboard()
        eprint("Reading blueprint string from clipboard")
        json_text = pyperclip.paste()
    elif str(source) == "-":
        eprint("Reading blueprint string from STDIN")
        json_text = "".join(sys.stdin.readlines())
    else:
        if not source.is_file():
            raise ValueError(f"Source file does not exist, or it is not a file: {source}")
        eprint(f"Reading blueprint string from {source}")
        json_text = source.read_text(encoding="utf8")
    processor = Processor(verbose, sort_mode, ids_mode, normalize_shift, compact, merge_index, merge_shift,
                          (override_shift_x, override_shift_y))
    data = processor.decode(json_text)
    if str(destination) == "-":
        print(to_pretty_json(data, compact))
    else:
        processor.write_files(data, destination)


def encode_cmd(args: argparse.Namespace):
    if str(args.source) == "-":
        eprint("Reading json from STDIN")
        data = json.loads("".join(sys.stdin.readlines()))
    elif args.source.is_file():
        eprint(f"Reading a json file from {args.source}")
        data = json.loads(args.source.read_text(encoding="utf8"))
    elif args.source.is_dir():
        eprint(f"Reading json files from directory {args.source}")
        data = read_files(args.source, args.verbose)
    else:
        raise ValueError(f"Invalid source file or directory: {args.source}")
    processor = Processor(args.verbose)
    encoded = processor.encode(data)
    if args.destination is None:
        assert_clipboard()
        pyperclip.copy(encoded)
        eprint(f"Encoded blueprint string was copied to clipboard.")
    elif str(args.destination) == "-":
        print(encoded)
    else:
        eprint(f"Writing to {args.destination}")
        args.destination.write_text(encoded, "utf8")


def get_non_index_key(data):
    keys = set(data.keys())
    keys.discard("index")
    if len(keys) != 1:
        raise ValueError(f"Expected a single sub-entry in the input data, found: {','.join(keys)}")
    return keys.pop()


def read_files(dir_path: Path, verbose: bool) -> dict:
    # Recursively reads a directory of JSON files and returns a dict with the blueprint book
    metadata_path = dir_path / "_metadata.json"
    if not metadata_path.is_file():
        raise ValueError(f"Missing metadata file: {metadata_path}")
    data = json.loads(metadata_path.read_text(encoding="utf8"))
    assert type(data) == dict
    blueprints = []
    key = get_non_index_key(data)
    # Factorio orders blueprints before the rest of the keys
    data[key] = {"blueprints": blueprints, **data[key]}
    for path in dir_path.iterdir():
        if path.is_dir():
            blueprints.append(read_files(path, verbose))
        elif path.is_file():
            if path.suffix != ".json":
                eprint(f"Ignoring non-json file: {path}")
                continue
            if path.name == "_metadata.json":
                continue
            if verbose:
                eprint(f"Loading {path}")
            blueprints.append(json.loads(path.read_text(encoding="utf8")))
        else:
            eprint(f"Skipping unrecognized {path}")
    blueprints.sort(key=lambda v: v.get("index", 0))
    return data


def assert_clipboard():
    if pyperclip is None:
        raise ValueError("pyperclip library is required to use clipboard.\n"
                         "Install it with:   pip3 install pyperclip\n"
                         "See https://github.com/nyurik/fatul#readme")


@dataclass
class PosEntity:
    pos: Position
    entity: dict
    hash: Optional[str] = None


class Processor:
    def __init__(self, verbose: bool, sort_mode: SortMode = "none", ids_mode: IdsMode = "keep", normalize_shift=False,
                 compact=False, merge_index=False, merge_shift=False, override_shift=None):
        self.verbose = verbose
        self.normalize_shift = normalize_shift
        self.disable_shift = False
        self.sort_keys = sort_mode == "all" or sort_mode == "keys"
        self.sort_entities = sort_mode == "all" or sort_mode == "entities"
        self.remove_entity_number = ids_mode == "refs"
        self.use_rel_ids = ids_mode != "keep"
        self.compact = compact
        self.merge_index = merge_index
        self.merge_shift = merge_shift
        self.override_shift = (None, None) if override_shift is None else override_shift

    def decode(self, json_text: str) -> dict:
        if not json_text.startswith("0"):
            raise ValueError("Invalid blueprint string. It must start with a 0.")
        data = json.loads(zlib.decompress(base64.b64decode(json_text[1:])).decode("utf8"))
        self.process_ids(data, to_abs_ids=False)
        if self.sort_keys:
            sort_dicts_rec(data)
        return data

    def encode(self, data: dict) -> str:
        # if this was part of a blueprint book, get rid of the index in the output
        # the index will be re-added by migrate_old_data() when decoding into the same file
        data.pop("index", None)
        self.disable_shift = True
        self.process_ids(data, to_abs_ids=True)
        compressed = zlib.compress(bytes(to_json(data), "utf8"), level=9)
        return "0" + base64.b64encode(compressed).decode("utf8")

    def process_ids(self, data: dict, to_abs_ids: bool):
        if type(data) != dict or len(data) != 1:
            raise ValueError("Invalid blueprint string. It must contain exactly one object.")
        if self.verbose:
            eprint(f"Processing {get_label(data)}")
        self._process_ids_rec(data, to_abs_ids)

    def _process_ids_rec(self, data: Any, to_abs_ids: bool) -> None:
        if type(data) == dict:
            if "blueprint" in data:
                bp = Blueprint(self, data, to_abs_ids)
                if to_abs_ids:
                    bp.create_new_entity_numbers()
                else:
                    bp.cache_entity_numbers()
                bp.update_references()
                if self.remove_entity_number:
                    bp.delete_entity_numbers()
                if self.disable_shift:
                    bp.set_shift(None)
                elif self.normalize_shift:
                    bp.shift_by_usage()
            else:
                for key, val in data.items():
                    if type(val) in COMPLEX_TYPES:
                        self._process_ids_rec(val, to_abs_ids)
        elif type(data) == list:
            for idx, val in enumerate(data):
                if type(val) in COMPLEX_TYPES:
                    self._process_ids_rec(val, to_abs_ids)

    def write_files(self, data: dict, dest: Path) -> None:
        # We are "loading" now
        label = get_label(data)
        if "blueprint_book" not in data:
            dest = dest.with_suffix(".json")
            eprint(f"Writing {label} to {dest}")
            self.write_single_file(data, dest)
            return
        if dest.is_file() or dest.suffix == ".json":
            eprint(f"WARNING: Destination "
                   f"{'already exists' if dest.is_file() else 'has a .json extension, treating it as a file'}. "
                   f"Saving entire blueprint book as a single file to {dest}")
            self.write_single_file(data, dest)
            return
        eprint(f"Creating {label} {dest}")
        dest.mkdir(parents=True, exist_ok=True)
        book = data["blueprint_book"]
        blueprints = book.pop("blueprints", [])
        (dest / "_metadata.json").write_text(to_pretty_json(data, self.compact) + "\n", "utf8")
        files = set()
        for bp in blueprints:
            is_dir = "blueprint_book" in bp
            name = get_label(bp).lower()
            name = re.sub(r"[/\\.:&|]+", "-", name)
            name = re.sub(r"  +", " ", name)
            name = name.replace(" ", "-")
            name = re.sub(r"-+", "-", name)
            name = name.strip("_-. ")
            if name in files:
                copy = 2
                while True:
                    test_name = f"{name}{'_' if is_dir else ' '}({copy})"
                    if test_name not in files:
                        name = test_name
                        break
                    copy += 1
            files.add(name)
            self.write_files(bp, dest / name)

    def write_single_file(self, data: dict, dest: Path) -> None:
        if dest.exists():
            self.migrate_old_data(data, dest)
        dest.write_text(to_pretty_json(data, self.compact) + "\n", "utf8")

    def migrate_old_data(self, new_data: dict, dest: Path) -> None:
        msg = f"Overwriting {dest} with new data"
        old_data = None
        if self.merge_index or self.merge_shift:
            old_data = json.loads(dest.read_text(encoding="utf8"))
        if self.merge_index and "index" not in new_data:
            index = old_data.get("index", None)
            if index is not None:
                new_data["index"] = index
                msg += f", index restored to {index}"
        if self.merge_shift:
            old_data_type = get_non_index_key(old_data)
            new_data_type = get_non_index_key(new_data)
            if old_data_type != new_data_type:
                msg += f", changing type {old_data_type} → {new_data_type}"
                eprint(msg)
                return
            if old_data_type == "blueprint":
                old_bp = Blueprint(self, old_data, False)
                new_bp = Blueprint(self, new_data, False)
                msg += ", " + new_bp.merge_shift_from_old(old_bp)
        if self.verbose:
            eprint(msg)


class IdEncoder:
    def __init__(self, label, to_abs_ids, use_rel_ids):
        self.label = label
        self.to_abs_ids = to_abs_ids
        self.use_rel_ids = use_rel_ids
        self.entity_ids: Dict[EID, PosEntity] = {}
        self.position_to_entity_ids: Dict[Position, List[EID]] = {}
        self.new_id = EID(1)
        self.min_x: Optional[int] = None
        self.min_y: Optional[int] = None

    def save_entity_info(self, entity_data: dict) -> None:
        eid = entity_data["entity_number"]
        if eid < 1:
            raise ValueError(f"Invalid entity_number {eid} in {self.label}:\n" + to_json(entity_data))
        if eid in self.entity_ids:
            raise ValueError(f"Duplicate entity_number {eid} in {self.label}:\n" + to_json(entity_data))
        position = entity_data.get("position")
        if position is None:
            raise ValueError(f"Missing position in {self.label}:\n" + to_json(entity_data))
        x, y = position.get("x"), position.get("y")
        if type(x) not in NUMBER_TYPES or type(y) not in NUMBER_TYPES:
            raise ValueError(
                f"Unrecognized position object {to_json(position)} in {self.label}:\n" + to_json(entity_data))
        pos = Position((coord_to_int(x), coord_to_int(y)))
        if self.min_x is None or self.min_x > pos[0]:
            self.min_x = pos[0]
        if self.min_y is None or self.min_y > pos[1]:
            self.min_y = pos[1]
        self.entity_ids[eid] = PosEntity(pos, entity_data)
        ids = self.position_to_entity_ids.get(pos)
        if ids is None:
            self.position_to_entity_ids[pos] = [eid]
        else:
            ids.append(eid)
            for eid in ids:
                pos_entity = self.entity_ids[eid]
                if pos_entity.hash is None:
                    new_hash = get_obj_hash(pos_entity.entity)
                    if any((True for v in ids if self.entity_ids[v].hash == hash)):
                        raise ValueError(f"Duplicate hash {new_hash} in {self.label}:\n" + to_json(entity_data))
                    pos_entity.hash = new_hash

    def update_rel_ids(self, entity_number: EID, data: Any, parent_key: str = None) -> None:
        if type(data) == dict:
            for key, val in data.items():
                self.update_rel_ids(entity_number, val, key)
            entity_id = data.get("entity_id")
            rel_id = data.get("entity_rel")
            if entity_id is not None:
                if rel_id is not None:
                    raise ValueError(f"Cannot have both entity_id and entity_rel in {entity_number}")
                # Validate referenced entity_id, even if we don"t use it
                rel_id = self._make_rel_id(entity_number, entity_id)
                if self.use_rel_ids:
                    del data["entity_id"]
                    data["entity_rel"] = rel_id
            elif rel_id is not None:
                entity_id = self._parse_rel_id(entity_number, rel_id)
                if not self.use_rel_ids:
                    del data["entity_rel"]
                    data["entity_id"] = entity_id
        elif type(data) == list:
            if len(data) == 0 or parent_key != "neighbours":
                for val in data:
                    self.update_rel_ids(entity_number, val)
                return
            self.update_ref_list(data, entity_number, parent_key)

    def update_ref_list(self, data, entity_number, typ):
        list_is_int = all(type(v) == int for v in data)
        list_is_str = all(type(v) == str for v in data)
        if not list_is_str and not list_is_int:
            raise ValueError(f"Invalid {typ} list {entity_number}: all values must be either ints or strs")
        if not self.to_abs_ids and not list_is_int:
            raise ValueError(f"Invalid {typ} list {entity_number} - all values must be ints")
        if self.use_rel_ids != list_is_str:
            # Convert entity IDs to relative IDs or vice versa
            old_list = data.copy()
            data.clear()
            for val in old_list:
                if self.use_rel_ids:
                    data.append(self._make_rel_id(entity_number, val, typ))
                else:
                    data.append(self._parse_rel_id(entity_number, val, typ))

    def update_wires_list(self, data, entity_number, typ):
        if len(data) != 4:
            raise ValueError(f"Invalid {typ} list {entity_number}: must have 4 values")
        if type(data[1]) != int or type(data[3]) != int:
            raise ValueError(
                f"Invalid {typ} list {entity_number}: values 2 and 4 must be ints (e.g. 1=red, 2=green, 5=copper)")
        list_is_int = type(data[0]) == int and type(data[2]) == int
        list_is_str = type(data[0]) == str and type(data[2]) == str
        if not list_is_str and not list_is_int:
            raise ValueError(
                f"Invalid {typ} list {entity_number}: source/destination values must be either ints or strs")
        if not self.to_abs_ids and not list_is_int:
            raise ValueError(f"Invalid {typ} list {entity_number} - source/destination values must be ints")
        if self.use_rel_ids != list_is_str:
            # Convert entity IDs to relative IDs or vice versa
            old_list = data.copy()
            data.clear()
            for idx, val in enumerate(old_list):
                if idx % 2 == 0:
                    if self.use_rel_ids:
                        data.append(self._make_rel_id(entity_number, val, typ))
                    else:
                        data.append(self._parse_rel_id(entity_number, val, typ))
                else:
                    data.append(val)

    def update_obj_values(self, data: dict, entity_number, typ):
        list_is_int = all(type(v) == int for v in data.values())
        list_is_str = all(type(v) == str for v in data.values())
        if not list_is_str and not list_is_int:
            raise ValueError(f"Invalid {typ} object {entity_number}: all values must be either ints or strs")
        if not self.to_abs_ids and not list_is_int:
            raise ValueError(f"Invalid {typ} object {entity_number} - all values must be ints")
        if self.use_rel_ids != list_is_str:
            # Convert entity IDs to relative IDs or vice versa
            for key in data.keys():
                if self.use_rel_ids:
                    data[key] = self._make_rel_id(entity_number, data[key], typ)
                else:
                    data[key] = self._parse_rel_id(entity_number, data[key], typ)

    def _make_rel_id(self, from_entity_number: EID, to_entity_id: EID, typ: Optional[str] = None) -> str:
        """Convert an absolute entity ID to a relative ID.
           from_entity_number is the ID of the current entity,
           unless typ is one of the SPECIAL_REF_TYPES, in which case it is just a debug string."""
        assert type(to_entity_id) == int
        if not typ in SPECIAL_REF_TYPES:
            from_entity = self.entity_ids[from_entity_number]
            from_x, from_y = from_entity.pos
        else:
            from_entity = None
            from_x, from_y = self.min_x, self.min_y
        to_entity = self.entity_ids.get(to_entity_id)
        if to_entity is None:
            extra = ":\n" + to_json(from_entity.entity) if from_entity is not None else f" in {from_entity_number}"
            raise ValueError(f"Unrecognized entity ID {to_entity_id} in {self.label}{extra}")
        x_diff = int_to_coord(to_entity.pos[0] - from_x)
        y_diff = int_to_coord(to_entity.pos[1] - from_y)
        result = f"{x_diff},{y_diff}"
        if to_entity.hash is not None:
            result += f",{to_entity.hash}"
        return result

    def _parse_rel_id(self, entity_number: EID, rel_id: str, typ: Optional[str] = None) -> EID:
        """Convert a relative entity value to an entity ID.
           entity_number is the ID of the current entity,
           unless typ is one of the SPECIAL_REF_TYPES, in which case it is just a debug string."""
        assert type(rel_id) == str
        if not typ in SPECIAL_REF_TYPES:
            pe = self.entity_ids[entity_number]
            from_x, from_y = pe.pos
        else:
            pe = None
            from_x, from_y = self.min_x, self.min_y
        rel_parts = rel_id.split(",", 3)
        if len(rel_parts) < 2 or len(rel_parts) > 3:
            extra = ":\n" + to_json(pe.entity) if pe is not None else f" in {entity_number}"
            raise ValueError(f"Unrecognized relative ID {rel_id} in {self.label}{extra}")
        pos = Position((from_x + coord_to_int(float(rel_parts[0])),
                        from_y + coord_to_int(float(rel_parts[1]))))
        ids = self.position_to_entity_ids.get(pos)
        if ids is None:
            extra = ":\n" + to_json(pe.entity) if pe is not None else f" in {entity_number}"
            raise ValueError(
                f"No entities found for relative ID {rel_id} ({pos[0], pos[1]}) in {self.label}{extra}")
        if len(ids) == 1:
            if len(rel_parts) == 3:
                eprint(f"Warning: ignoring hash {rel_parts[2]} in {self.label}")
            return ids[0]
        if len(rel_parts) == 2:
            raise ValueError(
                f"Ambiguous relative ID {rel_id} must have had a hash in {self.label}:\n{to_json(pe.entity)}")
        ids = [v for v in ids if self.entity_ids[v].hash == rel_parts[2]]
        if len(ids) == 0:
            raise ValueError(f"Hash for relative ID {rel_id} not found in {self.label}:\n{to_json(pe.entity)}")
        return ids[0]

    def set_new_entity_id(self, entity_data: dict) -> None:
        assert "entity_number" not in entity_data
        while self.new_id in self.entity_ids:
            self.new_id += 1
        # Entity number is created as a first key by Factorio, keep it consistent
        tmp = entity_data.copy()
        entity_data.clear()
        entity_data["entity_number"] = self.new_id
        entity_data.update(tmp)
        self.new_id += 1


class Blueprint:
    def __init__(self, processor: Processor, data: dict, to_abs_ids: bool):
        self.sort_entities = processor.sort_entities
        self.override_shift = processor.override_shift
        self.blueprint = data["blueprint"]
        self.label = get_label(data)
        self.entities = self.blueprint.get("entities", [])
        self.ids = IdEncoder(self.label, to_abs_ids, processor.use_rel_ids)

    def cache_entity_numbers(self) -> None:
        for idx, entity_data in enumerate(self.entities):
            if "entity_number" not in entity_data:
                raise ValueError(f"Missing entity_number in {self.label}:\n" + to_json(entity_data))
            self.ids.save_entity_info(entity_data)

    def create_new_entity_numbers(self) -> None:
        missing_ids = []
        for idx, entity_data in enumerate(self.entities):
            if "entity_number" not in entity_data:
                missing_ids.append(idx)
            else:
                self.ids.save_entity_info(entity_data)
        for idx in missing_ids:
            self.ids.set_new_entity_id(self.entities[idx])
            self.ids.save_entity_info(self.entities[idx])

    def delete_entity_numbers(self):
        for entity_data in self.entities:
            del entity_data["entity_number"]

    def update_references(self):
        # Recursively switch between entity_id and entity_rel (relative position)
        for entity_data in self.entities:
            self.ids.update_rel_ids(entity_data["entity_number"], entity_data)
        for idx, locomotive in enumerate(self.blueprint.get("schedules", [])):
            self.ids.update_ref_list(locomotive["locomotives"], f"schedule[{idx}]", "locomotives")
        for idx, wires in enumerate(self.blueprint.get("wires", [])):
            self.ids.update_wires_list(wires, f"wires[{idx}]", "wires")
        for idx, conn in enumerate(self.blueprint.get("stock_connections", [])):
            self.ids.update_obj_values(conn, f"stock_connections[{idx}]", "stock_connections")

    def shift_by_usage(self):
        hist_x = self.calc_histogram("x", by_name=False)
        shift_x = self.calc_coordinate_shift(hist_x)
        hist_y = self.calc_histogram("y", by_name=False)
        shift_y = self.calc_coordinate_shift(hist_y)
        self.set_shift((shift_x, shift_y))

    def merge_shift_from_old(self, old_bp: "Blueprint") -> str:
        if not old_bp.entities:
            return "shift is unchanged because old blueprint has no entities"
        if not self.entities:
            return "shift is unchanged because new blueprint has no entities"
        old_hist_x = old_bp.calc_histogram("x", by_name=True)
        new_hist_x = self.calc_histogram("x", by_name=True)
        shift_x = self.calc_histogram_diff(old_hist_x, new_hist_x)
        old_hist_y = old_bp.calc_histogram("y", by_name=True)
        new_hist_y = self.calc_histogram("y", by_name=True)
        shift_y = self.calc_histogram_diff(old_hist_y, new_hist_y)
        if shift_x == 0 and shift_y == 0:
            return "entities were not shifted"
        else:
            self.set_shift((shift_x, shift_y))
            return f"entities shifted by x={shift_x}, y={shift_y}"

    def set_shift(self, adjust_by: Optional[Tuple[int, int]]) -> None:
        shift_x = self.blueprint.get("shift_x", 0)
        shift_y = self.blueprint.get("shift_y", 0)
        if adjust_by is None:
            target_x, target_y = 0, 0
        else:
            if self.override_shift[0] is not None:
                target_x = self.override_shift[0]
            else:
                target_x = shift_x + adjust_by[0]
            if self.override_shift[1] is not None:
                target_y = self.override_shift[1]
            else:
                target_y = shift_y + adjust_by[1]
        adjust_x = shift_x - target_x
        adjust_y = shift_y - target_y
        if adjust_x != 0 or adjust_y != 0:
            for entity in self.entities:
                position = entity["position"]
                position["x"] += adjust_x
                position["y"] += adjust_y
        if adjust_by is None or (target_x == 0 and target_y == 0):
            self.blueprint.pop("shift_x", None)
            self.blueprint.pop("shift_y", None)
        else:
            self.blueprint["shift_x"] = target_x
            self.blueprint["shift_y"] = target_y
        if self.sort_entities:
            self.entities.sort(key=entity_sort_key)

    @staticmethod
    def calc_coordinate_shift(histogram: Histogram) -> int:
        """Find the most "stable" value for the x or y position coordinate.
        First creates a histogram of all values, looks at the first 20%,
        and finds the biggest "jump", i.e. from 2,1,4,34,... -- the 34 would be it."""
        if not histogram:
            return 0
        min_entities = min((v[1] for v in histogram))
        max_entities = max((v[1] for v in histogram))
        threshold = min_entities + (max_entities - min_entities) / 4
        # Find first row/column which increases the number of entities by more than threshold
        return next((histogram[i] for i in range(len(histogram))
                     if (histogram[i][1] - (histogram[i - 1][1] if i > 0 else 0)) > threshold),
                    histogram[0])[0]

    def calc_histogram_diff(self, old_hist: Histogram, new_hist: Histogram) -> int:
        old_min = old_hist[0][0][0]
        old_max = old_hist[-1][0][0]
        new_min = new_hist[0][0][0]
        new_max = new_hist[-1][0][0]
        old_range = old_max - old_min + 1
        new_range = new_max - new_min + 1
        overlap_size = min(old_range, new_range) // 2
        if new_range > old_range:
            shift_range = range(old_max - new_max - overlap_size, old_min - new_min + overlap_size)
        else:
            shift_range = range(old_min - new_min - overlap_size, old_max - new_max + overlap_size)
        diffs = []
        for shift in shift_range:
            diffs.append((shift, self.calc_diff_score(old_hist, new_hist, shift)))
        res = -min(diffs, key=lambda x: x[1])[0]
        return res

    @staticmethod
    def calc_diff_score(old_hist: Histogram, new_hist: Histogram, shift: int) -> int:
        score = 0
        old_idx, new_idx = 0, 0
        while True:
            if old_idx < len(old_hist) and new_idx < len(new_hist):
                old_val = old_hist[old_idx]
                new_val = (new_hist[new_idx][0][0] + shift, new_hist[new_idx][0][1]), new_hist[new_idx][1]
                if old_val[0] == new_val[0]:
                    diff = abs(old_val[1] - new_val[1])
                    if diff == 0:
                        # Boost score when the number of entities of the same type and index is identical
                        score -= 0
                    else:
                        # Mismatching of larger entities get heavier score penalty
                        multiplier = ENTITY_SCORES.get(old_val[0][1], 1)
                        score += diff * multiplier
                    old_idx += 1
                    new_idx += 1
                elif old_val[0] < new_val[0]:
                    score += old_val[1]
                    old_idx += 1
                else:
                    score += new_val[1]
                    new_idx += 1
                continue
            if old_idx < len(old_hist):
                score += sum((v[1] for v in old_hist[old_idx:]))
            else:
                score += sum((v[1] for v in new_hist[new_idx:]))
            return score

    def calc_histogram(self, by_x_or_y: str, by_name: bool) -> Histogram:
        if by_name:
            values = ((int(v["position"][by_x_or_y]), v["name"]) for v in self.entities)
        else:
            values = (int(v["position"][by_x_or_y]) for v in self.entities)
        res = [(k, sum(1 for _ in v)) for k, v in groupby(sorted(values))]
        res.sort(key=lambda v: v[0])
        return Histogram(res)


def sort_dicts_rec(data: Any, parent: Optional[str] = None) -> None:
    if type(data) == dict:
        for key, val in data.items():
            sort_dicts_rec(val, key)
        sort_dict(data)
    elif type(data) == list:
        has_entity_rel = True
        for val in data:
            has_entity_rel = has_entity_rel and type(val) == dict and "entity_rel" in val
            sort_dicts_rec(val)
        if has_entity_rel:
            data.sort(key=lambda v: list(v.items()))
        elif parent == "neighbours":
            data.sort()


def sort_dict(data) -> None:
    """Sort dict in place.
    Order first by group (prefix) followed by the key name alphabetically.
    Put special keys like 'name' first, then simple values (strings/ints/...) then dicts/lists."""

    def _key_sorter(key: str):
        prefix = SORT_ORDER.get(key)
        if prefix is None:
            prefix = SORT_ORDER["_complex" if type(old_data[key]) in COMPLEX_TYPES else "_simple"]
        return prefix + key

    # Since Python 3.7+, dict key insertion order is officially preserved
    old_data = data.copy()
    data.clear()
    for k in sorted(old_data.keys(), key=_key_sorter):
        data[k] = old_data[k]


def entity_sort_key(entity: dict):
    """Sort blueprint entities by their combined x,y position"""
    position = entity["position"]
    return entity["name"], to_morton_number(position["x"], position["y"])


def to_morton_number(x, y) -> int:
    # Create a single interleaved number (Morton number) to use as a sorting key.
    # This approach tries to keep features that are nearby in the X,Y plane near each other in a list.
    # Adapted from http://graphics.stanford.edu/~seander/bithacks.html#InterleaveBMN
    def prepare_number(val):
        # Normalize to an unsigned 16 bit value
        val = min(max(coord_to_int(val) + (2 ** 15), 0), 2 ** 16 - 1)
        for shift, mask in [(8, 0x00FF00FF), (4, 0x0F0F0F0F), (2, 0x33333333), (1, 0x55555555)]:
            val = (val | (val << shift)) & mask
        return val

    return prepare_number(x) | (prepare_number(y) << 1)


def coord_to_int(val) -> int:
    res = round(val * COORD_MULTIPLIER)
    return res


def int_to_coord(val: int) -> Union[float, int]:
    res = float(val) / float(COORD_MULTIPLIER)
    return int(res) if res.is_integer() else res


def get_label(data: dict) -> str:
    key = get_non_index_key(data)
    label = data[key].get("label")
    if label is None:
        label = data[key].get("item", key)
    return label


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_obj_hash(obj: Any) -> str:
    """get a short string hash of the object, ignoring unstable values like entity IDs"""

    def _rm_volatile(o: Any):
        if type(o) == dict:
            for k, v in list(o.items()):
                if k in ("connections", "position", "entity_id", "entity_number", "entity_rel", "neighbours"):
                    del o[k]
                else:
                    _rm_volatile(v)
        elif type(o) == list:
            for v in o:
                _rm_volatile(v)

    # deep clone the object and remove values that are not likely to stay the same
    obj = json.loads(json.dumps(obj))
    _rm_volatile(obj)
    # sort the object to ensure the hash is stable
    sort_dicts_rec(obj)
    return hashlib.md5(to_json(obj).encode("utf8")).hexdigest()[:4]


def to_json(data):
    return json.dumps(data, ensure_ascii=False, allow_nan=False, separators=(",", ":"))


def to_pretty_json(data, compact=True):
    if compact:
        return "".join(_make_iterencode()(data, 0))
    else:
        return json.dumps(data, ensure_ascii=False, allow_nan=False, indent=2)


def _make_iterencode():
    """This is a slightly modified version of the _make_iterencode function from the Python's core json module.
    It is modified to allow for a one-liner output for complex objects, if the objects are small enough."""

    # The _encoder is used for simple values (str, int, float) and to test the length of a complex one-line value.
    _encoder = json.JSONEncoder(ensure_ascii=False, check_circular=False, allow_nan=False,
                                separators=(", ", ": ")).encode
    _indent = " " * 2
    _item_separator = ","
    _key_separator = ": "

    def _encode_one_line(o):
        """Encode complex object using standard JSON encoder without line breaks,
        and test if the result is short enough."""
        # Possible optimization: estimate the result size by recursively adding string lengths and breaking early
        res = _encoder(o)
        return res if len(res) <= MAX_LINE_LENGTH else None

    def _iterencode_list(lst, _current_indent_level):
        if not lst:
            yield "[]"
            return
        buf = _encode_one_line(lst)
        if buf is not None:
            yield buf
            return
        _current_indent_level += 1
        newline_indent = "\n" + _indent * _current_indent_level
        separator = _item_separator + newline_indent
        buf = "[" + newline_indent
        first = True
        for value in lst:
            if first:
                first = False
            else:
                buf = separator
            if isinstance(value, str):
                yield buf + _encoder(value)
            elif value is None:
                yield buf + "null"
            elif value is True:
                yield buf + "true"
            elif value is False:
                yield buf + "false"
            elif isinstance(value, int):
                yield buf + _encoder(value)
            elif isinstance(value, float):
                yield buf + _encoder(value)
            else:
                yield buf
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value, _current_indent_level)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value, _current_indent_level)
                else:
                    chunks = _iterencode(value, _current_indent_level)
                yield from chunks
        _current_indent_level -= 1
        yield "\n" + _indent * _current_indent_level + "]"

    def _iterencode_dict(dct, _current_indent_level):
        if not dct:
            yield "{}"
            return
        buf = _encode_one_line(dct)
        if buf is not None:
            yield buf
            return
        _current_indent_level += 1
        newline_indent = "\n" + _indent * _current_indent_level
        item_separator = _item_separator + newline_indent
        yield "{" + newline_indent
        first = True
        for key, value in dct.items():
            if isinstance(key, str):
                pass
            elif isinstance(key, float):
                key = _encoder(key)
            elif key is True:
                key = "true"
            elif key is False:
                key = "false"
            elif key is None:
                key = "null"
            elif isinstance(key, int):
                key = _encoder(key)
            else:
                raise TypeError(f"keys must be str, int, float, bool or None, "
                                f"not {key.__class__.__name__}")
            if first:
                first = False
            else:
                yield item_separator
            yield _encoder(key)
            yield _key_separator
            if isinstance(value, str):
                yield _encoder(value)
            elif value is None:
                yield "null"
            elif value is True:
                yield "true"
            elif value is False:
                yield "false"
            elif isinstance(value, int):
                yield _encoder(value)
            elif isinstance(value, float):
                yield _encoder(value)
            else:
                if isinstance(value, (list, tuple)):
                    chunks = _iterencode_list(value, _current_indent_level)
                elif isinstance(value, dict):
                    chunks = _iterencode_dict(value, _current_indent_level)
                else:
                    chunks = _iterencode(value, _current_indent_level)
                yield from chunks
        _current_indent_level -= 1
        yield "\n" + _indent * _current_indent_level + "}"

    def _iterencode(o, _current_indent_level):
        if isinstance(o, str):
            yield _encoder(o)
        elif o is None:
            yield "null"
        elif o is True:
            yield "true"
        elif o is False:
            yield "false"
        elif isinstance(o, int):
            yield _encoder(o)
        elif isinstance(o, float):
            yield _encoder(o)
        elif isinstance(o, (list, tuple)):
            yield from _iterencode_list(o, _current_indent_level)
        elif isinstance(o, dict):
            yield from _iterencode_dict(o, _current_indent_level)
        else:
            raise TypeError(f"Object of type {o.__class__.__name__} "
                            f"is not JSON serializable")

    return _iterencode


if __name__ == "__main__":
    main()
