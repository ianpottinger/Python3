import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
pygame.display.set_caption("Rotating Platonic Shape Bouncing Around a Canvas")

# Set up OpenGL
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (WIDTH/HEIGHT), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)

# Set up the Platonic shape
sides = 12
radius = 1
vertices = []
for i in range(sides):
    angle = 2 * math.pi * i / sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Set up the rotation angle
angle = 0

# Set up the initial position and velocity
position = [0, 0, -5]
velocity = [0.1, 0.2, 0.3]

# Set up the bouncing boundaries
x_bounds = [-3, 3]
y_bounds = [-2, 2]
z_bounds = [-10, -1]

# Start the main game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Set up the rotation matrix
    glLoadIdentity()
    glTranslate(position[0], position[1], position[2])
    glRotate(angle, 1, 1, 1)

    # Draw the Platonic shape
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex3f(vertex[0], vertex[1], 0)
    glEnd()

    # Update the rotation angle
    angle += 1

    # Update the position
    for i in range(3):
        position[i] += velocity[i]

    # Bounce off the boundaries
    if position[0] < x_bounds[0] or position[0] > x_bounds[1]:
        velocity[0] *= -1
    if position[1] < y_bounds[0] or position[1] > y_bounds[1]:
        velocity[1] *= -1
    if position[2] < z_bounds[0] or position[2] > z_bounds[1]:
        velocity[2] *= -1

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
