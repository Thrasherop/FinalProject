from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
<<<<<<< HEAD

from game.constants import ENEMY_MOVEMENT_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
=======
import math
from time import time
>>>>>>> feee3cc871a288b3995bddf3d691b66ed64762fc


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
        # Get the distance to the player
        dx = self.target._get_center_x() - self._get_center_x()
        dy = self.target._get_center_y() - self._get_center_y()
        distance = math.sqrt(dx*dx + dy*dy)

        # Player is in range: run
        if distance < KILL_RANGE:
            self._escape_player()
        # Player is out of range: wander
        else:
            self._wander()


        self.boundary_check()

    def update(self):
        self.move()

    def interaction(self, player):

        player.consume()
        self.remove_from_sprite_lists()
    
    def get_points(self):
        return self.point_value

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

