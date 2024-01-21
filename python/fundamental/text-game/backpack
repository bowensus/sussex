class Backpack:
    """
    A class to allow us to pickup and put down items...
    Backpack is limited to number of items set by capacity.
    This example incorporates a user defined exception.
    """

    def __init__(self, capacity):
        self.contents = []
        self.capacity = capacity

    def add_item(self, item):
        """Adds an item to our backpack."""
        if len(self.contents) < self.capacity:
            self.contents.append(item)
            return True
        return False

    def remove_item(self, item):
        """Removes an item from our backpack."""
        try:
            if item not in self.contents:
                raise NotInBackpackError(item, 'is not in the backpack.')
            self.contents.remove(item)
        except NotInBackpackError:
            print('Exception handled here...')
        finally:
            print('Carrying on...')

    def check_item(self, item):
        """Returns True if item is in backpack, False otherwise."""
        return item in self.contents


class NotInBackpackError(Exception):
    def __init__(self, item, message):
        print(f'{item} {message}')


class Player:

    def __init__(self):
        self.bag = Backpack(5)
        self.statue = {"hp":200, "atk":15, "def":10, "crit":2, "luck":2}
        self.gold = 0
        self.blessed = False
        self.buff = False
        self.magic = False # elimite next enemy
        self.escape = False # escape 100%

class Monster:

    def __init__(self):
        self.statue  = {"hp":1, "atk":1, "def":1}
