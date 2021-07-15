import arcade
from game.constants import *
import time
import threading


class Sound:


    def __init__(self):

        self.path_sound_list = [FLY_SOUND_EAT,
                                FLY_SOUND_DEATH,
                                SPIDER_SOUND_EAT,
                                SPIDER_SOUND_DEATH,
                                BIRD_SOUND_EAT,
                                BIRD_SOUND_DEATH,
                                CAT_SOUND_EAT,
                                CAT_SOUND_DEATH,
                                SHARK_SOUND_EAT,
                                SHARK_SOUND_DEATH,
                                GODZILLA_EAT,
                                GODZILLA_DEATH]

        self.sound_list = []

        self.poop_death = arcade.load_sound(POOP_DEATH)

        for x in self.path_sound_list:

            if x is not None:
                # arcade.load_sound(x)
                self.sound_list.append(arcade.load_sound(x))

            else:
                self.sound_list.append(arcade.load_sound(FOO_SOUND))


        self.cur_evolution_index = 0


    def death(self, evolution):

        if evolution == -1:
            self._playsound(self.poop_death)

        else:
            death_num = evolution * 2 + 1
            print(f"DeathNum: {death_num}")

            self._playsound(self.sound_list[death_num])


    def consume(self, evolution):

        self.cur_evolution_index = evolution

        thread = threading.Thread(target=self._consume_threading_target)
        thread.start()


    def _consume_threading_target(self):

        time.sleep(CONSUME_DELAY)

        death_num = self.cur_evolution_index * 2

        print(f"consume num: {death_num}")

        self._playsound(self.sound_list[death_num])


    def _playsound(self, index):

        arcade.play_sound(index, SOUND_VOLUME)

        pass