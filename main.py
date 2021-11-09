from Board import board
from Square import square
from Display import board_UI
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

full_test_board = board()
root = Tk()
board_UI(root,full_test_board)


# for z in range (5):
#     full_test_board.hor_comp()
#     full_test_board.vert_comp()
#     full_test_board.square_check()
#     full_test_board.num_inst_chk()
#     print("Num_Instance")
#     full_test_board.print_table()
#     full_test_board.naked_matches()
#     print()
#     print("Obv Pairs")
#     full_test_board.print_table()