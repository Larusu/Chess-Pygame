from pygame import Rect, draw, Surface, font, SRCALPHA
from ..utils.utilities import get_font_path
from .config import SQUARE_SIZE, OFFSET, BOARD_COLORS
from ..engine.board import Board
from ..pieces.piece import Piece

class BoardView:
    def __init__(self):
        # Instantiate
        self.board_state = Board("5k2/ppp5/4P3/3R3p/6P1/1K2Nr2/PP3P2/8 b - - 1 32")

        # Global settings pulled from config
        self.offset = OFFSET              # margin/border around the board
        self.square_size = SQUARE_SIZE    # size of each square
        self.board_colors = BOARD_COLORS  # dictionary of board_colors

        # Local settings
        self.size_of_board = (self.square_size * 8) + (self.offset * 2)
        self.board_surface = Surface((self.size_of_board, self.size_of_board)).convert()
        self.board_surface.fill(self.board_colors["background"])
        self.font_path = get_font_path("AGENCYR.TTF")
        self.font_size = 15
    
    # function to be called in the game
    def draw_board(self) -> Surface:
        self._draw_board()
        return self.board_surface

    def draw_piece(self) -> Surface:
        transparent_bg = Surface((self.size_of_board, self.size_of_board), SRCALPHA).convert_alpha() 
        transparent_bg.fill((0,0,0,0))

        for row in range(8):
            for col in range(8):
                x_pos = (col * self.square_size) + self.offset
                y_pos = (row * self.square_size) + self.offset   
                self._draw_piece(transparent_bg, row, col, (x_pos, y_pos))
        return transparent_bg

    # private functions
    def _draw_piece(self, surface, row, col, position):
        piece = self.board_state.get_board(row, col)

        if piece is not None:
            piece.set_position(position)
            piece.draw(surface)
    
    def _is_white(self, x, y) -> bool:
        return (x + y) % 2 == 0
    
    # function to draw ranks (1–8)
    def _draw_ranks(self, row):
        board_size = self.board_surface.get_width()
        fonts = font.Font(self.font_path, self.font_size)

        x_pos = board_size - (self.offset - 5)
        y_pos = self.offset + ((row + 0.4) * self.square_size)

        text = str(8 - row)

        rank = fonts.render(text, True, self.board_colors["font"])
        rank_pos = rank.get_rect(x = x_pos, y = y_pos)

        self.board_surface.blit(rank, rank_pos)

    # function to draw files (a–h)
    def _draw_files(self):
        board_size = self.board_surface.get_height()
        fonts = font.Font(self.font_path, self.font_size)

        text = ["a", "b", "c", "d", "e", "f", "g", "h"]

        for col in range(8):
            x_pos = self.offset + ((col + 0.5) * self.square_size)
            y_pos = board_size - self.offset

            file = fonts.render(text[col], True, self.board_colors["font"])
            file_pos = file.get_rect(x = x_pos, y = y_pos)

            self.board_surface.blit(file, file_pos)

    # function to draw the board, aside the ranks and files
    def _draw_board(self):
        width = height = self.square_size

        for row in range(8):
            for col in range(8):
                x_pos = (col * self.square_size) + self.offset
                y_pos = (row * self.square_size) + self.offset   

                # Create a NEW square for each position (row, col)
                square = Rect(x_pos, y_pos, width, height)

                if self._is_white(col, row):
                    draw.rect(self.board_surface, self.board_colors["white"], square)
                else:
                    draw.rect(self.board_surface, self.board_colors["black"], square)

            self._draw_ranks(row)

        self._draw_files()


