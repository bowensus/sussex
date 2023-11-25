import pygame
from pygame.math import Vector2 as v
from setting import *


class Player:

    def __init__(self):
        self.x = 11
        self.y = 11
        self.pos = v(self.x, self.y)
        self.direction = v(-1, 0)

        self.surface = pygame.display.get_surface()
        self.image_left01 = pygame.image.load("../graphics/player/braver02.png")
        self.image_left02 = pygame.image.load("../graphics/player/braver12.png")
        self.image_up01 = pygame.image.load("../graphics/player/braver04.png")
        self.image_up02 = pygame.image.load("../graphics/player/braver14.png")
        self.image_down01 = pygame.image.load("../graphics/player/braver01.png")
        self.image_down02 = pygame.image.load("../graphics/player/braver11.png")
        self.image_right01 = pygame.image.load("../graphics/player/braver03.png")
        self.image_right02 = pygame.image.load("../graphics/player/braver13.png")

        # show different direction
        self.left = [self.image_left01, self.image_left02]
        self.up = [self.image_up01, self.image_up02]
        self.down = [self.image_down01, self.image_down02]
        self.right = [self.image_right01, self.image_right02]

        # set another player fps
        self.frame_switch_interval = 500
        self.last_frame_time = 0
        self.current_frame = 0

        self.statue = {"hp":3000, "atk":30, "def":30, "lv":0, "fly":False, "saved":True}
        self.items = {"gold":0, "exp":0, "key1":3, "key2":3, "key3":3, "key4":0}

    def draw_player(self):
        player_rect = pygame.Rect(cell_size * self.pos.x, cell_size * self.pos.y, cell_size, cell_size)
        current_time = pygame.time.get_ticks()

        if current_time - self.last_frame_time >= self.frame_switch_interval:
            self.current_frame = (self.current_frame + 1) % len(self.left)
            self.last_frame_time = current_time

        if self.direction == v(-1, 0):
            self.surface.blit(self.left[self.current_frame], player_rect)
        if self.direction == v(1, 0):
            self.surface.blit(self.right[self.current_frame], player_rect)
        if self.direction == v(0, -1):
            self.surface.blit(self.up[self.current_frame], player_rect)
        if self.direction == v(0, 1):
            self.surface.blit(self.down[self.current_frame], player_rect)

    def move_player(self):
        self.pos += self.direction


class NonPlayer:

    def __init__(self, pos, image_path):
        self.surface = pygame.display.get_surface()
        self.image = image_path
        self.pos = pos
        self.index = 0

    def draw(self):
        nonplayer_rect = pygame.Rect(self.pos[0], self.pos[1], cell_size, cell_size)
        current_time = pygame.time.get_ticks()
        while current_time > 500:
            current_time -= 500
            self.index += 1
        self.index = self.index % 2
        self.surface.blit(self.image[self.index], nonplayer_rect)


class Sprite(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/npc/npc01.png")
        self.image2 = pygame.image.load("../graphics/npc/npc02.png")
        self.image = [self.image1, self.image2]
        super().__init__(pos, self.image)


class Elder(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/npc/elder01.png")
        self.image2 = pygame.image.load("../graphics/npc/elder02.png")
        self.image = [self.image1, self.image2]
        super().__init__(pos, self.image)


class Merchant(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/npc/merchant01.png")
        self.image2 = pygame.image.load("../graphics/npc/merchant02.png")
        self.image = [self.image1, self.image2]
        super().__init__(pos, self.image)


class Thief(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/npc/thief01.png")
        self.image2 = pygame.image.load("../graphics/npc/thief02.png")
        self.image = [self.image1, self.image2]
        super().__init__(pos, self.image)


class MonsterA(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/A01.png")
        self.image2 = pygame.image.load("../graphics/monster/A02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":200, "atk":50, "def":20}
        self.items = {"gold":100, "exp":50}
        super().__init__(pos, self.image)


class MonsterB(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/B01.png")
        self.image2 = pygame.image.load("../graphics/monster/B02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":300, "atk":60, "def":20}
        self.items = {"gold":120, "exp":70}
        super().__init__(pos, self.image)


class MonsterC(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/C01.png")
        self.image2 = pygame.image.load("../graphics/monster/C02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":600, "atk":100, "def":80}
        self.items = {"gold":150, "exp":100}
        super().__init__(pos, self.image)


class MonsterD(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/D01.png")
        self.image2 = pygame.image.load("../graphics/monster/D02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":1000, "atk":120, "def":120}
        self.items = {"gold":160, "exp":120}
        super().__init__(pos, self.image)


class MonsterE(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/E01.png")
        self.image2 = pygame.image.load("../graphics/monster/E02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":1500, "atk":150, "def":150}
        self.items = {"gold":200, "exp":150}
        super().__init__(pos, self.image)


class MonsterF(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/F01.png")
        self.image2 = pygame.image.load("../graphics/monster/F02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":1200, "atk":160, "def":120}
        self.items = {"gold":200, "exp":150}
        super().__init__(pos, self.image)


class MonsterG(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/G01.png")
        self.image2 = pygame.image.load("../graphics/monster/G02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":2000, "atk":150, "def":150}
        self.items = {"gold":200, "exp":150}
        super().__init__(pos, self.image)


class MonsterH(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/H01.png")
        self.image2 = pygame.image.load("../graphics/monster/H02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":1800, "atk":160, "def":160}
        self.items = {"gold":220, "exp":160}
        super().__init__(pos, self.image)


class MonsterI(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/I01.png")
        self.image2 = pygame.image.load("../graphics/monster/I02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":2500, "atk":200, "def":160}
        self.items = {"gold":250, "exp":180}
        super().__init__(pos, self.image)


class MonsterJ(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/J01.png")
        self.image2 = pygame.image.load("../graphics/monster/J02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":3000, "atk":250, "def":250}
        self.items = {"gold":300, "exp":220}
        super().__init__(pos, self.image)


class MonsterK(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/K01.png")
        self.image2 = pygame.image.load("../graphics/monster/K02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":2500, "atk":220, "def":220}
        self.items = {"gold":280, "exp":200}
        super().__init__(pos, self.image)


class MonsterL(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/L01.png")
        self.image2 = pygame.image.load("../graphics/monster/L02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":2600, "atk":230, "def":200}
        self.items = {"gold":280, "exp":200}
        super().__init__(pos, self.image)


class MonsterM(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/M01.png")
        self.image2 = pygame.image.load("../graphics/monster/M02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":3000, "atk":250, "def":220}
        self.items = {"gold":300, "exp":220}
        super().__init__(pos, self.image)


class MonsterN(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/N01.png")
        self.image2 = pygame.image.load("../graphics/monster/N02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":5000, "atk":400, "def":400}
        self.items = {"gold":400, "exp":250}
        super().__init__(pos, self.image)


class MonsterO(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/O01.png")
        self.image2 = pygame.image.load("../graphics/monster/O02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":12000, "atk":800, "def":600}
        self.items = {"gold":650, "exp":580}
        super().__init__(pos, self.image)


class MonsterP(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/P01.png")
        self.image2 = pygame.image.load("../graphics/monster/P02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":8000, "atk":500, "def":500}
        self.items = {"gold":500, "exp":350}
        super().__init__(pos, self.image)


class MonsterQ(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/Q01.png")
        self.image2 = pygame.image.load("../graphics/monster/Q02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":7000, "atk":550, "def":450}
        self.items = {"gold":500, "exp":350}
        super().__init__(pos, self.image)


class MonsterR(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/R01.png")
        self.image2 = pygame.image.load("../graphics/monster/R02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":10000, "atk":600, "def":600}
        self.items = {"gold":600, "exp":400}
        super().__init__(pos, self.image)


class MonsterS(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/S01.png")
        self.image2 = pygame.image.load("../graphics/monster/S02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":12000, "atk":1000, "def":1000}
        self.items = {"gold":800, "exp":600}
        super().__init__(pos, self.image)


class MonsterT(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/T01.png")
        self.image2 = pygame.image.load("../graphics/monster/T02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":20000, "atk":1600, "def":1600}
        self.items = {"gold":800, "exp":600}
        super().__init__(pos, self.image)


class MonsterU(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/U01.png")
        self.image2 = pygame.image.load("../graphics/monster/U02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":15000, "atk":1200, "def":1200}
        self.items = {"gold":800, "exp":600}
        super().__init__(pos, self.image)


class MonsterV(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/V01.png")
        self.image2 = pygame.image.load("../graphics/monster/V02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":16000, "atk":1300, "def":1300}
        self.items = {"gold":900, "exp":700}
        super().__init__(pos, self.image)


class MonsterW(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/W01.png")
        self.image2 = pygame.image.load("../graphics/monster/W02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":18000, "atk":1400, "def":1400}
        self.items = {"gold":900, "exp":800}
        super().__init__(pos, self.image)


class MonsterX(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/X01.png")
        self.image2 = pygame.image.load("../graphics/monster/X02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":18000, "atk":1400, "def":1400}
        self.items = {"gold":900, "exp":800}
        super().__init__(pos, self.image)


class MonsterY(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/Y01.png")
        self.image2 = pygame.image.load("../graphics/monster/Y02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":20000, "atk":1500, "def":1500}
        self.items = {"gold":900, "exp":800}
        super().__init__(pos, self.image)


class MonsterZ(NonPlayer):

    def __init__(self, pos):
        self.image1 = pygame.image.load("../graphics/monster/Z01.png")
        self.image2 = pygame.image.load("../graphics/monster/Z02.png")
        self.image = [self.image1, self.image2]
        self.statue = {"hp":30000, "atk":2000, "def":2000}
        self.items = {"gold":1000, "exp":1000}
        super().__init__(pos, self.image)