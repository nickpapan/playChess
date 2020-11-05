import chess


def continue_playing(board):
    return not board.is_game_over() and not board.is_stalemate() and not board.is_insufficient_material()


def get_move():
    return input()


def check_to_queen(board):
    attackers = [board.attackers(chess.WHITE, chess.SQUARES[y]) for y in range(0, 64) if board.piece_at(y) if
                 board.piece_at(y).symbol() == 'q']
    if attackers[0]:
        print("your queen is under attack")


def check_to_king(board):
    attackers = [board.attackers(chess.WHITE, chess.SQUARES[y]) for y in range(0, 64) if board.piece_at(y) if
                 board.piece_at(y).symbol() == 'k']
    if attackers[0]:
        print("your king is under attack")