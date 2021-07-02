
## Overview

You begin life as a lonely fly, trying to avoid being eaten by predators. However, once you eat
some food, YOU become the predator. Your previous enemies will begin fleeing from your presence.
Continue consuming to continue evolving, but make sure to watch the time limit!


## Technologies

This game will rely on the following technologies:

* Python 3
* the arcade module


## Features

This game will have a number of python classes, all handling different aspects of the game
(see included file "class_layout.pdf")

## Timeline:

* By June 26th, we will have an alpha release that has basic functionality
* By July 3rd, we will have all features implemented in a beta
* By July 10th, we will begin rolling out release candidates
* Finally, by July 17th, we will have a stable release

## HEIRARCHY

* Poop, Breadcrumbs
* Fly, Ant
* Spider, Dragon Fly
* Tweety Bird, Praying Mantis
* Cat, Hawk, Electric Eel
* Shark (rare), Wolf
* Godzilla Fly

## ABILITIES
* Poop: Safety
* Breadcrumbs: Speed
* Fly: Speed
* Ant: Time
* Spider: Safety
* Dragon Fly: Fire Breathing
* Tweety Bird: Time
* Praying Mantis: Speed
* Cat: Time (adds 9?)
* Hawk: Safety
* Electric Eel: Makes you look cool, Force Field (Only a chance of getting force field)
* Shark: Safety and Speed
* Wolf: Speed
* Godzilla Fly: All of the above

* Speed: Breadcrumbs, Fly, Praying Mantis
* Safety (slows enemies): Poop, Electric Eels, Spider
* Time (Adds): Ant, Tweety Bird, Cat
* Fire Breathing (Longer reach): Dragon Fly
* Force Field: Eel

## IDEAS
* Once you get to Godzilla status, you have to eat enough to impress your mate so that you can breed.
* Once you breed, you spawn as a fly again.

* To attract the Godzilla mate, you have to go around and collect all of the abilities.
* Show a progress bar of the abilities you've collected.

* Create an Ability class

## Priorities

0) Player Movement
1) Enemy/food spawning
2) Timer
2) Score
3) Enemy/food movement
3) Death (Start/End)
4) Evolution (Sprites and Background)
4) New Godzilla Fly (Difficulty Increase)
4) Abilities
4) Enemy Adrenaline Boost (when they see you)