import pygame, sys
from pygame.math import Vector2 as v
from setting import *
from room import *


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.name = pygame.display.set_caption("Adventure Odyssey: Enchanted Tower")
        self.clock = pygame.time.Clock()
        self.room = Room()

    def start(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.room.current_stage = "running"
                    if event.key == pygame.K_LEFT and self.room.current_stage == "running":
                        self.room.player.direction = v(-1, 0)
                        if not self.room.check_collision():
                            self.room.update()
                    elif event.key == pygame.K_RIGHT and self.room.current_stage == "running":
                        self.room.player.direction = v(1, 0)
                        if not self.room.check_collision():
                            self.room.update()
                    elif event.key == pygame.K_UP and self.room.current_stage == "running":
                        self.room.player.direction = v(0, -1)
                        if not self.room.check_collision():
                            self.room.update()
                    elif event.key == pygame.K_DOWN and self.room.current_stage == "running":
                        self.room.player.direction = v(0, 1)
                        if not self.room.check_collision():
                            self.room.update()
                    elif event.key == pygame.K_SPACE and self.room.current_stage == "running":
                        self.room.open_door()
                        self.room.check_battle()
                        if self.room.dialogue():
                            self.room.current_stage = "dialogue"
                    if self.room.current_stage == "dialogue":
                        if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                            self.room.buy(event)
                    if event.key == pygame.K_f and self.room.player.statue["fly"]:
                        self.room.fly(event)
                    if self.room.current_stage == "flying":
                        if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3:
                            self.room.fly(event)
                    if event.key == pygame.K_ESCAPE and self.room.current_stage == "dialogue":
                        self.room.current_stage = "running"

            self.room.update_auto()
            self.room.draw_current_map()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.start()
