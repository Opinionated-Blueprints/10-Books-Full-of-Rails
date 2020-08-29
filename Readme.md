At this point the original title is inaccurate. There no longer is just 10 books... but 55. And that's only the endpoints of the book tree.



###### Quarantine proved to be the perfect time to spend more than a week pretty much only designing some intersections. I've got to 107 before I finally said to myself: "ENOUGH". Actually, there were 214 (rail) blueprints (now 218), but half of that is just versions with solar panels and accumulators fit in between the lanes because "why not?". At first, these were called "Books of 1001 Railway Blueprints" and there were 10 books to get separately, but since 1.0 came out, I've decided to finally make use of book nesting and do some polishing/updates with the recent features and some new ideas. Hope you'll enjoy, and remember: Factory Must Grow.



# Features:

### Rails:

<img src="https://preview.redd.it/3l9ao5k6ogi51.png?width=1637&format=png&auto=webp&s=84a9b1b3c0b49fa5e067717d8092529057e0e612" width="100%">
<font size = 1><div align="center">
all blueprints with solar panels and accumulators <br>
right click & open image in new tab for better resolution
</font></div>

- All blueprints are always upgradable into their equivalents from other books placed lower on the list in the "Rail Book Categories" section as long as they are in the same category
 - some blueprints are upgradable into others from the same book or even other categories
   - some of that upgradability was sacrificed for the sake of throughput
 - to achieve that, many blueprints don't have the best possible signal placement
- Each book comes in 2 variants:
 - standard (no ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png) &![accumulator](https://wiki.factorio.com/images/thumb/Accumulator.png/32px-Accumulator.png))
 - ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png) &![accumulator](https://wiki.factorio.com/images/thumb/Accumulator.png/32px-Accumulator.png) included because why would you want to waste so much space (aesthetics first though)
   - there are some paths left between solar panels so you can get run over by a train again
- Rail Spacing: ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) - - ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) - - - ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) - - ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)
- Made for 6 ![locomotive](https://wiki.factorio.com/images/thumb/Locomotive.png/32px-Locomotive.png)/![cargo wagon](https://wiki.factorio.com/images/thumb/Cargo_wagon.png/32px-Cargo_wagon.png) long trains, but works well with 2, and 3 ![locomotive](https://wiki.factorio.com/images/thumb/Locomotive.png/32px-Locomotive.png)/![cargo wagon](https://wiki.factorio.com/images/thumb/Cargo_wagon.png/32px-Cargo_wagon.png) (to maximize throughput add signals on non-crossing lanes) and with multiples of 6 (you'll need to increase space between intersections accordingly to avoid potential deadlocks)
- ![green wire](https://wiki.factorio.com/images/thumb/Green_wire.png/32px-Green_wire.png) & ![red wire](https://wiki.factorio.com/images/thumb/Red_wire.png/32px-Red_wire.png) + ![small lamp](https://wiki.factorio.com/images/thumb/Lamp.png/32px-Lamp.png) included
- Modular
- Right-Hand Drive
- Each section is 21x21 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) or 42x42 tiles big (books are focused on throughput for 6  ![locomotive](https://wiki.factorio.com/images/thumb/Locomotive.png/32px-Locomotive.png)/![cargo wagon](https://wiki.factorio.com/images/thumb/Cargo_wagon.png/32px-Cargo_wagon.png) trains and that is exactly the border length of the square in which all blueprints here fit, hence they are not chunk aligned)
- Grid and Absolute Reference Point are on, so you can use them like a "chunk aligned network" (blueprints can only be placed on an artificial grid that lets you start building from 2 completely disconnected points on the map and ensures that they can still be perfectly connected, see [FFF #357](https://factorio.com/blog/post/fff-357) under the "Snapping" section)
- Every blueprint has ![landfill](https://wiki.factorio.com/images/thumb/Landfill.png/32px-Landfill.png) underlay to allow placing on water (Shift+LMB to place landfill, and LMB to place blueprint, you can also just double-click Shift+LMB)

### Stations:

<img src=https://i.imgur.com/gddN5h7.png width = 100%>
<font size = 1><div align="center">
Blue Belt Stations | Row 1: Provider - Front | Row 2: Provider - Rear | Row 3: Provider - Front & Rear | Row 4: Requester - Front | Row 5: Requester - Rear | Row 6: Requester - Front & Rear<br>
LTN Depots  and some other stations are not visible here <br>
right click & open image in new tab for better resolution
</font></div>

- Every station comes in 2 variants:
   - Vanilla
   - [Logistic Train Network](https://mods.factorio.com/mods/Optera/LogisticTrainNetwork) mod compatible (see: [LTN - Logistic Train Network - Manual](https://forums.factorio.com/viewtopic.php?t=51072) & [Guide for a Low-Effort LTN User](https://www.reddit.com/r/factorio/comments/73xyd5/guide_for_a_loweffort_ltn_user/) & [LTN Mod Tutorial - Logistic Train Network](https://www.youtube.com/watch?v=a3ujEdPfGHk) & [Factorio 0.17 Logistic Train Network Tutorial](https://www.youtube.com/watch?v=bpfVzfWeqj8))
- Compatible trains: <C || >C> || <CC || <CCCC> || <<CCCC || <CCCC<>CCCC> || <<CCC<>CCC> || <<CCCC<<CCCC || <<CCCCCCCCCC
- Some basic train stackers - nothing special, but still nice to have (currently available lengths: 12, 6, 4, 3)
- Includes a book with some smaller parts for creating custom stations
- Balanced loading and unloading using MadZuri's designs
- ![small lamp](https://wiki.factorio.com/images/thumb/Lamp.png/32px-Lamp.png) included
- ![red belt](https://wiki.factorio.com/images/thumb/Fast_transport_belt.png/32px-Fast_transport_belt.png) and ![blue belt](https://wiki.factorio.com/images/thumb/Express_transport_belt.png/32px-Express_transport_belt.png) versions (upgradable)
- (LTN) Depots included
- "Instructions" book to help with setting up balanced loading, and LTN stations



# Rail Book Categories:

- ##### Category A - Basic Blueprints
(90% of every rail network ever made)

 - <span style="color:orange">2 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)</span> (14bp)
 - <span style="color:cyan">2 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span> (14bp)

<img src="https://i.imgur.com/HF0K6lB.png" width="100%">

<font size = 1><div align="center">
2 Lane Solar | Row 1: Vertical/Horizontal exits | Row 2: Vertical/Horizontal/Diagonal exits | Row 3: Diagonal exits  <br>
right click & open image in new tab for better resolution
</font></div>

 - <span style="color:orange">4 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)</span> (16bp)
 - <span style="color:cyan"> 4 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span> (16bp)

<img src="https://i.imgur.com/7Vhy52k.png" width="100%">

<font size = 1><div align="center">
4 Lane Solar | Row 1: Vertical/Horizontal exits | Row 2: Vertical/Horizontal/Diagonal exits | Row 3: Diagonal exits <br>
"Straight Lane Switch U-turn" and "Diagonal Lane Switch U-turn" are not visible here <br>
right click & open image in new tab for better resolution
</font></div>


- ##### Category B1 - Lane Mergers/Splitters
(exits don't have equal amount of lanes)

 - <span style="color:orange">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)</span> (27bp)
 - <span style="color:cyan">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span> (27bp)


<img src="https://i.imgur.com/oyPy9NB.png" width = 100%>

<font size = 1><div align="center">
4:2:1 Lane Solar | Row 1: 4 & 1 Lane exits | Row 2: 4 & 2 Lane exits | Row 3: 2 & 1 Lane exits<br>
right click & open image in new tab for better resolution
</font></div>


- ##### Category B2 - Lane Mergers/Splitters (Diagonal)
(exits don't have equal amount of lanes)

 - <span style="color:orange">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) Diagonal </span>(27bp)
 - <span style="color:cyan">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) Diagonal ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span> (27bp)

<img src="https://i.imgur.com/oVcE7aV.png" width="100%">

<font size = 1><div align="center">
4:2:1 Lane Solar Diagonal | Row 1: 4 & 1 Lane exits | Row 2: 4 & 2 Lane exits | Row 3: 2 & 1 Lane exits <br>
right click & open image in new tab for better resolution
</font></div>


- ##### Category C - Split Junctions
(not all exits are connected to each other)

 - <span style="color:orange">2 & 4 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) Split</span> (23bp)
 - <span style="color:cyan">2 & 4 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) Split ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span> (23bp)

<img src="https://i.imgur.com/8vYzmOz.png" width="100%">

<font size = 1><div align="center">
2 & 4 Lane Solar Split Junctions | Row 1: Vertical/Horizontal exits | Row 2: Vertical/Horizontal/Diagonal exits | Row 3: Diagonal exits<br>
right click & open image in new tab for better resolution
</font></div>

###### *Categories do not represent book nesting



# Notes:


### Rails:

- Most of your network will consist of blueprints from Category A, Category B will find some use for sure, but these books are more specialized, and Category C will be used very rarely if at all 
- Outer lanes in 4-way Intersections from 4 Lane books (category A) do not have left turns. Use Line changers provided
- Category B has some split junctions. The main difference between B and C is that category C blueprints all have the same number of lanes. Blueprints from category B don't
- Remember to leave enough space between each section with lanes crossing each other to fit the longest train that is going to use that part of your network. Otherwise, when it stops on the next signal, it WILL block trains on other lanes. That is true for any train network, not only one built with my blueprints
- No ![roboport](https://wiki.factorio.com/images/thumb/Roboport.png/32px-Roboport.png) between rails so you don't accidentally recreate [Population transfers in the Soviet Union](https://en.wikipedia.org/wiki/Population_transfer_in_the_Soviet_Union), except bots. The real reason: 1. bots have a limited supply of power. 2. When it depletes, they go to recharge at the nearest roboport. 3. They go straight to their destination without considering their power reserves. That means that if you have a "C" shaped logistic network (that often forms with rails), where the distance in a straight line between both ends of this "C" is 2x greater than your robot's range, it won't reach its destination and instead, its power reserves will deplete, the bot will come back to where it started to recharge and try again thus falling into an endless loop
- ![copper cable](https://wiki.factorio.com/images/thumb/Copper_cable.png/32px-Copper_cable.png) look cool
- Floor tiles seen on the rail pictures are included in the book but require [Asphalt Roads](https://mods.factorio.com/mod/AsphaltRoads) mod to work, (there is a vanilla version too, but it's not as pretty). Feel free to use those for designing your own rail blueprints. If you go for a different grid size [they're for 6 ![locomotive](https://wiki.factorio.com/images/thumb/Locomotive.png/32px-Locomotive.png)/![cargo wagon](https://wiki.factorio.com/images/thumb/Cargo_wagon.png/32px-Cargo_wagon.png)(length) or 21x21 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) or 42x42 tiles] you'll have to rescale them


### Other:

- There is a lot of Factorio's in-game Rich Text - it's awesome, believe me
- If you don't have aforementioned mods (LTN, Asphalt Roads) You'll get some error messages in the chat when importing this book. That only means that you won't be able to use blueprints that require those mods. All of them have vanilla friendly equivalents. You don't need those mods to make use of my blueprints
- I'm no master of LTN nor I consider myself to be any close to one, so the logic is one of the simplest you can do. If you'd like to make something more sophisticated that would be compatible with my blueprints, go ahead, but post it as your own. Let me know, and I'll link it here



# Known Issues:
- Most books included here have their names display a bit bugged when in grid view in the blueprint library. I don't think I can do anything about it  without changing their names and/or used Rich Text (reported to devs)

          
# The Plan
- ~~Add bot serviced stations~~ (abandoned, at least for now)
- New category - D - merging C and B by creating Split intersections (C) where exits have a different amount of lanes (B). Would anyone ever use one of those? That's the main reason holding me back, so let me know if you'd like something like this
- Idk, maybe I've missed some blueprint? If so, let me know, and I'll make it
- If you have any suggestions on how I could improve this book, let me know. I can't promise that I'll check the comments often, but better late than never



# Change Log:

18:00 UTC 22.08.2020
- Added the missing accumulator to "![](https://factorioprints.com/icons/signal-D.png)iagonal ![](https://factorioprints.com/icons/signal-4.png)-way" from "<span style="color:cyan">4 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span>" book
- All non-diagonal blueprints now have grid settings to enable placing by dragging. They're placed next to the previous one but only on the horizontal or vertical axis, not on diagonals. If support for that releases I'll update them too.
- New title

19:00 UTC 23.08 2020
- Landfill added under every blueprint to allow placing on water
- For some stupid reason, I've renamed all 45° turn blueprints to 135° previously, now it's the right way again
- Improved upgradability in and between Category A (Solar) books

20:00 UTC 25.08.2020
- Added more pictures to description

13:30 UTC 23.08.2020
- Added Absolute Reference Point setting to every blueprint
- Changed Non-Solar Books' colour-coding from yellow to dark orange for better visibility on toolitps
- Fixed "![](https://factorioprints.com/icons/signal-4.png):![](https://factorioprints.com/icons/signal-2.png) ![](https://factorioprints.com/icons/signal-T.png) Junction ![](https://factorioprints.com/icons/signal-R.png)ight" from "<span style="color:orange">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)</span>" and
 "<span style="color:cyan">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png) ![solar panel](https://wiki.factorio.com/images/thumb/Solar_panel.png/32px-Solar_panel.png)</span>" books (one exit was 1 piece of rail too long)
- Added missing lamps to "![](https://factorioprints.com/icons/signal-4.png):![](https://factorioprints.com/icons/signal-2.png) ![](https://factorioprints.com/icons/signal-T.png) Junction ![](https://factorioprints.com/icons/signal-L.png)eft" from "<span style="color:orange">4:2:1 ![rail](https://wiki.factorio.com/images/thumb/Straight_rail.png/32px-Straight_rail.png)</span>" book

22:30 UTC 25.08.2020
- Added stations for < C || < C > || < CC || < CCCC > || << CCCC || < CCCC <> CCCC > || << CCC <> CCC > trains and their simple LTN equivalents
- Added blueprints for creating stations from smaller components both for vanilla and LTN

12:00 UTC 26.08.2020
- Added missing signals to double-headed stations
- All LTN stations now have appropriate maximum and minimum train length set

15:30 UTC 26.08.2020
- Slightly redesigned all <CC stations and all but <<CCC<>CCC>> provider stations in order to make all stations red belt compatible 
- Added Red Belt stations (upgradable to blue belt)
- Removed the unnecessary middle power pole from all "![](https://factorioprints.com/icons/signal-S.png)traight ![](https://factorioprints.com/icons/signal-T.png) Junction" (Category A) blueprints

16:00 UTC 26.08.2020
- Fixed "Provider - Loading" from Rails -> Stations -> Vanilla (Red Belt) -> Station Parts (was the same blueprint as for LTN version)

17:00 UTC 26.0.8.2020
- Added "Provider - Front & Rear" and "Requester - Front & Rear" Stations for all 12 car station books

01:00 UTC 27.08.2020
- Redesigned all stations to make them smaller and simplify the balanced loading/unloading using MadZuri's design
- Added "Provider Front & Rear" and "Requester Front & Rear" to all 12 car stations
- Added more blueprints to "Stations Parts" books

15:30 UTC 27.08.2020
- Added "![](https://factorioprints.com/icons/signal-S.png)traight ![](https://factorioprints.com/icons/signal-L.png)ane ![](https://factorioprints.com/icons/signal-S.png)witch ![](https://factorioprints.com/icons/signal-U.png)-turn" and "![](https://factorioprints.com/icons/signal-D.png)iagonal ![](https://factorioprints.com/icons/signal-L.png)ane ![](https://factorioprints.com/icons/signal-S.png)witch ![](https://factorioprints.com/icons/signal-U.png)-turn" to all 4 Lane Category A Books
- Reworked signaling in "![](https://factorioprints.com/icons/signal-S.png)traight ![](https://factorioprints.com/icons/signal-U.png)-turn" and "![](https://factorioprints.com/icons/signal-D.png)iagonal ![](https://factorioprints.com/icons/signal-U.png)-turn" in all 4 Lane Category A Books in order to make them upgradable to the above. Also "![](https://factorioprints.com/icons/signal-D.png)iagonal ![](https://factorioprints.com/icons/signal-U.png)-turn" looks like a square now.
- Fixed modularity of rail blueprints with diagonal exits (previously solar panels would overlap)

16:30 UTC 28.08.2020
- Changed some blueprints in "Station Parts" books and added new ones
- Added "Instructions" book. Inside you can find instructions on setting up MadZuri's Balanced Train Loading and my LTN Stations
- Fixed wiring in Provider stations
- Simplified LTN Station Logic "Provide Threshold" and "Request Threshold" replaced with "Provide Stack Threshold" and "Request Stack Threshold"
- Added train stations for 2L-10C Single-headed trains

17:30 UTC 28.0.2020
- Normalized train stations
- Added train stackers
- Improved some signalling/removed misplaced "yellow state" signals

21:30 UTC 29.08.2020
- Provider stations finally work as they should be I swear (all it took was changing "Anything" to "Everything" in inserter settings so you can just put new station over the old one and settings ill be updated)

---

I think it may be the longest blueprint string on Factorio Prints. <br>
Also: Bookworm Adventures Deluxe

---

Great thanks for all feedback, MadZuri for his balanced train loading/unloading designs and Hactar for his rail network, I've been using before making this book. <br>
https://gist.github.com/HactarCE/bc85d8c49d3e686d66d181d471cd50b1
