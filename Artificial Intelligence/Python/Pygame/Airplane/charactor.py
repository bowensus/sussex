import pygame
from element import *


class Player:

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface((50, 50))
        self.rect = self.surface.get_rect(midtop=(300, 750))
        self.key_statue = {pygame.K_LEFT: False, pygame.K_UP: False, pygame.K_RIGHT: False, pygame.K_DOWN: False}
        self.speed = 5
        self.bullets = []

        self.bullets_last_shot = pygame.time.get_ticks()
        self.bullets_shot_interval = 100

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

        self.surface.fill((0, 255, 0))
        self.screen.blit(self.surface, self.rect)

    def create_bullet(self):
        new_bullet_mid = Bullet(self.rect.centerx, self.rect.y)
        new_bullet_left = Bullet_Left(self.rect.centerx-25, self.rect.y)
        new_bullet_right = Bullet_Right(self.rect.centerx+25, self.rect.y)
        self.bullets.append(new_bullet_mid)
        self.bullets.append(new_bullet_left)
        self.bullets.append(new_bullet_right)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.bullets_last_shot > self.bullets_shot_interval:
            self.create_bullet()
            self.bullets_last_shot = current_time

        for bullet in self.bullets:
            bullet.update()

        self.get_input()
        self.draw()

    def get_input(self):
        # a bool list, index are keys on keyboard
        keys = pygame.key.get_pressed()
        for key in self.key_statue.keys():
            # statue updated by keys, keydown is true, keyup is false
            self.key_statue[key] = keys[key]

        if self.key_statue[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if self.key_statue[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if self.key_statue[pygame.K_RIGHT] and self.rect.x <= 550:
            self.rect.x += self.speed
        if self.key_statue[pygame.K_DOWN] and self.rect.y <= 750:
            self.rect.y += self.speed
