import pygame, sys, time
from settings import *
from debug import debug
from level import Level

class Game:
    def __init__(self):

        # setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('ZELDA CLONE')
        self.clock = pygame.time.Clock()

        self.level = Level()


        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops= -1)

    def run(self):
        last_time = time.time()
        while True:

            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            # game logic
            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
 