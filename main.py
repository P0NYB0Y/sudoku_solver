from Board import board
from Square import square

# full_test_table = ([square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()],
# [square(),square(),square(),square(),square(),square(),square(),square(),square()])

full_test_table = ([square(),square(2),square(1),square(),square(),square(4),square(8),square(3),square()],
[square(4),square(),square(3),square(5),square(),square(8),square(2),square(),square(1)],
[square(),square(6),square(),square(1),square(3),square(),square(),square(),square()],
[square(),square(9),square(2),square(),square(7),square(),square(5),square(4),square()],
[square(1),square(),square(5),square(3),square(),square(),square(),square(),square()],
[square(),square(),square(7),square(),square(),square(),square(),square(),square(8)],
[square(),square(5),square(),square(),square(2),square(),square(3),square(),square()],
[square(2),square(3),square(),square(),square(),square(),square(),square(8),square(6)],
[square(7),square(1),square(),square(6),square(8),square(3),square(4),square(5),square()])

full_test_board = board(full_test_table)
for z in range (100):
    full_test_board.hor_comp()
    full_test_board.vert_comp()
    full_test_board.square_check()
    full_test_board.num_inst_chk()
full_test_board.print_table()