class Board:
    def __init__(self, fen_str):
        self.piece_placement = fen_str.split(" ")[0] # piece placement field only
        self._generate_placement()

    def _assign_piece(self, char):
        if char.isdigit():
            return ["x"] * int(char)
        return [char]

    def _generate_placement(self):
        ranks = self.piece_placement.split("/")
        
        self.board = []

        for rank in ranks:
            for c in rank:
                self.board.extend(self._assign_piece(c))
    
    def get_board(self) -> list:
        return self.board
