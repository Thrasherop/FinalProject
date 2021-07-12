from random import randint

from arcade.physics_engines import PhysicsEngineSimple

from time import time
import arcade

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
    from game.score import Score
    from game.timer import Timer
    

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
    from game.score import Score
    from game.timer import Timer

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Pick background color
        arcade.set_background_color((200, 200, 200))
        
        # Prey
        self.prey_list = None
        self.prey_engines = []
        # Predators
        self.predator_list = None
        self.predator_engines = []
        # Player
        self.player_list = None
        self.player_sprite = None

        #UI
        self.ui_list = arcade.SpriteList()
        self.is_over = False

        # Other
        self.all_sprites = arcade.SpriteList(use_spatial_hash=True)
        self.level = 0
        self.evolve_status = 0

        self.cur_evolution = 0


    def spawn_player(self):
        self.player_sprite = Player(FLY_IMAGE)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)

        self.physics_engine = PhysicsEngineSimple(self.player_sprite, self.all_sprites)

    def spawn_prey(self):
        prey = Prey(POOP_IMAGE, PREY_SCALING, 1, self.player_sprite, self.cur_evolution)
        self.prey_list.append(prey)
        self.prey_engines.append(PhysicsEngineSimple(prey, self.all_sprites))

    def spawn_predator(self):
        predator = Predator(SPIDER_IMAGE, PREDATOR_SCALING, 1, self.player_sprite)
        self.predator_list.append(predator)
        self.predator_engines.append(PhysicsEngineSimple(predator, self.all_sprites))


    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Initialize the sprite variables with classes
        self.player_list = arcade.SpriteList()
        self.prey_list = arcade.SpriteList(use_spatial_hash=True)
        self.predator_list = arcade.SpriteList(use_spatial_hash=True)

        # Initialize the score class
        self.score = Score()
        # Initialize the timer class
        self.timer = Timer()
        self.timer.set_time(60)
        self.start_time = time()
        self.total_time = 0

        # Set up the player
        self.spawn_player()


        # self.all_sprites.append(self.player_sprite)
        # self.all_sprites.append(self.predator_list)

        # Set up the prey
        for i in range(NUMBER_OF_PREY):
            self.spawn_prey()
        # Set up the predator
        for i in range(NUMBER_OF_PRADATORS):
            self.spawn_predator()

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
        if True: #not self.is_over:
            arcade.start_render()

            # Sprites
            self.prey_list.draw()
            self.predator_list.draw()
            self.player_list.draw()
            arcade.draw_text(str(self.score.get_score()), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 25, arcade.color.BLACK, 12, anchor_x = "right", anchor_y = "top")


        self.ui_list.draw()

        # Sprites
        self.prey_list.draw()
        self.predator_list.draw()
        self.player_list.draw()
        arcade.draw_text(str(f"Score:  {self.score.get_score()}"), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 25, arcade.color.BLACK, 12, anchor_x = "right", anchor_y = "top")
        arcade.draw_text(str(f"Seconds: {int(self.timer.get_time())}"), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 40, arcade.color.BLACK, 12, anchor_x = "right", anchor_y = "top")


    def on_update(self, delta_time):
        """Movement and game logic"""



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

        old_total = self.total_time
        self.total_time = time() - self.start_time

        self.timer.lose_time(self.total_time - old_total)

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
            self.spawn_prey()
            self.score.add_score(prey.get_points())
            self.evolve_status += 1
            #print(self.score.get_score())

            # upgrade
            self.level += 1

            if self.level == 1:
                pass    
            # Play a sound
            #arcade.play_sound()

        if self.evolve_status >= 5:
            self.evolve()
            self.evolve_status = 0

    def player_lost(self):
        # TODO Finish this
        self.player_sprite.remove_from_sprite_lists()
        self.score = Score()
        #self.spawn_player() Don't respawn player

        print(self.is_over)

        if not self.is_over:
            loss_sprite = arcade.Sprite(DEATH_IMAGE, DEATH_SCALING)
            loss_sprite.center_x = SCREEN_WIDTH / 2
            loss_sprite.center_y = SCREEN_HEIGHT / 2
            self.ui_list.append(loss_sprite)
            self.is_over = True



            print("inside")


        for predator in self.predator_list:
            predator.target = self.player_sprite

        for prey in self.prey_list:
            prey.target = self.player_sprite

        print("Player has perished")

        pass

    def evolve(self):

        print("\n\n\n Evolving")

        for thing in self.prey_list:
            thing.evolve()

        for thing in self.predator_list:
            thing.evolve()

        for thing in self.player_list:
            thing.evolve()

        self.cur_evolution += 1

        pass


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()