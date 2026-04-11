from pygame import Rect, draw, Surface, font, SRCALPHA, sprite
from ..utils.utilities import get_font_path
from .config import SQUARE_SIZE, OFFSET, BOARD_COLORS
from ..engine.board import Board

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
        self.font_path = get_font_path("AGENCYR.TTF")
        self.font_size = 15

        # pygame vars
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.pieces = sprite.Group()
        self.selected_piece = None  # for left click
        self.highlight = None
        self.annotation = None      # for right click
        self.annotation_list = []   # to store the annotation
        
        # iniatilize variables
        self._set_squares()
        self._set_pieces()

    def _set_squares(self):
        for row in range(8):
            for col in range(8):
                x_pos = (col * self.square_size) + self.offset
                y_pos = (row * self.square_size) + self.offset
                rect = Rect(x_pos, y_pos, self.square_size, self.square_size)
                self.squares[row][col] = rect
    
    def _set_pieces(self):
        self.pieces = sprite.Group()
        for row in range(8):
            for col in range(8):
                piece = self._valid_piece(row, col)
                
                if piece is None: 
                    continue

                self.pieces.add(piece)

    """
    DRAWING ONLY 
    """
    # FOR PIECES
    def _valid_piece(self, row, col):
        piece = self.board_state.get_board(row, col)
        if piece is not None:
            piece.set_position((self.squares[row][col].x,
                               self.squares[row][col].y))
            return piece

        return None

    def draw_piece(self) -> Surface:
        overlay = Surface(
                (self.size_of_board, self.size_of_board), 
                SRCALPHA).convert_alpha() 
        overlay.fill((0,0,0,0))
        
        # highlight should be drawn before the pieces B)
        if self.highlight or self.annotation:
            self._highlight_square(overlay)

        self.pieces.update()
        self.pieces.draw(overlay)

        return overlay 

    def _highlight_square(self, surface):
        if self.highlight:
            square = self.highlight
            draw.rect(surface, self.board_colors["selected"], square)
        elif self.annotation:
            for square in self.annotation_list:
                draw.rect(surface, self.board_colors["annotation"], square)
    
    # FOR BOARD
    def draw_board(self) -> Surface:
        board = Surface((self.size_of_board, self.size_of_board)).convert()
        board.fill(self.board_colors["background"])
        fonts = font.Font(self.font_path, self.font_size)

        for row in range(8):
            # draw the squares
            for col in range(8):
                color = self._square_color(col, row)
                draw.rect(
                        board, 
                        self.board_colors[color], 
                        self.squares[row][col])
            
            # draw the ranks (numbers) 
            x_pos = board.get_width() - (self.offset - 5)
            y_pos = self.offset + ((row + 0.4) * self.square_size)
            text = str(8 - row)
            rank = fonts.render(text, True, self.board_colors["font"])
            rank_pos = rank.get_rect(x=x_pos, y=y_pos)
            board.blit(rank, rank_pos)
            
        # draw the files (letters)
        text = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for col in range(8):
            x_pos = self.offset + ((col + 0.5) * self.square_size)
            y_pos = board.get_height() - self.offset
            file = fonts.render(text[col], True, self.board_colors["font"])
            file_pos = file.get_rect(x = x_pos, y = y_pos)
            board.blit(file, file_pos)
        
        return board
    
    def _square_color(self, x, y) -> str:
        if (x + y) % 2 == 0:
            return "white"
        else:
            return "black"

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

                # for highlight
                x, y = self._get_square_pos((piece.rect.x, piece.rect.y))
                self.highlight = self.squares[x][y]
                break
            else: 
                self.selected_piece = None

    def handle_right_click(self, mouse_pos):
        position = self._get_square_pos(mouse_pos)

        if position is not None:
            self.selected_piece = None
            self.annotation = self.squares[position[0]][position[1]]
            self._assign_annotation()

    def _get_square_pos(self, position):
        for row in range(8):
            for col in range(8):
                if self.squares[row][col].collidepoint(position):
                    return row, col
        return None

    def _assign_annotation(self):
        if self.annotation in self.annotation_list:
            self.annotation_list.remove(self.annotation)
        else:
            self.annotation_list.append(self.annotation)

    def deselect_piece(self):
        self.selected_piece = None
        self.highlight = None

    def move_piece(self, position):
        if self.selected_piece:
            self.selected_piece.rect.center = position
        # dapat visually move muna yung piece to square 
        # check kung saang square pasok
        # tsaka mo na i set_position for that piece




