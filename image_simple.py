import pygame


def draw_background(surface, grass, sky, moon):
    pygame.draw.rect(surface, grass, (0, 350, 400, 250))
    pygame.draw.rect(surface, sky, (0, 0, 400, 350))
    pygame.draw.circle(surface, moon, (250, 190), 60)


def draw_clouds(surface, color1, color2):
    """
    :param surface: is your surface
    :param color1: is dark cloud
    :param color2: is light cloud
    :return:
    """

    pygame.draw.ellipse(surface, color1, [-90, 180, 340, 70], 0)
    pygame.draw.ellipse(surface, color1, [190, 205, 340, 70], 0)
    pygame.draw.ellipse(surface, color1, [-150, 30, 340, 120], 0)
    pygame.draw.ellipse(surface, color1, [250, 5, 270, 70], 0)
    pygame.draw.ellipse(surface, color1, [160, 110, 380, 80], 0)
    pygame.draw.ellipse(surface, color2, [100, 70, 360, 60], 0)
    pygame.draw.ellipse(surface, color2, [-90, 140, 300, 70], 0)
    pygame.draw.ellipse(surface, color2, [100, 240, 360, 60], 0)


def draw_ufo(surface, light1, light2, window1, window2, lights):
    """
    :param surface: is your surface
    :param light1: is blue light
    :param light2: is green light
    :param window1: is little window
    :param window2: is big window
    :param lights: is lights
    :return:
    """

    pygame.draw.polygon(surface, light1, [(98, 260), (2, 450), (202, 450)])
    pygame.draw.polygon(surface, light2, [(98, 260), (53, 350), (147, 350)])
    pygame.draw.ellipse(surface, window2, [5, 253, 195, 70], 0)
    pygame.draw.ellipse(surface, window1, [32, 250, 140, 45], 0)
    pygame.draw.ellipse(surface, lights, [12, 283, 22, 12], 0)
    pygame.draw.ellipse(surface, lights, [172, 283, 22, 12], 0)
    pygame.draw.ellipse(surface, lights, [40, 298, 22, 12], 0)
    pygame.draw.ellipse(surface, lights, [144, 298, 22, 12], 0)
    pygame.draw.ellipse(surface, lights, [73, 305, 22, 12], 0)
    pygame.draw.ellipse(surface, lights, [107, 305, 22, 12], 0)


def alien_body_ellipse(location, Color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize, wid,
                       scale):
    """
    now we calculate parameters for alien and draw main part
    """

    Alien_surface = pygame.Surface([500, 500], pygame.SRCALPHA)
    pygame.draw.ellipse(Alien_surface, Color,
                        (alien_bodypart_xcoord * scale, alien_bodypart_ycoord * scale, asize * scale, bsize * scale),
                        wid)
    surface_rot = pygame.transform.rotate(Alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)


def alien_body_arc(location, Color, alien_bodypart_xcoord, alien_bodypart_ycoord, bodypart_angle, asize, bsize,
                   startang, endang, wid, scale):
    """
    now we calculate parameters for alien and draw main part
    """

    Alien_surface = pygame.Surface([300, 300], pygame.SRCALPHA)
    pygame.draw.arc(Alien_surface, Color,
                    (alien_bodypart_xcoord * scale, alien_bodypart_ycoord * scale, asize * scale, bsize * scale),
                    startang, endang, wid)
    surface_rot = pygame.transform.rotate(Alien_surface, bodypart_angle)
    screen.blit(surface_rot, location)


def draw_alien(Alien_location, color_alien, color_black, color_white, scale):
    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)
    # Main Body
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0], Alien_body_location[1], 0, 65, 125, 0,
                       scale)

    # Left arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, Alien_body_location[1], 0, 35, 35, 0,
                       scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 45, Alien_body_location[1], 0, 35, 35, 0,
                       scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 33, (Alien_body_location[1] + 20), 0, 27,
                       17, 0, scale)

    # Right arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 45, (Alien_body_location[1] + 35), 0, 15,
                       20, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 20), 0, 27,
                       20, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 95, Alien_body_location[1] + 35, 0, 30, 17,
                       0, scale)

    # Left Leg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 0, (Alien_body_location[1] + 100), 0, 25,
                       40, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, (Alien_body_location[1] + 130), 0, 20,
                       50, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 25, (Alien_body_location[1] + 170), 0, 25,
                       25, 0, scale)

    # Rightleg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 50, (Alien_body_location[1] + 100), 0, 25,
                       40, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 65, (Alien_body_location[1] + 130), 0, 20,
                       50, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 170), 0, 25,
                       25, 0, scale)

    # Head
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 5), (Alien_body_location[1] - 60), 0, 60,
                       60, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 25), (Alien_body_location[1] - 80), 0, 60,
                       60, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 20), (Alien_body_location[1] - 80), 0, 60,
                       60, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, Alien_body_location[1] - 85, 0, 85, 35,
                       0, scale)

    # Eyes
    # Left
    alien_body_ellipse(Alien_location, color_black, Alien_body_location[0], (Alien_body_location[1] - 65), 0, 25, 25, 0,
                       scale)
    alien_body_ellipse(Alien_location, color_white, (Alien_body_location[0] + 13), (Alien_body_location[1] - 54), 0, 8,
                       8, 0, scale)
    # Right
    alien_body_ellipse(Alien_location, color_black, (Alien_body_location[0] + 40), (Alien_body_location[1] - 64), 0, 22,
                       22, 0, scale)
    alien_body_ellipse(Alien_location, color_white, (Alien_body_location[0] + 50), (Alien_body_location[1] - 55), 0, 8,
                       8, 0, scale)

    # Ears
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 20), (Alien_body_location[1] - 105), 0,
                       15, 35, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] - 30), (Alien_body_location[1] - 120), 0,
                       25, 25, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 60), (Alien_body_location[1] - 105), 0,
                       15, 35, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, (Alien_body_location[0] + 60), (Alien_body_location[1] - 120), 0,
                       25, 25, 0, scale)


def draw_apple(i, Alien_location, color_apple, color_black, scale):
    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)
    # Apple
    alien_body_ellipse(Alien_location, color_apple, (Alien_body_location[0] + 110), Alien_body_location[1] - i, 0, 45,
                       45, 0, scale)
    pi = 3.14
    alien_body_arc(Alien_location, color_black, Alien_body_location[0] + 130, Alien_body_location[1] - 20 - i, 0, 40,
                   50, pi / 2, pi, 2, scale)
    alien_body_ellipse(Alien_location, (0, 200, 0), Alien_body_location[0] + 118, Alien_body_location[1] - 20 - i, 0,
                       20, 10, 0, scale)
    alien_body_ellipse(Alien_location, color_black, Alien_body_location[0] + 118, Alien_body_location[1] - 20 - i, 0,
                       20, 10, 1, scale)


def print_all(counter):
    draw_background(screen, (0, 51, 0), (0, 42, 51), (255, 255, 255))
    draw_clouds(screen, (102, 102, 102), (63, 63, 63))
    draw_ufo(screen, (100, 151, 100), (100, 142, 151), (191, 191, 191), (130, 130, 130), (255, 255, 255))
    draw_alien((150 + counter, 250), (0, 255, 127), (0, 0, 0), (255, 255, 255), 0.9)

    draw_apple(counter, (150, 250), (255, 0, 0), (0, 0, 0), 0.9)


def animation(counter):
    print_all(counter)


size_window_x = 400
size_window_y = 600

FPS = 30
screen = pygame.display.set_mode((size_window_x, size_window_y))

# animation(0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for i in range(100):
        animation(i)
        pygame.display.update()
        clock = pygame.time.Clock()

    for i in range(100, 0, -1):
        animation(i)
        pygame.display.update()
        clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
