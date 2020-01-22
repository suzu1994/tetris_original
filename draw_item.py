import pygame
from pygame.locals import *

from setting import *
from block import *
class DrawItem:
    def __init__(self):
        self.block_colors = BLOCK_COLOR = [(50, 50, 50), (150, 150, 150), (255, 0, 0), (0, 0, 255), (255, 165, 0),
                   (255, 0, 255), (0, 255, 0), (0, 255, 255), (255, 255, 0), (200, 200, 200), (100, 100, 100)]

    def draw_board(self,screen,board):
        for row in range(MAX_ROW + 2):
            for col in range(MAX_COL+2):
                pygame.draw.rect(screen, (255, 255, 255), Rect(30+35*col, 30+35*row, 35, 35))
                pygame.draw.rect(screen,self.block_colors[board[row][col]],Rect(31+35*col, 31+35*row, 34, 34))
    
    def draw_moving_block(self,screen,block):
        for row ,col in block.shape:
            row += block.row
            col += block.col
            pygame.draw.rect(screen,self.block_colors[block.type],Rect(31+35*col, 31+35*row, 34, 34))


        
        