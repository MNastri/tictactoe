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

BG_COLOR = (33, 189, 172)
LINE_COLOR = (25, 161, 146)
PLAYER_COLOR = [(84, 84, 84), (242, 235, 212)]

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


def cell_is_available(board: ndarray, row: int, column: int) -> bool:
    return board[row][column] == 0


def board_is_full(board: ndarray) -> bool:
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            if board[row][column] == 0:
                return False
    return True


def player_won(board: ndarray) -> bool:
    count = 0
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS-1):
            count += board[row][column] == board[row][column+1]
            if count == 3:
                return True
    count = 0
    for column in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS-1):
            count += board[row][column] == board[row+1][column]
            if count == 3:
                return True
    count = 0
    for row in range(BOARD_ROWS-2):
        count += board[row][row] == board[row+1][row+1]
        if count == 3:
            return True
        break
    count = 0
    for row in range(BOARD_ROWS-2):
        count += board[row][BOARD_COLUMNS-row-1] == board[row+1][BOARD_COLUMNS-row-2]
        if count == 3:
            return True
    return False


def draw_marker(surface: Union[Surface, SurfaceType], row: int, column: int, player: int):
    player -= 1
    if player == 1:
        left = int(column * WIDTH / BOARD_COLUMNS)
        top = int(row * HEIGHT / BOARD_ROWS)
        width = int(WIDTH / BOARD_COLUMNS)
        height = int(HEIGHT / BOARD_ROWS)
        pygame.draw.ellipse(surface,
                            PLAYER_COLOR[player],
                            (left, top, width, height),
                            LINE_WIDTH)
    else:
        xi = column * WIDTH / BOARD_COLUMNS
        yi = row * HEIGHT / BOARD_ROWS
        xe = (column + 1) * WIDTH / BOARD_COLUMNS
        ye = (row + 1) * HEIGHT / BOARD_ROWS
        pygame.draw.line(surface,
                         PLAYER_COLOR[player],
                         (xi, yi),
                         (xe, ye),
                         LINE_WIDTH)
        pygame.draw.line(surface,
                         PLAYER_COLOR[player],
                         (xe, yi),
                         (xi, ye),
                         LINE_WIDTH)


def main_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill(BG_COLOR)
    draw_playing_grid(screen)
    board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
    player_turn = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board_is_full(board):
                    screen.fill(BG_COLOR)
                    draw_playing_grid(screen)
                    board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
                    player_turn = 1
                    continue
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                row_height = HEIGHT/BOARD_ROWS
                column_width = WIDTH/BOARD_COLUMNS
                clicked_row = int(mouse_y//row_height)
                clicked_column = int(mouse_x//column_width)
                if cell_is_available(board, clicked_row, clicked_column):
                    mark_cell(board, clicked_row, clicked_column, player_turn)
                    draw_marker(screen, clicked_row, clicked_column, player_turn)
                    if player_won(board):
                        print(f'Player{player_turn} has won')
                    player_turn = 1 if player_turn == 2 else 2
                print(board)
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
