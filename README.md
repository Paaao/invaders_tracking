# Invaders tracking application

## Finished development assignment
Application must take a radar sample as an argument and reveal possible locations of pesky invaders.


There is a lot of space for improvement :) of the application, like:
- making it possible for users to change options with arguments (not making it only hard-coded)
- saving all found matches and then choosing best ones within perimeter (now when first match found application is skipping columns by provided offset in order to not count same invaders twice)
- option to save output as .html (or even image) file with highlighted invaders on radar image
- making some details (like saving output to file) optional
- rotating radar image to not miss invaders which are “falling” and not just nicely descending :)


### Known invaders:
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

### Example radar sample:
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

### Example of output with invaders overlay:
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

