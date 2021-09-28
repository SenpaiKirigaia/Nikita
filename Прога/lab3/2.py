import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
surf = pygame.Surface((794, 1123))
surf.fill((255, 255, 255))
l = 650
w = 165

window = pygame.Surface((794, 1123), pygame.SRCALPHA)
window.fill((0))
screen.blit(surf, (0, 0))
wwindow = pygame.Surface((794, 1123), pygame.SRCALPHA)
wwindow.fill((0))
screen.blit(surf, (0, 0))

ellipse(window, (152, 166, 171, 100), (-200, 80, 700, 150))
rect(screen, (185, 196, 199), (0, 0, 794, 650))
rect(screen, (88, 107, 103), (0, 655, 794, 468))
rect(screen, (152, 166, 171), (10, 16, w, l))
rect(screen, (221, 227, 226), (620, 20, w, l))
rect(screen, (118, 134, 148), (570, 180, w, l))
ellipse(wwindow, (152, 166, 171, 100), (200, -40, 700, 200))
ellipse(wwindow, (152, 166, 171, 100), (150, 250, 700, 200))
ellipse(screen, (183, 196, 193), (-50, 900, 1000, 500))
ellipse(window, (152, 166, 171, 100), (110, 920, 200, 50))
ellipse(window, (152, 166, 171, 100), (-100, 800, 200, 50))
ellipse(window, (152, 166, 171, 100), (100, 850, 200, 50))
ellipse(screen, (10, 33, 42), (260, 1000, 60, 10))
rect(screen, (93, 201, 250), (290, 1123 - w, 2 * w, 60))
rect(screen, (93, 201, 250), (360, 1093 - w, w, 60))
rect(screen, (220, 245, 254), (370, 1103 - w, 50, 25))
rect(screen, (220, 245, 254), (460, 1103 - w, 50, 25))
ellipse(screen, (10, 33, 42), (325, 1000, 60, 40))
ellipse(screen, (10, 33, 42), (525, 1000, 60, 40))

screen.blit(window, (0, 0))
rect(screen, (152, 171, 167), (195, 80, w, l))
rect(screen, (187, 199, 196), (135, 150, w, l))
screen.blit(wwindow, (0, 0))

#screen.blit(surf, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()