from ..pieces.pawn import Pawn
from ..pieces.king import King
from ..pieces.piece import Piece
from .board import Board

def get_valid_moves(piece: Piece, board: Board, fen_str: str = "") -> list:
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
    
    if isinstance(piece, Pawn):
        _handle_pawn_move(piece, board, legal_moves, fen_str) 

    if isinstance(piece, King):
        _handle_king_move(piece, board, legal_moves, fen_str)

    return legal_moves

def _is_enemy(own_color, other_color):
    return own_color != other_color

def _handle_pawn_move(piece: Pawn, board: Board, legal_moves: list, fen_str):
    possible_takes = piece.available_takes()
    for col, row in possible_takes:
        target_piece = board.get_piece_by_pos(row, col)

        if target_piece is None:
            continue
        elif _is_enemy(piece.get_color(), target_piece.get_color()):
            legal_moves.append((col, row))

    en_passant_move = _get_en_passant_move(piece, fen_str)
    if en_passant_move is not None:
        legal_moves.append(en_passant_move)

def _get_en_passant_move(piece: Pawn, fen_str: str) -> tuple | None:
    if fen_str == "-":
        return None
    own_pos = piece.get_board_position()
    target_pos = algebraic_to_coords(fen_str)
    correct_file = abs(target_pos[0] - own_pos[0]) == 1
    correct_rank = (
        target_pos[1] == own_pos[1] - 1 if piece.get_color() == "white"
        else target_pos[1] == own_pos[1] + 1
    )
    return target_pos if correct_file and correct_rank else None

def _handle_king_move(king: King, board: Board, legal_moves: list, fen_str):
    file, rank = king.get_board_position()
    right_side = True
    left_side = True
    # for right side
    for col in range(1, 7):
        piece = board.get_piece_by_pos(rank, col)
        
        if piece is not None and col < file:
            left_side = False
            continue
        if piece is not None and col > file:
            right_side = False
            continue
    
    if right_side:
        if "K" in fen_str and king.get_color() == "white":
            legal_moves.append(king.get_castling_move("right"))
        elif "k" in fen_str and king.get_color() == "black":
            legal_moves.append(king.get_castling_move("right"))
    if left_side:
        if "Q" in fen_str and king.get_color() == "white":
            legal_moves.append(king.get_castling_move("left"))
        elif "q" in fen_str and king.get_color() == "black":
            legal_moves.append(king.get_castling_move("left"))

def get_piece_valid_takes(piece: Piece, board: Board, en_passant: str):
    takes = []

    if isinstance(piece, Pawn):
        possible_takes = piece.available_takes()
        for col, row in possible_takes:
            target_piece = board.get_piece_by_pos(row, col)

            if target_piece is None:
                takes.append((col, row))

        en_passant_move = _get_en_passant_move(piece, en_passant)
        if en_passant_move is not None:
            takes.append(en_passant_move)

        return takes

    move_paths = piece.generate_possible_moves()

    for direction_paths in move_paths:
        for col, row in direction_paths:
            target_piece = board.get_piece_by_pos(row, col)
            if target_piece is None:
                takes.append((col, row))
            else:
                break

    return takes
    
def get_enemy_at(piece: Piece, board: Board, target_row, target_col,
                 en_passant = "-") -> Piece | None:
    target_piece = board.get_piece_by_pos(target_row, target_col)
    own_color = piece.get_color()

    # for normal takes
    if target_piece and _is_enemy(own_color, target_piece.get_color()):
        return target_piece

    # for en passant
    if en_passant != "-" and is_en_passant_target(target_row, target_col, 
                                                  en_passant):
        if piece.get_color() == "white":
            return board.get_piece_by_pos(target_row + 1, target_col)
        else:
            return board.get_piece_by_pos(target_row - 1, target_col)

    return None

def is_en_passant_target(target_row, target_col, en_passant = "-") -> bool:
    if en_passant == "-":
        return False
    
    en_passant_pos = algebraic_to_coords(en_passant)

    return (target_col, target_row) == en_passant_pos 

def get_castle_move(piece: Piece, board: Board, old_file):
    if not isinstance(piece, King):
        return None
    file, rank = piece.get_board_position()
    
    if (file - old_file) == 2:
        return board.get_piece_by_pos(rank, old_file + 3)
    elif (file - old_file) == -2:
        return board.get_piece_by_pos(rank, old_file - 4)
    return None 

def algebraic_to_coords(notation: str) -> tuple[int, int]:
    file = notation[0]
    rank = notation[1]
    file_map = {
        "a": 0, "b": 1, "c": 2, "d": 3,
        "e": 4, "f": 5, "g": 6, "h": 7,
    }
    
    return int(file_map[file]), 8 - int(rank) 
