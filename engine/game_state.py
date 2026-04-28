from .board import Board
from ..pieces.piece import Piece
from ..pieces.pawn import Pawn
from ..pieces.king import King
from ..pieces.rook import Rook
from .rules import get_valid_moves, get_enemy_at, is_en_passant_target, \
algebraic_to_coords, get_castle_move, get_piece_valid_takes

class GameState:
    def __init__(self):
        # later, fen_str should be from a json or somewhere
        self.fen_str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move \
        = self.fen_str.split(" ")

        # instantiate
        self.board = Board(self.piece_placement)

        self.selected_piece: Piece | None = None
        self.old_rect_pos : tuple = ()
        self.old_board_pos : tuple = ()
        self.move_count = 1

    # =======================
    # BOARD RELATED FUNCTIONS
    # =======================
    def get_board_by_position(self, row, col) -> Piece | None:
        return self.board.get_piece_by_pos(row, col)
        
    # =======================
    # PIECE RELATED FUNCTIONS
    # =======================
    def set_selected_piece(self, piece):
        if piece is None:
            print("\033[31mNo selected piece!\033[0m")
            return

        if isinstance(piece, Pawn):
            self.valid_moves = get_valid_moves(piece, self.board, 
                                               self.possible_en_passant)
        elif isinstance(piece, King):
            valid_moves = get_valid_moves(piece, self.board, self.castling_rights)
            self.valid_moves = [moves for moves in valid_moves
                                if moves not in self._all_attacking(piece)]
        else:
            self.valid_moves = get_valid_moves(piece, self.board)
        self.selected_piece = piece
        self.old_rect_pos = (piece.rect.x, piece.rect.y)
        self.old_board_pos = (piece.file, piece.rank)
    
    def get_available_moves(self) -> list: 
        return self.valid_moves

    def move_piece(self, new_position, coords):
        if self.selected_piece is None:
            print("\033[31mNo selected piece!\033[0m")
            return "invalid"

        # if invalid move
        if coords not in self.valid_moves:
            self.selected_piece.set_position(self.old_rect_pos)
            return "invalid"
        
        x_coord, y_coord = coords
        old_x, old_y = self.old_board_pos
        
        # handle captures
        enemy_piece = get_enemy_at(self.selected_piece, self.board, 
                                y_coord, x_coord, self.possible_en_passant)

        if is_en_passant_target(y_coord, x_coord, self.possible_en_passant):
            x_pos, y_pos = algebraic_to_coords(self.possible_en_passant)
            self.board.set_piece_at(y_pos, x_pos, None)
        
        if enemy_piece is not None:
            if isinstance(enemy_piece, Rook):
                self._rook_castling_rights(enemy_piece)
            enemy_piece.kill() # remove from sprites
        
        # set new position
        self.board.update_board(self.selected_piece, y_coord, x_coord)
        self.selected_piece.move(new_position, x_coord, y_coord)
       
        # handle castling
        castled_rook = get_castle_move(self.selected_piece, self.board, old_x)

        if castled_rook is not None:
            rook_x, rook_y = castled_rook.get_board_position()
            
            # castle queen side
            if rook_x + rook_y < old_x + old_y:
                self.board.update_board(castled_rook, rook_y, x_coord + 1)
                castled_rook.move("queen", x_coord + 1, rook_y)
            # castle king side
            else:
                self.board.update_board(castled_rook, rook_y, x_coord - 1)
                castled_rook.move("king", x_coord - 1, rook_y)

        self._update_fen_after_move()

        self.selected_piece = None
        self.old_rect_pos = ()
        self.old_board_pos = ()
        self.w_king_moved = self.b_king_moved = False

    # =======================
    # ACCESSORS AND MUTATORS
    # =======================
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

    # =======================
    # PRIVATE FUNCTIONS
    # =======================
    def _update_fen_after_move(self):
        if self.selected_piece is None:
            return

        piece_placement: str = self.board.generate_fen_placement()         
        piece = self.selected_piece
        own_color = piece.get_color()

        # change color and count full move
        if own_color == "white":
            self.active_color = "b"
        elif own_color == "black":
            self.active_color = "w"
            self.full_move = int(self.full_move) + 1
        
        # handle en passant and 50-move rule
        if isinstance(piece, Pawn):
            self.half_move = 0
            if abs(self.selected_piece.rank - self.old_board_pos[1]) == 2:
                self.possible_en_passant = self._to_algebraic(piece)
            else:
                self.possible_en_passant = "-"
        else:
            self.half_move = int(self.half_move) + 1
            self.possible_en_passant = "-"

        # check for possible castle
        if isinstance(piece, King):
            castling_fen = self.castling_rights
            if own_color == "white":
                self.castling_rights = castling_fen.replace("KQ", "")
            elif own_color == "black":
                self.castling_rights = castling_fen.replace("kq", "")

        if isinstance(piece, Rook):
            self._rook_castling_rights()

        if len(self.castling_rights) == 0:
            self.castling_rights = "-"

        self.fen_str = piece_placement + " " + self.active_color + " "
        self.fen_str += self.castling_rights + " " + self.possible_en_passant
        self.fen_str += " " + str(self.half_move) + " " + str(self.full_move)

    def _rook_castling_rights(self, rook: Rook | None = None):
        old_position = (0, 0)
        if rook is None:
            old_position = self.old_board_pos
        else: 
            old_position = rook.get_board_position()

        castling_fen = self.castling_rights

        rook_map = { (0, 7): "Q", (0, 0): "q", (7, 7): "K", (7, 0): "k", }
        self.castling_rights = castling_fen.replace(rook_map[old_position], "")

    def _to_algebraic(self, piece: Piece) -> str:
        file, rank = piece.get_board_position()
        old_rank = self.old_board_pos[1]
        
        file_map = "abcdefgh"
        
        if (isinstance(piece, Pawn) and abs(old_rank - rank) == 2): 
            middle = (old_rank + rank) // 2 # floor division
            return f"{file_map[file]}{8 - middle}"

        return f"{file_map[file]}{8 - rank}"

    def _all_attacking(self, piece: Piece) -> list:
        all_pieces = self.board.get_all_pieces()
        squares = set()

        for target in all_pieces:
            if target.get_color() != piece.get_color():
                target_takes = get_piece_valid_takes(target, self.board, 
                                                     self.possible_en_passant)
                squares.update(target_takes)

        return list(squares)
