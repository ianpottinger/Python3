import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Define some colors
COLORS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1400, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF|OPENGL)
pygame.display.set_caption("Rotating Platonic Shapes")

# Set up OpenGL
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (WIDTH/HEIGHT), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glEnable(GL_DEPTH_TEST)

# Set up the Platonic shape
def create_platonic_shape(sides, radius):
    vertices = []
    for i in range(sides):
        angle = 2 * math.pi * i / sides
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append((x, y))
    return vertices

# Set up the Platonic shapes
num_shapes = 12
shapes = []
for i in range(num_shapes):
    sides = random.randint(3, 12)
    radius = random.uniform(0.5, 1.0)
    vertices = create_platonic_shape(sides, radius)
    color = random.choice(COLORS)
    shape = {"vertices": vertices, "color": color, "angle": 0, "position": [0, 0, -0.1], "velocity": [random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1)]}
    shapes.append(shape)

# Set up the center point
center = [1, 1, -1]

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

    # Rotate the Platonic shapes
    for shape in shapes:
        glLoadIdentity()
        glTranslate(center[0], center[1], center[2])
        glRotate(shape["angle"], 0, 1, 0)
        glTranslate(shape["position"][0], shape["position"][1], shape["position"][2])
        glColor3f(shape["color"][0], shape["color"][1], shape["color"][2])
        glBegin(GL_POLYGON)
        for vertex in shape["vertices"]:
            glVertex3f(vertex[0], vertex[1], 0)
        glEnd()
        shape["angle"] += 1

        # Update the position
        for i in range(3):
            shape["position"][i] += shape["velocity"][i]

    # Update the center point
    center[0] = (center[0] + 0.01) % 1

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)
