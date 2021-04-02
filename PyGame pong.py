#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5"
__metadata__ = [__author__, __date__, __contact__, __version__]

import builtins, keyword, os, sys, time
import queue, collections, threading, pickle, concurrent
import numbers, operator, math, decimal, fractions, random, itertools
import string, re, unicodedata, locale, uuid, hashlib
import doctest, unittest, cProfile, timeit, logging, traceback, datetime
import ftplib, poplib, nntplib, smtplib, telnetlib, email
import argparse, calendar, pprint
#import ipaddress, tkinter, dateutil
import maths, ropes, moreadt, whisper, pygame


# Implementation of classic arcade game Pong (It started this way, honest)

from tkinter import *
from tkinter import ttk
from pygame.locals import *
from moreadt import *



# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 960
HEIGHT = 540
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

# KEY_MAP = {'a': 65, 'A': 65, 'b': 66, 'B': 66, 'c': 67, 'C': 67, 'd': 68, 'D': 68, 'e': 69, 'E': 69, 'f': 70, 'F': 70, 'g': 71, 'G': 71, 'h': 72, 'H': 72, 'i': 73, 'I': 73, 'j': 74, 'J': 74, 'k': 75, 'K': 75, 'l': 76, 'L': 76, 'm': 77, 'M': 77, 'n': 78, 'N': 78, 'o': 79, 'O': 79, 'p': 80, 'P': 80, 'q': 81, 'Q': 81, 'r': 82, 'R': 82, 's': 83, 'S': 83, 't': 84, 'T': 84, 'u': 85, 'U': 85, 'v': 86, 'V': 86, 'w': 87, 'W': 87, 'x': 88, 'X': 88, 'y': 89, 'Y': 89, 'z': 90, 'Z': 90, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, 'space': 32, 'left': 37, 'up': 38, 'right': 39, 'down': 40}

pong_pos = [WIDTH / 2, HEIGHT / 2]
pong_vel = [5, 5]
pong_tail = []
left_pos, right_pos = HEIGHT / 2 - HALF_PAD_HEIGHT, HEIGHT / 2 - HALF_PAD_HEIGHT
left_vel = right_vel = 5.0
left_hand = right_hand = 0

moving_right, moving_down = True, False
left_down = left_up = right_down = right_up = False

# Special guest appearance
helping_hand = tracking = True
ping_pos = [WIDTH / 2, HEIGHT / 2]
ping_vel = [5, 5]
ping_tail = []
moving_left, moving_up = False, True

# Computer assisted auto-player
left_assist = right_assist = True
temp_vel = []

rally, flurry, highest, tag_team, difficulty = 0, 0, 0, 4, 1
level = {0:("Paused", 'White'),
         1:("Easy", 'Green'),
         2:("Medium", 'Yellow'),
         3:("Hard", 'Red')}

football_pitch = tennis_court = hockey_field = True
lines = White
fixture = {}

# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def pong_init(right):
    global pong_pos, pong_vel, pong_tail # these are vectors stored as lists
    global moving_right, rally, highest, helping_hand

    # Computer serves from centre of court
    pong_vel[0] = random.randrange(difficulty + 1, difficulty * 3)
    pong_vel[1] = random.randrange(difficulty + 1, difficulty * 3)
    pong_pos = [WIDTH / 2, HEIGHT / 2]
    pong_tail = [pong_pos]
    if rally > highest:
        highest = rally
    rally = 0
    if abs(left_hand - right_hand) >= tag_team:
        helping_hand = True

    # Determines the direction pong travels from previous point
    if not right:
        moving_right = False
    else:
        moving_right = True

def ping_init(left):
    global ping_pos, ping_vel, ping_tail # these are vectors stored as lists
    global moving_left, flurry, highest, helping_hand

    # Core launches from out of nowhere
    ping_vel[0] = random.randrange(difficulty + 1, difficulty * 3)
    ping_vel[1] = random.randrange(difficulty + 1, difficulty * 3)
    ping_pos = [WIDTH / 2, random.randrange(HEIGHT / 2)]
    ping_tail = [ping_pos]
    if rally + flurry > highest:
        highest = flurry + rally
    flurry = 0
    if abs(left_hand - right_hand) <= tag_team / 2:
        helping_hand = False

    # Determines the direction ping travels from previous point
    if not left:
        moving_left = False
    else:
        moving_left = True

def resize():
    global fixture

    fixture = {'tcl' : [WIDTH / 2, 0],
               'bcl' : [WIDTH / 2, HEIGHT],
               'tlg' : [PAD_WIDTH, 0],
               'blg' : [PAD_WIDTH, HEIGHT],
               'trg' : [WIDTH - PAD_WIDTH, 0],
               'brg' : [WIDTH - PAD_WIDTH, HEIGHT],
               'fcc' : [(WIDTH / 100) * 50, (HEIGHT / 60) *  30],
               'fcs' : (WIDTH / 100),
               'tt1' : [(WIDTH / 78) * 0, (HEIGHT / 36) *  4.5],
               'bt1' : [(WIDTH / 78) * 78, (HEIGHT / 36) *  4.5],
               'tt2' : [(WIDTH / 78) * 0, (HEIGHT / 36) *  31.5],
               'bt2' : [(WIDTH / 78) * 78, (HEIGHT / 36) *  31.5],
               'tt3' : [(WIDTH / 78) * 18, (HEIGHT / 36) *  18],
               'bt3' : [(WIDTH / 78) * 60, (HEIGHT / 36) *  18],
               'tt4' : [(WIDTH / 78) * 18, (HEIGHT / 36) *  4.5],
               'bt4' : [(WIDTH / 78) * 18, (HEIGHT / 36) *  31.5],
               'tt5' : [(WIDTH / 78) * 60, (HEIGHT / 36) *  4.5],
               'bt5' : [(WIDTH / 78) * 60, (HEIGHT / 36) *  31.5],
               'tt6' : [(WIDTH / 78) * 39, (HEIGHT / 36) *  4.5],
               'bt6' : [(WIDTH / 78) * 39, (HEIGHT / 36) *  31.5],
               'tlh' : [(WIDTH / 100) * 25, (HEIGHT / 60) *  0],
               'blh' : [(WIDTH / 100) * 25, (HEIGHT / 60) *  60],
               'tch' : [(WIDTH / 100) * 50, (HEIGHT / 60) *  0],
               'bch' : [(WIDTH / 100) * 50, (HEIGHT / 60) *  60],
               'trh' : [(WIDTH / 100) * 75, (HEIGHT / 60) *  0],
               'brh' : [(WIDTH / 100) * 75, (HEIGHT / 60) *  60],
               'hcc' : [(WIDTH / 100) * 50, (HEIGHT / 60) *  30],
               'hcs' : ((WIDTH / 100) * 5),
               'lht' : (WIDTH * (11/32), HEIGHT * (1/2)),
               'rht' : (WIDTH * (17/32), HEIGHT * (1/2)),
               'lvt' : (WIDTH * (15/32), HEIGHT * (15/32)),
               'svt' : (WIDTH * (16/32), HEIGHT * (14/32)),
               'lst' : (WIDTH * (16/32), HEIGHT * (17/32)),
               'sst' : (WIDTH * (17/32), HEIGHT * (17/32)),
               'crt' : (WIDTH * (5/16), HEIGHT * (1/16)),
               'hrt' : (WIDTH * (9/16), HEIGHT * (1/16)),
               'dst' : (WIDTH * (9/16), HEIGHT * (15/16)),
               'gdt' : (WIDTH * (5/16), HEIGHT * (15/16)) }

# define event handlers weddings, birthdays, parties
def init():
    global left_pos, right_pos, left_vel, right_vel  # these are floats
    global left_hand, right_hand, rally, highest  # these are ints
    global helping_hand  # these are useful and highly appreciated

    #resize()
    pong_init(moving_right)
    ping_init(moving_left)

    reset_paddle = HEIGHT / 2 - HALF_PAD_HEIGHT
    left_pos, right_pos = reset_paddle, reset_paddle

    # Reset the paddle velocity to the ball vertical velocity
    left_vel = right_vel = max(pong_vel[1], ping_vel[1])

    left_hand, right_hand = 0, 0
    rally, highest = 0, 0
    helping_hand = True   # Surprise entrance

def pause():
    global pong_vel, ping_vel, temp_vel

    if temp_vel == []:
        temp_vel.append(pong_vel)
        temp_vel.append(ping_vel)
        pong_vel = [0, 0]
        ping_vel = [0, 0]
    else:
        pong_vel = temp_vel[0]
        ping_vel = temp_vel[1]
        temp_vel = []

def easier():
    global difficulty

    if not difficulty == 1:
        difficulty -= 1

def harder():
    global difficulty

    if not difficulty == 3:
        difficulty += 1

def pinch(paddle):
    # Returns true if the position of pong is within the range of the paddle
    paddle = int(paddle)
    return int(pong_pos[1]) in range(paddle - 2, paddle + PAD_HEIGHT + 2)

def punch(paddle):
    # Returns true if the position of ping is within the range of the paddle
    paddle = int(paddle)
    return int(ping_pos[1]) in range(paddle - 2, paddle + PAD_HEIGHT + 2)

def distance_between_points(vector1, vector2):
    return math.sqrt( (vector1[0] - vector2[0]) ** 2 +
                      (vector1[1] - vector2[1]) ** 2)

def tracing():
    global tracking

    if not tracking:
        tracking = True
    else:
        tracking = False

def football():
    global football_pitch, tennis_court, hockey_field

    tennis_court = hockey_field = False
    if not football_pitch:
        football_pitch = True
    else:
        football_pitch = False

def tennis():
    global football_pitch, tennis_court, hockey_field

    football_pitch = hockey_field = False
    if not tennis_court:
        tennis_court = True
    else:
        tennis_court = False

def hockey():
    global football_pitch, tennis_court, hockey_field

    football_pitch = tennis_court = False
    if not hockey_field:
        hockey_field = True
    else:
        hockey_field = False

def help_left():
    global left_assist

    if not left_assist:
        left_assist = True
    else:
        left_assist = False

def help_right():
    global right_assist

    if not right_assist:
        right_assist = True
    else:
        right_assist = False

def collide():
    global moving_right, moving_left, moving_down, moving_up
    if moving_right and moving_left:
        moving_right = False
        moving_left = False
    else:
        moving_right = True
        moving_left = True

    if moving_down and moving_up:
        moving_down = False
        moving_up = False
    else:
        moving_down = True
        moving_up = True

# 3D enhanced version with bullet time using an engine to demanding for modern computers
# Pong wrestling 3D 2020 Unicorn edition: A feature too far, remastered with a BFG

def drawing(crayon):
    global left_hand, right_hand, left_pos, right_pos, pong_pos, pong_vel
    global moving_right, moving_down, rally, flurry
    global left_down, left_up, right_down, right_up
    global moving_left, moving_up
    global pong_tail, ping_tail

    # update paddle's vertical position, keep paddle on the screen
    if left_assist:
        if helping_hand and pong_pos[0] > ping_pos[0]:
            if ping_pos[1] > left_pos + HALF_PAD_HEIGHT:
                left_down = True
                left_up = False
            else:
                left_up = True
                left_down = False
        else:
            if pong_pos[1] > left_pos + HALF_PAD_HEIGHT:
                left_down = True
                left_up = False
            else:
                left_up = True
                left_down = False

    if left_down:
        if not left_pos >= HEIGHT - PAD_HEIGHT:
            left_pos += left_vel
        else:
            left_down = False

    if left_up:
        if not left_pos <= 0:
            left_pos -= left_vel
        else:
            left_up = False

    if right_assist:
        if helping_hand and pong_pos[0] < ping_pos[0]:
            if ping_pos[1] > right_pos + HALF_PAD_HEIGHT:
                right_down = True
                right_up = False
            else:
                right_up = True
                right_down = False
        else:
            if pong_pos[1] > right_pos + HALF_PAD_HEIGHT:
                right_down = True
                right_up = False
            else:
                right_up = True
                right_down = False

    if right_down:
        if not right_pos >= HEIGHT - PAD_HEIGHT:
            right_pos += right_vel
        else:
            right_down = False

    if right_up:
        if not right_pos <= 0:
            right_pos -= right_vel
        else:
            right_up = False

    # draw mid line and gutters
    pygame.draw.line(crayon, Grey, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(crayon, Brown, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(crayon, Brown, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)

    if football_pitch:
        pygame.draw.circle(crayon, lines,
                           [int((WIDTH / 100) * 50), int((HEIGHT / 60) *  30) ],
                           int((WIDTH / 100) * 5), 1)

    if tennis_court:
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 0, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 78, (HEIGHT / 36) *  4.5], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 0, (HEIGHT / 36) *  31.5], [(WIDTH / 78) * 78, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 18, (HEIGHT / 36) *  18], [(WIDTH / 78) * 60, (HEIGHT / 36) *  18], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 18, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 18, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 60, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 60, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 78) * 39, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 39, (HEIGHT / 36) *  31.5], 1)

    if hockey_field:
        pygame.draw.line(crayon, lines, [(WIDTH / 100) * 25, (HEIGHT / 60) *  0], [(WIDTH / 100) * 25, (HEIGHT / 60) *  60], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 100) * 50, (HEIGHT / 60) *  0], [(WIDTH / 100) * 50, (HEIGHT / 60) *  60], 1)
        pygame.draw.line(crayon, lines, [(WIDTH / 100) * 75, (HEIGHT / 60) *  0], [(WIDTH / 100) * 75, (HEIGHT / 60) *  60], 1)
        pygame.draw.circle(crayon, lines,
                           [int((WIDTH / 100) * 50), int((HEIGHT / 60) *  30)],
                           int((WIDTH / 100) * 5), 1)


    # draw paddles
    pygame.draw.line(crayon, Green, [(PAD_WIDTH / 2) + 1, left_pos],[(PAD_WIDTH / 2) + 1, left_pos + PAD_HEIGHT], PAD_WIDTH)
    pygame.draw.line(crayon, Blue, [WIDTH - (PAD_WIDTH / 2) - 1, right_pos],[WIDTH - (PAD_WIDTH / 2) - 1, right_pos + PAD_HEIGHT], PAD_WIDTH)

#    if distance_between_points(ping_pos, pong_pos) < BALL_RADIUS * 2:
#        collide()

    # update pong
    pong_tail.append(tuple(pong_pos))
    if not moving_right:
        if pong_pos[0] >= BALL_RADIUS + PAD_WIDTH:
            pong_pos[0] -= pong_vel[0]
        elif pinch(left_pos):
            pong_vel[0] = left_vel + 1
            pong_vel[1] = left_vel + 1
            moving_right = True
            rally += 1
            os.system('\a')
        else:
            moving_right = True
            right_hand += 1
            pong_init(moving_right)

    if moving_right:
        if pong_pos[0] <= WIDTH - BALL_RADIUS - PAD_WIDTH:
            pong_pos[0] += pong_vel[0]
        elif pinch(right_pos):
            pong_vel[0] = right_vel + 1
            pong_vel[1] = right_vel + 1
            moving_right = False
            rally += 1
            os.system('\a')
        else:
            moving_right = False
            left_hand += 1
            pong_init(moving_right)

    # Pong velocity increases from paddle strikes
    # Pong velocity decreases from walls bounces

    if not moving_down:
        if pong_pos[1] >= BALL_RADIUS:
            pong_pos[1] -= pong_vel[1]
        else:
            pong_vel[1] -= 1
            moving_down = True

    if moving_down:
        if pong_pos[1] <= HEIGHT - BALL_RADIUS:
            pong_pos[1] += pong_vel[1]
        else:
            pong_vel[1] -= 1
            moving_down = False

    # update ping
    if helping_hand:
        ping_tail.append(tuple(ping_pos))
        if not moving_left:
            if ping_pos[0] >= BALL_RADIUS + PAD_WIDTH:
                ping_pos[0] -= ping_vel[0]
            elif punch(left_pos):
                ping_vel[0] = left_vel + 1
                ping_vel[1] = left_vel + 1
                moving_left = True
                flurry += 1
                os.system('\a')
            else:
                moving_left = True
                right_hand += 1
                ping_init(moving_left)

        if moving_left:
            if ping_pos[0] <= WIDTH - BALL_RADIUS - PAD_WIDTH:
                ping_pos[0] += ping_vel[0]
            elif punch(right_pos):
                ping_vel[0] = right_vel + 1
                ping_vel[1] = right_vel + 1
                moving_left = False
                flurry += 1
                os.system('\a')
            else:
                moving_left = False
                left_hand += 1
                ping_init(moving_left)

        # Ping velocity increases from paddle strikes
        # Ping velocity decreases from walls bounces

        if not moving_up:
            if ping_pos[1] >= BALL_RADIUS:
                ping_pos[1] -= ping_vel[1]
            else:
                ping_vel[1] -= 1
                moving_up = True

        if moving_up:
            if ping_pos[1] <= HEIGHT - BALL_RADIUS:
                ping_pos[1] += ping_vel[1]
            else:
                ping_vel[1] -= 1
                moving_up = False


    leader = max(left_hand, right_hand)
    chaser = min(left_hand, right_hand)
    gutter = abs(leader - chaser)

    # draw TT&T
    if tracking:
        if len(pong_tail) > 1:
            pygame.draw.lines(crayon, Yellow, False, pong_tail, 1)
        #pygame.draw.line(crayon, Red, False, pong_tail[0], pong_pos, 3)
        if helping_hand:
            if len(pong_tail) > 1:
                pygame.draw.lines(crayon, Red, False, ping_tail, 1)
            #pygame.draw.line(crayon, ping_tail[0], ping_pos, 3, "Yellow")

    # draw ball and scores
    """
    left_score = crayon.create_text(WIDTH * (11/32), HEIGHT * (1/2),
                                    text = ("Left hand: "+str(left_hand) ),
                                    font = "Verdana 16", fill = 'Green')
    right_score = crayon.create_text(WIDTH * (17/32), HEIGHT * (1/2),
                                     text = ("Right hand: "+str(right_hand) ),
                                     font = "Verdana 16", fill = 'Blue')
    v_sign = crayon.create_text(WIDTH * (15/32), HEIGHT * (15/32),
                                text = ("V"),
                                font = "Verdana 32", fill = 'Red')
    endetta = crayon.create_text(WIDTH * (16/32), HEIGHT * (14/32),
                                 text = ("endetta"),
                                 font = "Verdana 10", fill = 'Red')
    s_sign = crayon.create_text(WIDTH * (16/32), HEIGHT * (17/32),
                                text = ("S"),
                                font = "Verdana 32", fill = 'Red')
    upreme = crayon.create_text(WIDTH * (17/32), HEIGHT * (17/32),
                                text = ("upreme"),
                                font = "Verdana 10", fill = 'Red')
    current = crayon.create_text(WIDTH * (5/16), HEIGHT * (1/16),
                                 text = ("Current rally: "+str(rally + flurry) ),
                                 font = "Verdana 10", fill = 'Red')
    previous = crayon.create_text(WIDTH * (9/16), HEIGHT * (1/16),
                                  text = ("Highest rally: "+str(highest) ),
                                  font = "Verdana 10", fill = 'Maroon')
    challenge = crayon.create_text(WIDTH * (9/16), HEIGHT * (15/16),
                                   text = ("Difficulty/Speed: "+level[difficulty][0] ),
                                   font = "Verdana 10", fill = level[difficulty][1])
    balance = crayon.create_text(WIDTH * (5/16), HEIGHT * (15/16),
                                 text = ("Gutter difference: "+str(gutter) ),
                                 font = "Verdana 10", fill = 'Brown')
                                 """
    pongball = pygame.draw.circle(crayon, Yellow, (int(pong_pos[0] - BALL_RADIUS),
                                                   (int(pong_pos[1] - BALL_RADIUS) ) ),
                                  int(BALL_RADIUS), 2)
    """
    ponging = crayon.create_text(pong_pos[0], pong_pos[1],
                                 text = ("Pong"),
                                 font = "Verdana 12", fill = 'Black')
                                 """
    if helping_hand:
        pingball = pygame.draw.circle(crayon, Red, (int(ping_pos[0] - BALL_RADIUS),
                                                    (int(ping_pos[1] - BALL_RADIUS) ) ),
                                      int(BALL_RADIUS), 2)
        """
        pinging = crayon.create_text(ping_pos[0], ping_pos[1],
                                     text = ("Ping"),
                                     font = "Verdana 12", fill = 'White')
                                     """



controls = {'w' : left_up,
            's' : left_down,
            'up' : right_up,
            'down' : right_down}

def keydown(key):
    global left_vel, right_vel
    global left_down, left_up, right_down, right_up

    """
    if key == simplegui.KEY_MAP["s"]:
        left_down = True
        left_vel += 1

    if key == simplegui.KEY_MAP["w"]:
        left_up = True
        left_vel += 1

    if key == simplegui.KEY_MAP["up"]:
        right_up = True
        right_vel += 1

    if key == simplegui.KEY_MAP["down"]:
        right_down = True
        right_vel += 1
    """

    if key in controls:
        controls[key] = True

    if left_up or left_down:
        left_vel += 1

    if right_up or right_down:
        right_vel += 1

def keyup(key):
    global left_vel, right_vel
    global left_down, left_up, right_down, right_up

    """
    if key == simplegui.KEY_MAP["s"]:
        left_down = False

    if key == simplegui.KEY_MAP["w"]:
        left_up = False

    if key == simplegui.KEY_MAP["up"]:
        right_up = False

    if key == simplegui.KEY_MAP["down"]:
        right_down = False
    """

    if key in controls:
        controls[key] = False

    # Match the paddle velocities to the ball vertical velocity
    left_vel = right_vel = max(pong_vel[1], ping_vel[1])


#panel = Frame(window, width = 150, height = HEIGHT, bg = 'White')
#panel.grid(row = 0, column = 0)

#canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = 'Black')
#canvas.grid(row = 0, column = 1)


#canvas.set_draw_handler(drawing)
#panel.set_keydown_handler(keydown)
#panel.set_keyup_handler(keyup)
"""
reset = ttk.Button(panel, text = "Restart Set", command = init, width = 12)
reset.grid(row = 1, column = 0)

hold = ttk.Button(panel, text = "Halt / Thaw", command = pause, width = 12)
hold.grid(row = 2, column = 0)

slow = ttk.Button(panel, text = "Slow & Easy", command = easier, width = 12)
slow.grid(row = 3, column = 0)

fast = ttk.Button(panel, text = "Hard & Fast", command = harder, width = 12)
fast.grid(row = 4, column = 0)

target = ttk.Button(panel, text = "Toggle TT&T", command = tracing, width = 12)
target.grid(row = 5, column = 0)

leftaid = ttk.Button(panel, text = "Left Assist", command = help_left, width = 12)
leftaid.grid(row = 6, column = 0)

rightaid = ttk.Button(panel, text = "Right Assist", command = help_right, width = 12)
rightaid.grid(row = 7, column = 0)

pitch = ttk.Button(panel, text = "Footy pitch", command = football, width = 12)
pitch.grid(row = 8, column = 0)

court = ttk.Button(panel, text = "Tennis court", command = tennis, width = 12)
court.grid(row = 9, column = 0)

field = ttk.Button(panel, text = "Hockey field", command = hockey, width = 12)
field.grid(row = 10, column = 0)
"""
#for button in window.winfo_children():
#    button.grid_configure(padx = 10, pady = 10)

# create frame
pygame.init()
window = pygame.display.set_mode([WIDTH, HEIGHT])
alpha_mask = window.convert_alpha()
#window.geometry(str(WIDTH+150)+"x"+str(HEIGHT+50)+"+50+25")
pygame.display.set_caption("Not Pong as you know it HD 2012: The Vendetta Supreme, featuring evil twin Ping, in Double Ding Dong")

# start frame
resize()

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
    drawing(window)
    pygame.display.update()
    #window.after(10, drawing(canvas) )
    #window.mainloop()


"""
curtime = ''
clock = Tkinter.Label()
clock.pack()

def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(200, tick)

tick()
clock.mainloop()


# for python 3.x use 'tkinter' rather than 'Tkinter'
import Tkinter as tk
import time

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=App()
app.mainloop()
"""
