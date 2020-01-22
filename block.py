import copy
class block:
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