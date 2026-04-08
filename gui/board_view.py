from pygame import Rect, draw, Surface, font
from ..utils.utilities import get_font_path
from .config import SQUARE_SIZE, OFFSET, BOARD_COLORS
from ..engine.board import Board
from ..pieces.pawn import Pawn
from ..pieces.rook import Rook
from ..pieces.knight import Knight
from ..pieces.bishop import Bishop
from ..pieces.queen import Queen
from ..pieces.king import King

class BoardView:
    def __init__(self):
        # Global settings pulled from config
        self.offset = OFFSET              # margin/border around the board
        self.square_size = SQUARE_SIZE    # size of each square
        self.board_colors = BOARD_COLORS  # dictionary of board_colors
        self.pawn = Pawn()
        self.rook = Rook()
        self.knight = Knight()
        self.bishop = Bishop()
        self.queen = Queen()
        self.king = King()

    def _is_white(self, x, y) -> bool:
        return (x + y) % 2 == 0

    # function to draw ranks (1–8)
    def _draw_ranks(self, row, board: Surface, font_obj):
        board_size = board.get_width()

        x_pos = board_size - (self.offset - 5)
        y_pos = self.offset + ((row + 0.4) * self.square_size)

        text = str(8 - row)

        rank = font_obj.render(text, False, self.board_colors["font"])
        rank_pos = rank.get_rect(x = x_pos, y = y_pos)

        board.blit(rank, rank_pos)

    # function to draw files (a–h)
    def _draw_files(self, board: Surface, font_obj):
        board_size = board.get_height()

        text = ["a", "b", "c", "d", "e", "f", "g", "h"]

        for col in range(8):
            x_pos = self.offset + ((col + 0.5) * self.square_size)
            y_pos = board_size - self.offset

            file = font_obj.render(text[col], True, self.board_colors["font"])
            file_pos = file.get_rect(x = x_pos, y = y_pos)

            board.blit(file, file_pos)

    # function to draw the board, aside the ranks and files
    def _draw_board(self, board, fonts):
        width = height = self.square_size

        for row in range(8):
            for col in range(8):
                # Create a NEW square for each position (row, col)
                square = Rect(
                    (col * self.square_size) + self.offset,  # X position
                    (row * self.square_size) + self.offset,  # Y position
                    width,
                    height
                )

                if self._is_white(col, row):
                    draw.rect(board, self.board_colors["white"], square)
                else:
                    draw.rect(board, self.board_colors["black"], square)

            self._draw_ranks(row, board, fonts)

        self._draw_files(board, fonts)

    # function to be called in the game
    def board_surface(self) -> Surface:
        board_size = (self.square_size * 8) + (self.offset * 2)

        board = Surface((board_size, board_size)).convert()
        board.fill(self.board_colors["background"])

        font_path = get_font_path("AGENCYR.TTF")
        fonts = font.Font(font_path, 13)

        self._draw_board(board, fonts)

        return board
