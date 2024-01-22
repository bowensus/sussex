"""
This class is the main class of the "Adventure World" application.
'Adventure World' is a very simple, text based adventure game. Users can walk
around some scenery. That's all. It should really be extended to make it more
interesting!

To play this game, create an instance of this class and call the "play" method.

This main class creates and initialises all the others: it creates all rooms,
creates the parser and starts the game. It also evaluates and executes the
commands that the parser returns.

This game is adapted from the 'World of Zuul' by Michael Kolling and 
David J. Barnes. The original was written in Java and has been simplified and
converted to Python by Kingsley Sage.
"""

from backpack import *
from room import Room
from text_ui import *
import random
import time
import unittest

class Game:

    def __init__(self):

        self.level = 1
        self.create_rooms()
        self.textUI = TextUI()
        self.area_clean = False # finish all in this map, and then go next
        self.player = Player()
        self.search_times = 0 # numbers of items and monsters in room
        self.death = False # death setting
        self.next = False # finish search on this area and can go next aera

    def create_rooms(self):

        self.outside = Room(outside)
        self.lobby = Room(lobby)
        self.corridor = Room(corridor)
        self.lab = Room(lab)
        self.office = Room(office)
        self.secret = Room(secret)
        self.current_room = self.outside  # initial room

        if self.level == 1:
            self.outside.set_exit("east", self.lobby)               #  map01:
            self.outside.set_exit("south", self.lab)                #    corridor--outside--lobby
            self.outside.set_exit("west", self.corridor)            #                 |
            self.lobby.set_exit("west", self.outside)               #                lab---office
            self.corridor.set_exit("east", self.outside)
            self.lab.set_exit("north", self.outside)
            self.lab.set_exit("east", self.office)
            self.office.set_exit("west", self.lab)
        if self.level == 2:
            self.office.set_exit("east", self.lobby)               #  map02:
            self.lobby.set_exit("south", self.outside)             #      office--lobby--lab
            self.lobby.set_exit("west", self.office)               #                |
            self.lobby.set_exit("east", self.lab)                  #              outside--corridor
            self.outside.set_exit("north", self.lobby)             #                |
            self.outside.set_exit("east", self.corridor)           #              secret
            self.lab.set_exit("west", self.lobby)
            self.corridor.set_exit("west", self.outside)
        if self.level == 3:
            self.office.set_exit("north", self.outside)             #  map03:
            self.corridor.set_exit("south", self.outside)           #       lab--corridor--lobby
            self.corridor.set_exit("west", self.lab)                #               |
            self.corridor.set_exit("east", self.lobby)              #            outside
            self.outside.set_exit("north", self.corridor)           #               |
            self.outside.set_exit("south", self.office)             #             office--secert
            self.lab.set_exit("east", self.corridor)
            self.lobby.set_exit("west", self.corridor)
        if self.level == 4:
            self.office.set_exit("west", self.corridor)             #  map04:
            self.corridor.set_exit("north", self.outside)           #      lobby--outside--lab
            self.corridor.set_exit("east", self.office)             #                |
            self.lobby.set_exit("east", self.outside)               #             corridor--office
            self.outside.set_exit("weat", self.lobby)
            self.outside.set_exit("east", self.lab)
            self.lab.set_exit("west", self.outside)
            self.outside.set_exit("south", self.corridor)
        if self.level == 5:
            self.office.set_exit("east", self.lobby)               #  map05:
            self.lobby.set_exit("south", self.lab)                 #      office--lobby--secret
            self.lobby.set_exit("west", self.office)               #                |
            self.lab.set_exit("north", self.lobby)                 #               lab
            self.outside.set_exit("north", self.lab)               #                |
            self.outside.set_exit("east", self.corridor)           #              outside--corridor
            self.lab.set_exit("south", self.outside)
            self.corridor.set_exit("west", self.outside)
        if self.level == 6:
            self.corridor.set_exit("east", self.outside)           #  map06:
            self.lobby.set_exit("north", self.secret)              #     secret
            self.lobby.set_exit("south", self.outside)             #       |
            self.secret.set_exit("south", self.lobby)              #     lobby
            self.outside.set_exit("west", self.corridor)           #       |
            self.outside.set_exit("east", self.lab)                #    corridor--outside--lab
            self.lab.set_exit("west", self.outside)
            self.corridor.set_exit("north", self.lobby)
        if self.level == 7:
            self.office.set_exit("north", self.outside)            #  map07:
            self.lobby.set_exit("south", self.lab)                 #     lobby--secert
            self.corridor.set_exit("west", self.outside)           #       |
            self.lab.set_exit("north", self.lobby)                 #      lab--outside--corridor
            self.outside.set_exit("west", self.lab)                #              |
            self.outside.set_exit("east", self.corridor)           #            office
            self.lab.set_exit("east", self.outside)
            self.outside.set_exit("south", self.office)
        if self.level == 8:
            self.office.set_exit("east", self.lobby)               #  map08:
            self.lobby.set_exit("west", self.office)               #       office--lobby
            self.lobby.set_exit("south", self.outside)             #                 |
            self.corridor.set_exit("east", self.outside)           #     corridor--outside
            self.outside.set_exit("north", self.lobby)             #                 |
            self.outside.set_exit("south", self.lab)               #                lab
            self.lab.set_exit("north", self.outside)
            self.outside.set_exit("west", self.corridor)
        if self.level == 9:
            self.corridor.set_exit("west", self.lobby)             #  map09:
            self.lab.set_exit("east", self.outside)                #       lab--outside
            self.lobby.set_exit("north", self.outside)             #               |
            self.lobby.set_exit("east", self.corridor)             #     secret--lobby--corridor
            self.outside.set_exit("west", self.lab)
            self.outside.set_exit("south", self.lobby)
        if self.level == 10:
            self.lab.set_exit("west", self.corridor)               #  map010:
            self.lab.set_exit("south", self.outside)               #     corridor--lab
            self.corridor.set_exit("east", self.lab)               #                |
            self.outside.set_exit("north", self.lab)               #              outside

    def play(self):

        finish = False
        self.print_welcome()
        while not finish:
            try:
                command = self.textUI.get_command()  # Returns a 2-tuple
                finish = self.process_command(command)
            except Exception as e:
                print("Game Error")
                break
        print("Thank you for playing!")

    def print_welcome(self):

        self.textUI.print_to_textUI("You are lost. You are alone. You wander")
        self.textUI.print_to_textUI("around the deserted complex.")
        self.textUI.print_to_textUI("")
        self.textUI.print_to_textUI(f'Your command words are: {self.show_command_words()}')

    def show_command_words(self):
        return ['help', 'go', 'quit', 'search', 'fight', 'escape', 'destory', 'check', 'open', 'pick', 'leave', 'use', 'buy']

    def process_command(self, command):

        command_word, second_word = command
        if command_word != None:
            command_word = command_word.upper()

        want_to_quit = False # end setting
        # the input() are available in any situations
        # some are only alailable in search
        if command_word == "HELP":
            self.print_help()
        elif command_word == "GO":
            self.do_go_command(second_word)
        elif command_word == "SEARCH":
            self.do_search_command()
        elif command_word == "CHECK":
            self.do_check_command(second_word)
        elif command_word == "BUY":
            self.do_buy_command()
        elif command_word == "QUIT":
            want_to_quit = True
        else:
            # Unknown command...
            self.textUI.print_to_textUI("Don't know what you mean.")

        # condition of ending this game
        if self.death:
            want_to_quit = True
        if self.level == 10 and self.current_room.description == corridor and self.next:
            want_to_quit = True
            self.textUI.print_to_textUI("Congratulation! You have finished the game!")
        return want_to_quit

    def print_help(self):

        self.textUI.print_to_textUI(help_text)

    def do_go_command(self, second_word):

        if second_word == None:
            # Missing second word...
            self.textUI.print_to_textUI("Go where?")
            self.textUI.print_to_textUI(self.current_room.get_long_description())
        elif second_word == "next" and self.next and self.current_room.description == corridor:
            self.textUI.print_to_textUI("You have moved into next area.")
            # update new map, and initial next
            self.level += 1
            self.create_rooms()
            self.next = False
        elif second_word == "next" and not self.next:
            self.textUI.print_to_textUI("You haven't searched all rooms in current area.")
        elif second_word == "next" and self.current_room.description != corridor:
            self.textUI.print_to_textUI("You have to go to a corridor to move into next area.")
        else:
            next_room = self.current_room.get_exit(second_word)
            if next_room == None:
                self.textUI.print_to_textUI("There is no door!")
            else:
                self.current_room = next_room
                self.textUI.print_to_textUI(self.current_room.get_long_description())
                if self.current_room.description == secret:
                    self.textUI.print_to_textUI("Congratulation! You find a secret room!")
                if self.current_room.description == outside or self.current_room.description == corridor: # cuto finish search
                    self.current_room.clean = True

        self.check_next_area() # check next and secret when press go

    def do_search_command(self):

        if self.current_room.description in [outside, corridor]:
            self.current_room.clean = True
        if self.current_room.description in [lab, lobby]:
            self.search_times = 3
        if self.current_room.description == office:
            self.search_times = 4
        if self.current_room.description == secret:
            self.search_times = 5

        if self.current_room.clean:
            self.textUI.print_to_textUI("There is nothing here.")
            return

        if self.player.blessed: # strengthen you before entering into room
            self.player.statue["luck"] += 3
        if self.player.buff:
            self.player.statue["crit"] += 3

        while not self.current_room.clean and not self.death:
            ret = random.randint(1, 10) # a random number to simulate what you will meet while searching
            # set different difficulties for different rooms
            if self.current_room.description == office:
                if ret >= 4:
                    self.textUI.print_to_textUI("You meet a monster, fight or escape?") # meet monster
                    self.check_battle()
                elif ret == 1:
                    self.textUI.print_to_textUI("You find a treasure chest, open or leave?") # find treasure
                    self.check_open()
                else:
                    self.textUI.print_to_textUI("You find a gold.") # find gold, auto pick and doesn't account into capacity
                    self.player.gold += 1
                    self.search_times -= 1

            if self.current_room.description == lab or self.current_room.description == lobby:
                if ret >= 2:
                    self.textUI.print_to_textUI("You meet a monster, fight or escape?")
                    self.check_battle()
                else:
                    self.textUI.print_to_textUI("You find a gold.")
                    self.player.gold += 1
                    self.search_times -= 1

            if self.current_room.description == secret:
                if ret >= 7:
                    self.textUI.print_to_textUI("You find a treasure chest, open or leave?")
                    self.check_open()
                elif ret == 1:
                    self.textUI.print_to_textUI("You find a blessing potion, pick or leave?")
                    self.check_pick("a blessing potion")
                elif ret == 2:
                    self.textUI.print_to_textUI("You find a holy water elixir, pick or leave?")
                    self.check_pick("a holy water")
                elif ret == 3:
                    self.textUI.print_to_textUI("You find an invisibility cloak, pick or leave?")
                    self.check_pick("an invisibility cloak")
                elif ret == 4:
                    self.textUI.print_to_textUI("You find a dark magic, pick or leave?")
                    self.check_pick("a dark magic")
                else:
                    self.textUI.print_to_textUI("You find a key, pick or leave?")
                    self.check_pick("a key")

            if self.player.blessed: # buff time end
                self.player.statue["luck"] -= 3
                self.player.blessed = False
            if self.player.buff:
                self.player.statue["crit"] -= 3
                self.player.buff = False

            if self.search_times == 0 and not self.death:
                self.textUI.print_to_textUI("There is nothing here.")
                self.current_room.clean = True  # finish search and update the room statue
                break

    def do_check_command(self, second_word):

        if second_word == None:
            self.textUI.print_to_textUI("What do you want to check, info, bag, monster or command? For example: check info")
        elif second_word == "info":
            self.textUI.print_to_textUI("hp: {:d} atk: {:d} def: {:d}".
                                        format(self.player.statue["hp"], self.player.statue["atk"], self.player.statue["def"]))
        elif second_word == "bag":
            self.textUI.print_to_textUI("These are items in your backpack:")
            for i, item in enumerate(self.player.bag.contents):
                print("[{:d}] {:s}".format(i + 1, item))
            self.textUI.print_to_textUI("Would you want to use someone?")
            self.do_use_command()
        elif second_word == "monster":
            monster = Monster()
            monster.statue["hp"] = monster.statue["hp"] * 10 + self.level * 5
            monster.statue["atk"] = monster.statue["atk"] * 10 + self.level * 3
            monster.statue["def"] = monster.statue["def"] * 6 + self.level * 2
            self.textUI.print_to_textUI("The attribute of monsters in current area:")
            self.textUI.print_to_textUI("hp: {:d} atk: {:d} def: {:d}".
                                        format(monster.statue["hp"], monster.statue["atk"], monster.statue["def"]))
        elif second_word == "command":
            self.textUI.print_to_textUI(self.show_command_words())
        else:
            self.textUI.print_to_textUI("Don't know what you mean.")

    def do_fight_command(self):

        monster = Monster()  # evert time need to set a new class
        self.textUI.print_to_textUI("Battle Start:")
        # set difficuties for different levels
        monster.statue["hp"] = monster.statue["hp"] * 10 + self.level * 10
        monster.statue["atk"] = monster.statue["atk"] * 10 + self.level * 3
        monster.statue["def"] = monster.statue["def"] * 6 + self.level * 2

        atk = max(0, self.player.statue["atk"] - monster.statue["def"])
        hit = max(0, monster.statue["atk"] - self.player.statue["def"])

        if self.player.magic:
            self.textUI.print_to_textUI("You use magic to eliminate an enemy.")
            self.search_times -= 1
            self.player.magic = False
            return

        while True:
            crit_success = random.randint(1, 50) # crit setiing
            if crit_success <= self.player.statue["crit"]:
                monster.statue["hp"] -= atk * 2
                self.textUI.print_to_textUI("> You dealt {:d} points of critical hit damage to the monster.". format(atk * 2))
                time.sleep(0.5)
            else:
                monster.statue["hp"] -= atk
                self.textUI.print_to_textUI("> You dealt {:d} point of damage to the monster.". format(atk))
                time.sleep(0.5) # show by fps
            self.player.statue["hp"] -= hit
            self.textUI.print_to_textUI("> You were bitten and took {:d} point of damage.". format(hit))
            time.sleep(0.5)

            if monster.statue["hp"] <= 0:
                self.textUI.print_to_textUI("You defeated the monster, continue searching.")
                break
            elif self.player.statue["hp"] <= 0:
                self.textUI.print_to_textUI("Sorry, you lost the game.")
                self.death = True
                break

        self.search_times -= 1

    def do_escape_command(self):

        if self.player.escape:
            self.textUI.print_to_textUI("You ues an invisibility cloak to escape successfully, continue searching.")
            self.search_times -= 1
            self.player.escape = False
            return

        escape_rate = random.randint(1, 10)
        if escape_rate <= self.player.statue["luck"]:
            self.textUI.print_to_textUI("Escape successfully, continue searching.")
            self.search_times -= 1
        else:
            self.textUI.print_to_textUI("You've been discovered and forced into battle!")
            heavy_hit = self.level * 5 # punishment of failure
            self.player.statue["hp"] -= heavy_hit
            self.textUI.print_to_textUI("You take {:d} points of heavy hit damage.". format(heavy_hit))
            self.secret_times = self.do_fight_command()

    def do_pick_command(self, item):

        while True:
            if self.player.bag.add_item(item): # add item into your bag
                self.textUI.print_to_textUI("You've picked " + item + '.')
                self.search_times -= 1
                break
            else:
                self.textUI.print_to_textUI("Your backpack is full. You must discard an item.")
                self.check_destory()

    def do_leave_command(self):
        self.search_times -= 1

    def do_destory_command(self):

        destoryed = True
        self.textUI.print_to_textUI("These are items in your backpack:")
        for i, item in enumerate(self.player.bag.contents):
            print("[{:d}] {:s}". format(i+1, item))
        self.textUI.print_to_textUI("Which one do you want to destory? For example: destory 1")

        command_01, command_02 = self.textUI.get_command()
        # the input() is always a string
        i = int(command_02)-1
        if i in list(range(len(self.player.bag.contents))) and command_01 == "destory":
            self.textUI.print_to_textUI("You discarded " + self.player.bag.contents[i])
            del self.player.bag.contents[i]
        else:
            self.textUI.print_to_textUI("Don't know what you mean.")
            destoryed = False # did not destory, continue check destory loop
        return destoryed

    def do_open_command(self):

        ret = random.randint(1, 4)
        # random get an item, used by a key
        self.player.bag.contents.remove("a key")
        if ret == 1:
            self.player.bag.add_item("a blessing potion")
            self.textUI.print_to_textUI("You open a treasure and find a blessing potion.")
        elif ret == 2:
            self.player.bag.add_item("a holy water")
            self.textUI.print_to_textUI("You open a treasure and find a holy water.")
        elif ret == 3:
            self.player.bag.add_item("an invisibility cloak")
            self.textUI.print_to_textUI("You open a treasure and find an invisibility cloak.")
        elif ret == 4:
            self.player.bag.add_item("a dark magic")
            self.textUI.print_to_textUI("You open a treasure and find a dark magic.")

    def check_battle(self):
        # if command is invalid, continuely input until it is right
        command = self.textUI.get_command()[0]
        while True:
            if command == "fight":
                self.do_fight_command()
                break
            elif command == "escape":
                self.do_escape_command()
                break
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")
                command = self.textUI.get_command()[0]

    def check_pick(self, item):
        # if command is invalid, continuely input until it is right
        command = self.textUI.get_command()[0]
        while True:
            if command == "pick":
                self.do_pick_command(item)
                break
            elif command == "leave":
                self.do_leave_command()
                break
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")
                command = self.textUI.get_command()[0]

    def check_destory(self):
        # if command is invalid, continuely input until it is right
        command = self.textUI.get_command()[0]
        while True:
            if command == "destory":
                if self.do_destory_command():
                    break # destory successfully, end
                else:
                    continue # invalid input, continue
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")
                command = self.textUI.get_command()[0]

    def check_open(self):

        command = self.textUI.get_command()[0]
        while True:
            if command == "open" and "a key" in self.player.bag.contents:
                self.do_open_command()
                break
            elif command == "open" and "a key" not in self.player.bag.contents:
                self.textUI.print_to_textUI("You don't have a key to open it. Leave to continue search.")
                self.do_leave_command()
                break
            elif command == "leave":
                self.do_leave_command()
                break
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")
                command = self.textUI.get_command()[0]

    def do_use_command(self):

        command_01, command_02 = self.textUI.get_command()
        i = int(command_02) - 1
        if i in list(range(len(self.player.bag.contents))) and command_01 == "use":
            self.textUI.print_to_textUI("You used " + self.player.bag.contents[i])
            if self.player.bag.contents[i] == "a blessing potion": # effective for one room
                self.player.statue["hp"] += 10
                self.textUI.print_to_textUI("You restored some of your health and temporarily increased your luck.")
                self.player.bag.contents.remove("a blessing potion")
                self.player.blessed = True
            elif self.player.bag.contents[i] == "a holy water":
                self.player.statue["atk"] += 2
                self.player.statue["def"] += 1
                self.textUI.print_to_textUI("You increased some attributes and temporarily boosted your critical hit rate.")
                self.player.bag.contents.remove("a holy water")
                self.player.buff = True
            elif self.player.bag.contents[i] == "an invisibility cloak": # only effective for next enemy
                self.player.escape = True
                self.textUI.print_to_textUI("You can use it to evade the next enemy.")
                self.player.bag.contents.remove("an invisibility cloak")
            elif self.player.bag.contents[i] == "a dark magic":
                self.player.magic = True
                self.textUI.print_to_textUI("You can use it to directly eliminate the next enemy.")
                self.player.bag.contents.remove("a dark magic")
            elif self.player.bag.contents[i] == "a key":
                self.textUI.print_to_textUI("You can't use it here. Bag closed.")
        else:
            self.textUI.print_to_textUI("It seems that you don't want to use anything. Bag closed.")

    def do_buy_command(self):

        if self.current_room.description == corridor and self.level in [1, 3, 5, 6, 8, 10]:
            if len(self.player.bag.contents) == self.player.bag.capacity:  # if bag is full, cannot buy and return
                self.textUI.print_to_textUI("Your backpack is full. Choose an item and use it, then come back.")
                return

            self.textUI.print_to_textUI(shop_list)
            self.textUI.print_to_textUI("What would you want to buy? For example: buy 1")
            command_01, command_02 = self.textUI.get_command()
            if command_01 == "buy" and command_02 == '1' and self.player.gold >= 10:
                self.textUI.print_to_textUI("You spend 10 golds to buy a blessing potion.")
                self.player.bag.add_item("a blessing potion")
                self.player.gold -= 10
            elif command_01 == "buy" and command_02 == '2' and self.player.gold >= 10:
                self.textUI.print_to_textUI("You spend 10 golds to buy a holy water.")
                self.player.bag.add_item("a holy water")
                self.player.gold -= 10
            elif command_01 == "buy" and command_02 == '3' and self.player.gold >= 5:
                self.textUI.print_to_textUI("You spend 5 golds to buy an invisibility cloak.")
                self.player.bag.add_item("an invisibility cloak")
                self.player.gold -= 5
            elif command_01 == "buy" and command_02 == '4' and self.player.gold >= 5:
                self.textUI.print_to_textUI("You spend 5 golds to buy a dark magic.")
                self.player.bag.add_item("a dark magic")
                self.player.gold -= 5
            elif command_01 == "buy" and command_02 == '5' and self.player.gold >= 3:
                self.textUI.print_to_textUI("You spend 3 golds to buy a key.")
                self.player.bag.add_item("a key")
                self.player.gold -= 3
            elif command_01 == "buy" and command_02 in ['1', '2'] and self.player.gold < 10:
                self.textUI.print_to_textUI("You don't have enough money.")
            elif command_01 == "buy" and command_02 in ['3', '4'] and self.player.gold < 5:
                self.textUI.print_to_textUI("You don't have enough money.")
            elif command_01 == "buy" and command_02 =='5' and self.player.gold < 5:
                self.textUI.print_to_textUI("You don't have enough money.")
            else:
                self.textUI.print_to_textUI("Don't know what you mean.")
        else:
            self.textUI.print_to_textUI("There is no shop here.")

    def check_next_area(self):

        self.next = False
        rooms_searched = [self.outside, self.lobby, self.corridor, self.lab, self.office]
        for room in rooms_searched:
            if not room.clean:
                return
            else:
                continue

        self.next = True # create secret room
        if self.next:
            self.create_secret_room()

    def create_secret_room(self):

        # the location of secreat room in some certain levels
        if self.level == 2:
            self.secret.set_exit("north", self.outside)
            self.outside.set_exit("south", self.secret)
        elif self.level == 3:
            self.secret.set_exit("west", self.office)
            self.office.set_exit("east", self.secret)
        elif self.level == 5:
            self.secret.set_exit("west", self.lobby)
            self.lobby.set_exit("east", self.secret)
        elif self.level == 6:
            self.secret.set_exit("south", self.lobby)
            self.lobby.set_exit("north", self.secret)
        elif self.level == 7:
            self.secret.set_exit("west", self.lobby)
            self.lobby.set_exit("east", self.secret)
        elif self.level == 9:
            self.secret.set_exit("east", self.lobby)
            self.lobby.set_exit("west", self.secret)


# class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        del self.game

    def test_connect_rooms(self):
        # test whether two rooms are connected
        self.game.outside.set_exit("east", self.game.lobby)
        self.game.lobby.set_exit("west", self.game.outside)
        self.game.current_room = self.game.outside
        self.assertEqual(self.game.current_room.get_exit("east"), self.game.lobby)

    def test_go_command(self):
        # test go function to move to next room
        self.game.current_room = self.game.outside
        self.game.do_go_command("east")
        self.assertEqual(self.game.current_room, self.game.lobby)

    def test_end_game(self):
        self.game.death = True
        command = ("go", "west")
        self.assertTrue(self.game.process_command(command))


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
