import pygame

FPS = 30
screen = pygame.display.set_mode((400, 600))
#                                                  - говнокод -
#                                             (написан без функций)

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

# UFO
pygame.draw.polygon(screen, (100, 151, 100), [(98, 260), (2, 450), (202, 450)])
pygame.draw.polygon(screen, (100, 142, 151), [(98, 260), (53, 350), (147, 350)])
pygame.draw.ellipse(screen, (130, 130, 130), [5, 253, 195, 70], 0)
pygame.draw.ellipse(screen, (191, 191, 191), [32, 250, 140, 45], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [12, 283, 22, 12], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [172, 283, 22, 12], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [40, 298, 22, 12], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [144, 298, 22, 12], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [73, 305, 22, 12], 0)
pygame.draw.ellipse(screen, (255, 255, 255), [107, 305, 22, 12], 0)

# alien
pygame.draw.ellipse(screen, (255, 255, 255), [270, 420, 30, 70], 0)
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


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
