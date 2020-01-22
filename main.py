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
        
        draw_item.draw_board(screen,game.board)
        pygame.display.update()

        
        #あとで抽出する
        for event in pygame.event.get():
            # close button
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()