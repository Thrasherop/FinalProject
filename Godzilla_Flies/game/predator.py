from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
from game.player import Player
import math
import arcade


from game.constants import *


class Predator(Creature):
    def __init__(self, sprite, scaling, point_value, player):

        self.sprite_list = ["./assets/spider.png", './assets/tweety_bird.png', './assets/cat.png',
                             './assets/shark.png', './assets/godzilla_fly.png']


        self.cur_sprite = self.sprite_list[0]

        super().__init__(sprite, scaling, ENEMY_MOVEMENT_SPEED)


        self.point_value = point_value
        self.target = player
        self.spawn()

        for item in self.sprite_list:
            self.append_texture(arcade.load_texture(item))

        self.sprite_index = 0

    def spawn(self):
        while True:
            x, y = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
            x_diff = abs(self.center_x - x)
            y_diff = abs(self.center_y - y)
            if x_diff > PREDATOR_SPAWN_DISTANCE and y_diff > PREDATOR_SPAWN_DISTANCE:
                break
        self.position = [x, y]

    def move(self):
        # self.change_y = randint(0, self.speed) * choice((-1, 1))
        # self.change_x = randint(0, self.speed - abs(self.change_y)) * choice((-1, 1))
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()

        #Get the hypotenuse
        d = math.sqrt(dx*dx + dy*dy)

        #Calculate the change to the enemy position
        cx = self.speed * dx / d
        cy = self.speed * dy / d
        # Note that sqrt(cx*cx + cy*cy) == speed

        # Update enemy position
        self.change_x = cx
        self.change_y = cy


        self.boundary_check()

    def boundary_check(self):
        # Adjust for boundary if needed
        # # Top
        if self._get_top() > SCREEN_HEIGHT - 1:
            self.change_y = 0
            self._set_top(SCREEN_HEIGHT - 1)
        # # Bottom
        elif self._get_bottom() < 0:
            self.change_y = 0
            self._set_bottom(0)
        # # Left
        if self._get_left() < 0:
            self.change_x = 0
            self._set_left(0)
        # # Right
        elif self._get_right() > SCREEN_WIDTH - 1:
            self.change_x = 0
            self._set_right(SCREEN_WIDTH - 1)

    def update(self):
        self._go_to_player(self.target)
        self.move()


    def interact(self, other):

        if isinstance(other, Player):
            other.remove_from_sprite_lists()

    def _go_to_player(self, player):

        #print(player.get_location())
        pass

    def evolve(self):

        print("Predator is evolving!")

        self.sprite_index += 1

        self.cur_sprite = self.sprite_list[self.sprite_index]

        self.set_texture(self.sprite_index + 1)

        self.changed = True

        pass


