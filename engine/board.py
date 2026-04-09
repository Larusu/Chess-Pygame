from ..pieces.piece import Piece
from ..pieces.pawn import Pawn
from ..pieces.rook import Rook
from ..pieces.knight import Knight
from ..pieces.bishop import Bishop
from ..pieces.queen import Queen
from ..pieces.king import King

class Board:
    def __init__(self, fen_str):
        self.board = [["" for _ in range(8)] for _ in range(8)]
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move = fen_str.split(" ")
        self._generate_placement()

    def _assign_piece(self, char):
        if char.isdigit():
            return ["x"] * int(char)
        return [char]

    def _instantiate_piece(self, entireRow, rowCount):
        for index, char in enumerate(entireRow):
            match char:
                case "p":
                    self.board[rowCount][index] = Pawn("black")
                case "r":
                    self.board[rowCount][index] = Rook("black")
                case "n":
                    self.board[rowCount][index] = Knight("black")
                case "b":
                    self.board[rowCount][index] = Bishop("black")
                case "q":
                    self.board[rowCount][index] = Queen("black")
                case "k":
                    self.board[rowCount][index] = King("black")
                case "P": 
                    self.board[rowCount][index] = Pawn("white")
                case "R":  
                    self.board[rowCount][index] = Rook("white")
                case "N":  
                    self.board[rowCount][index] = Knight("white")
                case "B":  
                    self.board[rowCount][index] = Bishop("white")
                case "Q":  
                    self.board[rowCount][index] = Queen("white")
                case "K": 
                    self.board[rowCount][index] = King("white")
                case "x":
                    self.board[rowCount][index] = None  

    def _generate_placement(self):
        ranks = self.piece_placement.split("/")
        
        for index, rank in enumerate(ranks):
            row = []
            for c in rank:
                row.extend(self._assign_piece(c))
            self._instantiate_piece(row, index)
    
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
