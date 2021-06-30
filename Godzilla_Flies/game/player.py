from random import randint
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature


class Player(Creature):
    def __init__(self, sprite):
        super().__init__(sprite, PLAYER_MOVEMENT_SPEED)