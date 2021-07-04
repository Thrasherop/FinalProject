from random import randint

from arcade.physics_engines import PhysicsEngineSimple

try: 
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

    from game.prey import Prey
    from game.creature import Creature
    from game.player import Player
    from game.predator import Predator
    from game.score import *

    import arcade

except:
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

    from game.prey import Prey
    from game.creature import Creature
    from game.player import Player
    from game.predator import Predator
    from game.score import *

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
        self.level = 0
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

        # Initialize the score class
        self.score = Score()

        # Set up the player
        self.player_sprite = Player(FLY_IMAGE)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)


        # self.all_sprites.append(self.player_sprite)
        # self.all_sprites.append(self.predator_list)

        # Set up the prey
        coordinate_list = [[512, 200], [256, 300], [786, 300]]
        for coordinate in coordinate_list:
            # prey = arcade.Sprite(POOP_IMAGE, SCALING)
            prey = Prey(POOP_IMAGE, PREY_SCALING, 1, self.player_sprite)
            prey.position = coordinate
            self.prey_list.append(prey)
            # self.all_sprites.append(prey)
        # Set up the predator
        coordinate_list = [[512, 100], [256, 100], [786, 100]]
        for coordinate in coordinate_list:
            # predator = arcade.Sprite(SPIDER_IMAGE, PREDATOR_SCALING)
            predator = Predator(SPIDER_IMAGE, PREDATOR_SCALING, 1, self.player_sprite)
            predator.position = coordinate
            self.predator_list.append(predator)
            # self.all_sprites.append(predator)

        # Physics engine for player
        self.physics_engine = PhysicsEngineSimple(self.player_sprite, self.all_sprites)

        self.predator_engines = []

        for predator in self.predator_list:

            self.predator_engines.append(PhysicsEngineSimple(predator, self.all_sprites))

        self.prey_engines = []

        for prey in self.prey_list:

            self.prey_engines.append(PhysicsEngineSimple(prey, self.all_sprites))

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
        arcade.draw_text(str(self.score.get_score()), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 25, arcade.color.BLACK, 12, anchor_x = "right", anchor_y = "top")

    def on_update(self, delta_time):
        """Movement and gane logic"""


        # Move the player with the physics engine
        self.physics_engine.update()

        # Moves predators
        for engine in self.predator_engines:
            engine.update()
        for predator in self.predator_list:
            predator.update()

        # Moves prey
        for engine in self.prey_engines:
            engine.update()
        for prey in self.prey_list:
            prey.update()



        # See if we hit anything
        self.check_for_collisions()
        

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

    def check_for_collisions(self):
        prey_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.prey_list)

        predator_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.predator_list)

        if len(predator_hit_list) > 0:
           self.player_lost()

        # Loop through each coin we hit (if any) and remove it
        for prey in prey_hit_list:
            # Remove the coin
            # prey.remove_from_sprite_lists()
            self.player_sprite.consume(prey)
            self.score.add_score(prey.get_points())
            print(self.score.get_score())

            # upgrade
            self.level += 1

            if self.level == 1:
                pass    
            # Play a sound
            #arcade.play_sound()

    def player_lost(self):
        # TODO Finish this
        self.player_sprite.remove_from_sprite_lists()
        print("Player has perished")

        pass





def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()