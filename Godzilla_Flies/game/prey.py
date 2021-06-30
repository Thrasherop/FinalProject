from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature


class Prey(Creature):
    def __init__(self, sprite, point_value, player):
        super().__init__(sprite, ENEMY_MOVEMENT_SPEED)
        self.point_value = point_value
        self.target = player

    def move(self):
        self.sprite.change_y = randint(0, self.speed) * choice((-1, 1))
        self.sprite.change_x = randint(0, self.speed - abs(self.sprite.change_y)) * choice((-1, 1))

        self.boundary_check()

    def boundary_check(self):
        # Adjust for boundary if needed
        # # Top
        if self.sprite._get_top() > SCREEN_HEIGHT - 1:
            self.sprite.change_y = 0
            self.sprite._set_top(SCREEN_HEIGHT - 1)
        # # Bottom
        elif self.sprite._get_bottom() < 0:
            self.sprite.change_y = 0
            self.sprite._set_bottom(0)
        # # Left
        if self.sprite._get_left() < 0:
            self.sprite.change_x = 0
            self.sprite._set_left(0)
        # # Right
        elif self.sprite._get_right() > SCREEN_WIDTH - 1:
            self.sprite.change_x = 0
            self.sprite._set_right(SCREEN_WIDTH - 1)

    def update(self):
        self.move()