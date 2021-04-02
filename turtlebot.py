#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]

import doctest
import pdb
import turtle
import unittest
import keyword
import random
import moreadt

DEBUG_MODE = True
if DEBUG_MODE:
    import pdb
    #pdb.set_trace()
    import logging
    FORMAT = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s'
    logging.basicConfig(level = logging.INFO, format = FORMAT)
    #logging.basicConfig(level = logging.WARNING, format = FORMAT)
    #logging.basicConfig(level = logging.DEBUG, format = FORMAT)
    #logging.basicConfig(level = logging.ERROR, format = FORMAT)
    #logging.basicConfig(level = logging.CRITICAL, format = FORMAT)

RESERVED = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
            'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec',
            'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'nonlocal', 'not', 'or', 'pass', 'print',
            'raise', 'return', 'try', 'while', 'with', 'yield']
KEYWORDS = keyword.kwlist

sides = 360
size = 3


def polygon(sides, length, colour = "Black", width = 1, speed = 10):

    turtle.pencolor(colour)
    turtle.width(width)
    turtle.speed(speed)
    turtle.pendown()
    for vector in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)
    turtle.penup()
    turtle.done()

pencolours = list(moreadt.web_colours.keys() )
pens = len(pencolours)
colour_selections = list()

ninja = turtle.Turtle()

ninja.speed(1000)
ninja.pensize(8)


for i in range(45):
    ninja.forward(100)
    #ninja.left(172)
    #ninja.circle(100)
    #ninja.right(172)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)

    pencolour = pencolours[random.randrange(pens) ]
    print (pencolour, moreadt.web_colours[pencolour])
    colour_selections += pencolour
    ninja.pencolor(pencolour)
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    #ninja.circle(100)

    ninja.right(8)


turtle.done()







if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
    polygon(8, 50, 'yellow', 10, 1000)
