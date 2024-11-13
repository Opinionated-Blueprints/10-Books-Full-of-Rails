The biggest (and probably most bloated) rail book out there, updated for 2.0 and Space Age.

##### [GitHub](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails) is the main page of the project.

##### For issues with the blueprints themselves, make a [GitHub issue](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/issues)

##### For questions, check the [wiki](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/wiki). If you can't find anything there, check if it has been asked in [discussions](https://github.com/Opinionated-Blueprints/10-Books-Full-of-Rails/discussions) and finally if that still doesn't help, make a new discussion thread.

<details>
  <summary><span style="color:cyan">1.0 Change Log (pre factorio 2.0)</summary>

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
# General Info

<details>
 <summary>(click to expand)</summary>

- Rails are based on a 42x42 tile grid, which matches 6-car trains perfectly. Supports 3-car and 2-car trains well too
- Blueprints for up to 12 cars are available
- Alternative hypermodular rail blueprints on a tiny 14x14 (2 car length) grid, exactly 1/3 of the regular grid. Both sets are compatible with each other.
- Straight and Turn -> T-Junction -> 4-way in both elevations are directly upgradable
- There are lamps (probably too many tbh)
- ![red circuit](https://github.com/user-attachments/assets/0f4f54c1-5259-49cd-ac2c-6cb983b83d50) and ![green circuit](https://wiki.factorio.com/images/thumb/Green_wire.png/32px-Green_wire.png) connections between large power poles
- (very) wide selection of blueprints: ground, elevated, elevation switch, grade-separated interchanges and more
- above but also with ![solar pannels](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png) and ![accumulator](https://github.com/user-attachments/assets/62d02975-a510-4a2d-b435-523d05f30cac)
 crammed in. Can be placed directly over non-solar blueprints.
- Modular stations with a selection of loading and unloading designs and dynamic train limit and priority control based on the number of items in the buffers
- Alternative (and objectively better :p) bufferless provider stations
- Depots
- Refuelling system with a central supply station and dedicated logistic train that can supply all refuelling stations
- Inline stations - optimised for the smallest possible footprint by placing in-between and very close to straight rails
- Wide selection of stacker designs for all train lengths 2-12
- Premade trains in some common configurations for 2-, 3- and 6-car lengths + DIY locomotives with preset interrupts for more eccentric configurations
- Wall blueprints that follow the same grid as rails (due for an overhaul, currently can't survive 100% evolution)
- Solar array blueprints that follow the same grid as rails for Nauvis, Vulcanus and Gleba ratios

</details>

# Showcase

### Book Structure

![image](https://github.com/user-attachments/assets/f95f4051-b607-4b97-a31c-36e2ee2c51bd)
![image](https://github.com/user-attachments/assets/ddcb859c-4ee1-4885-b36c-490fa607bea9)

### Hypermodular Rail
While most blueprints in this book are designed around a 42x42 tile grid, this set of blueprints functions on a much smaller, 14x14 one, allowing for unmatched flexibility. They integrate nicely with the regular 42x42 blueprints being exactly 1/3 of their size.
Elevated versions are also available.

https://github.com/user-attachments/assets/f77fbdd6-fbfb-456a-b0c7-b97f4f9dfbf2

https://github.com/user-attachments/assets/d322f5e7-90b8-4d5e-80a0-ee15ec282eb7

### Level Switch blueprints

https://github.com/user-attachments/assets/61ba7c37-fec8-43a3-a11b-e9a41d5eb2fb

### Wide selection of grade-separated interchanges
All are scored for throughput, with test results in descriptions.

https://github.com/user-attachments/assets/1ded018b-a13a-4c55-a9d4-131c1e841136

### Entry/Exit blueprints
High-precision conversion to single track for building stations.
There are no blind spots as large power poles on straight rail are dense enough that removing one with super-force-building doesn't remove the power connection.
The same is available for elevated rail with care to replace any broken supports so no additional manual work is required.

https://github.com/user-attachments/assets/19a82445-3b68-4bd4-a698-3fcb3d447e33

### Upgreadability of basic blueprints

https://github.com/user-attachments/assets/41c7e9d6-eeb7-4a96-912f-0b67cf128878

https://github.com/user-attachments/assets/a8e48359-0a12-4566-9b87-b82be69068da

https://github.com/user-attachments/assets/abf0173e-35b0-45d0-a360-7204a1b194b0

#### All rails upgrade into solar counterparts

https://github.com/user-attachments/assets/95d37614-fc8b-41a8-832b-d50c3163e072

### Stations with stackers

https://github.com/user-attachments/assets/177cc15f-2282-4462-8baf-a4d2e7d894c8

https://github.com/user-attachments/assets/8d082ab7-fd27-4a60-9d5a-fadc47a9d502

https://github.com/user-attachments/assets/59ff87ca-f81b-4cc3-92d2-3dee4ede8158

### Setting up modular stations

https://github.com/user-attachments/assets/d3de5948-d00c-43b4-a419-9eb50a676f09

https://github.com/user-attachments/assets/9226d311-599d-44a8-9767-101b5f8ea263

https://github.com/user-attachments/assets/02ce2ab0-92f5-494b-a13f-f3ca983cf3f5

### Inline stations

https://github.com/user-attachments/assets/8b7e6c23-dde5-472b-acf1-a9551bafb610

### Loader and Unloader designs have been tasted for each stage of the game
The inserters required to maintain full throughput are listed in blueprint descriptions

![inserter requirements](https://github.com/user-attachments/assets/e23bc27b-6862-40e9-974d-2c654f60afc7)

### Trains

https://github.com/user-attachments/assets/bf36e778-96be-46ba-b345-8247e207ebe5

### Smart Refuelling System
Fuel-priority based
Priority is set in a constant combinator signal group
Higher-priority fuel will be handled preferentially. If a higher-priority fuel shows up than is currently available, the stations/locomotives will be depleted of it in favour of the higher-priority one and it will be brought back to the Fuel Supply Provider Station.
This behaviour can be seen in the videos below:

https://github.com/user-attachments/assets/5c7e33db-d02b-414c-932a-828757ec05d4

https://github.com/user-attachments/assets/89f0a33d-2e8c-4c33-938d-826a47f8b2b9

https://github.com/user-attachments/assets/7e488f43-d66d-413c-961b-796f02a8961a

### More to come

---

### Special Thank You
- Kelvin, who first came up with hypermodular rails
- An Entire Sleeve, for helping out with testing, many reports and suggestions
- @Niventill for testing and teaching me about the interrupts
- [Nilaus](https://www.youtube.com/channel/UCD80bzqJh1N7lOqn7n0vKTg) for his 1.0 fluid buffer designs (used in 1.0 versions)
- MadZuri for his balanced train loading/unloading designs (used in earlier versions)
- Hactar for [his rail network](https://gist.github.com/HactarCE/bc85d8c49d3e686d66d181d471cd50b1), I've been using before making this book
