import pygame
from time import sleep
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

fps = 50
x = 100
y0 = 100
a = 20

def yGet(y0, a, t):
    # Down is positive in this coordinate system
    y = y0 + a * 0.5 * t ** 2
    return int(y)

# 50 fps, 8 seconds, 400 frames
for f in range(400):
    clock.tick(fps)
    screen.fill(WHITE)
    t = f/50
    y = yGet(y0, a, t)
    pygame.draw.circle(screen, BLACK, (x, y), 8)
    pygame.display.update()

sleep(1)
pygame.quit()
