import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS=30
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# game loop
running = True
while running:
    screen.fill(BLACK)


