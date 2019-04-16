import pygame
import random
import time

screen = pygame.display.set_mode((600, 800))

class Speck:
    '''
    Create a speck (square) with lifetime of 1 second
    It will fade from black to white
    '''

    def __init__(self, xcircle, ycircle, t0):
        self.t0 = t0

        edge = random.randint(5, 10)
        xavg = xcircle - edge // 2
        yavg = ycircle - edge // 2
        x = xavg + random.randint(-3, 3)
        y = yavg + random.randint(-3, 3)

        self.rect = pygame.Rect(x, y, edge, edge)

    def draw(self, screen, t):
        dt = t - self.t0
        if dt < 1:
            screen.fill((t * 255, t * 255, t * 255), self.rect)
        else:
            screen.fill((255, 255, 255), self.rect)


a = Speck(10, 10, 0)
print(a.rect)
a.draw(screen, 0)

pygame.display.update()
time.sleep(1)
pygame.quit()
