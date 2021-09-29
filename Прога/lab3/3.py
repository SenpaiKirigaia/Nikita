import pygame
from pygame.draw import *

pygame.init()


elem = [0 for i in range(100)]
element = [0 for i in range(100)]
def car(x, y, size, a): #car(300, 1000, 0.3, a)
    ellipse(screen, (10, 33, 42), (x - 30 * size + a * 330 * size, y + 42 * size, 60 * size, 10 * size))
    rect(screen, (93, 201, 250), (x, y, 330 * size, 60 * size)) #корпус
    rect(screen, (93, 201, 250), (25 * a * size + 70 * size + x, y - 30 * size, 165 * size, 60 * size)) #капот
    rect(screen, (220, 245, 254), (25 * a * size + 80 * size + x, y - 20 * size, 50 * size, 25 * size))
    rect(screen, (220, 245, 254), (25 * a * size + 170 * size + x, y - 20 * size, 50 * size, 25 * size))
    ellipse(screen, (10, 33, 42), (35 * size + x, 42 * size + y, 60 * size, 40 * size))
    ellipse(screen, (10, 33, 42), (235 * size + x, 42 * size + y, 60 * size, 40 * size))

FPS = 30
screen = pygame.display.set_mode((794, 1123))
screen.fill((255, 255, 255))
window1 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window1.fill((0))
window2 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window2.fill((0))
window3 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window3.fill((0))
window4 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window4.fill((0))
window5 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window5.fill((0))
window6 = pygame.Surface((794, 1123), pygame.SRCALPHA)
window6.fill((0))

rect(window1, (1, 0, 0, 50), (0, 0, 80, 300)) #первый
ellipse(window2, (1, 0, 0, 30), (-364, -50, 748, 150)) #first
rect(window2, (1, 0, 0, 150), (0, 150, 150, 200)) #второй
ellipse(window3, (1, 0, 0, 150), (-200, 220, 521, 100)) #second
rect(window1, (1, 0, 0, 50), (263, 30, 144, 300)) #третий
rect(window2, (1, 0, 0, 150), (303, 130, 186, 300)) #четвертый
rect(window3, (1, 0, 0, 50), (392, 0, 187, 300)) #пятый
rect(window1, (1, 0, 0, 50), (432, 0, 216, 300)) #шестой
rect(window4, (1, 0, 0, 100), (442, 0, 206, 300)) #седьмой
rect(window2, (1, 0, 0, 150), (512, 0, 136, 300)) #восьмой
ellipse(window5, (1, 0, 0, 100), (110, 25, 794, 150)) #third
ellipse(window6, (1, 0, 0, 50), (230, -25, 794, 150)) #fourth
ellipse(window1, (1, 0, 0, 100), (700, 160, 794, 150)) #fivth
line(window4, (255, 255, 255), (597, 0), (597, 800), 3)
screen.blit(window1, (0, 0))
screen.blit(window2, (0, 0))
screen.blit(window3, (0, 0))
screen.blit(window4, (0, 0))
screen.blit(window5, (0, 0))
#------------
for i in range(50):
    elem[i] = pygame.Surface((794, 1123), pygame.SRCALPHA)
    elem[i].fill((0))
    ellipse(elem[i], (255, 255, 255, 6), (0 - 3 * i, -10 - 3 * i, 40 + 12 * i, 20 + 6 * i))

for i in range(50):
    ellipse(elem[i], (1, 0, 0, 10), (200 - 6 * i, 220 - 6 * i, 40 + 24 * i, 20 + 12 * i))

for i in range(35):
    ellipse(elem[i], (1, 0, 0, 8), (750 - 6 * i, 100 - 6 * i, 40 + 24 * i, 20 + 12 * i))
    screen.blit(elem[i], (0, 0))
#------------
rect(screen, (88, 107, 103), (0, 761, 794, 362)) #фон
rect(screen, (186, 196, 199), (300, 250, 494, 521)) #дом правый
line(screen, (255, 255, 255), (300, 251), (794, 251), 3) #обводка второго дома
line(screen, (255, 255, 255), (301, 251), (301, 772), 3) #обводка второго дома
line(screen, (255, 255, 255), (300, 772), (794, 772), 3) #обводка второго дома
rect(screen, (118, 144, 138), (400, 390, 119, 455)) #башня 5
rect(screen, (186, 196, 199), (0, 266, 444, 521)) #дом левый
line(screen, (255, 255, 255), (0, 267), (444, 267), 3) #обводка первого дома
line(screen, (255, 255, 255), (444, 267), (444, 787), 3) #обводка первого дома
line(screen, (255, 255, 255), (444, 787), (0, 787), 3) #обводка первого дома
ellipse(screen, (170, 185, 186), (464, 302, 500, 90))
rect(screen, (152, 166, 171), (-110, 300, 119, 455)) #башня 0
rect(screen, (153, 171, 167), (40, 332, 119, 455)) #башня 2
rect(screen, (187, 199, 196), (0, 392, 119, 455)) #башня 1
rect(screen, (222, 227, 226), (300, 292, 119, 495)) #башня 4
rect(screen, (118, 144, 138), (260, 410, 119, 455)) #башня 3
rect(screen, (153, 171, 167), (610, 302, 119, 470)) #башня 6
rect(screen, (152, 166, 171), (740, 266, 119, 505)) #башня 8
rect(screen, (187, 199, 196), (654, 372, 119, 455)) #башня 7
#------
car(50, 847, 0.3, 1)
car(80, 907, 1, 0)
car(300, 857, 0.3, 1)
car(444, 847, 0.3, 1)
car(634, 877, 0.3, 1)
car(424, 1007, 1, 1)
for i in range(35):
    element[i] = pygame.Surface((794, 1132), pygame.SRCALPHA)
    element[i].fill((0))
    ellipse(element[i], (186, 196, 199, 8), (300 - 12 * i, 1000 - 12 * i, 40 + 48 * i, 20 + 24 * i))
    screen.blit(element[i], (0, 0))

screen.blit(window6, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
