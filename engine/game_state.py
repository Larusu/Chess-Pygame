from .board import Board
from ..pieces.piece import Piece
from .rules import get_valid_moves

class GameState:
    def __init__(self):
        # later, fen_str should be from a json or somewhere
        self.fen_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b - - 1 32"
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move \
        = self.fen_str.split(" ")

        # instantiate
        self.board = Board(self.piece_placement)

        self.selected_piece: Piece | None = None
        self.current_pos: tuple = ()

    # =======================
    # BOARD RELATED FUNCTIONS
    # =======================
    def get_board_by_position(self, row, col) -> Piece:
        return self.board.get_piece_by_pos(row, col)
        
    # =======================
    # PIECE RELATED FUNCTIONS
    # =======================
    def set_selected_piece(self, piece):
        self.selected_piece = piece
    
    def get_available_moves(self) -> list: 
        return get_valid_moves(self.selected_piece, self.board)

    def move_piece(self, position):
        self.selected_piece.move(position)
        self.board.new_board_position(self.selected_piece) 
        self.selected_piece = None
        self.current_pos = ()

    def get_active_color(self) -> str:
        if self.active_color == "w":
            return "white"
        elif self.active_color == "b":
            return "black"
        else:
            print("\033[31mError: active color\033[0m")
            return ""

    def get_castling_rights(self):
        return self.castling_rights

    def get_possible_en_passant(self):
        return self.possible_en_passant

    def get_half_move(self):
        return self.half_move

    def get_full_move(self):
        return self.full_move
