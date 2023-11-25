import pygame
from pygame.math import Vector2 as v
from elements import *
from setting import *
from player import *

class Room:

    def __init__(self):
        self.background = pygame.display.get_surface()
        self.background_image = pygame.image.load("../graphics/background/back.png")
        self.start_image = pygame.image.load("../graphics/background/start.png")
        self.end_image = pygame.image.load("../graphics/background/end.png")
        self.background_rect = self.background.get_rect()
        self.text_window = pygame.image.load("../graphics/background/textwindow.png")
        self.image_dialogue1 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue2 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue3 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue4 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue5 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue6 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue7 = pygame.image.load("../graphics/background/dialogue1.png")
        self.image_dialogue8 = pygame.image.load("../graphics/background/dialogue1.png")

        self.player = Player()
        self.obstacles = []
        self.npc = []
        self.monster = []

        self.floor = 0
        self.upstairs = []
        self.downstairs = []
        self.explore = False

        self.current_stage = "start" # change surfaces by current stage

        self.font1 = pygame.font.Font(None, 36)
        self.font2 = pygame.font.Font(None, 30)
        self.text_lv = "Lv: " + str(self.player.statue["lv"])
        self.text_Hp = "Hp: " + str(self.player.statue["hp"])
        self.text_Atk = "Atk: " + str(self.player.statue["atk"])
        self.text_Def = "Def: " + str(self.player.statue["def"])
        self.text_yKey = "Key: " + str(self.player.items["key1"])
        self.text_bKey = "Key: " + str(self.player.items["key2"])
        self.text_rKey = "Key: " + str(self.player.items["key3"])
        self.text_gKey = "Key: " + str(self.player.items["key4"])
        self.text_gold = "Gold: " + str(self.player.items["gold"])
        self.text_exp = "Exp: " + str(self.player.items["exp"])
        self.text_floor = "Floor:" + str(self.floor)
        self.text_sprite1 = "If you can find the legendary cross,"
        self.text_sprite2 = "I will boost your abilities by 20%. (press 1)"
        self.text_older1 = "press 1 to increase 1 lv (need 500exp)"
        self.text_older2 = "press 2 to increase 5 atk (need 200exp)"
        self.text_older3 = "press 3 to increase 5 def (need 200exp)"
        self.text_merchant1 = "press 1 to buy 5 yellow keys (need 200 glod)"
        self.text_merchant2 = "press 2 to buy 3 blue keys (need 300 glod)"
        self.text_merchant3 = "press 3 to buy 2 red keys (need 500 glod)"
        self.text_shop1 = "press 1 to increase 1000 hp (need 300 glod)"
        self.text_shop2 = "press 2 to increase 5 atk (need 300 glod)"
        self.text_shop3 = "press 3 to increase 5 def (need 300 glod)"
        self.text_thief1 = "Thank you for rescuing me. As a reward,"
        self.text_thief2 = "I'll split what I have with you. (press 1)"
        self.text_older4 = "press 1 to increase 3 lv (need 1200exp)"
        self.text_older5 = "press 2 to increase 20 atk (need 500exp)"
        self.text_older6 = "press 3 to increase 20 def (need 500exp)"
        self.text_shop4 = "press 1 to increase 3000 hp (need 1000 glod)"
        self.text_shop5 = "press 2 to increase 20 atk (need 1000 glod)"
        self.text_shop6 = "press 3 to increase 20 def (need 1000 glod)"
        self.text_fly1 = "choose the floor as below (press f)"
        self.text_fly2 = "1). floor04  2). floor 09  3). floor 14"

        self.sound_bgm01_path = "../music/bgm01.wav"
        self.sound_bgm02_path = "../music/bgm02.wav"
        self.sound_bgm03_path = "../music/bgm03.wav"
        self.sound_fight_path = "../music/fight.wav"
        self.sound_open_path = "../music/opendoor.wav"
        self.sound_get_path = "../music/get_item.wav"
        self.sound_defeat_path = "../music/cannot_attack.wav"
        self.sound_end_path = "../music/bgm_end.wav"
        self.sound_lvup_path = "../music/lv_up.wav"

    # update by keydown
    def update(self):
        self.player.move_player()
        self.check_floor()
        self.take_items()

    # update automatically
    def update_auto(self):
        self.text_lv = "Lv: " + str(self.player.statue["lv"])
        self.text_Hp = "Hp: " + str(self.player.statue["hp"])
        self.text_Atk = "Atk: " + str(self.player.statue["atk"])
        self.text_Def = "Def: " + str(self.player.statue["def"])
        self.text_yKey = "Key: " + str(self.player.items["key1"])
        self.text_bKey = "Key: " + str(self.player.items["key2"])
        self.text_rKey = "Key: " + str(self.player.items["key3"])
        self.text_gKey = "Key: " + str(self.player.items["key4"])
        self.text_gold = "Gold: " + str(self.player.items["gold"])
        self.text_exp = "Exp: " + str(self.player.items["exp"])
        if self.floor >= 10: self.text_floor = "Floor: " + str(self.floor)
        else: self.text_floor = "Floor: 0" + str(self.floor)

    def draw_current_map(self):
        if self.current_stage == "running":
            self.draw_background()
            self.draw_elements(self.floor)
            self.player.draw_player()
        if self.current_stage == "dialogue":
            self.dialogue()
        if self.current_stage == "start" or self.current_stage == "end":
            self.draw_background()


    def draw_background(self):
        if self.current_stage == "running" or self.current_stage == "dialogue":
            self.background.blit(self.background_image, self.background_rect)
            rect = self.text_window.get_rect(topleft=(50, 160))
            self.background_image.blit(self.text_window, rect)
            # need update continually
            self.draw_text(self.text_lv, (60, 160), (224, 255, 255))
            self.draw_text(self.text_Hp, (60, 200), (224, 255, 255))
            self.draw_text(self.text_Atk, (60, 240), (224, 255, 255))
            self.draw_text(self.text_Def, (60, 280), (224, 255, 255))
            self.draw_text(self.text_yKey, (60, 400), (238, 238, 0))
            self.draw_text(self.text_bKey, (160, 400), (132, 112, 255))
            self.draw_text(self.text_rKey, (60, 440), (255, 48, 48))
            self.draw_text(self.text_gKey, (160, 440), (64, 224, 208))
            self.draw_text(self.text_gold, (60, 320), (224, 255, 255))
            self.draw_text(self.text_exp, (60, 360), (224, 255, 255))
            self.draw_text(self.text_floor, (60, 500), (255, 255, 255))
        elif self.current_stage == "start":
            self.background.blit(self.start_image, self.background_rect)
        elif self.current_stage == "end":
            self.background.blit(self.end_image, self.background_rect)

    def draw_text(self, text, pos, color):
        text_image = self.font1.render(text, False, color)
        text_rect = text_image.get_rect(topleft=pos)
        self.background_image.blit(text_image, text_rect)

    def draw_dialogue(self, image, text, pos, color=(255, 255, 255)):
        dialogue_rect = image.get_rect(topleft=(350, 100))
        self.background.blit(image, dialogue_rect) # every time use new image
        text_image = self.font2.render(text, False, color)
        text_rect = text_image.get_rect(topleft=pos)
        image.blit(text_image, text_rect)

    def check_collision(self):
        next_pos = self.player.pos + self.player.direction
        if next_pos in self.obstacles:
            return True
        else:
            return False

    # free lists
    def clear_elements(self):
        self.obstacles.clear()
        self.downstairs.clear()
        self.upstairs.clear()

    def check_floor(self):
        if self.player.pos in self.upstairs:
            self.floor += 1
            self.clear_elements()
            # upstairs and downstairs are not in same position
            if self.floor == 18:
                self.player.pos = v(11, 11)
            if self.floor == 12:
                self.player.pos = v(11, 1)
        if self.player.pos in self.downstairs:
            self.floor -= 1
            self.clear_elements()
            if self.floor == 17:
                self.player.pos = v(11, 1)
            # fix the mistake in map
            if self.floor == 11:
                self.player.pos = v(11, 11)
        if self.floor == 14:
            self.explore = True

    def open_door(self):
        next_pos = self.player.pos + self.player.direction
        i = int(next_pos.x - 5)
        j = int(next_pos.y)

        if self.player.items["key1"] >= 1 and map_list[self.floor][j][i] == '1':
            self.player.items["key1"] -= 1
            map_list[self.floor][j][i] = 'o'
        if self.player.items["key2"] >= 1 and map_list[self.floor][j][i] == '2':
            self.player.items["key2"] -= 1
            map_list[self.floor][j][i] = 'o'
        if self.player.items["key3"] >= 1 and map_list[self.floor][j][i] == '3':
            self.player.items["key3"] -= 1
            map_list[self.floor][j][i] = 'o'
        if self.player.items["key4"] >= 1 and map_list[self.floor][j][i] == '4':
            self.player.items["key4"] -= 1
            map_list[self.floor][j][i] = 'o'
        self.clear_elements()

    def take_items(self):
        i = int(self.player.pos.x - 5)
        j = int(self.player.pos.y)

        if map_list[self.floor][j][i] == '9':
            self.player.items["key1"] += 1
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '8':
            self.player.items["key2"] += 1
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '7':
            self.player.items["key3"] += 1
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '6':
            self.player.items["key4"] += 1
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '!':
            self.player.statue["hp"] += 200
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '@':
            self.player.statue["hp"] += 500
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '#':
            self.player.statue["hp"] += 500
            self.player.statue["atk"] += 5
            self.player.statue["def"] += 5
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '$':
            self.player.items["exp"] += 300
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '%':
            self.player.statue["atk"] += 5
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '^':
            self.player.statue["def"] += 5
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '&':
            self.player.statue["atk"] += 10
            self.player.statue["def"] += 10
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == '*':
            self.player.items["gold"] += 400
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == 'a':
            self.player.statue["atk"] += 100
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == 'b':
            self.player.statue["def"] += 100
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == 'c':
            self.player.statue["atk"] += 300
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == 'e':
            self.player.statue["def"] += 300
            map_list[self.floor][j][i] = 'o'
        if map_list[self.floor][j][i] == 'h':
            self.player.statue["fly"] = True
            map_list[self.floor][j][i] = 'o'

    def dialogue(self):
        next_pos = self.player.pos + self.player.direction
        i = int(next_pos.x - 5)
        j = int(next_pos.y)
        if map_list[self.floor][j][i] in ['(', ')', '-', '=', '{', '}', '|']: # talk with npc
            if map_list[self.floor][j][i] == '(':
                self.draw_dialogue(self.image_dialogue1, self.text_sprite1, (20, 20))
                self.draw_dialogue(self.image_dialogue1, self.text_sprite2, (20, 60))
            elif map_list[self.floor][j][i] == ')':
                if self.floor == 5:
                    self.draw_dialogue(self.image_dialogue2, self.text_older1, (20, 20))
                    self.draw_dialogue(self.image_dialogue2, self.text_older2, (20, 60))
                    self.draw_dialogue(self.image_dialogue2, self.text_older3, (20, 100))
                else:
                    self.draw_dialogue(self.image_dialogue6, self.text_older4, (20, 20))
                    self.draw_dialogue(self.image_dialogue6, self.text_older5, (20, 60))
                    self.draw_dialogue(self.image_dialogue6, self.text_older6, (20, 100))
            elif map_list[self.floor][j][i] == '-':
                self.draw_dialogue(self.image_dialogue3, self.text_merchant1, (20, 20))
                self.draw_dialogue(self.image_dialogue3, self.text_merchant2, (20, 60))
                self.draw_dialogue(self.image_dialogue3, self.text_merchant3, (20, 100))
            elif map_list[self.floor][j][i] in ['{', '}', '|']:
                if self.floor == 3:
                    self.draw_dialogue(self.image_dialogue4, self.text_shop1, (20, 20))
                    self.draw_dialogue(self.image_dialogue4, self.text_shop2, (20, 60))
                    self.draw_dialogue(self.image_dialogue4, self.text_shop3, (20, 100))
                else:
                    self.draw_dialogue(self.image_dialogue7, self.text_shop4, (20, 20))
                    self.draw_dialogue(self.image_dialogue7, self.text_shop5, (20, 60))
                    self.draw_dialogue(self.image_dialogue7, self.text_shop6, (20, 100))
            elif map_list[self.floor][j][i] == '=':
                self.draw_dialogue(self.image_dialogue5, self.text_thief1, (20, 20))
                self.draw_dialogue(self.image_dialogue5, self.text_thief2, (20, 60))
            return True
        else:
            return False

    def buy(self, event):
        next_pos = self.player.pos + self.player.direction
        i = int(next_pos.x - 5)
        j = int(next_pos.y)
        if map_list[self.floor][j][i] == ')':
            if self.floor == 5:
                if event.key == pygame.K_1 and self.player.items["exp"] >= 500:
                    self.player.statue["lv"] += 1
                    self.player.items["exp"] -= 500
                    self.player.statue["hp"] += 1000
                    self.player.statue["atk"] += 5
                    self.player.statue["def"] += 5
                if event.key == pygame.K_2 and self.player.items["exp"] >= 200:
                    self.player.items["exp"] -= 200
                    self.player.statue["atk"] += 10
                if event.key == pygame.K_3 and self.player.items["exp"] >= 200:
                    self.player.items["exp"] -= 200
                    self.player.statue["def"] += 10
            else:
                if event.key == pygame.K_1 and self.player.items["exp"] >= 1200:
                    self.player.statue["lv"] += 3
                    self.player.items["exp"] -= 1200
                    self.player.statue["hp"] += 3000
                    self.player.statue["atk"] += 20
                    self.player.statue["def"] += 20
                if event.key == pygame.K_2 and self.player.items["exp"] >= 500:
                    self.player.items["exp"] -= 500
                    self.player.statue["atk"] += 25
                if event.key == pygame.K_3 and self.player.items["exp"] >= 500:
                    self.player.items["exp"] -= 500
                    self.player.statue["def"] += 25
        elif map_list[self.floor][j][i] == '-':
            if event.key == pygame.K_1 and self.player.items["gold"] >= 200:
                self.player.items["gold"] -= 200
                self.player.items["key1"] += 5
            if event.key == pygame.K_2 and self.player.items["gold"] >= 300:
                self.player.items["gold"] -= 200
                self.player.items["key2"] += 3
            if event.key == pygame.K_3 and self.player.items["gold"] >= 500:
                self.player.items["gold"] -= 500
                self.player.items["key2"] += 2
        elif map_list[self.floor][j][i] in ['{', '}', '|']:
            if self.floor == 3:
                if event.key == pygame.K_1 and self.player.items["gold"] >= 300:
                    self.player.items["gold"] -= 300
                    self.player.statue["hp"] += 1000
                if event.key == pygame.K_2 and self.player.items["gold"] >= 300:
                    self.player.items["gold"] -= 300
                    self.player.statue["atk"] += 5
                if event.key == pygame.K_3 and self.player.items["gold"] >= 300:
                    self.player.items["gold"] -= 300
                    self.player.statue["def"] += 5
            else:
                if event.key == pygame.K_1 and self.player.items["gold"] >= 1000:
                    self.player.items["gold"] -= 1000
                    self.player.statue["hp"] += 3000
                if event.key == pygame.K_2 and self.player.items["gold"] >= 1000:
                    self.player.items["gold"] -= 1000
                    self.player.statue["atk"] += 20
                if event.key == pygame.K_3 and self.player.items["gold"] >= 1000:
                    self.player.items["gold"] -= 1000
                    self.player.statue["def"] += 20
        elif map_list[self.floor][j][i] == '=':
            if event.key == pygame.K_1 and self.player.statue["saved"]:
                self.player.items["gold"] += 10000
                self.player.items["key1"] += 10
                self.player.items["key2"] += 5
                self.player.items["key3"] += 5
                self.player.items["key4"] += 1
                map_list[self.floor][j][i] = 'o'
                self.clear_elements()

    def fly(self, event):
        if event.key == pygame.K_f:
            self.current_stage = "flying" # distinguish with buying
            self.draw_dialogue(self.image_dialogue8, self.text_fly1, (20, 20))
            self.draw_dialogue(self.image_dialogue8, self.text_fly2, (20, 70))
        if event.key == pygame.K_1:
            self.floor = 4
            self.player.pos = v(8, 11)
            self.current_stage = "running"
        if event.key == pygame.K_2:
            self.floor = 9
            self.player.pos = v(6, 1)
            self.current_stage = "running"
        if event.key == pygame.K_3 and self.explore:
            self.floor = 14
            self.player.pos = v(11, 1)
            self.current_stage = "running"
        self.clear_elements()

    def draw_elements(self, n):
        cell_mapping = {
            'o': Ground,
            'w': Wall,
            'f': Fire,
            'q': River,
            'u': Upstairs,
            'd': Downstairs,
            '1': Door_01,
            '2': Door_02,
            '3': Door_03,
            '4': Door_04,
            '9': Key_01,
            '8': Key_02,
            '7': Key_03,
            '6': Key_04,
            '!': Potion_01,
            '@': Potion_02,
            '#': Potion_03,
            '$': Potion_04,
            '%': Rune_01,
            '^': Rune_02,
            '&': Rune_03,
            '*': Rune_04,
            '(': Sprite,
            ')': Elder,
            '-': Merchant,
            '=': Thief,
            '|': Shop1,
            '{': Shop2,
            '}': Shop3,
            'a': Sword_01,
            'b': Shield_01,
            'c': Sword_02,
            'e': Shield_02,
            'h': Fly_01,
            'A': MonsterA,
            'B': MonsterB,
            'C': MonsterC,
            'D': MonsterD,
            'E': MonsterE,
            'F': MonsterF,
            'G': MonsterG,
            'H': MonsterH,
            'I': MonsterI,
            'J': MonsterJ,
            'K': MonsterK,
            'L': MonsterL,
            'M': MonsterM,
            'N': MonsterN,
            'O': MonsterO,
            'P': MonsterP,
            'Q': MonsterQ,
            'R': MonsterR,
            'S': MonsterS,
            'T': MonsterT,
            'U': MonsterU,
            'V': MonsterV,
            'W': MonsterW,
            'X': MonsterX,
            'Y': MonsterY,
            'Z': MonsterZ,
        }

        for y, row in enumerate(map_list[n]):
            for x, cell in enumerate(row):
                pos = ((x + 5) * cell_size, y * cell_size)
                vt = v(x + 5, y)

                if cell in cell_mapping:
                    obj_class = cell_mapping[cell]
                    obj_item = obj_class(pos)
                    obj_item.draw()
                    if cell in ['w', 'f', 'q', '1', '2', '3', '4', '(', ')', '-', '=',
                                '|', '{', '}', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                                'U', 'V', 'W', 'X', 'Y', 'Z']:
                        self.obstacles.append(vt)
                        if cell in ['(', ')', '-', '=']:
                            self.npc.append(vt)
                        if cell in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                            self.monster.append(vt)
                    elif cell in ["u"]:
                        self.upstairs.append(vt)
                    elif cell in ['d']:
                        self.downstairs.append(vt)

    def check_battle(self):
        next_pos = self.player.pos + self.player.direction
        i = int(next_pos.x - 5)
        j = int(next_pos.y)
        if map_list[self.floor][j][i] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            self.start_battle()

    def start_battle(self):
        next_pos = self.player.pos + self.player.direction
        i = int(next_pos.x - 5)
        j = int(next_pos.y)
        pos = (next_pos.x * cell_size, next_pos.y * cell_size)

        if map_list[self.floor][j][i] == 'A':
            monster_a = MonsterA(pos)
            self.fighting(monster_a, j, i)
        elif map_list[self.floor][j][i] == 'B':
            monster_b = MonsterB(pos)
            self.fighting(monster_b, j, i)
        elif map_list[self.floor][j][i] == 'C':
            monster_c = MonsterC(pos)
            self.fighting(monster_c, j, i)
        elif map_list[self.floor][j][i] == 'D':
            monster_d = MonsterD(pos)
            self.fighting(monster_d, j, i)
        elif map_list[self.floor][j][i] == 'E':
            monster_e = MonsterE(pos)
            self.fighting(monster_e, j, i)
        elif map_list[self.floor][j][i] == 'F':
            monster_f = MonsterF(pos)
            self.fighting(monster_f, j, i)
        elif map_list[self.floor][j][i] == 'G':
            monster_g = MonsterG(pos)
            self.fighting(monster_g, j, i)
        elif map_list[self.floor][j][i] == 'H':
            monster_h = MonsterH(pos)
            self.fighting(monster_h, j, i)
        elif map_list[self.floor][j][i] == 'I':
            monster_i = MonsterI(pos)
            self.fighting(monster_i, j, i)
        elif map_list[self.floor][j][i] == 'J':
            monster_j = MonsterJ(pos)
            self.fighting(monster_j, j, i)
        elif map_list[self.floor][j][i] == 'K':
            monster_k = MonsterK(pos)
            self.fighting(monster_k, j, i)
        elif map_list[self.floor][j][i] == 'L':
            monster_l = MonsterL(pos)
            self.fighting(monster_l, j, i)
        elif map_list[self.floor][j][i] == 'M':
            monster_m = MonsterM(pos)
            self.fighting(monster_m, j, i)
        elif map_list[self.floor][j][i] == 'N':
            monster_n = MonsterN(pos)
            self.fighting(monster_n, j, i)
        elif map_list[self.floor][j][i] == 'O':
            monster_o = MonsterO(pos)
            self.fighting(monster_o, j, i)
        elif map_list[self.floor][j][i] == 'P':
            monster_p = MonsterP(pos)
            self.fighting(monster_p, j, i)
        elif map_list[self.floor][j][i] == 'Q':
            monster_q = MonsterQ(pos)
            self.fighting(monster_q, j, i)
        elif map_list[self.floor][j][i] == 'R':
            monster_r = MonsterR(pos)
            self.fighting(monster_r, j, i)
        elif map_list[self.floor][j][i] == 'S':
            monster_s = MonsterS(pos)
            self.fighting(monster_s, j, i)
        elif map_list[self.floor][j][i] == 'T':
            monster_t = MonsterS(pos)
            self.fighting(monster_t, j, i)
        elif map_list[self.floor][j][i] == 'U':
            monster_u = MonsterU(pos)
            self.fighting(monster_u, j, i)
        elif map_list[self.floor][j][i] == 'V':
            monster_v = MonsterV(pos)
            self.fighting(monster_v, j, i)
        elif map_list[self.floor][j][i] == 'W':
            monster_w = MonsterW(pos)
            self.fighting(monster_w, j, i)
        elif map_list[self.floor][j][i] == 'X':
            monster_x = MonsterX(pos)
            self.fighting(monster_x, j, i)
        elif map_list[self.floor][j][i] == 'Y':
            monster_y = MonsterY(pos)
            self.fighting(monster_y, j, i)
        elif map_list[self.floor][j][i] == 'Z':
            monster_z = MonsterZ(pos)
            self.fighting(monster_z, j, i)
            # check finish
            if map_list[self.floor][j][i] == 'o':
                self.current_stage = "end"

    def fighting(self, monster, j, i):
        player_hp = self.player.statue["hp"]
        monster_hp = monster.statue["hp"]
        start = False
        # no die setting
        while True:
            monster_hp -= (self.player.statue["atk"] - monster.statue["def"])
            player_hp -= (monster.statue["atk"] - self.player.statue["def"])
            if monster_hp <= 0:
                start = True
                break
            if player_hp <= 0:
                break

        # monster can be eliminated
        while start:
            monster.statue["hp"] -= max((self.player.statue["atk"] - monster.statue["def"]), 0)
            self.player.statue["hp"] -= max((monster.statue["atk"] - self.player.statue["def"]), 0) # avoid increase hp
            if monster.statue["hp"] <= 0:
                break
        if start:
            self.player.items["exp"] += monster.items["exp"]
            self.player.items["gold"] += monster.items["gold"]
            map_list[self.floor][j][i] = 'o'
            self.clear_elements()



