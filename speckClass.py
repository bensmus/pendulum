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
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# First layer is drawn on first and is further away, falls slower
ACCELS = [5, 20, 45]

# First layer is smaller
SIZES = [8, 12, 16]

# Each layer has a different alpha
ALPHAS = [120, 120, 200]

LAYERS = [pygame.surface.Surface((WIDTH, HEIGHT)) for i in range(3)]

# Layers after the base layer only blit non-white pixels
for LAYER in LAYERS[1:]:
    LAYER.set_colorkey(WHITE)

for i, LAYER in enumerate(LAYERS):
    LAYER.set_alpha(ALPHAS[i])

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

        # speck sizes half those of balls
        edge = random.randint(SIZES[layer]/2-2, SIZES[layer]/2+2)  # min and max edge size

        xleft = xcenter - edge // 2
        ytop = ycenter - edge // 2
        x = xleft + random.randint(-3, 3)
        y = ytop + random.randint(-3, 3)
        hue_range = 0.1

        self.rect = pygame.Rect(x, y, edge, edge)

        # random hue for HSV color with maximum value and saturation
        # python colorsys HSV and RGB uses color values between 0 and 1
        hue = base_hue + random.random()*hue_range
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

    def __init__(self, layer, x0, y0, base_hue) -> None:
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
        self.y = self.y0 + ACCELS[self.layer] * 0.5 * time_elapsed ** 2 + v0 * time_elapsed
        pygame.draw.rect(LAYERS[self.layer], hsv_to_rgb255(
            (self.base_hue, 1, 1)), (self.x0 - 10, self.y - 10, SIZES[self.layer], SIZES[self.layer]))

        # adding speck
        print(time_elapsed)
        if round(time_elapsed * 100) % 6 == 0:
            print("adding speck")
            self.speck_list.append(Speck(self.x0, self.y - 20, self.base_hue, self.layer))

        # drawing all specks
        for speck in self.speck_list:
            speck.draw()


def randomBall():
    layer = random.randint(0, 2)
    x0 = random.randint(30, WIDTH - 30)
    y0 = 0
    base_hue = random.random()
    return Ball(layer, x0, y0, base_hue)


if __name__ == '__main__':
    balls = []
    running = True
    while running:
        SCREEN.fill(WHITE)
        for LAYER in LAYERS:
            LAYER.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i, ball in enumerate(balls):
            ball.draw()
            if ball.y > 2 * HEIGHT:  # saving memory
                balls.pop(i)

        if random.random() < 0.02:
            balls.append(randomBall())

        # draw the three layers
        for LAYER in LAYERS:
            SCREEN.blit(LAYER, (0, 0))

        pygame.display.update()
    pygame.quit()
