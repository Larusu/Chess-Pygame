from pygame import Rect, draw, Surface, font
from ..utils.utilities import get_font_path
from .config import SQUARE_SIZE, OFFSET, BOARD_COLORS

# Global settings pulled from config
offset = OFFSET              # margin/border around the board
square_size = SQUARE_SIZE    # size of each square
board_colors = BOARD_COLORS  # dictionary of colors

def _is_white(x, y) -> bool:
    # Returns True if the square should be white
    # Pattern: alternating colors like a chessboard
    return (x + y) % 2 == 0

# function to draw each individual square
def _draw_square(col, board, square,  color):
    # Set the horizontal (X) position of the square
    square.left = (col * square_size) + OFFSET
    draw.rect(board, color, square)

# function to draw the board, aside the ranks and files
def _draw_board(board, fonts):
    width = height = square_size

    for row in range(8):
        for col in range(8):
            # Create a NEW square for each position (row, col)
            square = Rect(
                (col * square_size) + offset,  # X position
                (row * square_size) + offset,  # Y position
                width,
                height
            )

            if _is_white(col, row):
                _draw_square(col, board, square, board_colors["white"])
            else:
                _draw_square(col, board, square, board_colors["black"])

        _draw_ranks(row, board, fonts)

    _draw_files(board, fonts)

# function to draw ranks (1–8)
def _draw_ranks(row, board: Surface, font_obj):
    board_size = board.get_width()

    x_pos = board_size - (OFFSET - 5)
    y_pos = offset + ((row + 0.4) * square_size)

    text = str(8 - row)

    rank = font_obj.render(text, False, board_colors["font"])
    rank_pos = rank.get_rect(x=x_pos, y=y_pos)

    board.blit(rank, rank_pos)


# function to draw files (a–h)
def _draw_files(board: Surface, font_obj):
    board_size = board.get_height()

    text = ["a", "b", "c", "d", "e", "f", "g", "h"]

    for col in range(8):
        x_pos = offset + ((col + 0.5) * square_size)
        y_pos = board_size - offset

        file = font_obj.render(text[col], True, board_colors["font"])
        file_pos = file.get_rect(x=x_pos, y=y_pos)

        board.blit(file, file_pos)


# function to be called in the game
def board_surface() -> Surface:
    board_size = (square_size * 8) + (OFFSET * 2)

    board = Surface((board_size, board_size)).convert()
    board.fill(board_colors["background"])

    font_path = get_font_path("AGENCYR.TTF")
    fonts = font.Font(font_path, 13)

    _draw_board(board, fonts)

    return board
