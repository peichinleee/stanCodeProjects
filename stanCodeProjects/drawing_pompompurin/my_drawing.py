"""
File: my_drawing.py
Name: Pei
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GLine, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: 胖胖布丁～～布丁狗卡哇伊
    """
    w = GWindow(width=500, height=500, title='PomPomPurin!')
    bg = GRect(500, 500)
    bg.filled = True
    bg.fill_color = 'wheat'
    w.add(bg)
    label = GLabel('*~Pom Pom Purin!~*/(＾ω＾)/')
    label.font = 'Courier-25-bold'
    label.color = 'saddlebrown'
    w.add(label, x=20, y=130)
    # draw face
    face_1 = GOval(250, 220, x=110, y=195)
    face_1.filled = True
    face_1.fill_color = 'lemonchiffon'
    face_1.color = 'lemonchiffon'
    w.add(face_1)
    face_2 = GArc(300, 700, 0, 180, x=100, y=250)
    face_2.filled = True
    face_2.fill_color = 'lemonchiffon'
    face_2.color = 'lemonchiffon'
    w.add(face_2)
    ear_1 = GOval(80, 80, x=55, y=290)
    ear_1.filled = True
    ear_1.fill_color = 'lemonchiffon'
    ear_1.color = 'lemonchiffon'
    w.add(ear_1)
    ear_2 = GOval(80, 80, x=330, y=230)
    ear_2.filled = True
    ear_2.fill_color = 'lemonchiffon'
    ear_2.color = 'lemonchiffon'
    w.add(ear_2)
    ear_3 = GPolygon()
    ear_3.add_vertex((65, 305))
    ear_3.add_vertex((150, 235))
    ear_3.add_vertex((290, 215))
    ear_3.add_vertex((385, 232))
    ear_3.filled = True
    ear_3.fill_color = 'lemonchiffon'
    ear_3.color = 'lemonchiffon'
    w.add(ear_3)
    # draw hat
    hat = GOval(90, 40, x=165, y=185)
    hat.filled = True
    hat.fill_color = 'sienna'
    hat.color = 'sienna'
    w.add(hat)
    tip = GPolygon()
    tip.add_vertex((205, 178))
    tip.add_vertex((203, 190))
    tip.add_vertex((215, 190))
    tip.filled = True
    tip.fill_color = 'sienna'
    tip.color = 'sienna'
    w.add(tip)
    # draw emotion
    leye_1 = GLine(170, 270, 190, 275)
    leye_1.color = 'sienna'
    w.add(leye_1)
    leye_2 = GLine(177, 285, 190, 275)
    leye_2.color = 'sienna'
    w.add(leye_2)
    reye_1 = GLine(245, 265, 262, 252)
    reye_1.color = 'sienna'
    w.add(reye_1)
    reye_2 = GLine(245, 265, 265, 270)
    reye_2.color = 'sienna'
    w.add(reye_2)
    nose = GOval(10, 8, x=215, y=272)
    nose.filled = True
    nose.fill_color = 'sienna'
    nose.color = 'sienna'
    w.add(nose)
    nose_2 = GLine(220, 278, 222, 290)
    nose_2.color = 'sienna'
    w.add(nose_2)
    nose_3 = GArc(15, 35, 185, 170, x=222, y=280)
    nose_3.color = 'sienna'
    w.add(nose_3)
    nose_4 = GArc(15, 35, 185, 170, x=207, y=282)
    nose_4.color = 'sienna'
    w.add(nose_4)
    blush_1 = GOval(20, 10, x=170, y=295)
    blush_1.filled = True
    blush_1.fill_color = 'lightpink'
    blush_1.color = 'lightpink'
    w.add(blush_1)
    blush_2 = GOval(20, 10, x=250, y=280)
    blush_2.filled = True
    blush_2.fill_color = 'lightpink'
    blush_2.color = 'lightpink'
    w.add(blush_2)
    hand_1 = GArc(40, 20, 120, 170, x=300, y=330)
    hand_1.color = 'sienna'
    w.add(hand_1)
    hand_2 = GArc(40, 20, 260, 170, x=160, y=350)
    hand_2.color = 'sienna'
    w.add(hand_2)


if __name__ == '__main__':
    main()
