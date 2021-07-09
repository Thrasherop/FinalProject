from random import randint
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
import arcade
from abc import ABC, abstractmethod



class Creature(arcade.Sprite):
    def __init__(self, sprite, scaling, speed):
        super().__init__(sprite, scaling)
        
        self.speed = speed
        #sself.sprite_list = []
        self.evolution_index = 0


    @abstractmethod
    def evolve(self):
        pass
