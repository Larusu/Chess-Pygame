from ..pieces.piece import Piece
from ..pieces.pawn import Pawn
from ..pieces.rook import Rook
from ..pieces.knight import Knight
from ..pieces.bishop import Bishop
from ..pieces.queen import Queen
from ..pieces.king import King

class Board:
    def __init__(self, fen_string):
        self.board: list[list[Piece | None]] = \
                [[None for _ in range(8)]for _ in range(8)]
        self._generate_placement(fen_string)

    def _assign_piece(self, row: str, rowCount: int):
        piece_map = {
            "p": (Pawn, "black", 'p'),
            "r": (Rook, "black", 'r'),
            "n": (Knight, "black", 'n'),
            "b": (Bishop, "black", 'b'),
            "q": (Queen, "black", 'q'),
            "k": (King, "black", 'k'),
            "P": (Pawn, "white", 'P'),
            "R": (Rook, "white", 'R'),
            "N": (Knight, "white", 'N'),
            "B": (Bishop, "white", 'B'),
            "Q": (Queen, "white", 'Q'),
            "K": (King, "white", 'K'),
        }

        col = 0  
        for char in row:
            if char.isdigit():
                col += int(char)
            else:
                piece_class, color, char = piece_map[char]
                self.board[rowCount][col] = \
                        piece_class(color, col, rowCount)
                col += 1
    
    def _generate_placement(self, fen_placement):
        ranks = fen_placement.split("/")
        for index, rank in enumerate(ranks):
            self._assign_piece(rank, index)
    
    def update_board(self, piece: Piece, target_row: int, target_col: int):
        old_row, old_col = piece.rank, piece.file
        
        self.board[old_row][old_col] = None
        self.board[target_row][target_col] = piece

    def get_piece_by_pos(self, row, col) -> Piece | None:
         return self.board[row][col]
