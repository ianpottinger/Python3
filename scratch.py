import pygame
import random
#import pgzrun


WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')


pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("PyGame screen")

icon = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\My Icon.png")
pygame.display.set_icon(icon)

