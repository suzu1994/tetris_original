import pygame
import sys
from pygame.locals import *

from setting import *
from game import *
from draw_item import *
def main():
    pygame.init()
    screen  = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(GAMETITLE)
    
    game = Game()
    game.initialize()
    draw_item = DrawItem()

    while(True):
        pygame.time.wait(300)
        screen.fill(BACK_COLOR)

        game.block.constant_drop()
        is_bottom = game.block.is_bottom(game.board)
        if is_bottom:
            game.set_block_to_board()
            game.set_newblock()

        draw_item.draw_board(screen,game.board)
        draw_item.draw_moving_block(screen,game.block)
        
        pygame.display.update()

        
        #あとで抽出する
        for event in pygame.event.get():
            # close button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()