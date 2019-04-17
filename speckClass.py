import random
import pygame
import time

class Speck:
    '''
    Create a speck (square) with lifetime of 1 second
    It will fade from black to white
    '''

    def __init__(self, xcenter, ycenter, t0):
        self.t0 = t0

        edge = random.randint(10, 15)
        xleft = xcenter - edge // 2
        ytop = ycenter - edge // 2 - 20
        x = xleft + random.randint(-3, 3)
        y = ytop + random.randint(-3, 3)

        self.rect = pygame.Rect(x, y, edge, edge)

    def draw(self, screen, t):
        dt = t - self.t0
        if dt < 1:
            screen.fill((dt * 200, dt * 200, dt * 200), self.rect)
        else:
            screen.fill((255, 255, 255), self.rect)

if __name__ == '__main__':
    screen = pygame.display.set_mode((600, 800))
    a = Speck(10, 10, 0)
    print(a.rect)
    a.draw(screen, 0)

    pygame.display.update()
    time.sleep(1)
    pygame.quit()
