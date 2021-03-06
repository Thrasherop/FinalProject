from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
from game.player import Player
import math
from time import time
import arcade
import random



class Entity(Creature):
    def __init__(self, sprite, scaling, point_value, player, type, cur_evolution = 0, randomize_sprite = False):

        self.type = type


        if self.type == PREDATOR:
            self.sprite_list = [SPIDER_IMAGE, BIRD_IMAGE, CAT_IMAGE,
                                SHARK_IMAGE, GODZILLA_IMAGE]

            self.cur_sprite = self.sprite_list[0]

            super().__init__(self.cur_sprite, scaling, ENEMY_MOVEMENT_SPEED)

            self.point_value = point_value
            self.target = player
            self.spawn()

            for item in self.sprite_list:
                self.append_texture(arcade.load_texture(item))

            self.sprite_index = 0

            self._update_interval = 3

        else:
            self.sprite_list = [POOP_IMAGE, FLY_IMAGE, SPIDER_IMAGE,
                                BIRD_IMAGE, CAT_IMAGE,
                                SHARK_IMAGE, GODZILLA_IMAGE]



            self.cur_sprite = self.sprite_list[cur_evolution]

            super().__init__(self.cur_sprite, scaling, ENEMY_MOVEMENT_SPEED)
            self.point_value = point_value
            self.target = player
            self.spawn()

            for item in self.sprite_list:
                self.append_texture(arcade.load_texture(item))

            self.sprite_index = cur_evolution

            self._update_interval = 1.5

        if randomize_sprite:
            self.randomize_sprite()

    def spawn(self):
        if self.type:  # Predator
            safe_zone = PREDATOR_SPAWN_DISTANCE
        else:
            safe_zone = PREY_SPAWN_DISTANCE
        while True:
            x, y = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
            x_diff = abs(self.target.center_x - x)
            y_diff = abs(self.target.center_y - y)
            diff = math.sqrt(x_diff**2 + y_diff**2)
            if diff > safe_zone:
                break
        self.center_x = x
        self.center_y = y

    def move(self):
        # Get the distance to the player
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()
        distance = math.sqrt(dx*dx + dy*dy)

        if self.type == PREDATOR: run_range = PREDATOR_KILL_RANGE
        else: run_range = PREY_KILL_RANGE

        # Player is in range: attack
        if distance < run_range:
            self._last_update = time()
            if self.type == PREDATOR: #predator
                self._chase_player()

            else: #prey
                self._escape_player()

        # Player is out of range: wander
        else:
            self._wander()


        self.boundary_check()

    def update(self):
        self.move()

    def get_points(self):
        return self.point_value

    # prey
    def _escape_player(self):
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()

        # a^2 + b^2 = c^2
        d = math.sqrt(dx*dx + dy*dy)

        # Calculate change for my position
        cx = self.speed * dx / d
        cy = self.speed * dy / d

        # Update my position
        self.change_x = -cx
        self.change_y = -cy

        # Update movement variables
        self._last_change = time()
        self._auto = True

    # predator
    def _chase_player(self):
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()

        # a^2 + b^2 = c^2
        d = math.sqrt(dx*dx + dy*dy)

        # Calculate change for my position
        cx = self.speed * dx / d
        cy = self.speed * dy / d

        # Update my position
        self.change_x = cx
        self.change_y = cy

        # Update movement variables
        self._last_change = time()
        self._auto = True

    def interact(self, prey, predator, player):
        
        if isinstance(predator, Player):
            predator.remove_from_sprite_lists()
        elif isinstance(prey, Player):
            player.consume()
            prey.remove_from_sprite_lists()


    def evolve(self):

        # self.type = PREDATOR


        # ("Predator is evolving!")

        self.sprite_index += 1

        self.cur_sprite = self.sprite_list[self.sprite_index]

        self.set_texture(self.sprite_index + 1)

        self.changed = True

    def devolve(self):
        # print("Devolving")

        self.sprite_index -= 1
        self.cur_sprite = self.sprite_index[self.sprite_list]

        self.set_texture(self.sprite_index + 1)

        self.changed = True

    def remove(self):

        self.remove_from_sprite_lists()

    def randomize_sprite(self):

        # print("Randomizing a sprite")
        #new_sprite = random.choice[self.sprite_list]

        self.sprite_index = random.randint(1, len(self.sprite_list)) - 1

        # print(self.sprite_index)

        self.cur_sprite = self.sprite_list[self.sprite_index]

        self.set_texture(self.sprite_index + 1)

        self.changed = True