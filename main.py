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


def draw_horizontal_line(surface: Union[Surface, SurfaceType], row: int, player: int) -> None:
    player -= 1
    xi = 0
    yi = (row + 0.5) * HEIGHT / BOARD_ROWS
    xe = WIDTH
    ye = (row + 0.5) * HEIGHT / BOARD_ROWS
    pygame.draw.line(surface,
                     PLAYER_COLOR[player],
                     (xi, yi),
                     (xe, ye),
                     LINE_WIDTH)


def draw_vertical_line(surface: Union[Surface, SurfaceType], column: int, player: int) -> None:
    player -= 1
    xi = (column+0.5) * WIDTH / BOARD_COLUMNS
    yi = 0
    xe = (column+0.5) * WIDTH / BOARD_COLUMNS
    ye = HEIGHT
    pygame.draw.line(surface,
                     PLAYER_COLOR[player],
                     (xi, yi),
                     (xe, ye),
                     LINE_WIDTH)


def draw_desc_diag_line(surface: Union[Surface, SurfaceType], player: int) -> None:
    player -= 1
    xi = 0
    yi = 0
    xe = WIDTH
    ye = HEIGHT
    pygame.draw.line(surface,
                     PLAYER_COLOR[player],
                     (xi, yi),
                     (xe, ye),
                     LINE_WIDTH)


def draw_asc_diag_line(surface: Union[Surface, SurfaceType], player: int) -> None:
    player -= 1
    xi = 0
    yi = HEIGHT
    xe = WIDTH
    ye = 0
    pygame.draw.line(surface,
                     PLAYER_COLOR[player],
                     (xi, yi),
                     (xe, ye),
                     LINE_WIDTH)


def draw_winning_line(surface: Union[Surface, SurfaceType], code: int, player: int) -> None:
    func = {0: draw_horizontal_line,
            1: draw_vertical_line,
            2: draw_desc_diag_line,
            3: draw_asc_diag_line}
    pp, ss = divmod(int(code), 10)
    if pp == 0 or pp == 1:
        func.get(pp)(surface, ss, player)
    else:
        func.get(pp)(surface, player)


def player_won(board: ndarray, player: int) -> tuple[bool, int]:
    for row in range(BOARD_ROWS):
        count = 0
        for column in range(BOARD_COLUMNS):
            count += 1 if player == board[row][column] else 0
        if count == 3:
            code = 0+row
            return True, code

    for column in range(BOARD_COLUMNS):
        count = 0
        for row in range(BOARD_ROWS):
            count += 1 if player == board[row][column] else 0
        if count == 3:
            code = 10+column
            return True, code

    count = 0
    for row in range(BOARD_ROWS):
        count += 1 if player == board[row][row] else 0
        if count == 3:
            code = 20
            return True, code

    count = 0
    for row in range(BOARD_ROWS):
        count += 1 if player == board[row][2-row] else 0
        if count == 3:
            code = 30
            return True, code

    return False, -1


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
    won = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board_is_full(board) or won:
                    screen.fill(BG_COLOR)
                    draw_playing_grid(screen)
                    board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))
                    player_turn = 1
                    won = False
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
                    won, code = player_won(board, player_turn)
                    if won:
                        print(f'Player{player_turn} has won')
                        draw_winning_line(screen, code, player_turn)
                    player_turn = 1 if player_turn == 2 else 2
                print(board)
        pygame.display.update()


if __name__ == "__main__":
    main_loop()
