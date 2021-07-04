from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
import math


class Prey(Creature):
    def __init__(self, sprite, scaling, point_value, player):
        super().__init__(sprite, scaling, ENEMY_MOVEMENT_SPEED)
        self.point_value = point_value
        self.target = player
        self.spawn()

    def spawn(self):
        while True:
            x, y = randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)
            x_diff = abs(self.center_x - x)
            y_diff = abs(self.center_y - y)
            if x_diff > PREY_SPAWN_DISTANCE and y_diff > PREY_SPAWN_DISTANCE:
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
        self.change_x = -cx
        self.change_y = -cy
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
        self.move()

    def interaction(self, player):

        player.consume()
        self.remove_from_sprite_lists()
    
    def get_points(self):
        return self.point_value

