import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Godzilla Flies"

MARGIN = 65

SCALING = .15

PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 2

PREDATOR = 1
PREY = 0

TIMER_TIME = 15

PREDATOR_SCALING = .4
PLAYER_SCALING = .3
PREY_SCALING = .15
DEATH_SCALING = 1

NUMBER_OF_PRADATORS = 3
NUMBER_OF_PREY = 5

PREY_SPAWN_DISTANCE = 200
PREDATOR_SPAWN_DISTANCE = 600

PREDATOR_KILL_RANGE = PREDATOR_SPAWN_DISTANCE * 3 / 8
PREY_KILL_RANGE = PREY_SPAWN_DISTANCE * 5 / 8

PATH = os.path.dirname(os.path.abspath(__file__))
FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'fly.png')
POOP_IMAGE = os.path.join(PATH, '..', 'assets', 'poop.png')
SPIDER_IMAGE = os.path.join(PATH, '..', 'assets', 'spider.png')
DEATH_IMAGE = os.path.join(PATH, '..', 'assets', 'Death.png')
MANTIS_IMAGE = os.path.join(PATH, '..', 'assets', 'praying_mantis.png')
DRAGON_FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'dragon_fly.png')
LEVEL_1_PREY_IMAGES = []