from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
import arcade

from abc import ABC, abstractmethod

from time import time




class Creature(arcade.Sprite):
    def __init__(self, sprite, scaling, speed):
        super().__init__(sprite, scaling)
        
        # Movement variables
        self.speed = speed

        #sself.sprite_list = []
        self.evolution_index = 0

        self._last_change = time()
        self._auto = False
        self._update_interval = 5


    @abstractmethod
    def evolve(self):
        pass

        self._last_change = time()
        self._auto = False


    def boundary_check(self):
        # Adjust for boundary if needed
        # # Top
        if self._get_top() > SCREEN_HEIGHT - 1:
            self.change_y *= -1
            self._set_top(SCREEN_HEIGHT - 1)
        # # Bottom
        elif self._get_bottom() < 0:
            self.change_y *= -1
            self._set_bottom(0)
        # # Left
        if self._get_left() < 0:
            self.change_x *= -1
            self._set_left(0)
        # # Right
        elif self._get_right() > SCREEN_WIDTH - 1:
            self.change_x *= -1
            self._set_right(SCREEN_WIDTH - 1)

    def _wander(self):
        """Randomly wanders the character around. Every time interval the creature switches from moving to pausing"""
        if time() - self._last_change > self._update_interval:
            self._last_change = time()

            # Continue movement
            if self.change_y == 0 and self.change_x == 0:
                # Choose a random movement direction
                direction = choice(((0, self.speed), (0, -self.speed), (self.speed, 0), (-self.speed, 0)))
                self.change_x = direction[0]
                self.change_y = direction[1]
 

            # Stall movement
            else:
                self.change_x = 0
                self.change_y = 0

        if self._auto:
            self.change_x = 0
            self.change_y = 0
            self._auto = False
            



