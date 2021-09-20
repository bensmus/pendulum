import random
from typing import Iterable
import pygame
import time
import colorsys
import numpy as np
pygame.init()

WHITE = 255, 255, 255
BLACK = 0, 0, 0
WIDTH = 600
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
ACCEL = 20

LAYERS = [pygame.surface.Surface((WIDTH, HEIGHT)) for i in range(3)]


def hsv_to_rgb255(hsv) -> Iterable:
    return np.round(np.array(colorsys.hsv_to_rgb(*hsv)) * 255)


class Speck:
    """
    Create a speck (square) with lifetime of 1 second
    It will fade from black to white
    """

    def __init__(self, xcenter, ycenter, base_hue, layer) -> None:
        self.time_birth = time.time()
        self.layer = layer

        edge = random.randint(5, 10)  # min and max edge size
        xleft = xcenter - edge // 2
        ytop = ycenter - edge // 2
        x = xleft + random.randint(-3, 3)
        y = ytop + random.randint(-3, 3)

        self.rect = pygame.Rect(x, y, edge, edge)

        # random hue for HSV color with maximum value and saturation
        # python colorsys HSV and RGB uses color values between 0 and 1
        hue = base_hue + random.random()*0.3
        self.hsv_color = np.array([hue, 1, 1])
        self.lifetime = 1

    def draw(self) -> None:
        time_elapsed = time.time() - self.time_birth
        if time_elapsed > self.lifetime:
            return

        # gets progressively less saturated as time goes on
        self.hsv_color[1] = self.lifetime - time_elapsed
        LAYERS[self.layer].fill(hsv_to_rgb255(self.hsv_color), self.rect)


class Ball:
    """Each ball has specks that are associated with it"""

    def __init__(self, x0, y0, layer, base_hue) -> None:
        self.time_birth = time.time()
        self.x0 = x0
        self.y0 = y0
        self.y = y0
        self.layer = layer
        self.speck_list = []
        self.base_hue = base_hue

    def draw(self) -> None:
        time_elapsed = time.time() - self.time_birth

        v0 = 100
        self.y = self.y0 + ACCEL * 0.5 * time_elapsed ** 2 + v0 * time_elapsed
        pygame.draw.rect(LAYERS[self.layer], hsv_to_rgb255(
            (self.base_hue, 1, 1)), (self.x0 - 10, self.y - 10, 20, 20))

        # adding speck
        print(time_elapsed)
        if round(time_elapsed * 100) % 6 == 0:
            print("adding speck")
            self.speck_list.append(Speck(self.x0, self.y - 20, self.base_hue, self.layer))

        # drawing all specks
        for speck in self.speck_list:
            speck.draw()


def randomBall():
    x0 = random.randint(30, WIDTH - 30)
    y0 = 0
    layer = random.randint(0, 2)
    base_hue = random.random()
    return Ball(x0, y0, layer, base_hue)


if __name__ == '__main__':
    ball = Ball(30, -20, 2, 0.5)
    balls = []
    running = True
    while running:
        SCREEN.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball.draw()
        # if random.random() < 0.05:
        #     balls.append(Ball())

        # draw the three layers
        for layer in LAYERS:
            SCREEN.blit(layer, (0, 0))

        pygame.display.update()
    pygame.quit()
