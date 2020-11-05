import chess
import Chess_utils
import chess.engine






board = chess.Board()

engine = chess.engine.SimpleEngine.popen_uci(r"c:\\stockfish_20090216_x64")

limit = chess.engine.Limit(time=2.0)

print(board)
print("Whites turn")
chess.Color = False

while Chess_utils.continue_playing(board):



    validmove = False

    if not chess.Color:
        result = engine.play(board, limit)
        board.push(result.move)
    else:
        while (not validmove):
            print("your move:")
            try:
                move = Chess_utils.get_move()
                if chess.Move.from_uci(move) in board.legal_moves:
                    m = chess.Move.from_uci(move)
                    board.push(m)
                    validmove = True
                else:
                    print("Please put a valid move")
            except:
                print("Please put a valid move")


    print(board)
    Chess_utils.check_to_queen(board)


    if chess.Color:
        print("Whites turn")
        chess.Color= False
    else:
        print("Blacks turn")
        chess.Color = True
if chess.Color:
    print("end of game dike mou, Black Wins")
else :
    print("end of game dike mou, White Wins")


