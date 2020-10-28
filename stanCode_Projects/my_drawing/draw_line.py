"""
File: draw_line.py
Name:林鼎鈞
-------------------------
This program enables users to draw line on canvas.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
dot = GOval(SIZE, SIZE)
addup = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_dot)


def draw_dot(m):
    """
    Creates a dot by one click. A line by two click.
    :param m: The information given by mouse click
    """
    global dot, addup
    if addup % 2 == 0:
        dot = GOval(SIZE, SIZE, x=m.x, y=m.y)
        window.add(dot)
        addup += 1
    else:
        line = GLine(dot.x, dot.y, m.x, m.y)
        window.add(line)
        window.remove(dot)
        addup += 1


if __name__ == "__main__":
    main()
