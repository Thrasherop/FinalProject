from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
from game.player import Player
import math
from time import time
import arcade



class Entity(Creature):
    def __init__(self, sprite, scaling, point_value, player, type, cur_evolution = 0):

        self.type = type


        if self.type == PREDATOR:
            self.sprite_list = ["./assets/spider.png", './assets/tweety_bird.png', './assets/cat.png',
                                './assets/shark.png', './assets/godzilla_fly.png']

            self.cur_sprite = self.sprite_list[0]

            super().__init__(self.cur_sprite, scaling, ENEMY_MOVEMENT_SPEED)

            self.point_value = point_value
            self.target = player
            self.spawn()

            for item in self.sprite_list:
                self.append_texture(arcade.load_texture(item))

            self.sprite_index = 0

        else:
            self.sprite_list = ['./assets/poop.png', './assets/fly.png', "./assets/spider.png",
                                './assets/tweety_bird.png', './assets/cat.png',
                                './assets/shark.png', './assets/godzilla_fly.png']



            self.cur_sprite = self.sprite_list[cur_evolution]

            super().__init__(self.cur_sprite, scaling, ENEMY_MOVEMENT_SPEED)
            self.point_value = point_value
            self.target = player
            self.spawn()

            for item in self.sprite_list:
                self.append_texture(arcade.load_texture(item))

            self.sprite_index = cur_evolution

    def spawn(self):
        while True:
            x, y = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
            x_diff = abs(self.center_x - x)
            y_diff = abs(self.center_y - y)
            if x_diff > PREDATOR_SPAWN_DISTANCE and y_diff > PREDATOR_SPAWN_DISTANCE:
                break
        self.position = [x, y]

    def move(self):
        # Get the distance to the player
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()
        distance = math.sqrt(dx*dx + dy*dy)

        # Player is in range: attack
        if distance < KILL_RANGE:
            if self.type == PREDATOR: #predator
                self._chase_player()

            else: #prey
                self._escape_player()

        # Player is out of range: wander
        else:
            #self._wander()
            pass


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

        self.type = PREDATOR 