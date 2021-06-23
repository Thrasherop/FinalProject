import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

MARGIN = 65

SCALING = .25

PLAYER_MOVEMENT_SPEED = 5

PATH = os.path.dirname(os.path.abspath(__file__))
FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'fly.png')
POOP_IMAGE = os.path.join(PATH, '..', 'assets', 'poop.png')
SPIDER_IMAGE = os.path.join(PATH, '..', 'assets', 'spider.png')
LEVEL_1_PREY_IMAGES = []