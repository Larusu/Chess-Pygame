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
        self.move = False
        self.scaled_moves = 0 

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
            self._possible_moves(surface)    
        elif self.annotation:
            for square in self.annotation_list:
                draw.rect(surface, self.board_colors["annotation"], square)
    
    def _possible_moves(self, surface):
        for x, y in self.scaled_moves:
            x_pos = ((x * SQUARE_SIZE) + OFFSET) + int(self.square_size / 2)
            y_pos = ((y * SQUARE_SIZE) + OFFSET) + int(self.square_size / 2)
            circle_size = 9
            draw.circle(surface, 
                        self.board_colors["circles"], 
                        (x_pos, y_pos),
                        circle_size)
    
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
         # clear right-click annotations
        self.annotation = None
        self.annotation_list.clear()
    
        clicked_square = self._get_square_by_pos(mouse_pos)

        if clicked_square is None:
            return
        
        target_pos = self._get_coords_by_square(clicked_square)
        
        # CASE 1: if there is piece already selected
        if self.selected_piece:
            if target_pos in self.scaled_moves:
                self.selected_piece.on_move(
                        clicked_square.center,
                        self.board_state
                        )

        # CASE 2: no piece selected yet or select another piece
        for piece in self.pieces:
            if piece.rect.collidepoint(mouse_pos):
                self.selected_piece = piece

                # for highlight
                square = self._get_square_by_pos(
                        (piece.rect.x, piece.rect.y))
                
                # assign availables moves
                self.scaled_moves = \
                        self.selected_piece.generate_directional_moves()
                
                self.highlight = square
                return

        # otherwise, cancel selection
        self.selected_piece = None
        self.highlight = None
        self.scaled_moves = None

    def handle_right_click(self, mouse_pos):
        square = self._get_square_by_pos(mouse_pos)

        if square is None:
            return

        self.selected_piece = None
        self.annotation = square 
        
        if square in self.annotation_list:
            self.annotation_list.remove(self.annotation)
        else:
            self.annotation_list.append(self.annotation)

    def _get_square_by_pos(self, position):
        for row in range(8):
            for col in range(8):
                if self.squares[row][col].collidepoint(position):
                    return self.squares[row][col]
        return None

    def _get_coords_by_square(self, square):
        for row in range(8):
            for col in range(8):
                if self.squares[row][col] == square:
                    return (col, row)
        return None
    
    def handle_mouse_up(self):
        if self.move:
            self.selected_piece.on_move(
                    self.selected_piece.rect.center,
                    self.board_state)
            self.move = False
        self.selected_piece = None

    def move_piece(self, position):
        if self.selected_piece:
            self.selected_piece.rect.center = position
            self.move = True
        




