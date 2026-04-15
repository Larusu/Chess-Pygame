from .board import Board
from ..pieces.piece import Piece
from .rules import get_valid_moves, get_enemy_at

class GameState:
    def __init__(self):
        # later, fen_str should be from a json or somewhere
        self.fen_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 1 32"
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move \
        = self.fen_str.split(" ")

        # instantiate
        self.board = Board(self.piece_placement)

        self.selected_piece: Piece | None = None
        self.old_position : tuple = ()

    # =======================
    # BOARD RELATED FUNCTIONS
    # =======================
    def get_board_by_position(self, row, col) -> Piece | None:
        return self.board.get_piece_by_pos(row, col)
        
    # =======================
    # PIECE RELATED FUNCTIONS
    # =======================
    def set_selected_piece(self, piece):
        self.selected_piece = piece
        self.valid_moves = get_valid_moves(piece, self.board)
        self.old_position = (piece.rect.x, piece.rect.y)
    
    def get_available_moves(self) -> list: 
        return self.valid_moves

    def move_piece(self, new_position, coords):
        if self.selected_piece is None:
            print("\033[31mNo selected piece!\033[0m")
            return "invalid"

        # if invalid move
        if coords not in self.valid_moves:
            self.selected_piece.set_position(self.old_position)
            return "invalid"
        
        x_coord, y_coord = coords
        
        target_piece = get_enemy_at(self.selected_piece, self.board, 
                                    y_coord, x_coord)

        if target_piece is not None:
            target_piece.kill() # remove from sprites

        # set new position
        self.board.update_board(self.selected_piece, y_coord, x_coord)
        self.selected_piece.move(x_coord, y_coord)
        self.selected_piece.set_position(new_position)

        # change color
        next_color = "b" if self.selected_piece.color == "white" else "w"
        self.active_color = next_color

        self.selected_piece = None
        self.old_position = ()

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
