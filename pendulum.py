import pygame
import math
pygame.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

def getXY(len, angle):
    'Coordinate system is relative to y axis'
    x = len * math.sin(angle)
    y = len * math.cos(angle)
    return x, y


def angleAccelGrav(grav, len, angle):
    'Angular acceleration due to gravity'
    'dependent on angle'
    angle_accel = - grav / len * math.sin(angle)
    return angle_accel


def angleAccelDrag(C, w):
    'Angular acceleration due to drag'
    'dependent on angular velocity'
    if w > 0:
        angle_accel = - C * w ** 2
    else:
        angle_accel = C * w ** 2
    return angle_accel


def angleAccelUser(pressedPos, pressedNeg, w):
    'Angular acceleration due to user arrow key presses'
    angle_accel = 0
    if pressedPos:
        angle_accel = 100
    elif pressedNeg:
        angle_accel = -100
    return angle_accel


len = 100
angle = math.pi / 2  # starting angle
w = 3  # starting angular velocity
x0 = 200
y0 = 200
grav = 100  # gravity field strength
C = 0.07  # drag coefficient


running = True
while running:
    pressedPos = pressedNeg = False
    screen.fill(WHITE)
    # at 2/3 speed
    dt = clock.tick(50) / 2500  # seconds, not mili

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check for a key press
        if event.type == pygame.KEYDOWN:
            # the up and down arrows
            if event.key == pygame.K_w:
                pressedPos = True
            elif event.key == pygame.K_s:
                pressedNeg = True

    # update the angle #
    angle_accel = angleAccelGrav(grav, len, angle) + angleAccelDrag(C, w) \
    + angleAccelUser(pressedPos, pressedNeg, w)

    w += angle_accel * dt
    angle += w * dt
    ####

    # draw the circles and the line #
    x, y = getXY(len, angle)
    pygame.draw.line(screen, BLACK, [x0, y0], [x + x0, y + y0], 5)
    pygame.draw.circle(screen, BLACK, (int(x + x0), int(y + y0)), 10)
    pygame.draw.circle(screen, BLACK, (x0, y0), 10)
    pygame.display.update()
    ####

pygame.quit()
