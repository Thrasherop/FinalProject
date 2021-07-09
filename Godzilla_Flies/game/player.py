from random import randint
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
#from game.ability import Ability

from game.constants import *


class Player(Creature):
    def __init__(self, sprite):
        super().__init__(sprite, PLAYER_SCALING, PLAYER_MOVEMENT_SPEED)
        self.force_field = False
    def consume(self, prey):

        prey.remove_from_sprite_lists()
        print("Player has consumed")

        pass

    def get_location(self):

        return self.center_x, self.center_y