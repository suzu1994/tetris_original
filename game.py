from setting import *
from block import *
import random
class Game:
    def __init__(self):
        self.board = [[0 for i in range(MAX_COL + 2)] for j in range(MAX_ROW + 2)]
        self.block = block(random.randint(2, 8))

    def initialize(self):
        for col in range(1,MAX_COL + 1):
            self.board[-1][col] = 1

        for row in range(1,MAX_ROW + 2):
            self.board[row][0] = 1
            self.board[row][-1] = 1