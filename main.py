import pygame
import sys

WIDTH = 600
HEIGHT = 600


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main_loop()
