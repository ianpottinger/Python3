import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
RED = (1, 0, 0)
GREEN = (0, 1, 0)
BLUE = (0, 0, 1)

# Initialize pygame
pygame.init()

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the field of view (in degrees)
FOV = 45.0

# Set the near and far clipping planes (in units)
NEAR = 0.1
FAR = 100.0

# Set the maximum number of shapes
MAX_SHAPES = 10

# Set the minimum and maximum size of the shapes (in units)
MIN_SHAPE_SIZE = 0.5
MAX_SHAPE_SIZE = 1.0

# Set the minimum and maximum number of sides of the shapes
MIN_NUM_SIDES = 3
MAX_NUM_SIDES = 5

# Define the vertices of the shape
def create_vertices(size, num_sides):
    vertices = []
    for i in range(num_sides):
        angle = math.radians(i * 360 / num_sides)
        x = size * math.cos(angle)
        y = size * math.sin(angle)
        vertices.append((x, y, 0.0))
    return vertices

# Define a class for a shape
class Shape:
    def __init__(self):
        # Set the size and number of sides of the shape
        self.size = random.uniform(MIN_SHAPE_SIZE, MAX_SHAPE_SIZE)
        self.num_sides = random.randint(MIN_NUM_SIDES, MAX_NUM_SIDES)

        # Set the position and velocity of the shape
        self.pos = [random.uniform(-SCREEN_WIDTH/2, SCREEN_WIDTH/2), random.uniform(-SCREEN_HEIGHT/2, SCREEN_HEIGHT/2), 0.0]
        self.vel = [random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)]

        # Set the rotation angles and speed of the shape
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0
        self.rotation_speed_x = random.uniform(1.0, 5.0)
        self.rotation_speed_y = random.uniform(1.0, 5.0)
        self.rotation_speed_z = random.uniform(1.0, 5.0)

        # Set the color of the shape
        self.color = (random.uniform(0.5, 1.0), random.uniform(0.5, 1.0), random.uniform(0.5, 1.0))

        # Set the vertices of the shape
        self.vertices = create_vertices(self.size, self.num_sides)

    # Update the position and rotation of the shape
    def update(self):
        for i in range(3):
            self.pos[i] += self.vel[i]
            if abs(self.pos[i]) > (SCREEN_WIDTH/2):
                self.vel[i] *= -1.0
        self.angle_x += self.rotation_speed_x
        self.angle_y += self.rotation_speed_y
