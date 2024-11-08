The biggest (and probably most bloated) rail book out there, updated for 2.0.
For I'm focusing on updating it with the new features. I'll make a showcase later.

##### [GitHub](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails) is the main page of the project.

##### For issues with the blueprints themselves, make a [GitHub issue](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/issues)

##### For questions, check the [wiki](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/wiki). If you can't find anything there, check if it has been asked in [discussions](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/discussions) and finally if that still doesn't help, make a new discussion thread.
Asking for anything on factorioprints is discouraged as it's hard to search for already asked questions and I have to repeat myself a bunch. I may also just miss it easily.

<details>
  <summary><span style="color:cyan">2.0 Change Log. Latest = v2.7.0</summary>

###### <span style="color:white">v2.7.0</color>
- Added underpass entry/exit blueprints
- Added parallel input addons for bufferless providers
- Moved bufferless provider blueprints to their own book

###### <span style="color:white">v2.6.0</color>
- Added bufferless providers (solids only)
- Added inline bufferless providers (solids only)

- Fixed inline 2-4-0 providers having wrong signals set in some combinators

###### <span style="color:white">v2.5.1</color>
- Removed check for carbon in train interrupts that prevented trains from importing when the DLC wasn't enabled
- Removed Carbon from the `Fuel Priority` signal group in the fuel supply stations that prevented them from importing when the DLC wasn't enabled
- Replaced the `depot` blueprint with a `platforms`-like book with whole depots premade as it was annoying to set up especially with depots not needing any power poles included in the platforms


###### <span style="color:white">v2.5.0</color>
- Added inline providers and requesters for 2-4-0, 1-2-0 and 1-1-0 trains
- Added inline depots for 6, 3 and 2-car trains
- Fixed Straight Stackers using legacy rails
- Added a `requester is not full` condition to trains for leaving providers to prevent annoying alerts for no path.

For existing saves: if you're fine with the no path alerts then you don't have to do anything. Otherwise, make your provider interrupts look like this with each occurrence of the parameter replaced by the appropriate `Train Group` icon:
![image](https://github.com/user-attachments/assets/0331d1cf-c6d0-4b0e-954c-29508431be8a)

Also add a similar condition to your refuelling train's schedule:

![image](https://github.com/user-attachments/assets/a2a71b49-ceff-4c15-bb84-bae207563c5f)

###### <span style="color:white">v2.4.0</color>
- Added walls (now officially and not by accident) - no maintenance system yet
- Removed some unneeded and non-functional signals from the windmill interchange
- Changed the refuelling interrupt to use Fuel (Any) instead of Fuel (All) - it's just a bit better, but (Any) works too so you don't need to change anything on existing saves if you don't want to
- Reworked the Refuelling Station (again, I know) - the old design has issues with nuclear fuel, so this one needs replacing again unfortunately

###### <span style="color:white">v2.3.3</color>
- Added Crossover Displaced Left Turn Interchange
- Fixed trains going to depots with full cargo when no requester was open and freeing the provider for more trains to get cargo they don't have a requester to dump to.

For existing saves: add an `Empty cargo inventory` condition to the Depot interrupt

###### <span style="color:white">v2.3.2</color>
- fixed depot name lacking a space between the symbols which made it not match with the interrupts

###### <span style="color:white">v2.3.1</color>
- Fixed issues with refuelling interrupts
- Rotated a total of 3 (there!) inserters in both refuelling stations (I have no idea how this happened, I tested them and it all worked before)

What to do if you have stations/trains from the v2.2.0+ versions:
- Super Force Build the corrected fuel-related stations over old ones
- Delete your train groups and interrupts 
- Place new trains to create new and updated groups and interrupts
- Re-add your trains to all the appropriate groups

###### <span style="color:white">v2.3.0</color>
- Added Solar versions for existing rail books except for the elevated ones because I don't see the point (you may try to convince me)

###### <span style="color:white">v2.2.0</color>
We're back above 10 books, yay!
- Added station books, there are some changes from pre-2.0
    - Platforms - simple straight rail between 2 and 12 car lengths with a station
    - Providers - Train Limit and Priority Controllers, Buffers
    - Depot
    - Refuelling system - probably a bit overengineered, will add some alternatives later
    - Stackers
- Added some solar arrays in the same grid as rails
- Added trains with preset interrupts for recommended sizes and a way to make custom configurations
- Fixed U-turn (again but for a different reason) not being centred
- Improved some signalling

There is a whole system going on with the trains and all the stations now that uses the interrupts, it's explained in (some) detail in the book itself.

This update is pretty big so I've been testing it "a bit" along with some other people, but I wouldn't be surprised if there are some big issues we've missed. You've been warned.

Big thanks to Niventill for huge help with finding my dumb mistakes nigh-instantly and teaching me how interrupts (and some other things) work. Without him, this would be more buggy than some AAA games and would need to go through like 3 more complete revisions afterwards...


###### <span style="color:white">v2.1.2</color>
- fixed a bunch of redundant or missing signalling (nothing that would break something)

###### <span style="color:white">v2.1.1</color>
-fixed U-turns (for real)
-fixed straights (I copied the diagonal bp by accident)


###### <span style="color:white">v2.1</color>
- Added Entry/Exit blueprints (ground and elevated, only copies from the pre-2.0 versions for now)
- Changed Entry/Exit blueprints from pre-2.0: the naming is now network-centric instead of station-centric
- Changed Large Power Pole positioning on both orthogonal and diagonal straight pieces so that each power pole can reach 2 others in each direction with all possible connections being used. This allows for deleting power poles when super force building Entry/Exit blueprints without severing power and circuit connections, effectively eliminating all previously existing blindspots. The same idea applies to elevated entry/exists with their supports.
Tested all orthogonal intersections/interchanges for 1-4-1 and 1-1-1 trains
- Fixed misaligned U-turns

###### <span style="color:white">v2.0</color>
Factorio 2.0 broke everything and there's a lot, so the updated book will be released across multiple updates.
This is the first of many and includes:
- Basic rail blueprints (pure ground level, pure elevated and level switch)
- 7 large 4-way interchanges
- 3 large 3-way interchanges
- All interchanges/intersections that do not feature diagonal exits are throughput tested with scores presented in descriptions (the tester doesn't support diagonal exits yet)
- Sane versioning


  </summary>
</details>

<details>
  <summary><span style="color:cyan">1.0 Change Log</summary>

###### <span style="color:white">18:00 UTC 22.08.2020</color>
- Added the missing accumulator to "Diagonal 4-way" from the "4 Lane Solar" book
- All non-diagonal blueprints now have grid settings to enable placing by dragging. They're placed next to the previous one but only on the horizontal or vertical axis, not on diagonals. If support for that releases I'll update them too.
- New title

###### <span style="color:white">19:00 UTC 23.08 2020</color>
- Landfill added under every blueprint to allow placing on water
- For some stupid reason, I've renamed all 45° turn blueprints to 135° previously, now it's the right way again
- Improved upgradability in and between Category A (Solar) books

###### <span style="color:white">20:00 UTC 25.08.2020</color>
- Added more pictures to description

###### <span style="color:white">13:30 UTC 23.08.2020</color>
- Added Absolute Reference Point setting to every blueprint
- Changed Non-Solar Books' color-coding from yellow to dark orange for better visibility on tooltips
- Fixed "4:2 T Junction Right" from "4:2:1 Lane" and
 "4:2:1 Lane Solar" books (one exit was 1 piece of rail too long)
- Added missing lamps to "4:2 T Junction Left" from "4:2:1 Lane" book

###### <span style="color:white">22:30 UTC 25.08.2020</color>
- Added stations for < C || < C > || < CC || < CCCC > || << CCCC || < CCCC <> CCCC > || << CCC <> CCC > trains and their simple LTN equivalents
- Added blueprints for creating stations from smaller components both for vanilla and LTN

###### <span style="color:white">12:00 UTC 26.08.2020</color>
- Added missing signals to double-headed stations
- All LTN stations now have appropriate maximum and minimum train length set

###### <span style="color:white">15:30 UTC 26.08.2020</color>
- Slightly redesigned all <CC stations and all but <<CCC<>CCC>> provider stations in order to make all stations red belt compatible 
- Added Red Belt stations (upgradable to blue belt)
- Removed the unnecessary middle power pole from all "Straight T Junction" (Category A) blueprints

###### <span style="color:white">16:00 UTC 26.08.2020</color>
- Fixed "Provider - Loading" from Rails -> Stations -> Vanilla (Red Belt) -> Station Parts (was the same blueprint as for LTN version)

###### <span style="color:white">17:00 UTC 26.0.8.2020</color>
- Added "Provider - Front & Rear" and "Requester - Front & Rear" Stations for all 12 car station books

###### <span style="color:white">01:00 UTC 27.08.2020</color>
- Redesigned all stations to make them smaller and simplify the balanced loading/unloading using MadZuri's design
- Added "Provider Front & Rear" and "Requester Front & Rear" to all 12 car stations
- Added more blueprints to "Stations Parts" books

###### <span style="color:white">15:30 UTC 27.08.2020</color>
- Added "Straight Lane Switch U-turn" and "Diagonal Lane Switch U-turn" to all 4 Lane Category A Books
- Reworked signalling in "Straight U-turn" and "Diagonal U-turn" in all 4 Lane Category A Books in order to make them upgradable to the above. Also Diagonal U)-turn" looks like a square now.
- Fixed modularity of rail blueprints with diagonal exits (previously solar panels would overlap)

###### <span style="color:white">16:30 UTC 28.08.2020</color>
- Changed some blueprints in "Station Parts" books and added new ones
- Added "Instructions" book. Inside you can find instructions on setting up MadZuri's Balanced Train Loading and my LTN Stations
- Fixed wiring in Provider stations
- Simplified LTN Station Logic "Provide Threshold" and "Request Threshold" replaced with "Provide Stack Threshold" and "Request Stack Threshold"
- Added train stations for 2L-10C Single-headed trains

###### <span style="color:white">17:30 UTC 28.0.2020</color>
- Normalized train stations
- Added train stackers
- Improved some signalling/removed misplaced "yellow state" signals

###### <span style="color:white">21:30 UTC 29.08.2020</color>
- Provider stations finally work as they should be I swear (all it took was changing "Anything" to "Everything" in inserter settings so you can just put a new station over the old one and settings will be updated)

###### <span style="color:white">12:30 UTC 31.08.2020</color>
- Fixed snapping on "2:1 Exit U-turned"

###### <span style="color:white">10:00 UTC  26.09.2020</color>
- Provider stations now have their chest number set in their arithmetic combinator for balanced loading

###### <span style="color:white">12:30 UTC 06.10.2020</color>
- Forgot to use an upgrade planner on red belt station books, fixed

###### <span style="color:white">18:00 UTC 05.12.2020</color>
- Moved signals from exits of rail blueprints to their entrances as suggested by Josch. Helps blueprints connect better by mitigating some conflicts (if you're planning to use this update on a save where you already have used older versions, you should place a signal in the middle of a big rail block that forms where old rails connect with new. That's not a perfect solution, but anything better would require replacing signalling on all old rails)
- Improved signalling on all "u-turned" blueprints from 4:2:1 books
- Changed "Diagonal U-turn" from 4 Lane books so it is upgradable to "Diagonal Lane Switch U-turn" as originally intended
- If you're playing on 1.1, Factorio saves cable connections in blueprints now, you know what that means

###### <span style="color:white">15:30 UTC 8.12.2020</color>
- Stackers for each train size now have their own books rather than all being shoved together

###### <span style="color:white">20:00 UTC 10.12.2020</color>
- I've missed all of 4:2:1 Solar book, when aligning blueprint grid after update from 06.10.2020 - Fixed
- After previous update, stackers had align to grid checked with some ridiculous values for some reason beyond my understanding- Fixed

###### <span style="color:white">12:30 UTC 13.12.2020</color>
- The reason beyond my understanding from the previous update has been understood. It has to do with changes to blueprint alignment settings in Factorio 1.1. Stations too have been affected by it - Fixed

###### <span style="color:white">19:30 UTC 18.12.2020</color>
(Compatible with older versions)
- All blueprints containing a 90° turn including the various 90° Turns have been redesigned to actually do so. Exceptions are 1) the entirety of Category B, since it was impossible to do, 2)curved/diagonal blueprints from Category C - impossible or already compatible
- Solar blueprints have been redesigned accordingly
- Overall this update increases the number of blueprints that both 2 Lane and 4 Lane 90° Turns can be upgraded into
- Great thanks to An Entire Sleeve for helping out

###### <span style="color:white">21:00 UTC 18.12.2020</color>
(Compatible with older versions)
- Added "Wall" book, containing 7 blueprints designed to protecc your trains from natives

###### <span style="color:white">1:00 UTC 27.12.2020</color>
(Compatible with older versions)
- Added "Entry/Exit" books (new category - D) containing most blueprints from category B with severe modifications (they are way better now)
- Added 4:1 4-way Intersections in 4 variants and their diagonal equivalents
- Stackers have grid snapping (again)
- Reworked blueprint naming so your eyes don't bleed anymore

###### <span style="color:white">1:00 UTC 28.12.2020</color>
(Compatible with older versions)
- Fixed signalling in category D (some blueprints had signals on the wrong side of the rail)
- deleted blueprints from category D in the 'Solar' book that had the singular lane connected to only one side of the main track

###### <span style="color:white">15:00 UTC 28.12.2020</color>
(Compatible with older versions)
- Added grid snapping to non-diagonal blueprints from category D. It actually works and it's amazing. Unfortunately, it's not possible to do this to diagonal blueprints right now

###### <span style="color:white">19:00 UTC 29.12.2020</color>
(Stations were completely reworked, but there shouldn't be any compatibility issues as long as you don't fiddle with the ones you already placed)
- Complete rework of the stations, more freedom with their setup, better belt layouts, switched from circuit-based balancing to mechanical on provider stations - thanks to this there is also less fiddling with LTN stations, no need to worry about where each wire is connected and so on. There are fewer blueprints overall and instead of having 2 separate books for red and blue belts, now there is only one with red ones, upgradable with a provided upgrade planners. Largely influenced by Nilaus's tutorials
- Added 4:2 4-way with three ends with 4 lanes and one end with 2 lanes
- Added 10 car and 5 car stackers
- It's a big update so there is more potential for bugs than normal, I'll fix them as I get reports or notice them myself

###### <span style="color:white">14:00 UTC 30.12.2020</color>
(Compatible with older versions)
- Added landfill to stackers

###### <span style="color:white">16:30 UTC 30.12.2020</color>
(Compatible with older versions)
- Lane split isn't fixed to a specific position on a straight line like it was before giving more freedom with its positioning
- 4:1 4-ways were replaced with a 4:1 4-way that actually is 4-way. 

###### <span style="color:white">22:30 UTC 30.12.2020</color>
(Compatible with older versions)
- Light on stations have been moved outside to allow for placing additional signals if one so desires
- Chests on vanilla stations have been connected with green wires for wire sorcerers

###### <span style="color:white">20:00 UTC 31.12.2020</color>
(Compatible with older versions)
- Added an outline of a  42x42 square of stone bricks to the Tiles book, it's the same size as the grid that all rail blueprints are based on, so it can be used as a placeholder for future rails
- some minor fixes like correcting spelling mistakes, changing blueprint tooltips a bit and so on

###### <span style="color:white">18:00 UTC 01.01.2021</color>
(Compatible with older versions)
- Station buffers got a bit of a remake and more have been added

###### <span style="color:white">18:30 UTC 01.01.2021</color>
(Compatible with older versions)
- Both 4 Lane Entries from Entry/Exit books had some signals on the wrong side of the rails, fixed

###### <span style="color:white">14:00 UTC 02.01.2021</color>
(Compatible with older versions)
- Added more wall blueprints
- Fixed some naming and icon errors 

###### <span style="color:white">14:30 UTC 03.01.2021</color>
(Compatible with older versions)
- Added more stackers
- Reworked stacker naming and icons

###### <span style="color:white">16:00 UTC 04.01.2021</color>
(Compatible with older versions)
- Added stations for 4 car long trains
- Added Maintenance book with a handful of blueprints to keep your walls in good shape

###### <span style="color:white">18:30 UTC 04.01.2021</color>
(Compatible with older versions)
- Walls were beautified
- Wall Maintenance requester stations are no more compact
- I LTN depots are now more compact
- Fixed wrong car numeration in LTN Depots

###### <span style="color:white">00.30 UTC 07.01.2021</color>
(Compatible with older versions)
- Wall Maintenance stations can now service artillery shells
 - Maintenance trains are now longer by 1 car (artillery wagon) which is used to transport said shells
 - There are still variants of those stations that do not have such capabilities for those who have yet to unleash the artillery's might (without artillery, the ones that can service it won't work)
- Added a U shaped wall segment (meant for surrounding U-turns
- Some more wall beautification happened, very likely to be the last

###### <span style="color:white">13:30 UTC 10.01.2021</color>
(Compatible with older versions)
- Blueprints from Entry/Exit books now have normal signals instead of chain signals at their ends, increased throughput

###### <span style="color:white">16:30 UTC 20.01.2021</color>
(Technically compatible but station names changed so you'll have to change the names of your existing stations accordingly or suffer OCD damage for the rest of the run. Alternatively, you can copy your 'Stations' book, and replace the one from this update with it to get the rest)
- Station names changed from coloured text to icons of respective logistic chests resulting in drastically reduced length
- Added 8 car stations
- Added 2 lane buffered 4-way intersections based on "Whirlpool" by Tallinu
- 4:2 4-way (2) has been improved. While It was proven impossible to make it upgradable from 2 lane 4-way, it is now symmetric and doesn't let trains change lanes resulting in higher throughput

###### <span style="color:white">17:00 UTC 20.01.2021</color>
(Compatible with older versions)
- Added 8 car stackers
- Removed unnecessary signals from diagonal stackers

###### <span style="color:white">11:00 UTC 29.01.2021</color>
(Compatible with older versions)
- Added another 4:2 4-way. This one has two 4L ends opposite of two 2L ends. Both straight and diagonal versions
- Added Power Indicators book. Who knows what's inside?
- Added Safe Rail Crossing blueprints
- With the 1.1 release it is now possible to flip blueprints using F and G. Because of this there is no reason to maintain both Left and Right versions of station buffers and as such, they were removed
- Slightly modified the "L" shaped wall so that it doesn't overlap with diagonal U-turns

###### <span style="color:white">21:30 UTC 30.01.2021</color>
(Train stop names in LTN depots have been changed - simple copy-paste will do) 
- Added Train Limit Control blueprints for vanilla Provider and Requester stations
- Added vanilla train Depots
- Added 3 more splits to 4:2:1 books
- (fix) Added green wire connecting vanilla requester stations' buffers
- All Station Buffers now have listed their storage capacity for different stack sizes
- Reworked colour-coding/symbolism in Stations book to make it more consistent
 - LTN Depots now use Roboport Icon instead of the Depot Signal and are colour-coded grey 
 - 'Stackers' book now uses purple, and books/blueprints inside it are plain white as blue was reserved for requesters

###### <span style="color:white">12:30 UTC 31.01.2021</color>
(Compatible with older versions)
- Slight improvements to signalling in 4:2:1 blueprints
- (fix) 2 Lane Safe Rail Crossing is no longer misaligned
- (fix) Solar Safe Lane Crossing blueprints now are truly solar 

###### <span style="color:white">20:30 UTC 02.02.2021</color>
(Compatible with older versions)
- Blueprint description changes/updates, more fancy rich text shenanigans
- Added 7, 9 and 11 car stations and stackers coz why not just have everything from 2 to 12 at this point. And let's not forget about the option of deleting blueprints you're never going to use

###### <span style="color:white">15:00 UTC 07.02.2021</color>
(Compatible with older versions)
- Added 1, 2 and 3 car balance fluid buffers and modified 4 car ones slightly so that it is possible to transfer information about stored fluid through a green wire. All are based on Nilaus's design.
- (fix) 7 car stacker book now has the right blueprints

###### <span style="color:white">18:00 UTC 07.02.2021</color>
(Compatible with older versions)
- (fix) Corrected that some blueprints had the wrong blueprint snapping mode or had it at all when they shouldn't

###### <span style="color:white">15:00 UTC 08.02.2021</color>
(Compatible with older versions)
- (fix) Added ONE missing belt to vanilla 1 car requester buffer ;)

###### <span style="color:white">15:00 UTC 09.02.2021</color>
(Compatible with older versions)
- Y junctions and splits are now more compact
- Added a cursed diagonal rail signal based power display
- Added a circular rail based power display (large and mini)
- Added ONION

###### <span style="color:white">12:30 UTC 10.02.2021</color>
(Compatible with older versions)
- (fix) some spelling in blueprint descriptions

###### <span style="color:white">13:00 UTC 10.02.2021</color>
(Compatible with older versions)
- small changes to wiring of 2 car fluid provider and requester buffers resulting in better pump behavior

######  <span style="color:white">17:00 UTC 08.03.2021</color>
(Compatible with older versions)
- Lamps on stations were moved to stations buffers instead to avoid collision with fluid buffers
- Improvements to grid snapping settings on station buffers
- (fix) Added missing wires on 'Provider -> 4 car fluid buffer'  connecting storage tanks to the power poles
- Some additions/changes to the "Tiles" book, I'm working on something more flexible too

######  <span style="color:white">17:30 UTC 09.03.2021</color>
(Compatible with older versions)
- In the "Tiles" book you can now find 4 new books (2 vanilla/2 modded) containing parts that let you construct new tile patterns like the pre-made ones but with custom size and rail spacing

######  <span style="color:white">12:30 UTC 13.03.2021</color>
(Compatible with older versions)
- In the previous update, I forgot to include the blueprint string

######  <span style="color:white">15:00 UTC 23.04.2021</color>
(Compatible with older versions)
- (fix) 'Non-Solar & solar -> Entry/Exit -> 4 Lane Exit (R)': a rail piece was missing

######  <span style="color:white">19:30 UTC 02.06.2021</color>
(Compatible with older versions)
- (fix) better gate behaviour in safe rail crossings, smaller probability of getting stuck inside

######  <span style="color:white">18:00 UTC 09.06.2021</color>
(Compatible with older versions)
- (fix) blueprints of gated walls didn't have gates in the dragon's teeth
- minor improvements to some tooltips (mostly aesthetic)
- changed landfill layout under safe rail crossing blueprints a bit

######  <span style="color:white">18:00 UTC 16.10.2021</color>
(You may need to change the naming scheme of your stations to be consistent with the new one if you're using a many-to-many train system or something similar, relying on station names. This console command should take care of renaming stations to the new format but only stations: ```/c
local stops = game.surfaces["nauvis"].find_entities_filtered{type="train-stop"}
for _, stop in pairs(stops) do
stop.backer_name = string.gsub(stop.backer_name, "item=", "img=item/")
stop.backer_name = string.gsub(stop.backer_name, "fluid=", "img=fluid/")
end```)
- Changed formatting for station names, so that chat messages are less cluttered and all-round more pleasant to look at
- Updated some tooltips
- Some more minor changes

######  <span style="color:white">21:30 UTC 23.01.2022</color>
(Compatible with older versions)
- maintenance train schedules updated to the latest station naming scheme
- maintenance requesters will now request a new delivery when any item goes below 20-25% (dependent on the item) of the requested amount (was 50 items below request); you can safely paste over the new blueprints over the old ones
- maintenance requester stations had their request numbers modified to require exactly 20 stacks for full delivery so that a maintenance train can carry 2 whole requesters' worth of supply
- filters in maintenance trains' wagons modified accordingly
- replaced storage chests with passive provider chests in maintenance requesters, don't even ask me it wasn't that way from the outset
- LTN providers now use filter inserters between buffer chests and trains
- Added the Whirlpool 2.0 power indicator featuring my latest achievements in Factorio animation

######  <span style="color:white">13:00 UTC 05.02.2022</color>
(Compatible with older versions)
- Added 2 new late-game unloading buffers, efficient, small and cheap
- General improvements to station buffer naming/descriptions
- Removed Station Construction Books - I'm constantly forgetting to bring them up to date with the main station books, and those main books became so customizable by now, that I don't feel like they're needed for anything anymore
- Book names now use bold font for better aesthetics

######  <span style="color:white">20:00 UTC 04.04.2022</color>
(Compatible with older versions)
- Fixed a deadlock case in the 'Entry/Exit' blueprints (not entire books, just the blueprints with 'Entry/Exit' in the name have been altered slightly)

######  <span style="color:white">10:30 UTC 31.05.2022</color>
(Compatible with older versions)
- Fixed that one of the cornerpieces in 'Gates' book was a duplicate of another one
- Changed some symbols in the 'Wall' book to more accurately represent the shape of the pieces with some more fancy symbols

######  <span style="color:white">15:00 UTC 11.06.2022</color>
(Compatible with older versions)
- Added Solar Array book. For now contains 3 designs, in variants with and without radars. Thanks to Omega for the idea and 2 of the designs.
- Fixed instructions for setting up the Train Limit Control for Vanilla Requesters (instructions for arithmetic combinators were switched)

######  <span style="color:white">13:30 UTC 22.06.2022</color>
(Compatible with older versions)
- missing rail piece in '4:2 T Junction (Left)' in '4:2:1 rail' (non soal) book fixed

######  <span style="color:white">15:30 UTC 13.07.2022</color>
(Compatible with older versions)
- Fixed 1-car fluid buffer being what the 2-car one was supposed to be
- Fixed 2-car buffer being just completely wrong

</details>

###### <span style="color:red">Before updating to a new version be sure to check logs, as there may be some compatibility issues with older ones </color>

---

### Special Thank You
- An Entire Sleeve,  for helping out with testing, many reports and suggestions
- [Nilaus](https://www.youtube.com/channel/UCD80bzqJh1N7lOqn7n0vKTg) for his 1.0 fluid buffer designs (used in 1.0 versions)
- MadZuri for his balanced train loading/unloading designs (used in earlier versions)
- Hactar for [his rail network](https://gist.github.com/HactarCE/bc85d8c49d3e686d66d181d471cd50b1), I've been using before making this book
