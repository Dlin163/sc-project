"""
File: my_drawing.py
Name:林鼎鈞
----------------------
This is a masterpiece done by David lol.
"""

from campy.graphics.gobjects import GOval, GRect
from campy.graphics.gwindow import GWindow
window = GWindow(800, 800, title='Illusion')


def main():
    """
    Drawing circles
    """
    # orange circles
    c1 = GOval(800, 800, x=0, y=0)
    c2 = GOval(750, 750, x=0, y=25)
    c3 = GOval(700, 700, x=0, y=50)
    c4 = GOval(650, 650, x=0, y=75)
    c5 = GOval(600, 600, x=0, y=100)

    c6 = GOval(550, 550, x=25, y=125)
    c7 = GOval(500, 500, x=75, y=150)
    c8 = GOval(450, 450, x=125, y=175)
    c9 = GOval(400, 400, x=175, y=200)

    c10 = GOval(300, 300, x=237.5, y=249)

    c11 = GOval(250, 250, x=237.5, y=274)
    c12 = GOval(200, 200, x=237.5, y=299)
    c13 = GOval(150, 150, x=237.5, y=324)
    c14 = GOval(100, 100, x=237.5, y=349)
    c15 = GOval(50, 50, x=237.5, y=374)

    # black circles
    b1 = GOval(775, 775, x=0, y=12.5)
    b2 = GOval(725, 725, x=0, y=37.5)
    b3 = GOval(675, 675, x=0, y=62.5)
    b4 = GOval(625, 625, x=0, y=87.5)
    b5 = GOval(575, 575, x=0, y=112.5)

    b6 = GOval(525, 525, x=50, y=137.5)
    b7 = GOval(475, 475, x=100, y=162.5)
    b8 = GOval(425, 425, x=150, y=187.5)
    b9 = GOval(375, 375, x=200, y=212.5)

    b10 = GOval(275, 275, x=237.5, y=262)
    b11 = GOval(225, 225, x=237.5, y=287)
    b12 = GOval(175, 175, x=237.5, y=312)
    b13 = GOval(125, 125, x=237.5, y=337)
    b14 = GOval(75, 75, x=237.5, y=362)
    b15 = GOval(25, 25, x=237.5, y=387)

    # add color orange circles
    c1.filled = True
    c1.color = 'darkorange'
    c1.fill_color = 'darkorange'
    c2.filled = True
    c2.color = 'darkorange'
    c2.fill_color = 'darkorange'
    c3.filled = True
    c3.color = 'darkorange'
    c3.fill_color = 'darkorange'
    c4.filled = True
    c4.color = 'darkorange'
    c4.fill_color = 'darkorange'
    c5.filled = True
    c5.color = 'darkorange'
    c5.fill_color = 'darkorange'
    c6.filled = True
    c6.color = 'darkorange'
    c6.fill_color = 'darkorange'
    c7.filled = True
    c7.color = 'darkorange'
    c7.fill_color = 'darkorange'
    c8.filled = True
    c8.color = 'darkorange'
    c8.fill_color = 'darkorange'
    c9.filled = True
    c9.color = 'darkorange'
    c9.fill_color = 'darkorange'
    c10.filled = True
    c10.color = 'darkorange'
    c10.fill_color = 'darkorange'
    c11.filled = True
    c11.color = 'darkorange'
    c11.fill_color = 'darkorange'
    c12.filled = True
    c12.color = 'darkorange'
    c12.fill_color = 'darkorange'
    c13.filled = True
    c13.color = 'darkorange'
    c13.fill_color = 'darkorange'
    c14.filled = True
    c14.color = 'darkorange'
    c14.fill_color = 'darkorange'
    c15.filled = True
    c15.color = 'darkorange'
    c15.fill_color = 'darkorange'

    # add color black circles
    b1.filled = True
    b1.fill_color = 'black'
    b2.filled = True
    b2.fill_color = 'black'
    b3.filled = True
    b3.fill_color = 'black'
    b4.filled = True
    b4.fill_color = 'black'
    b5.filled = True
    b5.fill_color = 'black'
    b6.filled = True
    b6.fill_color = 'black'
    b7.filled = True
    b7.fill_color = 'black'
    b8.filled = True
    b8.fill_color = 'black'
    b9.filled = True
    b9.fill_color = 'black'
    b10.filled = True
    b10.fill_color = 'black'
    b11.filled = True
    b11.fill_color = 'black'
    b12.filled = True
    b12.fill_color = 'black'
    b13.filled = True
    b13.fill_color = 'black'
    b14.filled = True
    b14.fill_color = 'black'
    b15.filled = True
    b15.fill_color = 'black'


    # add
    window.add(c1)
    window.add(b1)
    window.add(c2)
    window.add(b2)
    window.add(c3)
    window.add(b3)
    window.add(c4)
    window.add(b4)
    window.add(c5)
    window.add(b5)
    window.add(c6)
    window.add(b6)
    window.add(c7)
    window.add(b7)
    window.add(c8)
    window.add(b8)
    window.add(c9)
    window.add(b9)
    window.add(c10)
    window.add(b10)
    window.add(c11)
    window.add(b11)
    window.add(c12)
    window.add(b12)
    window.add(c13)
    window.add(b13)
    window.add(c14)
    window.add(b14)
    window.add(c15)
    window.add(b15)


if __name__ == '__main__':
    main()
