import pygame, sys
from charactor import Player
from setting import *


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WITDG, HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.window.fill((0, 0, 255))
            self.player.update()
            self.clock.tick(FPS)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
