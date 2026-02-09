from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
    import pygame
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("noise")

        self.tmx_maps = {0: load_pygame("data/levels/omni.tmx")}

        # self.tmx_maps = {0: load_pygame(join('..', 'data', 'levels', 'omni.tmx'))}
        # print(os.getcwd())
        # self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # self.current_stage.run()
            pygame.display.flip()

if __name__ == "__main__":

    game = Game()
    

    game.run()
    