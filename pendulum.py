import pygame
import math
import time
import random
pygame.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
specklist = []

def drawLine(screen, x0, y0, len, angle):
    'Coordinate system is relative to y axis'
    tip = [x0 + len * math.sin(angle), y0 + len * math.cos(angle)]
    pygame.draw.line(screen, BLACK, [x0, y0], tip, 10)


def angleAccelGrav(grav, len, angle):
    angle_accel = - grav / len * math.sin(angle)
    return angle_accel


def angleAccelDrag(C, w):
    if w > 0:
        angle_accel = - C * w ** 2
    else:
        angle_accel = C * w ** 2
    return angle_accel


len = 100
angle = math.pi / 2
w = 3
x0 = 200
y0 = 200
grav = 100
C = 0.07

time.sleep(1)
running = True
while running:
    screen.fill(WHITE)
    # at 2/3 speed
    dt = clock.tick(50) / 2500  # seconds, not mili

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the angle
    angle_accel = angleAccelGrav(grav, len, angle) + angleAccelDrag(C, w)
    w += angle_accel * dt
    angle += w * dt

    drawLine(screen, x0, y0, len, angle)
    pygame.display.update()

pygame.quit()
