##Tracy Batchelor
##16 Oct 2017
##CSC221
## M3HW2

import M3HW1

class Room(object):
    # create room
    def __init__(self, name='None'):
        self.name = name
        self.next_room = None

    def __str__(self):
        return "Room: ("+str(self.name)+")"
    # get room name
    def get_name(self):
        return self.name
    # link next room
    def next_room(self, room):
        self.next = room


a = Room(1)
b = Room(2)
a.next_room(b)
c = Room(end)
b.next_room(c)

class Dungeon(object):
    # create maze object
    def __init__(self):
        self.list = []
        self.currentroom = None

    def get_currentroom(self):
        return self.currentroom

    def set_currentroom(self, cell):
        self.currentroom = cell

Iamat = a
print(Iamat)
Iamat = Iamat.pop
print (Iamat)
Iamat = Iamat.pop
print (Iamat)
