import pygame
import numpy as np
import sys

from typing import Union

from numpy import ndarray
from pygame.surface import Surface, SurfaceType

WIDTH = 600
HEIGHT = 600

BOARD_ROWS = 3
BOARD_COLUMNS = 3

RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

LINE_WIDTH = 15


def draw_playing_grid(surface: Union[Surface, SurfaceType]) -> None:
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


def mark_cell(board: ndarray, row: int, column: int, player: int) -> None:
    board[row][column] = player


def is_cell_available(board: ndarray, row: int, column: int) -> bool:
    return board[row][column] == 0


def is_board_full(board: ndarray) -> bool:
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
    # end test
    """
    player_turn = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                clicked_row = int(mouse_y//(HEIGHT/BOARD_ROWS))
                clicked_column = int(mouse_x//(WIDTH/BOARD_COLUMNS))
                if is_cell_available(board, clicked_row, clicked_column):
                    mark_cell(board, clicked_row, clicked_column, player_turn)
                    player_turn = 1 if player_turn == 2 else 2
                print(board)
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
