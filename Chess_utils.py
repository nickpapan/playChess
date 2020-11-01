import chess

def continue_playing(board):
    return not board.is_game_over() and not board.is_stalemate() and not board.is_insufficient_material()


def get_move():
    return input()