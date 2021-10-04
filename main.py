import pygame
import numpy as np
import sys
from typing import Union

from pygame.surface import SurfaceType

WIDTH = 600
HEIGHT = 600

BOARD_ROWS = 3
BOARD_COLUMNS = 3

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


def mark_cell(board, row, column, player):
    board[row][column] = player


def is_cell_available(board, row, column) -> bool:
    return board[row][column] == 0


def is_board_full(board) -> bool:
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if board[row][column] == 0:
                return False
    return True


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BG_COLOR)
    pygame.display.set_caption('Tic Tac Toe')
    draw_playing_grid(screen)
    board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

    """
    # test
    is_board_full(board)
    mark_cell(board, 0, 0, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 0, 1, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 0, 2, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 1, 0, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 1, 1, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 1, 2, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 2, 0, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 2, 1, 1)
    print(board)

    is_board_full(board)
    mark_cell(board, 2, 2, 1)
    print(board)

    is_board_full(board)
    # end test
    """

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
