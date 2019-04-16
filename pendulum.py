import pygame
import math
pygame.init()

WHITE = 255, 255, 255; BLACK = 0, 0, 0
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

def drawline(screen, x0, y0, len = 100, angle = 0):
    'Coordinate system is relative to y axis'
    tip = [x0 + len * math.sin(angle), y0 + len * math.cos(angle)]
    pygame.draw.line(screen, BLACK, [x0, y0], tip, 3)

run = True
while run:
    dt = clock.tick(50)
    screen.fill(WHITE)
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawline(screen, 100, 100, len = 100, angle = -math.pi / 3)
    pygame.display.update()
pygame.quit()
