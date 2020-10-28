"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.brick_row = BRICK_ROWS
        self.brick_column = BRICK_COLS

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.filled = 'black'
        self.window.add(self.paddle, (self.window_width - paddle_width) / 2, self.window_height - paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(2 * BALL_RADIUS, 2 * BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'blue'
        self.ball.color = 'blue'
        self.window.add(self.ball, self.window_width / 2 - BALL_RADIUS, self.window_height / 2 - BALL_RADIUS)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.start_ball_switch = False
        self.accelaration = 1.15

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_follow)
        onmouseclicked(self.click_start_ball)

        # Draw bricks.
        for y in range(brick_rows):
            for x in range(brick_cols):
                brick = GRect(brick_width, brick_height)  # same concept as whack a mole
                x_spot = x * (brick_width + brick_spacing)
                y_spot = y * (brick_height + brick_spacing) + brick_offset
                brick.filled = True
                if 0 <= int(y % 10) <= 1:
                    brick.fill_color = 'red'
                elif 2 <= int(y % 10) <= 3:
                    brick.fill_color = 'orange'
                elif 4 <= int(y % 10) <= 5:
                    brick.fill_color = 'yellow'
                elif 6 <= int(y % 10) <= 7:
                    brick.fill_color = 'green'
                else:
                    brick.fill_color = 'blue'
                self.window.add(brick, x_spot, y_spot)

        # (Self create)reset ball
        self.set_ball_velocity()

        # (Self create)Create Label
        self.label = GLabel('')
        self.label_name = 'Lives:'
        self.lives = NUM_LIVES
        self.label.text = self.label_name + str(self.lives)
        self.label.font = '-20'
        self.label.color = 'black'
        self.window.add(self.label, x=0, y=self.window_height - 20)

        # (Self create)Score
        self.score_label = GLabel('')
        self.score_label_name = 'Scores:'
        self.score = 0
        self.score_label.text = self.score_label_name + str(self.score)
        self.score_label.font = '-20'
        self.score_label.color = 'black'
        self.window.add(self.score_label, x=0, y=self.window_height)

    def paddle_follow(self, m):  # mouse tracker
        switch = True
        if m.x == self.paddle.x + self.paddle.width / 2 and \
                m.y == self.paddle.y + self.paddle.height / 2:
            switch = True
        if switch is True and 0 + self.paddle.width / 2 < m.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = m.x - self.paddle.width / 2

    def click_start_ball(self, m):
        self.start_ball_switch = True

    def detect(self):
        if not self.score == 20 * self.brick_row * self.brick_column:
            self.hit_object()
            self.hit_boundary()
        else:
            self.all_done_end()


    def hit_object(self):
        obj_around_switch = False
        for i in range(2):
            for j in range(2):
                tempo = self.window.get_object_at(self.ball.x + j * 2 * BALL_RADIUS, self.ball.y + i * 2 * BALL_RADIUS)
                if tempo is not None and tempo is not self.label and tempo is not self.score_label:
                    obj_around_switch = True
                    if tempo is not self.paddle:
                        self.window.remove(tempo)
                        self.score += 20
                        self.score_label.text = self.score_label_name + str(self.score)
                        if self.score % 200 == 0:
                            self.speed_accelarate()
        if obj_around_switch is True:
            self.__dy *= -1

    def hit_boundary(self):
        if not 0 < self.ball.x < self.window.width - self.ball.width:
            self.__dx *= -1
        elif self.ball.y <= 0:
            self.__dy *= -1
        elif self.ball.y >= self.window.height:
            self.set_ball_velocity()
            self.reset_ball()
            self.lives -= 1
            self.label.text = self.label_name + str(self.lives)
            self.start_ball_switch = False

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED) * self.accelaration
        self.__dy = INITIAL_Y_SPEED * self.accelaration
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        self.ball.x = self.window_width / 2 - BALL_RADIUS
        self.ball.y = self.window_height / 2 - BALL_RADIUS

    def ball_move(self):
        self.ball.move(self.__dx, self.__dy)

    def speed_accelarate(self):
        self.__dx *= self.accelaration
        self.__dy *= self.accelaration

    def end(self):
        self.window.remove(self.ball)
        gameover = GLabel('GAME OVER')
        gameover.font = '-40'
        gameover.color = 'red'

        score = GLabel(f'YOU GOT {self.score} SCORES!!')
        self.window.add(gameover, x=113, y=350)
        self.window.add(score, x=150, y=370)

    def all_done_end(self):
        self.window.remove(self.ball)
        welldone = GLabel('WELL DONE')
        welldone.font = '-40'
        welldone.color = 'red'

        score = GLabel(f'YOU GOT {self.score} SCORES!!')
        self.window.add(welldone, x=113, y=350)
        self.window.add(score, x=150, y=370)



















