# Invaders tracking application

Application must take a radar sample as an argument and reveal possible locations of pesky invaders.

## Development assignment
Your Python application must take a radar sample as an argument and reveal possible locations of invaders.

#### Requirements:
- No image detection, this is all about ASCII patterns
- Good OOP architecture is a must. This is a perfect opportunity to demonstrate the SOLID design principle experience.
- Fully tested code using a framework of your choice

## Finished application
My approach to problem was using **difflib** standard library for calculating similarity between radar and invader(s).

Patterns of both invaders are saved into list. There could be any number of searched patterns not only two hard-coded invaders - it could be loaded from files, database, ...
And then searching for each pattern one by one in whole radar image following simple rules:

From starting line in radar image take row, and cut sample long as width of current invader, and calculate similarity with line of invader pattern.
Saving calculated similarity (between 0-1 == 0-100%) and offsetting to another line - repeating for height of invader.

Then calculating average similarity for whole invader (from saved values for each line).

And comparing if similarity is equal or greater than value in RadarSearchUsingDiff.**RATIO_MATCH**. If so, then pattern is "highlighted" in radar sample, 
currently with number of enumerated invaders. And then moving/offsetting starting line in radar to another line and repeating.

**RATIO_MATCH** is minimal matching ratio to consider as positive similarity match (between 0-1, currently with 0.79 .. which == 79%)
This value makes main difference when searching for invaders (nicely shown with results in *detailed_results.pdf*)

        
**Radar sample** is provided as an .txt file from optional argument (-f | --sample_file)
        
        $ python3 -m tracker --sample_file radar_sample.txt
        
        $ python3 -m trackery -f radar_sample.txt
        
        If not provided then filename stored in RADAR_FILE constant is used:
        $ python3 -m tracker

#### Result / output / invaders found 
After running and searching for all invaders application prints details, like:
~~~~
With similarity acceptance ratio: 79.0%
Invaders found: 8
Radar image with identified invaders saved in: ./data/output.txt
~~~~
And output with overlay of found invaders on radar map can be found in *output.txt* file.
Some detailed examples of output with invaders found (and highlighted) in *detailed_results.pdf*


There is a lot of space for improvement :) of the application, like:
- making it possible for users to change options with arguments (not making it only hard-coded)
- saving all found matches and then choosing best ones within perimeter (now when first match is found application is skipping columns by provided offset in order to not count same invaders twice)
- option to save output as .html (or even image) file with highlighted invaders on radar image
- making some details (like saving output to file or printing output on screen) optional
- rotating radar image to not miss invaders which are “falling” and not just nicely descending :)

### Testing application
**Unit tests** are created with build in library *unittest*  and can be executed
    
    python3 -m unittest tests/testTracker.py 
    
**BDD tests** are created with *mamba* library and can be executed (depending on environment ;) :
    
    pipenv run mamba tracker_spec.py 

### Example of output with invaders overlay
Each type of invader is represented by numbers (1 and 2 on this sample)

~~~~
----o--oo----o--ooo--ooo--o------o---oo-o----22---o--o---------o----o------o-------------o--o--o--o-
--o-o-----oooooooo-oooooo---o---o----o------222-2---o--o----o------o--o---111-----1--oo-o------o----
--o--------oo-ooo-oo-oo-oo-----O------------22222-----oo----o------o---o--1--1-1-1------o----o-o-o--
-------o--oooooo--o-oo-o--o-o-----oo--o-o-22--2-22-oo-o--------o-----o------1-11111---o--o--o-------
------o---o-ooo-ooo----o-----oo-------o---22-22222-o------o----o--------o-11--111-11-------------o-o
-o--o-----o-o---o-ooooo-o-------oo---o---------2-----o-oo-----------oo----1111111-11o-oo------------
o-------------ooooo-o--o--o--o-------o--o-22-22-2-o-o----oo------------o--1111--111-o----o-----o--o-
--o-------------------------oo---------oo-2-2--222----oo----o--o--o----o--1-1-----1-o------o-o------
-------------------o----------o------o--o------o--------o--------o--oo-o-----11-11---o--o---o-----oo
----------o----------o---o--------------o--o----o--o-o------------oo------o--o-o---o-----o----------
------o----o-o---o-----o-o---o-----oo-o--------o---------------------------------o-o-o--o-----------
---------------o-------o-----o-------o-------------------o-----o---------o-o-------------o-------oo-
-o--o-------------o-o-----o--o--o--oo-------------o----ooo----o-------------o----------11----1---o-o
-o--o-------------o----oo------o--o-------o--o-----o-----o----1-----1--o----o--oo-----------1-------
-o-----oo-------o------o----o----------o--o----o-----o-----o-------1-----------o---o-1--111111-----o
-o--------o-----o-----o---------oo----22---o-o---------o---o--1111-11--o-------o------11--11--1-----
------------o---------o---------o----2222-------------oo-oo-----111-11-----o-------o-11-11111111---o
----------------------o------------2222222o---o-----o-------1--111111-1------------o-1-1111111-1----
------------o------o---o---o-------22-22--o--o---------o--o-1-1-11111-1--------------11-1----1-1o-o-
---o-o----------oo-------oo----o----222222oo-------o----o-o-1-1-----1-1-----o----------111-11--1---o
-o-o---------o-o---------------o--2--2--22o---ooo-------o------11-11------------o--------o--o-o--o--
-------oo---------------------------2-22----------o------o-o-------o-----o----o-----o-oo-o-----o---o
---o--------o-----o-------o-oo-----22--22-o----oo----------o--o---oo------oo----o-----o-------o-----
---o--ooo-o---------o-o----o------------o---------o----o--o-------o----o--------o----------------oo-
---o------o----------------o----o------o------o---oo-----------o-------------o----------oo---------o
--oo---------------o--o------o---o-----o--o-------------o------o-------o-----o-----o----o------o--o-
-o-------o----------o-o-o-------o-----o--o-o-----------o-oo-----------o------o---------o-----o-o----
----------o----o-------o----o--o------o------------o---o---------------oo----o-----ooo--------------
----o--------oo----2-2----o--o------ooo----o-oooo---o--o-oo--------o-oo-----o-o---o-o--o-----oo-----
------o--------2-22222----o---o--o-----o---------------o-o-------o-----o----------------------------
o-------oo----o--222222-o---o--o------oooo----------o-oo-------o---o----------o------oo-------------
-o---o----------2--22-2o-o---o-----o-o-----------------------oo--o------o------o--------------------
-----oo-o-o-o---2222222oo----o----o--------o--o---oo---o------------o----------o-o---o------o-o--oo-
------o------o---222-2---------------------------o--o---o---o----o--o-------o-----o------o----o----o
-------o----------222-2-----o----o---o--o-oo--o--o-o--o------o--o-oo---ooo------------------------o-
-o-------o------2-2--22o--o---o---oo-----o----o-------------o----o-ooo-o------o--o-o------o-o-------
---oo--o---o-o---------o---o--------------o--o-----o-------o-----o--o---o-oo--------o----o----o-----
o------o----oo-o-----------oo--o---o--------o-o------o-------o-o------o-oo---------o-----oo---------
----o--o---o-o-----------o---o------------o-------o----o--o--o--o-o---------------o-----------------
-------oo--o-o-----o-----o----o-o--o----------------------o-------o------o----oo----ooo---------o---
o-----oo-------------------o--o-----o-----------o------o-------o----o-----------o----------------o--
--o---o-------o------------o--------------------o----o--o-------------oo---o---------22--------o----
--o--------o---------o------------o------o-------o------------o-------o---o---------22222-----------
------o--------------o-o-o---------o---o-------o--o-----o-------o-o----------o-----22-222----------o
--o---------------o----o--oo-------------o---------o-------------------oo---------22-2-222----------
-o-----------o------111----o----------------ooo-----o--------o--o---o-----------o-2-222222--------oo
-o---o-------o---1-1111-----o-------------------o----oo-----------------o--o--------2--2------o--o--
-------o---o------111111--o----ooo--o--------o-------o----------------------------22-22-2--o--------
o--oo------o-----11--1-11------------oo--o------o--o-------------oo----o------------2222-2------oo--
-----o----------111111111--------------oo--------------oo-----o-----o-o--o------o----------o----o---
~~~~



### Known invaders:
Type #1
~~~~
--o-----o--
---o---o---
--ooooooo--
-oo-ooo-oo-
ooooooooooo
o-ooooooo-o
o-o-----o-o
---oo-oo---
~~~~

Type #2
~~~~
---oo---
--oooo--
-oooooo-
oo-oo-oo
oooooooo
--o--o--
-o-oo-o-
o-o--o-o
~~~~

### Example radar sample (input file):
~~~~
----o--oo----o--ooo--ooo--o------o---oo-o----oo---o--o---------o----o------o-------------o--o--o--o-
--o-o-----oooooooo-oooooo---o---o----o------ooo-o---o--o----o------o--o---ooo-----o--oo-o------o----
--o--------oo-ooo-oo-oo-oo-----O------------ooooo-----oo----o------o---o--o--o-o-o------o----o-o-o--
-------o--oooooo--o-oo-o--o-o-----oo--o-o-oo--o-oo-oo-o--------o-----o------o-ooooo---o--o--o-------
------o---o-ooo-ooo----o-----oo-------o---oo-ooooo-o------o----o--------o-oo--ooo-oo-------------o-o
-o--o-----o-o---o-ooooo-o-------oo---o---------o-----o-oo-----------oo----ooooooo-ooo-oo------------
o-------------ooooo-o--o--o--o-------o--o-oo-oo-o-o-o----oo------------o--oooo--ooo-o----o-----o--o-
--o-------------------------oo---------oo-o-o--ooo----oo----o--o--o----o--o-o-----o-o------o-o------
-------------------o----------o------o--o------o--------o--------o--oo-o-----oo-oo---o--o---o-----oo
----------o----------o---o--------------o--o----o--o-o------------oo------o--o-o---o-----o----------
------o----o-o---o-----o-o---o-----oo-o--------o---------------------------------o-o-o--o-----------
---------------o-------o-----o-------o-------------------o-----o---------o-o-------------o-------oo-
-o--o-------------o-o-----o--o--o--oo-------------o----ooo----o-------------o----------oo----o---o-o
-o--o-------------o----oo------o--o-------o--o-----o-----o----o-----o--o----o--oo-----------o-------
-o-----oo-------o------o----o----------o--o----o-----o-----o-------o-----------o---o-o--oooooo-----o
-o--------o-----o-----o---------oo----oo---o-o---------o---o--oooo-oo--o-------o------oo--oo--o-----
------------o---------o---------o----oooo-------------oo-oo-----ooo-oo-----o-------o-oo-oooooooo---o
----------------------o------------oooooooo---o-----o-------o--oooooo-o------------o-o-ooooooo-o----
------------o------o---o---o-------oo-oo--o--o---------o--o-o-o-ooooo-o--------------oo-o----o-oo-o-
---o-o----------oo-------oo----o----oooooooo-------o----o-o-o-o-----o-o-----o----------ooo-oo--o---o
-o-o---------o-o---------------o--o--o--ooo---ooo-------o------oo-oo------------o--------o--o-o--o--
-------oo---------------------------o-oo----------o------o-o-------o-----o----o-----o-oo-o-----o---o
---o--------o-----o-------o-oo-----oo--oo-o----oo----------o--o---oo------oo----o-----o-------o-----
---o--ooo-o---------o-o----o------------o---------o----o--o-------o----o--------o----------------oo-
---o------o----------------o----o------o------o---oo-----------o-------------o----------oo---------o
--oo---------------o--o------o---o-----o--o-------------o------o-------o-----o-----o----o------o--o-
-o-------o----------o-o-o-------o-----o--o-o-----------o-oo-----------o------o---------o-----o-o----
----------o----o-------o----o--o------o------------o---o---------------oo----o-----ooo--------------
----o--------oo----o-o----o--o------ooo----o-oooo---o--o-oo--------o-oo-----o-o---o-o--o-----oo-----
------o--------o-ooooo----o---o--o-----o---------------o-o-------o-----o----------------------------
o-------oo----o--oooooo-o---o--o------oooo----------o-oo-------o---o----------o------oo-------------
-o---o----------o--oo-oo-o---o-----o-o-----------------------oo--o------o------o--------------------
-----oo-o-o-o---ooooooooo----o----o--------o--o---oo---o------------o----------o-o---o------o-o--oo-
------o------o---ooo-o---------------------------o--o---o---o----o--o-------o-----o------o----o----o
-------o----------ooo-o-----o----o---o--o-oo--o--o-o--o------o--o-oo---ooo------------------------o-
-o-------o------o-o--ooo--o---o---oo-----o----o-------------o----o-ooo-o------o--o-o------o-o-------
---oo--o---o-o---------o---o--------------o--o-----o-------o-----o--o---o-oo--------o----o----o-----
o------o----oo-o-----------oo--o---o--------o-o------o-------o-o------o-oo---------o-----oo---------
----o--o---o-o-----------o---o------------o-------o----o--o--o--o-o---------------o-----------------
-------oo--o-o-----o-----o----o-o--o----------------------o-------o------o----oo----ooo---------o---
o-----oo-------------------o--o-----o-----------o------o-------o----o-----------o----------------o--
--o---o-------o------------o--------------------o----o--o-------------oo---o---------oo--------o----
--o--------o---------o------------o------o-------o------------o-------o---o---------ooooo-----------
------o--------------o-o-o---------o---o-------o--o-----o-------o-o----------o-----oo-ooo----------o
--o---------------o----o--oo-------------o---------o-------------------oo---------oo-o-ooo----------
-o-----------o------ooo----o----------------ooo-----o--------o--o---o-----------o-o-oooooo--------oo
-o---o-------o---o-oooo-----o-------------------o----oo-----------------o--o--------o--o------o--o--
-------o---o------oooooo--o----ooo--o--------o-------o----------------------------oo-oo-o--o--------
o--oo------o-----oo--o-oo------------oo--o------o--o-------------oo----o------------oooo-o------oo--
-----o----------ooooooooo--------------oo--------------oo-----o-----o-o--o------o----------o----o---
~~~~
