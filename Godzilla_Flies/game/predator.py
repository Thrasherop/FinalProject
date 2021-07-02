from random import randint, choice
from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
from game.creature import Creature
from game.player import Player


from project_template.Godzilla_Flies.game.constants import *


class Predator(Creature):
    def __init__(self, sprite, scaling, point_value, player):
        super().__init__(sprite, scaling, ENEMY_MOVEMENT_SPEED)
        self.point_value = point_value
        self.target = player

    def move(self):
        # self.change_y = randint(0, self.speed) * choice((-1, 1))
        # self.change_x = randint(0, self.speed - abs(self.change_y)) * choice((-1, 1))

        self.change_y = 100
        self.change_x = 100

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

        print(player.get_location())



