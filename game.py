from setting import *
from block import *
import random
class Game:
    def __init__(self):
        self.board = [[0 for i in range(MAX_COL + 2)] for j in range(MAX_ROW + 2)]
        self.block = Block(random.randint(2, 8))

    def initialize(self):
        for row in range(MAX_ROW + 2):
            for col in range(MAX_COL + 2):
                self.board[row][col] = 0

        for col in range(1,MAX_COL + 1):
            self.board[-1][col] = 1

        for row in range(1,MAX_ROW + 2):
            self.board[row][0] = 1
            self.board[row][-1] = 1

    def set_block_to_board(self):
        for row, col in self.block.shape:
            row += self.block.row
            col += self.block.col
            self.board[row][col] = self.block.type

    def set_newblock(self):
        self.block = Block(random.randint(2, 8))
    
    def is_gameover(self):
        for col in range(1,MAX_COL + 1):
            if self.board[1][col] != 0:
                return True
        
        return False
    
    def delete_row(self):
        row_deleted = []
        for row in range(1,MAX_ROW + 1):
            isfull = True
            for col in range(1,MAX_COL + 1):
                if self.board[row][col] == 0:
                    isfull = False
                    break
            if isfull:
                row_deleted.append(row)
        if row_deleted != []:
            for row in range(row_deleted[0],len(row_deleted),-1):
                self.board[row] = self.board[row - len(row_deleted)] 
            