from random import randint
from game import constants
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService# program entry point

import arcade

def main():
    def main():
    
    # create the cast {key: tag, value: list}
    cast = {}

    paddle = Paddle()
    cast["paddle"] = [paddle]

    
    cast["balls"] = []

    for i in range(constants.NUM_BALLS):
        # TODO: Create a ball here and add it to the list of balls in the cast
        x = randint(200, 600)
        y = 100
        ball = Ball(x, y)
        cast["balls"].append(ball)

        

    cast["bricks"] = []
    for x in range(constants.BRICK_WIDTH * 2,
                constants.MAX_X - constants.BRICK_WIDTH * 2,
                constants.BRICK_WIDTH + constants.BRICK_SPACE):
        for y in range(int(constants.MAX_Y * .7),
                    int(constants.MAX_Y * .9),
                    constants.BRICK_HEIGHT + constants.BRICK_SPACE):
            brick = Brick(x, y)
            cast["bricks"].append(brick)
    


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    batter = Batter(cast, script, input_service)
    batter.setup()
    arcade.run()

if __name__ == "__main__":
    main()