import sys

import chess
import json
import stockfish
import pickle

STOCKFISH_PATH = "./stockfish_14.1/stockfish_14.1_win_x64_avx2.exe"
STOCKFISH = stockfish.Stockfish(STOCKFISH_PATH)
VERBOSE = False


def find_board_in_sequence(situation, sequence):
    board_tuple = (situation.turn, situation.__str__())

    for i in range(len(sequence)):
        if board_tuple in sequence[i]:
            return i
    return -1


def find_next_move(curr_board, s_index, s_n_sequence):
    STOCKFISH.set_fen_position(curr_board.fen())
    if curr_board.turn:
        if VERBOSE:
            print("---White:---")
            print("Starting in S" + str(s_index))
        for move in curr_board.legal_moves:
            curr_board.push(move)
            _tmp = find_board_in_sequence(curr_board, [s_n_sequence[s_index - 1]])
            s_index_tmp = s_index - 1
            if _tmp != -1:
                if VERBOSE:
                    print("    Move: " + str(move))
                    print("    S" + str(s_index_tmp))
                    print("Ended in S" + str(s_index))
                curr_board.pop()
                return s_index_tmp, move
            curr_board.pop()

        return -1, None
    else:
        if VERBOSE:
            print("---Black:---")
            print("Starting in S" + str(s_index))
        move = chess.Move.from_uci(STOCKFISH.get_best_move())
        curr_board.push(move)
        s_index = find_board_in_sequence(curr_board, s_n_sequence[:s_index])
        if VERBOSE:
            print("    Move: " + str(move))
            print("    S" + str(s_index))
            print("Ended in S" + str(s_index))
        curr_board.pop()
        return s_index, move


def calculate_all_moves(fen, s_n_sequence):
    moves = []

    board = chess.Board(fen)

    s_index = find_board_in_sequence(board, s_n_sequence)

    while s_index > 0:
        s_index, next_move = find_next_move(board, s_index, s_n_sequence)
        board.push(next_move)
        moves.append(next_move)

    if s_index == -1:
        return None

    return moves


def check_movelist_length():
    for i in range(len(S_n_sequence)):
        for j in range(len(S_n_sequence[i])):
            res = calculate_all_moves(S_n_sequence[i][j], S_n_sequence_tuples)
            if res is None:
                print("Error with Board" + str(j) + " in S_" + str(i) + " - No result found")
            elif len(res) > i:
                print("Error with Board" + str(j) + " in S_" + str(i) + " - Invalid length of movelist")

        print("Checked S_" + str(i))


def get_list_length():
    total = 0
    for i in range(len(S_n_sequence)):
        print("S_" + str(i) + ": " + str(len(S_n_sequence[i])))
        total += len(S_n_sequence[i])
    print("Total: " + str(total))


def check_for_duplicates():
    all_sets = set()
    count = 0
    for i in range(len(S_n_sequence_tuples)):
        count += len(S_n_sequence_tuples[i])
        all_sets |= S_n_sequence_tuples[i]
        if count != len(all_sets):
            print("Error in S" + str(i))

    if count == len(all_sets):
        print("Amount is correct")
    else:
        print("Amount is wrong")


def load_s_n():
    s_n_sequence = []
    s_n_sequence_tuples = []
    f = open("S_n_Results/S_n_seq_rook.chessAI", "r")
    tmp = json.loads(f.read())
    for item in tmp:
        tmp_list = []
        tmp_set = set()
        for board in item:
            chess_board = chess.Board(board)
            tmp_list.append(board)
            tmp_set.add((chess_board.turn, chess_board.__str__()))
        s_n_sequence.append(tmp_list)
        s_n_sequence_tuples.append(tmp_set)
    f.close()

    return s_n_sequence, s_n_sequence_tuples


'''
S_n_sequence, S_n_sequence_tuples = load_s_n()

S_n_objects = []
for s_n in S_n_sequence:
    tmp_list = []
    for fen in s_n:
        tmp_list.append(chess.Board(fen))
    S_n_objects.append(tmp_list)

f = open("S_n_Results/picke_test.chessAI", "wb")
pickle.dump(S_n_objects, f)


f = open("S_n_Results/picke_test.chessAI", "rb")
S_n_objects = pickle.load(f)


import time

start_time = time.time()
f = open("S_n_Results/picke_test_fens.chessAI", "rb")
S_n_objects = pickle.load(f)
end_time = time.time()
time_elapsed = (end_time - start_time)
print("FENs: " + str(time_elapsed))

start_time = time.time()
f = open("S_n_Results/picke_test_objects.chessAI", "rb")
S_n_sequence = pickle.load(f)
end_time = time.time()
time_elapsed = (end_time - start_time)
print("Objects: " + str(time_elapsed))
'''


s = set()
s.add({0: 'A', 1: 'B'})
print(s)
