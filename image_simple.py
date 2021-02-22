import pygame


def draw_background(surface, grass, sky, moon):
    """
    the function draws background on your surface with colors grass, sky and moon
    """
    pygame.draw.rect(surface, grass, (0, size_window_y * 0.4, size_window_x, size_window_y * 0.6))
    pygame.draw.rect(surface, sky, (0, 0, size_window_x, size_window_y * 0.6))
    pygame.draw.circle(surface, moon, (size_window_x * 0.6, size_window_y * 0.3), 60)


def draw_clouds(surface, color_dark, color_light):
    """
    the function draws clouds on your surface with dark and light colors
    """

    pygame.draw.ellipse(surface, color_dark, [-90, 180, 340, 70], 0)
    pygame.draw.ellipse(surface, color_dark, [190, 205, 340, 70], 0)
    pygame.draw.ellipse(surface, color_dark, [-150, 30, 340, 120], 0)
    pygame.draw.ellipse(surface, color_dark, [250, 5, 270, 70], 0)
    pygame.draw.ellipse(surface, color_dark, [160, 110, 380, 80], 0)
    pygame.draw.ellipse(surface, color_light, [100, 70, 360, 60], 0)
    pygame.draw.ellipse(surface, color_light, [-90, 140, 300, 70], 0)
    pygame.draw.ellipse(surface, color_light, [100, 240, 360, 60], 0)


def draw_ufo(surface, light1, light2, window1, window2, lights):
    """
    the function draws a UFO on your surface with different colors of lights
    """

    pygame.draw.polygon(surface, light1, [(0.25 * size_window_x, 0.433 * size_window_y), (0.025 * size_window_x, 0.75 * size_window_y), (0.505 * size_window_x, 0.75 * size_window_y)])
    pygame.draw.polygon(surface, light2, [(0.25 * size_window_x, 0.433 * size_window_y), (0.13 * size_window_x, 0.58 * size_window_y), (0.37 * size_window_x, 0.58 * size_window_y)])
    pygame.draw.ellipse(surface, window2, [5, 253, 195, 70], 0)
    pygame.draw.ellipse(surface, window1, [32, 250, 140, 45], 0)
    pygame.draw.ellipse(surface, lights, [12, 0.47 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)
    pygame.draw.ellipse(surface, lights, [172, 0.47 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)
    pygame.draw.ellipse(surface, lights, [40, 0.49 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)
    pygame.draw.ellipse(surface, lights, [144, 0.49 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)
    pygame.draw.ellipse(surface, lights, [73, 0.51 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)
    pygame.draw.ellipse(surface, lights, [107, 0.51 * size_window_y, 0.055 * size_window_y, 0.02 * size_window_y], 0)


def alien_body_ellipse(location, Color, alien_body_x, alien_body_y, body_angle, a_size, bsize, wid,
                       scale):
    """
    now we calculate parameters for alien and draw main part
    """

    Alien_surface = pygame.Surface([500, 500], pygame.SRCALPHA)
    pygame.draw.ellipse(Alien_surface, Color,
                        (alien_body_x * scale, alien_body_y * scale, a_size * scale, bsize * scale),
                        wid)
    surface_rot = pygame.transform.rotate(Alien_surface, body_angle)
    screen.blit(surface_rot, location)


def alien_body_arc(location, Color, alien_body_x, alien_body_y, body_angle, a_size, bsize,
                   start_ang, end_ang, wid, scale):
    """
    now we calculate parameters for alien and draw main part
    """

    Alien_surface = pygame.Surface([300, 300], pygame.SRCALPHA)
    pygame.draw.arc(Alien_surface, Color,
                    (alien_body_x * scale, alien_body_y * scale, a_size * scale, bsize * scale),
                    start_ang, end_ang, wid)
    surface_rot = pygame.transform.rotate(Alien_surface, body_angle)
    screen.blit(surface_rot, location)


def draw_high_part(counter, Alien_location, color_alien, scale):

    """
    the function draws a body and arms
    """

    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)
    # Main Body
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0], Alien_body_location[1], 0, 65, 125, 0,
                       scale)

    # Right arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, Alien_body_location[1], 0, 35, 35, 0,
                       scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 45, Alien_body_location[1], 0, 35, 35, 0,
                       scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 33, (Alien_body_location[1] + 20), 0, 27,
                       17, 0, scale)

    # Left arm
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 45, (Alien_body_location[1] + 35), 0, 15,
                       20, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 20) - counter * 0.02, 0, 27,
                       20, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 95 - counter * 0.02, Alien_body_location[1] + 35 - counter * 0.2, 0, 30, 17,
                       0, scale)


def draw_low_part(Alien_location, color_alien, scale):
    """
    the function draws legs
    """

    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)

    # Left leg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 0, (Alien_body_location[1] + 100), 0, 25,
                       40, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 10, (Alien_body_location[1] + 130), 0, 20,
                       50, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] - 25, (Alien_body_location[1] + 170), 0, 25,
                       25, 0, scale)

    # Right leg
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 50, (Alien_body_location[1] + 100), 0, 25,
                       40, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 65, (Alien_body_location[1] + 130), 0, 20,
                       50, 0, scale)
    alien_body_ellipse(Alien_location, color_alien, Alien_body_location[0] + 75, (Alien_body_location[1] + 170), 0, 25,
                       25, 0, scale)


def draw_head(Alien_location, color_alien, color_black, color_white, scale):
    """
        the function draws a head
    """

    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)

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


def draw_alien(counter, Alien_location, color_alien, color_black, color_white, scale):
    """
        the function draws an alien
    """

    draw_head(Alien_location, color_alien, color_black, color_white, scale)
    draw_high_part(counter, Alien_location, color_alien, scale)
    draw_low_part(Alien_location, color_alien, scale)


def draw_apple(counter, Alien_location, color_apple, color_black, scale):
    """
        the function draws an apple
    """

    Alien_body_location = (Alien_location[0] // 2, Alien_location[1] // 2)
    # Apple
    alien_body_ellipse(Alien_location, color_apple, (Alien_body_location[0] + 110), Alien_body_location[1] - counter, 0, 45,
                       45, 0, scale)
    pi = 3.14
    alien_body_arc(Alien_location, color_black, Alien_body_location[0] + 130, Alien_body_location[1] - 20 - counter, 0, 40,
                   50, pi / 2, pi, 2, scale)
    alien_body_ellipse(Alien_location, (0, 200, 0), Alien_body_location[0] + 118, Alien_body_location[1] - 20 - counter, 0,
                       20, 10, 0, scale)
    alien_body_ellipse(Alien_location, color_black, Alien_body_location[0] + 118, Alien_body_location[1] - 20 - counter, 0,
                       20, 10, 1, scale)


def print_all(counter):
    """
    the function print all on a screen
    """

    draw_background(screen, (0, 51, 0), (0, 42, 51), (255, 255, 255))
    draw_clouds(screen, (102, 102, 102), (63, 63, 63))
    draw_ufo(screen, (100, 151, 100), (100, 142, 151), (191, 191, 191), (130, 130, 130), (255, 255, 255))
    draw_alien(counter, (150, 250), (0, 255, 127), (0, 0, 0), (255, 255, 255), 0.9)

    draw_apple(counter, (150, 250), (255, 0, 0), (0, 0, 0), 0.9)


def animation(counter):
    """
    the function animated our picture
    """

    print_all(counter)


size_window_x = 400
size_window_y = 600

FPS = 30
screen = pygame.display.set_mode((size_window_x, size_window_y))

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
