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
        pygame.time.wait(150)
        screen.fill(BACK_COLOR)

        game.block.constant_drop()
        draw_item.draw_board(screen,game.board)
        draw_item.draw_moving_block(screen,game.block)
        pygame.display.update()

        is_bottom = game.block.is_bottom(game.board)
        if is_bottom:
            game.set_block_to_board()
            game.delete_row()
            is_gameover = game.is_gameover()
            if is_gameover:
                game.initialize()

            game.set_newblock()

        
        

        
        #あとで抽出する
        for event in pygame.event.get():
            # close button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                # block rotetion
                if event.key == K_SPACE: # anti-clockwise
                    game.block.rotate(game.board, 1)                    
                if event.key == K_RETURN: # clockwise
                    game.block.rotate(game.board, 0)
                # block movement
                if event.key == K_DOWN:
                    game.block.move(game.board, 0)
                if event.key == K_LEFT:
                    game.block.move(game.board, 1)
                if event.key == K_RIGHT:
                    game.block.move(game.board, 2)

if __name__ == "__main__":
    main()