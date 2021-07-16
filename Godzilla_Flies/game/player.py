from random import randint

import arcade
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature

from game.constants import *


class Player(Creature):
    def __init__(self, sprite):
        self.sprite_list = ['./assets/Sprites/fly.png', "./assets/Sprites/spider.png", './assets/Sprites/tweety_bird.png', './assets/Sprites/cat.png',
                             './assets/Sprites/shark.png', './assets/Sprites/godzilla_fly.png']

        self.cur_sprite = self.sprite_list[0]



        super().__init__(self.cur_sprite, PLAYER_SCALING, PLAYER_MOVEMENT_SPEED)

        self.sprite_list = ['./assets/Sprites/fly.png', "./assets/Sprites/spider.png",
                            './assets/Sprites/tweety_bird.png', './assets/Sprites/cat.png',
                            './assets/Sprites/shark.png', './assets/Sprites/godzilla_fly.png']

        for item in self.sprite_list:
            self.append_texture(arcade.load_texture(item))

        self.sprite_index = 0

        self.force_field = False




    def consume(self, prey):

        prey.remove_from_sprite_lists()
        # print("Player has consumed")



        pass

    def get_location(self):

        return self.center_x, self.center_y

    def evolve(self):
        # print("Player is evolving!")

        self.sprite_index += 1

        self.cur_sprite = self.sprite_list[self.sprite_index]

        self.set_texture(self.sprite_index + 1)

        self.changed = True

        pass