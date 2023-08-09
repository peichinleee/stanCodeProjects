"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Author: Pei
This is the user side of the breakout game.
Defines the animation including ball collision , winning conditions and limited lives.
Added label of remaining lives and result.
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel, GRect
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3		# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    remain_brick = graphics.brick_num

    # create label of remaining lives
    label = GLabel('Remaining lives: ' + str(lives))
    label.font = 'Courier-20-bold'
    label.color = 'Navy'
    graphics.window.add(label, x=0, y=25)

    # create win/lose label
    bg = GRect(graphics.window.width, 50, x=0, y=graphics.window.height/2-25)
    bg.filled = True
    bg.fill_color = 'yellow'
    bg.color = 'yellow'
    result = GLabel('You Win!!!', x=40, y=bg.y+50)
    result.font = 'Courier-50-bold'
    result.color = 'Black'

    while True:
        # check lives
        label.text = 'Remaining lives: ' + str(lives)
        if lives == 0:
            graphics.window.add(bg)
            result.text = 'You Lose!!!'
            graphics.window.add(result)
            break
        else:
            # ball movement
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)
            # check if drop
            if graphics.ball.y > graphics.window.height:
                lives -= 1
                graphics.reset_ball()

            # ball collision at top left corner
            obj_1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            # top right corner
            obj_2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball_size, graphics.ball.y)
            # bottom left corner
            obj_3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball_size)
            # bottom right corner
            obj_4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball_size, graphics.ball.y+graphics.ball_size)
            if obj_1 is not None and obj_1 is not label:
                # rebound
                graphics.rebound()
                # remove if ball hit brick (obj.y < paddle.y)
                if obj_1.y < graphics.paddle.y:
                    graphics.window.remove(obj_1)
                    remain_brick -= 1
            elif obj_2 is not None and obj_2 is not label:
                # rebound
                graphics.rebound()
                # ball hit brick (if obj.y < paddle.y)
                if obj_2.y < graphics.paddle.y:
                    graphics.window.remove(obj_2)
                    remain_brick -= 1
            elif obj_3 is not None and obj_3 is not label:
                # rebound
                graphics.rebound()
                # ball hit brick (if obj.y < paddle.y)
                if obj_3.y < graphics.paddle.y:
                    graphics.window.remove(obj_3)
                    remain_brick -= 1
            elif obj_4 is not None and obj_4 is not label:
                # rebound
                graphics.rebound()
                # ball hit brick (if obj.y < paddle.y)
                if obj_4.y < graphics.paddle.y:
                    graphics.window.remove(obj_4)
                    remain_brick -= 1

            # check if all bricks are gone
            if remain_brick == 0:
                graphics.window.add(bg)
                graphics.window.add(result)
                break
        # pause
        pause(FRAME_RATE)





if __name__ == '__main__':
    main()
