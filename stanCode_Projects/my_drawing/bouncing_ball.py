"""
File: bouncing _ball.py
Name:林鼎鈞
-------------------------
This file show a animation of a ball falling
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
switch = True
times = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global switch
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(drop)    # once activated could not quit


def drop(m):
    """
    The function is built to make the ball fall by detecting mouse click.
    :param m: The information given by mouse click
    """
    global ball, VX, DELAY, SIZE, switch, times
    l_g = GRAVITY
    if switch is True and times is not 3:  # cant be out side 'onmouseclick', which unable to turn off once activated
        switch = False
        while ball.x <= window.width:
            while ball.y + l_g <= window.height-SIZE/2 and l_g > 0:
                ball.move(VX, l_g)
                l_g += GRAVITY
                pause(DELAY)
            ball.move(VX*(window.height-ball.y)/l_g, window.height-ball.y)
            l_g = (-l_g) * 0.9
            pause(DELAY)
            while l_g <= 0:
                ball.move(VX, l_g)
                l_g += GRAVITY
                pause(DELAY)
            l_g = GRAVITY
        times += 1
        window.add(ball, x=START_X, y=START_Y)
        switch = True


if __name__ == "__main__":
    main()
