#! /usr/bin/env python		#Allow Unix shell to execute as a Python script
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

import builtins, keyword, os, sys, time
import queue, heapq, collections, threading, pickle, concurrent
import numbers, operator, math, cmath, decimal, fractions, random, itertools
import string, textwrap, re, unicodedata, locale, uuid, hashlib, binascii, zlib
import doctest, unittest, cProfile, timeit, logging, traceback, datetime
import socket, ftplib, poplib, nntplib, smtplib, telnetlib, email, functools
import argparse, calendar, pprint, struct, copy, pdb, socket, subprocess
import ipaddress, tkinter, colorama#, dateutil, numpy, scipy, pygame, matplotlib, pygobject

DEBUG_MODE = False
if DEBUG_MODE:
    pdb.set_trace()

RESERVED = ["and", "del", "from", "not", "while", "as", "elif",
            "global", "or", "with", "assert", "else", "if", "pass",
            "yield", "break","except", "import", "print", "class",
            "exec", "in", "raise", "continue", "finally", "is",
            "return", "def", "for", "lambda", "try"]

import turtle

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


ninja = turtle.Turtle()

ninja.speed(1000)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()







if __name__ == '__main__':
    doctest.testmod()
    unittest.main(exit=False)
    polygon(8, 50, 'yellow', 10, 1000)


