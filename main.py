from Board import board
from Square import square

full_test_table = ([square(),square(5),square(),square(1),square(7),square(9),square(3),square(8),square()],
[square(),square(),square(),square(),square(),square(4),square(),square(1),square()],
[square(),square(1),square(9),square(),square(),square(),square(7),square(2),square()],
[square(),square(),square(),square(),square(),square(8),square(2),square(),square()],
[square(2),square(6),square(),square(),square(4),square(),square(),square(),square(5)],
[square(8),square(3),square(),square(2),square(9),square(),square(),square(),square(7)],
[square(),square(4),square(3),square(),square(6),square(),square(),square(7),square(8)],
[square(6),square(),square(),square(8),square(),square(5),square(),square(4),square(3)],
[square(1),square(9),square(),square(4),square(3),square(),square(),square(),square(2)])

full_test_board = board(full_test_table)
for x in range(100):
    full_test_board.hor_comp()
    full_test_board.vert_comp()
    full_test_board.square_check()
full_test_board.print_table()