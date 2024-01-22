"""
Create a room described "description". Initially, it has no exits. The
'description' is something like 'kitchen' or 'an open court yard'.
"""
from text_ui import *

class Room:

    def __init__(self, description):
        self.description = description
        self.exits = {"west":None, "north":None, "east":None, "south":None}  # Dictionary
        self.clean = False

    def set_exit(self, direction, neighbour):
        # update dictionary, key is string of direction
        # value is a class instance of room
        self.exits.update({direction:neighbour}) # type of neighbour: class

    def get_short_description(self):
        return self.description

    def get_long_description(self):
        long_description = "Location: " + self.description + " Exits: "
        direction = list(self.exits.keys())
        room = list(self.exits.values())
        for i, exit in enumerate(direction): # list of class
            if room[i] and room[i].description != secret:
                long_description += exit
                long_description += ": "
                long_description += room[i].description
                long_description += ' '
        return long_description

    def get_exits(self):
        all_exits = list(self.exits.keys()) # all avaliable direction list
        return all_exits

    def get_exit(self, direction):
        if direction in self.exits.keys():
            return self.exits[direction] # return a class
        else:
            return None
