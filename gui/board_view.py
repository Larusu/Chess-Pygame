from pygame import Rect, draw, Surface, font, SRCALPHA, sprite
from ..utils.utilities import get_font_path
from .config import SQUARE_SIZE, OFFSET, BOARD_COLORS
from ..engine.board import Board
from ..pieces.piece import Piece

class BoardView:
    def __init__(self):
        # Instantiate
        self.board_state = Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b - - 1 32")

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
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self._set_squares() # for self.squares

        # pygame vars 
        self.pieces = sprite.Group() # only initialize once
        self.selected_piece = None  # fpr left click
        self.annotation = None      # for right click
        self.annotation_list = []   # to store the annotation

    """
    DRAWING ONLY 
    """
    # FOR PIECES
    def draw_piece(self) -> Surface:
        self.overlay = Surface((self.size_of_board, self.size_of_board), SRCALPHA).convert_alpha() 
        self.overlay.fill((0,0,0,0))
        
        self.pieces.empty() # to avoid multiple sprites being created

        for row in range(8):
            for col in range(8):
                piece = self._valid_piece(row, col)
                if piece is None: continue
                self.pieces.add(piece)
       
        # highlight should be drawn before the pieces B)
        if self.selected_piece or self.annotation:
            self._highlight_square()

        self.pieces.update()
        self.pieces.draw(self.overlay)

        return self.overlay 

    def _valid_piece(self, row, col):
        piece = self.board_state.get_board(row, col)
        if piece is not None:
            piece.set_position((self.squares[row][col].x,
                               self.squares[row][col].y))
            return piece

        return None

    def _highlight_square(self):
        if self.selected_piece:
            square = self.selected_piece.rect
            square.size = (self.square_size, self.square_size)
            draw.rect(self.overlay, self.board_colors["selected"], square)
        elif self.annotation:
            for square in self.annotation_list:
                draw.rect(self.overlay, self.board_colors["annotation"], square)
    
    # FOR BOARD
    def draw_board(self) -> Surface:
        for row in range(8):
            for col in range(8):
                color = self._square_color(col, row)
                draw.rect(self.board_surface, self.board_colors[color], self.squares[row][col])
            self._draw_ranks(row)
        self._draw_files()

        return self.board_surface
    
    def _square_color(self, x, y) -> str:
        if (x + y) % 2 == 0:
            return "white"
        else:
            return "black"

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

    """
    FOR HANDLING MOVES
    """
    def handle_left_click(self, mouse_pos):
        # make sure to remove all the annotation first
        self.annotation = None 
        self.annotation_list.clear()

        for piece in self.pieces:
            if piece.rect.collidepoint(mouse_pos):
                self.selected_piece = piece
                return # early return for memory efficiency
        
        self.selected_piece = None

    def handle_right_click(self, mouse_pos):
        for row in range(8):
            for col in range(8):
                if self.squares[row][col].collidepoint(mouse_pos):
                    # make sure to unhighlight the selected_piece first
                    self.selected_piece = None                     
                    self.annotation = self.squares[row][col]
                    self._check_annotation()
                    return # memory efficiency

    def _check_annotation(self):
        if self.annotation in self.annotation_list:
            self.annotation_list.remove(self.annotation)
        else:
            self.annotation_list.append(self.annotation)

    """
    HELPER FUNCTION
    """
    def _set_squares(self):
        for row in range(8):
            for col in range(8):
                x_pos = (col * self.square_size) + self.offset
                y_pos = (row * self.square_size) + self.offset
                rect = Rect(x_pos, y_pos, self.square_size, self.square_size)
                self.squares[row][col] = rect



