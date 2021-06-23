from random import randint

from arcade.physics_engines import PhysicsEngineSimple
from game.constants import *
#from game.point import Point
"""
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService# program entry point
"""

import arcade

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Pick background color
        arcade.set_background_color((200, 200, 200))

        # Sprite libraries
        self.prey_list = None
        self.predator_list = None
        self.player_list = None
        self.player_sprite = None
        self.all_sprites = arcade.SpriteList(use_spatial_hash=True)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Initialize the sprite variables with classes
        self.player_list = arcade.SpriteList()
        self.prey_list = arcade.SpriteList(use_spatial_hash=True)
        self.predator_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player
        self.player_sprite = arcade.Sprite(FLY_IMAGE, SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)
        self.all_sprites.append(self.player_sprite)

        # Set up the prey
        coordinate_list = [[512, 300], [256, 300], [786, 300]]
        for coordinate in coordinate_list:
            predator = arcade.Sprite(POOP_IMAGE, SCALING)
            predator.position = coordinate
            self.predator_list.append(predator)
            self.all_sprites.append(predator)
        # Set up the predator
        coordinate_list = [[512, 100], [256, 100], [786, 100]]
        for coordinate in coordinate_list:
            predator = arcade.Sprite(SPIDER_IMAGE, SCALING)
            predator.position = coordinate
            self.predator_list.append(predator)
            self.all_sprites.append(predator)

        # Physics engine
        self.physics_engine = PhysicsEngineSimple(self.player_sprite, self.all_sprites)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, key, modifiers):
        """Called whenever a key is released."""
        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A or key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Sprites
        self.prey_list.draw()
        self.predator_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """Movement and gane logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # Adjust for boundary if needed
        # # Top
        if self.player_sprite._get_top() > SCREEN_HEIGHT - 1:
            self.player_sprite.change_y = 0
            self.player_sprite._set_top(SCREEN_HEIGHT - 1)
        # # Bottom
        elif self.player_sprite._get_bottom() < 0:
            self.player_sprite.change_y = 0
            self.player_sprite._set_bottom(0)
        # # Left
        if self.player_sprite._get_left() < 0:
            self.player_sprite.change_x = 0
            self.player_sprite._set_left(0)
        # # Right
        elif self.player_sprite._get_right() > SCREEN_WIDTH - 1:
            self.player_sprite.change_x = 0
            self.player_sprite._set_right(SCREEN_WIDTH - 1)

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()