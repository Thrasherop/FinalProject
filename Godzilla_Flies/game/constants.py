import os

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Godzilla Flies"
CAUTION_BACKGROUND = (181, 93, 69)
SAFE_BACKGROUND = (200, 200, 200)
DANGER_BACKGROUND = (189, 32, 32)


MARGIN = 65

SCALING = .15

PLAYER_MOVEMENT_SPEED = 5
ENEMY_MOVEMENT_SPEED = 2

PREDATOR = 1
PREY = 0

TIMER_TIME = 11

PREDATOR_SCALING = .4
PLAYER_SCALING = .3
PREY_SCALING = .15
DEATH_SCALING = 1
VICTORY_SCALING = 1

NUMBER_OF_PRADATORS = 3
NUMBER_OF_PREY = 5

PREY_SPAWN_DISTANCE = 100
PREDATOR_SPAWN_DISTANCE = 200

PREDATOR_KILL_RANGE = PREDATOR_SPAWN_DISTANCE * 3 / 8
PREY_KILL_RANGE = PREY_SPAWN_DISTANCE * 5 / 8

PATH = os.path.dirname(os.path.abspath(__file__))
FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'fly.png')
POOP_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'poop.png')
SPIDER_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'spider.png')
DEATH_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'Death.png')
VICTORY_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'victory.png')
MANTIS_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'praying_mantis.png')
DRAGON_FLY_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'dragon_fly.png')
SHARK_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'shark.png')
WOLF_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'wolf.png')
CAT_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'cat.png')
BIRD_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'tweety_bird.png')
GODZILLA_IMAGE = os.path.join(PATH, '..', 'assets', 'Sprites', 'godzilla_fly.png')
LEVEL_1_PREY_IMAGES = []


# Sets the sound paths

SOUND_VOLUME = .8
CONSUME_DELAY = 2

FLY_SOUND_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'FLY_SOUND_EAT.m4a')
FLY_SOUND_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'FLY_SOUND_DEATH.m4a')
SPIDER_SOUND_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'spider_eat.mp3')
SPIDER_SOUND_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'spider_death.mp3')
BIRD_SOUND_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'bird_eating.m4a')
BIRD_SOUND_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'bird_death.mp3')
CAT_SOUND_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'CAT_SOUND_EAT.m4a')
CAT_SOUND_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'catDeath.m4a')
SHARK_SOUND_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'sharkEat.m4a')
SHARK_SOUND_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'sharkDeath.m4a')
GODZILLA_EAT = os.path.join(PATH, '..', 'assets', 'Audio', 'godzilla_eating.m4a')
GODZILLA_WIN = os.path.join(PATH, '..', 'assets', 'Audio', 'godzilla_win.m4a')
POOP_DEATH = os.path.join(PATH, '..', 'assets', 'Audio', 'POOP_DEATH.m4a')

FOO_SOUND = os.path.join(PATH, '..', 'assets', 'Audio', 'fooRecording.m4a')