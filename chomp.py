#!/usr/bin/python3
# Chomp player
# Bart Massey

import copy, random, sys

class Board(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.squares = [[True] * cols for _ in range(rows)]

    def __str__(self):
        result = '\n'.join([''.join(
            ['▣' if self.squares[r][c] else '▢' for c in range(self.cols)]
        ) for r in range(self.rows)])
        if self.squares[0][0]:
            result = 'x' + result[1:]
        return result

    def moves(self):
        return [(r, c) for r in range(rows) for c in range(cols)
                if board.squares[r][c]]

    def move(self, row, col):
        for r in range(row, self.rows):
            for c in range(col, self.cols):
                self.squares[r][c] = False

def winning_move(board, depth=0):
    if not board.squares[0][0]:
        return (0, 0)
    for r, c in board.moves():
        if board.squares[r][c]:
            tmp = copy.deepcopy(board)
            tmp.move(r, c)
            m = winning_move(tmp, depth=depth+1)
            # print(m, depth)
            if m is None:
                return (r, c)
    return None

cols = int(sys.argv[1])
rows = int(sys.argv[2])

board = Board(rows, cols)
while board.squares[0][0]:
    print()
    print(board)
    move = winning_move(board)
    if move is None:
        legal = board.moves()
        move = random.choice(legal)
        print(move, 'l')
    else:
        print(move, 'w')
    board.move(*move)
