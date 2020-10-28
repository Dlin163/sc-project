"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    g = BreakoutGraphics()
    while True:
        pause(FRAME_RATE)
        if g.start_ball_switch:
            if g.lives > 0:
                g.detect()
                g.ball_move()
            else:
                break
    g.end()

    
if __name__ == '__main__':
    main()
