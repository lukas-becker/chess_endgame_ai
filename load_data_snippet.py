import pickle
from zipfile import ZipFile


g_filename = "test_22_05"


def load_data():
    s_n_sequence_integers = []

    with ZipFile("S_n_Results/" + g_filename + ".chessAI", "r") as zipped:
        with zipped.open("piece_list.pickle") as piece_list:
            piece_list = pickle.loads(piece_list.read())

        file_list = zipped.namelist()
        file_list.remove("piece_list.pickle")
        for filename in file_list:
            with zipped.open(filename) as s_n:
                s_n_sequence_integers.append(pickle.loads(s_n.read()))
    return piece_list, s_n_sequence_integers
