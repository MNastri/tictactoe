import pygame
import sys

WIDTH = 600
HEIGHT = 600

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)

def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    pygame.display.set_caption('Tic Tac Toe')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
