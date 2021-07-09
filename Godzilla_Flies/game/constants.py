import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Godzilla Flies"

MARGIN = 65

SCALING = .15

PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 2

PREDATOR_SCALING = .4
PLAYER_SCALING = .3
PREY_SCALING = .15

NUMBER_OF_PRADATORS = 3
NUMBER_OF_PREY = 5

PREY_SPAWN_DISTANCE = 100
PREDATOR_SPAWN_DISTANCE = 500

KILL_RANGE = PREDATOR_SPAWN_DISTANCE * 5 / 8

PATH = os.path.dirname(os.path.abspath(__file__))
FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'fly.png')
POOP_IMAGE = os.path.join(PATH, '..', 'assets', 'poop.png')
SPIDER_IMAGE = os.path.join(PATH, '..', 'assets', 'spider.png')
LEVEL_1_PREY_IMAGES = []