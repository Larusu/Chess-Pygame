from ..pieces.piece import Piece
from ..pieces.pawn import Pawn
from ..pieces.rook import Rook
from ..pieces.knight import Knight
from ..pieces.bishop import Bishop
from ..pieces.queen import Queen
from ..pieces.king import King

class Board:
    def __init__(self, fen_str):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move = fen_str.split(" ")
        self._generate_placement()

    def _assign_piece(self, row: str, rowCount: int):
        piece_map = {
            "p": (Pawn, "black"),
            "r": (Rook, "black"),
            "n": (Knight, "black"),
            "b": (Bishop, "black"),
            "q": (Queen, "black"),
            "k": (King, "black"),
            "P": (Pawn, "white"),
            "R": (Rook, "white"),
            "N": (Knight, "white"),
            "B": (Bishop, "white"),
            "Q": (Queen, "white"),
            "K": (King, "white"),
        }

        col = 0  
        for char in row:
            if char.isdigit():
                col += int(char)
            else:
                piece_class, color = piece_map[char]
                self.board[rowCount][col] = piece_class(color)
                col += 1
    
    def _generate_placement(self):
        ranks = self.piece_placement.split("/")
        for index, rank in enumerate(ranks):
            self._assign_piece(rank, index)
    
    def get_board(self, row, col) -> Piece:
         return self.board[row][col]
        
    def get_active_color(self):
        return self.active_color

    def get_castling_rights(self):
        return self.castling_rights

    def get_possible_en_passant(self):
        return self.possible_en_passant

    def get_half_move(self):
        return self.half_move

    def get_full_move(self):
        return self.full_move
