import arcade
from game.constants import *
import math
import game.player
import game.prey
import game.predator


class Ability(arcade):
    def __init__(self, player, predator, prey):
        self.player = player
        self.predator = predator
        self.prey = prey
        
        
        

    def speed_up(self, add):
        self.player.speed += add
        return self.player.speed

    def safety(self, lower):
        self.predator.speed += (-lower)
        self.prey.speed += (-lower)
        return self.predator.speed and self.prey.speed
        

    def add_time(self, time):
        self.arcade.time += time
        return self.time

    def longer_reach(self, distance):
        self.fire_breathing += distance
        return self.fire_breathing

    def force_field(self):
        self.player.force_field = True
        return self.player.force_field
