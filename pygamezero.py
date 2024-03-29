#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]


import this
#import antigravity
import keyword
import os
import sys
import math
import random
import pygame
#import pgzrun
import multiprocessing
import concurrent
import threading
import asyncio

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

from tkinter import *
from tkinter import ttk
from pygame.locals import *
from pygame import mixer
from maths import *
from moreadt import *


pygame.init()
frameRate = 60
clock = pygame.time.Clock()

# Grab joystick 0
if pygame.joystick.get_count() == 0:
    joyPresent = False
else:
    joyPresent = True
    joy = pygame.joystick.Joystick(0)
    joyDeadzone = 2.0
    joy.init()
keyMove = False


# Use background image size as screen size
background = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\oneMcolours.png")
WIDTH = background.get_width()
HEIGHT = background.get_height()
frame = 0


# Pong setup
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



screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("PyGame screen")

icon = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\My Icon.png")
pygame.display.set_icon(icon)


# Background muisic
mixer.music.load("G:\WorkingData\My Music\Portable\Soul Divas\VideoGames.mp3")
mixer.music.play(-1)


# DaFont.com
score_font = pygame.font.Font("freesansbold.ttf", 32)
position_font = pygame.font.Font("freesansbold.ttf", 24)
scoreX = 32
scoreY = 32

# Generate crosshair
crosshair = pygame.surface.Surface((10, 10))
crosshair.fill(pygame.Color("magenta"))
pygame.draw.circle(crosshair, pygame.Color("blue"), (5,5), 5, 0)
crosshair.set_colorkey(pygame.Color("magenta"), pygame.RLEACCEL)
crosshair = crosshair.convert()


# Generate button surfaces
writer = pygame.font.Font(pygame.font.get_default_font(), 15)
buttons = {}
if joyPresent:
    for button in range(joy.get_numbuttons()):
        buttons[button] = [
            writer.render(
                hex(button)[2:].upper(),
                1,
                pygame.Color("red"),
                pygame.Color("black")
            ).convert(),
            # Get co-ords: ((width*slot)+offset, offset). Offsets chosen
            #                                             to match frames.
            ((15*button)+45, 560)
        ]


# Ready player
playerIMG = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\Dodecahedron.gif")
playerX = random.randint(0, WIDTH)
playerY = random.randint(0, HEIGHT)
playerWidth = playerIMG.get_width()
playerHeight = playerIMG.get_height()
playerXcentre = playerWidth // 2
playerYcentre = playerHeight // 2
playerXstep = 2
playerYstep = 2
playerXrate = 0
playerYrate = 0
playerScore = 0
playerJumping = False
playerJumper = 10

# Ready opponent
opponentImages = ['Tetrahedron.gif', 'Octahedron.gif', 'Icosahedron.gif', 'Hexahedron.gif']
opponentIMG = []
opponentX = []
opponentY = []
opponentWidth = []
opponentHeight = []
opponentXcentre = []
opponentYcentre = []
opponentXstep = []
opponentYstep = []
opponentXrate = []
opponentYrate = []
opponentScore = []
opponentXhitbox = []
opponentYhitbox = []
player_opponent = []
opponent_observer = []
opponents = 3

for opponent in range(opponents):
    opponentIMG.append(pygame.image.load(f"G:\WorkingData\Work @ Home\Humanity\{opponentImages[opponent]}"))
    opponentX.append(random.randint(0, WIDTH))
    opponentY.append(random.randint(0, HEIGHT))
    opponentWidth.append(opponentIMG[opponent].get_width())
    opponentHeight.append(opponentIMG[opponent].get_height())
    opponentXcentre.append(opponentWidth[opponent] // 2)
    opponentYcentre.append(opponentHeight[opponent] // 2)
    opponentXstep.append(1)
    opponentYstep.append(1)
    opponentXrate.append(1)
    opponentYrate.append(1)
    opponentXhitbox.append(0)
    opponentYhitbox.append(0)
    opponentScore.append(0)
    player_opponent.append(False)
    opponent_observer.append(False)


# Ready observer
observerIMG = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\GoldenRatioHorus.png")
observerX = None
observerY = None
observerWidth = observerIMG.get_width()
observerHeight = observerIMG.get_height()
observerXcentre = observerWidth // 2
observerYcentre = observerHeight // 2
observerXstep = 3
observerYstep = 3
observerXrate = 1
observerYrate = 1
oldobserverXrate = observerXrate
oldobserverYrate = observerYrate
observerwatching = False
observerScore = 0


def collision(object1X, object1Y, object2X, object2Y):
    distance = math.sqrt(
        math.pow( (object2X - object1X), 2) +
        math.pow( (object2Y - object1Y), 2)
        )
    return distance < 200


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
    pong_pos = [WIDTH // 2, HEIGHT // 2]
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
    ping_pos = [WIDTH // 2, random.randrange(HEIGHT // 2)]
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


def collide():
    global moving_right, moving_left, moving_down, moving_up
    if moving_right or moving_left:
        moving_right = False
        moving_left = True
    else:
        moving_right = True
        moving_left = False

    if moving_down or moving_up:
        moving_down = False
        moving_up = True
    else:
        moving_down = True
        moving_up = False

# 3D enhanced version with bullet time using an engine to demanding for modern computers
# Pong wrestling 3D 2020 Unicorn edition: A feature too far, remastered with a BFG

game_loop = True
while game_loop:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
            print (f"Frames: {frame}")
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            playerX, playerY = pygame.mouse.get_pos()
            playerX -= playerWidth // 2
            playerY -= playerHeight // 2
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.MOUSEWHEEL:
            pass

##        clicks = pygame.mouse.get_pressed()
##        if clicks[pygame.MOUSEMOTION]:
##            pass
##        if clicks[pygame.MOUSEBUTTONDOWN]:
##            playerX, playerY = pygame.mouse.get_pos()
##            playerX -= playerWidth // 2
##            playerY -= playerHeight // 2
##        if clicks[pygame.MOUSEBUTTONUP]:
##            pass
##        if clicks[pygame.MOUSEWHEEL]:
##            pass

        keys = pygame.key.get_pressed()
        for key in keys:

            if keys[pygame.K_LEFT]:
                keyMove = True
                playerXrate = -1.1
                #print (f"Moving LEFT: {playerX}")
            elif keys[pygame.K_RIGHT]:
                keyMove = True
                playerXrate = 1.1
                #print (f"Moving RIGHT: {playerX}")
            else:
                keyMove = False
                playerXrate = 0

            if not playerJumping:
                if keys[pygame.K_UP]:
                    keyMove = True
                    playerYrate = -1.1
                    #print (f"Moving UP: {playerY}")
                elif keys[pygame.K_DOWN]:
                    keyMove = True
                    playerYrate = 1.1
                    #print (f"Moving DOWN: {playerY}")
                else:
                    keyMove = False
                    playerYrate = 0

                if keys[pygame.K_SPACE]:
                    playerJumping = True
                    playerYrate = 0
                    #print(playerY, playerJumping, playerJumper)

            if keys[pygame.K_RCTRL]:
                if observerwatching == True:
                    observerwatching = False
                    observerX = None
                    observerY = None
                    oldobserverXrate = observerXrate
                    oldobserverYrate = observerYrate
                    observerXrate = 0
                    observerYrate = 0
                elif observerwatching == False:
                    observerwatching = True
                    observerX = random.randint(0, WIDTH)
                    observerY = random.randint(0, HEIGHT)
                    observerXrate = oldobserverXrate
                    observerYrate = oldobserverYrate


        # Detect key pressed state
##        if event.type == pygame.KEYDOWN:
##            #print (f"Key pressed at frame: {frame}")
##
##            if event.key == pygame.K_LEFT:
##                keyMove = True
##                playerXrate = -1.1
##                #print (f"Moving LEFT: {playerX}")
##            elif event.key == pygame.K_RIGHT:
##                keyMove = True
##                playerXrate = 1.1
##                #print (f"Moving RIGHT: {playerX}")
##
##            if not playerJumping:
##                if event.key == pygame.K_UP:
##                    keyMove = True
##                    playerYrate = -1.1
##                    #print (f"Moving UP: {playerY}")
##                elif event.key == pygame.K_DOWN:
##                    keyMove = True
##                    playerYrate = 1.1
##                    #print (f"Moving DOWN: {playerY}")
##
##                if event.key == pygame.K_SPACE:
##                    playerJumping = True
##                    playerYrate = 0
##                    print(playerY, playerJumping, playerJumper)
##
##            if event.key == pygame.K_RCTRL:
##                if observerwatching == True:
##                    observerwatching = False
##                    observerX = None
##                    observerY = None
##                    oldobserverXrate = observerXrate
##                    oldobserverYrate = observerYrate
##                    observerXrate = 0
##                    observerYrate = 0
##                elif observerwatching == False:
##                    observerwatching = True
##                    observerX = random.randint(0, WIDTH)
##                    observerY = random.randint(0, HEIGHT)
##                    observerXrate = oldobserverXrate
##                    observerYrate = oldobserverYrate
##                #print (f"observernwatching: {observerwatching}, {observerXrate}, {observerYrate}")
##
##        # Detect key released state
##        if event.type == pygame.KEYUP:
##            #print (f"Key released at frame: {frame}")
##
##            if not playerJumping:
##                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
##                    keyMove = False
##                    playerYrate = 0
##                    #print (f"Holding vertical: {playerY}")
##            else:
##                playerYrate = -1
##
##            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
##                keyMove = False
##                playerXrate = 0
##                #print (f"Holding horizontal: {playerX}")


    if playerJumping:
        if playerJumper >= -10:
            jumpRising = 1
            if playerJumper < 0:
                jumpRising = -1
            playerY -= (playerJumper ** 2) * 0.5 * jumpRising
            playerJumper -= 1
            #print(playerY, playerJumping, playerJumper, jumpRising)
        else:
            playerJumping = False
            playerJumper = 10
            #print(playerY, playerJumping, playerJumper)


    # Get joystick axes
    if joyPresent:
        joyX = joy.get_axis(0)
        joyY = joy.get_axis(1)

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


    # Random fill background
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    #screen.fill( (red, green, blue) )

    # Random circles
    circleX = random.randint(0, WIDTH)
    circleY = random.randint(0, HEIGHT)
    circleSize = random.randint(0, (playerWidth + playerHeight))
    #pygame.draw.circle(screen, (red, green, blue), (circleX, circleY), circleSize)

    # Background
    if (frame % 1) == 0:
        screen.blit(background, (0, 0) )
    clock.tick (frameRate)

    # draw mid line and gutters
    pygame.draw.line(screen, Grey, [WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1)
    pygame.draw.line(screen, Brown, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, Brown, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)

    if football_pitch:
        pygame.draw.circle(screen, lines,
                           [int((WIDTH / 100) * 50), int((HEIGHT / 60) *  30) ],
                           int((WIDTH / 100) * 5), 1)

    if tennis_court:
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 0, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 78, (HEIGHT / 36) *  4.5], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 0, (HEIGHT / 36) *  31.5], [(WIDTH / 78) * 78, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 18, (HEIGHT / 36) *  18], [(WIDTH / 78) * 60, (HEIGHT / 36) *  18], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 18, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 18, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 60, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 60, (HEIGHT / 36) *  31.5], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 78) * 39, (HEIGHT / 36) *  4.5], [(WIDTH / 78) * 39, (HEIGHT / 36) *  31.5], 1)

    if hockey_field:
        pygame.draw.line(screen, lines, [(WIDTH / 100) * 25, (HEIGHT / 60) *  0], [(WIDTH / 100) * 25, (HEIGHT / 60) *  60], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 100) * 50, (HEIGHT / 60) *  0], [(WIDTH / 100) * 50, (HEIGHT / 60) *  60], 1)
        pygame.draw.line(screen, lines, [(WIDTH / 100) * 75, (HEIGHT / 60) *  0], [(WIDTH / 100) * 75, (HEIGHT / 60) *  60], 1)
        pygame.draw.circle(screen, lines,
                           [int((WIDTH / 100) * 50), int((HEIGHT / 60) *  30)],
                           int((WIDTH / 100) * 5), 1)

    # Object collision detection
    playerXhitbox = playerX + playerXcentre
    playerYhitbox = playerY + playerYcentre

    for opponent in range(opponents):
        opponentXhitbox[opponent] = opponentX[opponent] + opponentXcentre[opponent]
        opponentYhitbox[opponent] = opponentY[opponent] + opponentYcentre[opponent]

    if observerwatching == True:
        observerXhitbox = observerX + observerXcentre
        observerYhitbox = observerY + observerYcentre

    for opponent in range(opponents):
        player_opponent[opponent] = collision(playerXhitbox, playerYhitbox, opponentXhitbox[opponent], opponentYhitbox[opponent])

    if observerwatching == True:
        for opponent in range(opponents):
            opponent_observer[opponent] = collision(opponentXhitbox[opponent], opponentYhitbox[opponent], observerXhitbox, observerYhitbox)

    if observerwatching == True:
        observer_player = collision(observerXhitbox, observerYhitbox, playerXhitbox, playerYhitbox)

    # Object scoring
    for opponent in range(opponents):
        if player_opponent[opponent]:
            playerScore += 1
            opponentScore[opponent] -= 1
            opponentX[opponent] = random.randint(0, WIDTH)
            opponentXrate[opponent] += playerXrate
            opponentY[opponent] = random.randint(0, HEIGHT)
            opponentYrate[opponent] += playerYrate

    for opponent in range(opponents):
        if opponent_observer[opponent]:
            opponentScore[opponent] += 1
            observerScore += 1
            opponentX[opponent] = random.randint(0, WIDTH)
            opponentXrate[opponent] += random.randint(-3, 3)
            opponentY[opponent] = random.randint(0, HEIGHT)
            opponentYrate[opponent] += random.randint(-3, 3)

    if observerwatching == True:
        if observer_player:
            playerScore -= 1
            observerScore += 1
            observerX = random.randint(0, WIDTH)
            observerXrate += random.randint(-3, 3)
            #observerXstep -= playerXstep
            observerY = random.randint(0, HEIGHT)
            observerYrate += random.randint(-3, 3)
            #observerYstep -= playerYstep

            #respawn = mixer.Sound("G:\WorkingData\My Music\Portable\Skits\Reloaded.mp3")
            #respawn.play()


    # draw TT&T
    if tracking:
        if len(pong_tail) > 1:
            pygame.draw.lines(screen, Yellow, False, pong_tail, 1)
        if helping_hand:
            if len(ping_tail) > 1:
                pygame.draw.lines(screen, Red, False, ping_tail, 1)


    # Set opponent position
    for opponent in range(opponents):
        opponentX[opponent] += opponentXstep[opponent] * opponentXrate[opponent]
        opponentY[opponent] += opponentYstep[opponent] * opponentYrate[opponent]
        # Restrict opponent position within boundaries
        if opponentX[opponent] < 0:
            opponentXrate[opponent] = 0.9
        if opponentX[opponent] > WIDTH - opponentWidth[opponent]:
            opponentXrate[opponent] = -0.9
        if opponentY[opponent] < 0:
            opponentYrate[opponent] = 0.9
        if opponentY[opponent] > HEIGHT - opponentHeight[opponent]:
            opponentYrate[opponent] = -0.9
        # Display opponent state
        screen.blit(opponentIMG[opponent], (opponentX[opponent], opponentY[opponent]) )

    # Set observer position
    if observerwatching == True:
        observerX += observerXstep * observerXrate
        observerY += observerYstep * observerYrate
        # Restrict observer position within boundaries
        if observerX < 0:
            observerX = 0
            observerXrate = 1.1
        elif observerX > WIDTH - observerWidth:
            observerX = WIDTH - observerWidth
            observerXrate = -1.1
        if observerY < 0:
            observerY = 0
            observerYrate = 1.1
        elif observerY > HEIGHT - observerHeight:
            observerY = HEIGHT - observerHeight
            observerYrate = -1.1
        # Display observer state
        screen.blit(observerIMG, (observerX, observerY) )

    # Set player position
    playerX += playerXstep * playerXrate
    if not playerJumping:
        playerY += playerYstep * playerYrate

    # Absolute joystick position control with deadzone
##    if (keyMove == False and
##        (abs(joyX * 255) > joyDeadzone) or
##        (abs(joyY * 255) > joyDeadzone) ):
##        playerX = round(joyX * (WIDTH / 2)) + (WIDTH / 2) - (playerWidth / 2)
##        playerY = round(joyY * (HEIGHT / 2)) + (HEIGHT / 2) - (playerHeight / 2)

    # Relative joystick position control with deadzone
    if joyPresent:
        if ((abs(joyX * 255) > joyDeadzone) or
            (abs(joyY * 255) > joyDeadzone) ):
            playerX += (joyX * playerXstep * 2)
            playerY += (joyY * playerYstep * 2)

    # Restrict player position within boundaries
    if playerX < 0:
        playerX = 0
    elif playerX > WIDTH - playerWidth:
        playerX = WIDTH - playerWidth
    if playerY < 0:
        playerY = 0
    elif playerY > HEIGHT - playerHeight:
        playerY = HEIGHT - playerHeight

    # Display player state
    screen.blit(playerIMG, (playerX, playerY) )

    if distance_2Dpoints(ping_pos, pong_pos) < BALL_RADIUS * 2:
        collide()

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


    # Draw paddles
    pygame.draw.line(screen, Green, [(PAD_WIDTH / 2) + 1, left_pos],[(PAD_WIDTH / 2) + 1, left_pos + PAD_HEIGHT], PAD_WIDTH)
    pygame.draw.line(screen, Blue, [WIDTH - (PAD_WIDTH / 2) - 1, right_pos],[WIDTH - (PAD_WIDTH / 2) - 1, right_pos + PAD_HEIGHT], PAD_WIDTH)


    # Draw Ping Pong
    pong_pos = list( [int(pong_pos[0]), int(pong_pos[1]) ] )
    ping_pos = list( [int(ping_pos[0]), int(ping_pos[1]) ] )
    pygame.draw.circle(screen, Red, pong_pos, BALL_RADIUS)
    pygame.draw.circle(screen, Yellow, ping_pos, BALL_RADIUS)


    # Update score board
    scores = f"Player: {playerScore}, Opponents: {opponentScore}, Observer: {observerScore}"
    score_board = score_font.render(scores, True, (192, 192, 192))
    screen.blit(score_board, (scoreX, scoreY) )


    # Update positions
    if observerwatching == True:
        positions = "Player: x {:01f} : y {:01f} , Observer: x {:02f} : y {:02f}".format(playerX, playerY, observerX, observerY)
    else:
        positions = "Player: x {:01f} : y {:01f} , Observer: Idle, press Ctrl to invoke".format(playerX, playerY)
    positions_board = position_font.render(positions, True, (128, 128, 128))
    screen.blit(positions_board, (scoreX, scoreY * 2) )


    # Get and display the joystick buttons
    if joyPresent:
        for button in range(joy.get_numbuttons()):
            if joy.get_button(button):
                screen.blit(buttons[button][0], buttons[button][1])


    # Update canvas
    #pygame.display.update()
    pygame.display.flip()
    frame += 1
