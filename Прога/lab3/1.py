import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (217, 217, 217), (0, 0, 400, 400))
circle(screen, (255, 255, 84), (200, 175), 150)
rect(screen, (1, 0, 0), (150, 250, 110, 20))
circle(screen, (233, 51, 35), (150, 125), 30)
circle(screen, (233, 51, 35), (260, 125), 20)
circle(screen, (1, 0, 0), (150, 125), 8)
circle(screen, (1, 0, 0), (260, 125), 8)
line(screen, (1, 0, 0), (190, 100), (95, 50), 15)
line(screen, (1, 0, 0), (230, 100), (325, 70), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()