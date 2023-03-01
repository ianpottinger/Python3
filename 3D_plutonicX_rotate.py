import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)

# Initialize pygame
pygame.init()

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF|pygame.OPENGL)

# Set the field of view (in degrees)
FOV = 45.0

# Set the near and far clipping planes (in units)
NEAR = 0.1
FAR = 100.0

# Set the center point of the shape
CENTER_X = 0.0
CENTER_Y = 0.0
CENTER_Z = -5.0

# Set the size of the shape (in units)
SHAPE_SIZE = 1.0

# Set the number of sides of the shape
NUM_SIDES = 5

# Define the vertices of the shape
vertices = []
for i in range(NUM_SIDES):
    angle = math.radians(i * 360 / NUM_SIDES)
    x = SHAPE_SIZE * math.cos(angle)
    y = SHAPE_SIZE * math.sin(angle)
    vertices.append((x, y, 0.0))

# Set the initial rotation angle (in degrees)
angle_x = 0.0
angle_y = 0.0
angle_z = 0.0

# Set the rotation speed (in degrees per frame)
rotation_speed_x = 1.0
rotation_speed_y = 2.0
rotation_speed_z = 3.0

# Set the clock for the game loop
clock = pygame.time.Clock()

# Set up the OpenGL environment
glViewport(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(FOV, float(SCREEN_WIDTH)/SCREEN_HEIGHT, NEAR, FAR)
glMatrixMode(GL_MODELVIEW)

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen and depth buffer
    glClearColor(*WHITE, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Rotate the shape around the center point
    glPushMatrix()
    glTranslatef(CENTER_X, CENTER_Y, CENTER_Z)
    glRotatef(angle_x, 1.0, 0.0, 0.0)
    glRotatef(angle_y, 0.0, 1.0, 0.0)
    glRotatef(angle_z, 0.0, 0.0, 1.0)
    glTranslatef(-CENTER_X, -CENTER_Y, -CENTER_Z)

    # Draw the rotated shape
    glBegin(GL_POLYGON)
    for vertex in vertices:
        glVertex3f(*vertex)
    glEnd()

    # Restore the modelview matrix
    glPopMatrix()

    # Update the rotation angles
    angle_x += rotation_speed_x
    angle_y += rotation_speed_y
    angle_z += rotation_speed_z

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

