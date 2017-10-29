##Tracy Batchelor
## 23 OCt 2017
## CSC221
## M3HW1 Data Structure classes

class Stack(object):
    #initialize object
    def __init__(self):
        self.contents = []
    # gets length of list    
    def __len__(self):
        return len(self.contents)
    # prints list
    def __str__(self):
        return str(self.contents)
    # add item to list
    def push(self, item):
        self.contents.append(item)
    # remove last item
    def pop(self):
        return self.contents.pop()

class Queue(object):
    #initialize object
    def __init__(self):
        self.contents = []
    # gets length of list    
    def __len__(self):
        return len(self.contents)
    # prints list
    def __str__(self):
        return str(self.contents)
    #add item to list
    def __add__(self, item):
        self.contents.append(item)
    # remove first item  
    def __remove__(self, item):
        return self.contents.pop(0)

#
