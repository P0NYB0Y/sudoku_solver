from Board import board
from Square import square
from Display import board_UI
from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

# full_test_board = ([square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()])

test_board = ([square(),square(),square(5),square(),square(7),square(8),square(),square(),square()],
                   [square(),square(7),square(),square(4),square(),square(),square(),square(),square()],
                   [square(2),square(),square(),square(5),square(6),square(1),square(3),square(7),square(4)],
                   [square(),square(),square(),square(),square(),square(),square(),square(),square()],
                   [square(),square(),square(),square(),square(4),square(5),square(2),square(1),square(8)],
                   [square(),square(),square(),square(),square(3),square(2),square(4),square(9),square()],
                   [square(),square(),square(),square(9),square(),square(),square(),square(),square(1)],
                   [square(3),square(),square(1),square(),square(),square(7),square(6),square(),square()],
                   [square(4),square(),square(9),square(),square(),square(),square(8),square(),square()])
full_test_board = board(test_board)

for z in range (100):
    full_test_board.hor_comp()
    full_test_board.vert_comp()
    full_test_board.square_check()
    full_test_board.num_inst_chk()

full_test_board.print_table()