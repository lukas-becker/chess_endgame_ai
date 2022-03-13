import chess
import chess.syzygy
import pickle
from zipfile import ZipFile

def load_s_n_sequence(filename):
    s_n_sequence_tuples = []
    with ZipFile("S_n_Results/" + filename + ".chessAI") as zipped:
        with zipped.open(filename + ".pickle") as calculation:
            tmp = pickle.loads(calculation.read())
            for item in tmp:
                s_n_sequence_tuples.append(item)
    return s_n_sequence_tuples

def get_board_and_turn(fen):
    split = fen.split()
    short_fen = str(split[0]) + " " + str(split[1])
    return short_fen

def load_s_n_fens(filename):
    s_n_sequence_fen = []
    s_n_sequence_short_fen = []
    with (open("S_n_Results/" + filename + ".chessTest", "rb")) as test_fens:
        tmp = pickle.loads(test_fens.read())
        for item in tmp:
            tmp_set_fen = set()
            tmp_set_short = set()
            for fen in item:
                tmp_set_fen.add(fen)
                tmp_set_short.add(get_board_and_turn(fen))
            s_n_sequence_fen.append(tmp_set_fen)
            s_n_sequence_short_fen.append(tmp_set_short)
    return s_n_sequence_fen, s_n_sequence_short_fen

'''
s_n = load_s_n_sequence("S_n_seq_pawn")

for n in range(len(s_n)):
    print(f"S{n}: {len(s_n[n])}")
    
print(25 * "-")
    

s_n = load_s_n_sequence("S_n_seq_pawn_12_03")

for n in range(len(s_n)):
    print(f"S{n}: {len(s_n[n])}")
'''

s_n_original = load_s_n_sequence("S_n_seq_queen")
s_n_new = load_s_n_sequence("S_n_seq_pawn_12_03")

if len(s_n_original) != len(s_n_new):
    print("Different Lengths")
    print(10* '*')

for n in range(min(len(s_n_original), len(s_n_new))):
    if s_n_original[n] == s_n_new[n]:
        print(f"S{n}: Same")
    else:
        if len(s_n_original[n]) == len(s_n_new[n]):
            print(f"S{n}: Different Elements")
        else:
            print(f"S{n}: Different Sizes")
            print(f"    Original: {len(s_n_original[n])}")
            print(f"    New: {len(s_n_new[n])}")
            
            
syzygy = chess.syzygy.Tablebase()
syzygy.add_directory("C:\\Users\\Lukas\\Studium\\5. Semester\\Studienarbeit\\syzgy")

s_n_fens, s_n_fens_short = load_s_n_fens("S_n_seq_pawn") #_12_03")

for n in range(len(s_n_fens)):
    counter = 0
    print(f"Checking S{n}")
    for fen in s_n_fens[n]:
        chess_board = chess.Board(fen)
        if n != abs(syzygy.probe_dtz(chess_board)) != n + 1:
            counter += 1
    print(f"S{n} contains {len(s_n_fens[n])} Boards. Syzygy believed {counter} were wrong")



#print(f"Board in wrong S_n ({n}) - Syzygy says {abs(syzygy.probe_dtz(chess_board))}")
            #print(chess_board)
            #print(chess_board.fen())
            #print((False, chess_board.__str__()) in s_n_new[0])
            #break
