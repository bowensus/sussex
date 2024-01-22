"""
A simple text based User Interface (UI) for the Adventure World game.
"""

outside = "You are outside"
lobby = "in the lobby"
corridor = "in a corridor"
lab = "in a computing lab"
office = "in the computing admin office"
secret = "in a secret room"

shop_list = """
These is the shop list:
[1]. a blessing potion (10 golds)
[2]. a holy water (10 golds)
[3]. an invisibility cloak (5 golds)
[4]. a dark magic (5 golds)
[5]. a key (3 golds)
"""

help_text = """
The types of room:
Outside: There is nothing here.
Corridor: Sometimes you probably will find a shop.
Office: You will meet monsters, but you can also find golds. If you are lucky, you will find a treasure chest.
Lab and Lobby: You will meet more monsters, and you can only find golds with a little chance. 
Secret: Once you have searched all rooms, perhaps you will find it. Lots of treasure are there.

The monsters:
They will become more dangerous once you enter into next area.

The command of search:
You can enter into room to search it or You can choose to leave to go to next room.

The critical hit:
You have a chance to trigger a critical hit, gaining double damage.

The items:
a blessing potion: You will increase 3 point of luck and 10 point of health.
a holy water: You will increase 2 point of atk and 1 point of def and 3 point of critical hit rate.
an invisibility cloak: You can escape successfully when you meet next enemy.
a dark magic: You can eliminate next enemy directly.
"""

class TextUI:

    def __init__(self):
        # Nothing to do...
        pass

    def get_command(self):

        word1 = None
        word2 = None
        print('> ', end='')
        input_line = input()
        if input_line != "":
            all_words = input_line.split()
            word1 = all_words[0]
            if len(all_words) > 1:
                word2 = all_words[1]
            else:
                word2 = None
            # Just ignore any other words
        return (word1, word2)

    def print_to_textUI(self, text):
        print(text)
