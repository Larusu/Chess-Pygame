class Board:
    def __init__(self, fen_str):
        self.piece_placement, self.active_color, self.castling_rights, \
        self.possible_en_passant, self.half_move, self.full_move = fen_str.split(" ")
        self._generate_placement()

    def _assign_piece(self, char):
        if char.isdigit():
            return ["x"] * int(char)
        return [char]

    def _generate_placement(self):
        ranks = self.piece_placement.split("/")
        
        self.board = []

        for rank in ranks:
            row = []
            for c in rank:
                row.extend(self._assign_piece(c))
            self.board.append(row)
    
    def get_board(self) -> list:
        return self.board

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
