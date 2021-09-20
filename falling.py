import pygame
import time
import speckClass

pygame.init()
WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pygame.display.set_mode((600, 800))
clock = pygame.time.Clock()

'''
constant acceleration
y(0) = 100
y(8) = 500
where time is in seconds
'''

FPS = 50
x = 100
y0 = 100
a = 20

specklist = []

def yGet(y0, a, t):
    # Down is positive in this coordinate system
    y = y0 + a * 0.5 * t ** 2
    return int(y)

# 50 fps, 8 seconds, 400 frames
for f in range(450):
    clock.tick(FPS)
    screen.fill(WHITE)
    t = f/50 + 1

    y = yGet(y0, a, t)
    pygame.draw.circle(screen, BLACK, (x, y), 20)

    if f % 4 == 0:  # every fourth frame add a speck
        # have specks be behind the ball by doing y - 20
        specklist.append(speckClass.Speck(x, y - 20, t, 0.5))  

    for speck in specklist:
        speck.draw(screen, t)

    pygame.display.update()

time.sleep(1)
pygame.quit()
