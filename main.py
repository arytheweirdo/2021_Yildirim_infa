import pygame
# from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

color1 = (255, 255, 0)
x1 = 200
y1 = 200
pygame.draw.circle(screen, color1, (x1, y1), 100)

color_black = (0, 0,0)
color2 = (255, 0, 0)
x2 = 160
y2 = 180
pygame.draw.circle(screen, color2, (x2, y2), 20)
pygame.draw.circle(screen, color_black, (x2, y2), 10)

x3 = 240
y3 = 180
pygame.draw.circle(screen, color2, (x3, y3), 25)
pygame.draw.circle(screen, color_black, (x3, y3), 15)

pygame.draw.rect(screen, color_black, (140, 230, 120, 25))

pygame.draw.line(screen, color_black, (210, 170), (270, 140), 20)
pygame.draw.line(screen, color_black, (120, 140), (190, 170), 25)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
