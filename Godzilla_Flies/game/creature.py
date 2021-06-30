from random import randint
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
import arcade.sprite



class Creature(arcade.sprite):
    def __init__(self, sprite, speed):
        super().__init__()
        self.sprite = sprite
        self.sprite.center_x = SCREEN_WIDTH / 2
        self.sprite.center_y = SCREEN_HEIGHT / 2
        
        self.speed = speed

