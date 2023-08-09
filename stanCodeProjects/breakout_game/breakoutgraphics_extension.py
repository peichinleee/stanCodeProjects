"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Author: Pei
This is the coder side of the breakout game.
Defines the basic elements including window, bricks, ball and paddle.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # # create label
        # label = GLabel('Remaining lives: ')
        # label.font = 'Courier-20-bold'
        # label.color = 'Navy'
        # self.window.add(label, x=0, y=brick_offset / 2 + 10)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_height-paddle_offset)
        self.paddle_height = paddle_height

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.reset_ball()
        self.ball_size = ball_radius*2

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.initialize_ball)
        onmousemoved(self.paddle_move)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                # set brick colors
                if j < brick_rows/5:
                    self.brick.fill_color = 'red'
                elif brick_rows/5 <= j < brick_rows/5*2:
                    self.brick.fill_color = 'orange'
                elif brick_rows/5*2 <= j < brick_rows/5*3:
                    self.brick.fill_color = 'yellow'
                elif brick_rows/5*3 <= j < brick_rows/5*4:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=(brick_width+brick_spacing)*i, y=brick_offset+(brick_height+brick_spacing)*j)

        self.brick_num = brick_cols * brick_rows
        self.brick_row = brick_rows

    def paddle_move(self, event):
        self.paddle.x = event.x - self.paddle.width/2
        # set left and right boundaries
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def initialize_ball(self, event):
        # only if ball is not moving
        if self.__dx == 0 and self.__dy == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED

    def get_vx(self):
        # reverse direction when touch boundaries
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
        return self.__dx

    def get_vy(self):
        # reverse direction when touch boundaries
        if self.ball.y <= 0:
            self.__dy = -self.__dy
        return self.__dy

    def reset_ball(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=self.window.width/2 - self.ball.width/2, y=self.window.height/2 - self.ball.width/2)
        self.__dx = 0
        self.__dy = 0

    def rebound_y(self):
        self.__dy = -self.__dy

    def rebound(self):
        self.rebound_y()
        if self.paddle.y - self.ball_size < self.ball.y < self.paddle.y + self.paddle_height:
            # ball hit at paddle sidewall
            if self.__dy > 0:
                self.rebound_y()












