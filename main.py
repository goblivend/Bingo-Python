from bingo import Bingo

board = [
    [( 7, False), (28, False), (42, False), (60, False), (82, False)],
    [( 3, False), (31, False), (48, False), (64, False), (88, False)],
    [( 9, False), (35, False), ( 0, True ), (69, False), (84, False)],
    [(13, False), (21, False), (47, False), (77, False), (99, False)],
    [( 8, False), (32, False), (55, False), (67, False), (96, False)],
]


print('Welcome to Bingo ! Have fun playing')
bingo = Bingo(board)
bingo.play()
