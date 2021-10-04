import pygame
import sys
from typing import Union

from pygame.surface import SurfaceType

WIDTH = 600
HEIGHT = 600

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

LINE_WIDTH = 15


def draw_playing_grid(surface: Union[pygame.Surface, SurfaceType]) -> None:
    for ii in range(1, 3):
        pygame.draw.line(surface,
                         LINE_COLOR,
                         (0, ii * WIDTH/3),
                         (HEIGHT, ii * WIDTH/3),
                         LINE_WIDTH)
        pygame.draw.line(surface,
                         LINE_COLOR,
                         (ii * HEIGHT/3, 0),
                         (ii * HEIGHT/3, WIDTH),
                         LINE_WIDTH)


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    pygame.display.set_caption('Tic Tac Toe')
    draw_playing_grid(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
