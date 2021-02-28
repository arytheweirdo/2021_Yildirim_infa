import pygame
import math
import random

FPS = 30
screen = pygame.display.set_mode((400, 600))
SnoopDogg = pygame.Surface((600, 800))  # Создаем отдельный слой для собачки и последующего редактирования


def drawscene():
    '''
    функция рисует статичный фон: облака, тарелку, инопланетянина
    '''
    # background
    pygame.draw.rect(screen, (0, 51, 0), (0, 350, 400, 250))
    pygame.draw.rect(screen, (0, 42, 51), (0, 0, 400, 350))
    pygame.draw.circle(screen, (255, 255, 255), (250, 190), 60)

    # clouds
    pygame.draw.ellipse(screen, (102, 102, 102), [-90, 180, 340, 70], 0)
    pygame.draw.ellipse(screen, (102, 102, 102), [190, 205, 340, 70], 0)
    pygame.draw.ellipse(screen, (102, 102, 102), [-150, 30, 340, 120], 0)
    pygame.draw.ellipse(screen, (102, 102, 102), [250, 5, 270, 70], 0)
    pygame.draw.ellipse(screen, (102, 102, 102), [160, 110, 380, 80], 0)
    pygame.draw.ellipse(screen, (63, 63, 63), [100, 70, 360, 60], 0)
    pygame.draw.ellipse(screen, (63, 63, 63), [-90, 140, 300, 70], 0)
    pygame.draw.ellipse(screen, (63, 63, 63), [100, 240, 360, 60], 0)

    # Tarelochka
    c1 = random.randint(40, 130)
    c2 = random.randint(130, 210)
    c3 = random.randint(100, 170)
    pygame.draw.polygon(screen, (100, 151, 100), [(98, 260), (2, 450), (202, 450)])
    pygame.draw.polygon(screen, (100, 142, 151), [(98, 260), (53, 350), (147, 350)])
    pygame.draw.ellipse(screen, (130, 130, 130), [5, 253, 195, 70], 0)
    pygame.draw.ellipse(screen, (191, 191, 191), [32, 250, 140, 45], 0)
    pygame.draw.ellipse(screen, (c1, c3, c2), [12, 283, 22, 12], 0)
    pygame.draw.ellipse(screen, (c2, c1, c3), [172, 283, 22, 12], 0)
    pygame.draw.ellipse(screen, (c3, c2, c1), [40, 298, 22, 12], 0)
    pygame.draw.ellipse(screen, (c1, c3, c2), [144, 298, 22, 12], 0)
    pygame.draw.ellipse(screen, (c2, c1, c3), [73, 305, 22, 12], 0)
    pygame.draw.ellipse(screen, (c3, c2, c1), [107, 305, 22, 12], 0)

    # alien
    pygame.draw.ellipse(screen, (255, 255, 255), [270, 420, 30, 70], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), (260, 410, 45, 10))
    # legs
    pygame.draw.ellipse(screen, (255, 255, 255), [264, 473, 15, 23], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [287, 481, 15, 23], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [262, 493, 12, 23], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [289, 500, 12, 23], 0)
    pygame.draw.circle(screen, (255, 255, 255), (257, 513), 7)
    pygame.draw.circle(screen, (255, 255, 255), (305, 520), 7)
    # arms
    pygame.draw.circle(screen, (255, 255, 255), (270, 433), 8)
    pygame.draw.circle(screen, (255, 255, 255), (305, 435), 8)
    pygame.draw.ellipse(screen, (255, 255, 255), [256, 438, 13, 10], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [253, 448, 8, 12], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [307, 438, 13, 10], 0)
    pygame.draw.ellipse(screen, (255, 255, 255), [320, 443, 13, 7], 0)
    # apple
    pygame.draw.circle(screen, (255, 0, 0), (340, 435), 12)
    pygame.draw.aaline(screen, (0, 0, 0), (343, 415), (340, 426), 2)
    # pygame.draw.ellipse(screen, )


def drawdog():
    '''
    Функция рисует собаку-кусаку
    '''
    SnoopDogg.set_colorkey((0, 0, 0))
    # собака-кусака
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (50, 580, 120, 70))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (150, 590, 90, 45))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (200, 600, 50, 50))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (150, 580, 50, 50))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (235, 620, 20, 50))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (180, 600, 20, 50))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (220, 665, 30, 10))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (165, 645, 30, 10))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (115, 625, 35, 70))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (40, 600, 35, 70))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (25, 665, 35, 15))
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (100, 690, 35, 15))
    pygame.draw.rect(SnoopDogg, (153, 102, 0), (45, 545, 80, 80))
    pygame.draw.aalines(SnoopDogg, (0, 0, 0), True, [[45, 545], [125, 545], [125, 625], [45, 625]])
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (30, 545, 20, 30))
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (30, 545, 20, 30), math.pi, 2 * math.pi, 1)
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (30, 545, 20, 30), 0, math.pi, 1)
    pygame.draw.ellipse(SnoopDogg, (153, 102, 0), (120, 545, 20, 30))
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (120, 545, 20, 30), math.pi, 2 * math.pi, 1)
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (120, 545, 20, 30), 0, math.pi, 1)
    pygame.draw.ellipse(SnoopDogg, (255, 255, 255), (100, 570, 20, 15))
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (100, 570, 20, 15), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (100, 570, 20, 15), 0, math.pi, 2)
    pygame.draw.ellipse(SnoopDogg, (255, 255, 255), (50, 570, 20, 15))
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (50, 570, 20, 15), math.pi, 2 * math.pi, 2)
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (50, 570, 20, 15), 0, math.pi, 2)
    pygame.draw.ellipse(SnoopDogg, (0, 0, 0), (55, 575, 5, 5))
    pygame.draw.ellipse(SnoopDogg, (0, 0, 0), (110, 575, 5, 5))
    pygame.draw.arc(SnoopDogg, (0, 0, 0), (65, 590, 40, 20), math.pi, 2 * math.pi, 2)
    pygame.draw.polygon(SnoopDogg, (255, 255, 255), [[70, 605], [70, 615], [75, 610]])
    pygame.draw.polygon(SnoopDogg, (255, 255, 255), [[100, 605], [100, 615], [95, 610]])
    pygame.draw.aalines(SnoopDogg, (0, 0, 0), True, [[70, 605], [70, 615], [75, 610]])
    pygame.draw.aalines(SnoopDogg, (0, 0, 0), True, [[100, 605], [100, 615], [95, 610]])


clock = pygame.time.Clock()
finished = False

scale = 100
poz = -300
drawdog()
dog2 = pygame.transform.flip(SnoopDogg, True, False)
VanDogg = pygame.transform.scale(dog2, (3 * scale, 4 * scale))

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    drawscene()
    if poz < -140:  # Перемещение собаки по горизонтали
        poz += 2
    if poz > -170 and scale > 0:  # Уменьшение размеров собаки
        VanDogg = pygame.transform.scale(dog2, (3 * scale, 4 * scale))
        scale -= 2

    # Добавление слоя собаки на фон
    screen.blit(VanDogg, (poz + (100 - scale) * 2.4, 150 + (100 - scale) * 1.7, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
