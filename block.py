import copy
class Block:
    def __init__(self, block_type):
        self.shapes = [[], [], # empty block and wall
                  [[0, -1], [0, 0], [0, 1], [0, 2]], # I block
                  [[-1, -1], [0, -1], [0, 0], [0, 1]], # J block
                  [[0, -1], [0, 0], [0, 1], [-1, 1]], # L block
                  [[0, -1], [0, 0], [-1, 0], [-1, 1]], # S blosk
                  [[-1, -1], [-1, 0], [0, 0], [0, 1]], # Z block
                  [[0, -1], [0, 0], [-1, 0], [0, 1]], # T block
                  [[0, 0], [-1, 0], [0, 1], [-1, 1]]] # square
        
        self.type = block_type
        self.shape = copy.deepcopy(self.shapes[block_type])
        self.row = 1 # initial position
        self.col = 5
    
    def constant_drop(self):
        self.row += 1
    
    def is_bottom(self, board):
        for row, col in self.shape:
            row += self.row
            col += self.col
            if board[row + 1][col] != 0:
                return True
        return False

    def move(self,board,move_type):
        if self.can_move(board,[-1,0]) and move_type == 0:
            self.row += 1

        if self.can_move(board,[0,-1]) and move_type == 1:
            self.col -= 1
        
        if self.can_move(board,[0,1]) and move_type == 2:
            self.col += 1
    def rotate(self,board,direction):
        # long bar rotates differently
        if self.type == 2:
            if direction == 0:
                for dx in self.shape:
                    dx[0], dx[1] = dx[1], 1-dx[0]
            elif direction == 1:
                for dx in self.shape:
                    dx[0], dx[1] = 1-dx[1], dx[0]
        # square doesn`t rotate
        elif self.type == 8:
            pass
        
        # other blocks
        elif direction == 0:
            for dx in self.shape:
                dx[0], dx[1] = dx[1], -dx[0]
        elif direction == 1:
            for dx in self.shape:
                dx[0], dx[1] = -dx[1], dx[0]

    def can_move(self,board,direction):
        for row,col in self.shape:
            row += (self.row + direction[0])
            col += (self.col + direction[1])
            if board[row][col] != 0:
                return False 
        return True