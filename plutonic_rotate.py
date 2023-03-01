import pygame
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set the width and height of the screen (in pixels)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the center point of the shape
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# Set the size of the shape (in pixels)
SHAPE_SIZE = 100

# Define the vertices of the shape
vertices = [
    (CENTER_X, CENTER_Y - SHAPE_SIZE),
    (CENTER_X - SHAPE_SIZE, CENTER_Y),
    (CENTER_X, CENTER_Y + SHAPE_SIZE),
    (CENTER_X + SHAPE_SIZE, CENTER_Y)
]

# Set the initial rotation angle (in degrees)
angle = 0

# Set the rotation speed (in degrees per frame)
rotation_speed = 1

# Set the clock for the game loop
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the vertices of the shape around the center point
    rotated_vertices = []
    for vertex in vertices:
        x = vertex[0] - CENTER_X
        y = vertex[1] - CENTER_Y
        rotated_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        rotated_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
        rotated_vertices.append((rotated_x + CENTER_X, rotated_y + CENTER_Y))

    # Draw the rotated shape
    pygame.draw.polygon(screen, BLACK, rotated_vertices)

    # Update the rotation angle
    angle += rotation_speed

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
