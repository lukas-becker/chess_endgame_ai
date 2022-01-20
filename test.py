import sys

import chess
import json

S_n_sequence_new = []
f = open("S_n_seq_12_01.json", "r")
tmp = json.loads(f.read())
for item in tmp:
    tmp_list = []
    for board in item:
        tmp_list.append(chess.Board(board))
    S_n_sequence_new.append(tmp_list)
f.close()

for i in range(len(S_n_sequence_new)):
    print("S_" + str(i) + ": " + str(len(S_n_sequence_new[i])))