import chess

board = chess.Board("8/6R1/8/2k5/4K3/8/8/6r1 w - - 4 45")
print(board)

attackers = board.attackers(chess.WHITE, chess.G1)
print(attackers)

print(chess.G7 in attackers)

print(board.piece_at(chess.G1))

s = 'ABCDEFGH'

print([y for y in range(1, 64) if board.piece_at(y)])

attackers = [board.attackers(chess.WHITE, chess.SQUARES[y]) for y in range(0, 64) if board.piece_at(y) if board.piece_at(y).symbol() == 'r']
print(attackers[0])
#for y in range(1, 64):
#    if board.piece_at(y) :
#        if board.piece_at(y).symbol() == 'Q':
#            print(board.piece_at(y))











# 'r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4'
