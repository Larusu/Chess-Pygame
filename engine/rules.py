from ..pieces.piece import Piece
from .board import Board

def get_valid_moves(piece: Piece, board: Board) -> list:
    move_paths = piece.generate_possible_moves()
    own_color = piece.get_color()

    legal_moves = []

    for direction_paths in move_paths:
        for col, row in direction_paths:
            target_piece = board.get_piece_by_pos(row, col)

            # empty square
            if target_piece is None:
                legal_moves.append((col, row))
            # potential take
            elif _is_enemy(own_color, target_piece.get_color()):
                legal_moves.append((col, row))
                break
            # blocked, if ally
            else:
                break
            
    return legal_moves

def _is_enemy(own_color, other_color):
    return own_color != other_color


def get_enemy_at(piece: Piece, board: Board, 
                 target_row, target_col) -> Piece | None:
    target_piece = board.get_piece_by_pos(target_row, target_col)
    own_color = piece.get_color()

    if target_piece and _is_enemy(own_color, target_piece.get_color()):
        return target_piece

    return None
