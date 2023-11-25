import pygame

class MapElement:
    def __init__(self, pos, image_path):
        self.surface = pygame.display.get_surface()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

    def draw(self):
        self.surface.blit(self.image, self.rect)

class Ground(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/ground.png")

class Wall(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/wall03.png")

class Upstairs(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/upstairs.png")

class Downstairs(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/downstairs.png")

class Fire(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/fire01.png")

class River(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/river03.png")

class Door_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/door1.png")

class Door_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/door2.png")

class Door_03(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/door3.png")

class Door_04(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/door4.png")

class Key_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/key01.png")

class Key_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/key02.png")

class Key_03(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/key03.png")

class Key_04(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/key04.png")

class Potion_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/potion1.png")

class Potion_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/potion2.png")

class Potion_03(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/potion3.png")

class Potion_04(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/potion4.png")

class Rune_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/rune1.png")

class Rune_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/rune2.png")

class Rune_03(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/rune3.png")

class Rune_04(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/rune4.png")

class Shop1(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/shop1.png")

class Shop2(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/shop2.png")

class Shop3(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/map/shop3.png")

class Sword_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/sword01.png")

class Sword_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/sword02.png")

class Shield_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/shield01.png")

class Shield_02(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/shield02.png")

class Fly_01(MapElement):
    def __init__(self, pos):
        super().__init__(pos, "../graphics/items/fly01.png")