
from random import randint
from time import time

from arcade.physics_engines import PhysicsEngineSimple

from game.constants import *

from game.prey import Prey
from game.creature import Creature
from game.player import Player
from game.predator import Predator
from game.entity import Entity
from game.score import Score
from game.timer import Timer
from game.sound import Sound
import math

import arcade

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Pick background color
        arcade.set_background_color(SAFE_BACKGROUND)
        
        self.is_win = False
        # Prey
        self.prey_list = None
        self.prey_engines = []
        # Predators
        self.predator_list = None
        self.predator_engines = []
        # Player
        self.player_list = None
        self.player_sprite = None
        # Other
        self.all_sprites = arcade.SpriteList(use_spatial_hash=True)
        self.level = 0
        self.is_godzilla = False
        self.game_over = False
        self.game_over_message = ""
        self.sound_player = Sound()
        self.win_sound_played = False



        # UI
        self.ui_list = arcade.SpriteList()
        self.is_over = False

        # Evolve
        self.evolve_status = 0
        self.cur_evolution = 0



    def spawn_player(self):
        self.player_sprite = Player(FLY_IMAGE)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/2
        self.player_list.append(self.player_sprite)

        self.physics_engine = PhysicsEngineSimple(self.player_sprite, self.all_sprites)

    def spawn_prey(self):
        prey = Entity(POOP_IMAGE, PREY_SCALING, 1, self.player_sprite, PREY, self.cur_evolution, self.is_godzilla)
        self.prey_list.append(prey)
        self.prey_engines.append(PhysicsEngineSimple(prey, self.all_sprites))

    def spawn_predator(self):
        predator = Entity(SPIDER_IMAGE, PREDATOR_SCALING, 1, self.player_sprite, PREDATOR, self.cur_evolution, self.is_godzilla)
        self.predator_list.append(predator)
        self.predator_engines.append(PhysicsEngineSimple(predator, self.all_sprites))
        self.all_sprites.append(predator)

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
        self.timer.set_time(TIMER_TIME)
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
        if True:  # not self.is_over:
            arcade.start_render()

            # Sprites
            self.prey_list.draw()
            self.predator_list.draw()
            self.player_list.draw()
            arcade.draw_text(str(f"Score: {self.score.get_score()}"), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 25, arcade.color.STEEL_BLUE, 12,
                             anchor_x="right", anchor_y="top")


            if not self.game_over:
                arcade.draw_text(str(f"Seconds: {math.floor(self.timer.get_time())}"), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 40, arcade.color.STEEL_BLUE, 12, anchor_x = "right", anchor_y = "top")

            else:
                arcade.draw_text(str(f" {(self.game_over_message)}"), SCREEN_WIDTH - 25, SCREEN_HEIGHT - 40,
                                 arcade.color.STEEL_BLUE, 12, anchor_x="right", anchor_y="top")

        self.ui_list.draw()


        # Shows final challenge message
        if self.is_godzilla and not self.is_win:
            arcade.draw_text(str(f"QUICK! EAT AS MUCH AS YOU CAN!!"), SCREEN_WIDTH-180, SCREEN_HEIGHT - 100, arcade.color.STEEL_BLUE, 35, anchor_x="right", anchor_y="top")

        # Shows score if win screen is displayed
        if self.is_win:
            self.game_over_message = f"Your score was {self.score.get_score()}"
            arcade.draw_text(str(self.game_over_message), SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 200, arcade.color.STEEL_BLUE, 35, anchor_x="right", anchor_y="top")

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
        
        if self.is_godzilla and self.timer.get_time() < 0:
                # Remove all entities and display win image
                try:
                    while len(self.predator_list) > 0:
                        del self.predator_list[0]
                    while len(self.prey_list) > 0:
                        del self.prey_list[0]
                    self.player_sprite.remove_from_sprite_lists()
                    
                    self.player_win()
                except:
                    self.player_win()


        # See if we hit anything
        self.check_for_collisions()
        self.check_time()

        if self.evolve_status >= 5:
            self.evolve()
        

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
    
    def check_time(self):
        if self.timer.get_time() <= 0 and not self.is_godzilla:
            self.player_lost()
        if self.timer.get_time() < 3:
            arcade.set_background_color(DANGER_BACKGROUND)
        elif self.timer.get_time() < 5:
            arcade.set_background_color(CAUTION_BACKGROUND)
        else:
            arcade.set_background_color(SAFE_BACKGROUND)

    def check_for_collisions(self):
        prey_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.prey_list)

        predator_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.predator_list)

        if len(predator_hit_list) > 0:
            if self.player_sprite.force_field == False :
                self.player_lost()

        # Loop through each coin we hit (if any) and remove it
        for prey in prey_hit_list:

            # Plays consume and death sound
            self.sound_player.consume(self.cur_evolution)
            self.sound_player.death(self.cur_evolution - 1)

            # Remove the coin
            # prey.remove_from_sprite_lists()
            self.player_sprite.consume(prey)
            self.spawn_prey()
            self.score.add_score(prey.get_points())
            print(self.score.get_score())

            self.evolve_status += 1

            # upgrade
            self.level += 1

            if self.level == 1:
                pass    
            # Play a sound
            #arcade.play_sound()

    def player_lost(self):
        # TODO Finish this
        self.player_sprite.remove_from_sprite_lists()
        #self.score = Score()
        # self.spawn_player() Don't respawn player

        # Plays death sound
        if not self.game_over:
            self.sound_player.death(self.cur_evolution)
            self.sound_player.consume(self.cur_evolution + 1)

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

        self.game_over = True
        self.game_over_message = "You lost!"

        pass

    def player_win(self):
        self.is_win = True
        
        win_sprite = arcade.Sprite(VICTORY_IMAGE, VICTORY_SCALING)
        win_sprite.center_x = SCREEN_WIDTH / 2
        win_sprite.center_y = SCREEN_HEIGHT / 2
        self.game_over = True
        self.game_over_message = f"You won with a score of {self.score.get_score()}"

        self.ui_list.append(win_sprite)

        # Plays win sound if needed
        if not self.win_sound_played:
            sound = arcade.load_sound(VICTORY_SOUND)
            arcade.play_sound(sound, SOUND_VOLUME)
            self.win_sound_played = True

        

    def evolve(self):

        print("cur_evolution", self.cur_evolution)

        print("__main__ evolving!!")

        if self.cur_evolution < 4:

            for thing in self.predator_list:
                thing.evolve()



            for thing in self.prey_list:
                thing.evolve()

            for thing in self.player_list:
                thing.evolve()

            self.cur_evolution += 1
            self.timer.set_time(TIMER_TIME)

        elif self.cur_evolution == 4:
            if not self.is_godzilla:

                for thing in self.predator_list:
                    thing.remove()
                    self.spawn_prey()

                for thing in self.predator_list:
                    thing.remove()
                    self.spawn_prey()

                for thing in self.prey_list:
                    thing.randomize_sprite()

                for thing in self.player_list:
                    thing.evolve()

                self.timer.set_time(TIMER_TIME)

                self.is_godzilla = True
                self.cur_evolution += 1

        self.evolve_status = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()