import pygame


class Bullet:

    def __init__(self, pos_x, pos_y):
        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface((5, 5))
        self.rect = self.surface.get_rect(midtop=(pos_x, pos_y))
        self.speed = 5

    def draw(self):
        self.surface.fill((255, 0, 0))
        self.screen.blit(self.surface, self.rect)

    def update(self):
        self.rect.y -= self.speed


class Bullet_Left(Bullet):

    def update(self):
        self.rect.y -= self.speed
        self.rect.x -= self.speed/5


class Bullet_Right(Bullet):

    def update(self):
        self.rect.y -= self.speed
        self.rect.x += self.speed/5
