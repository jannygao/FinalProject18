import random
def setup():
    """creates the grid for the game"""
    size(300, 450)
    background(250)
    for x in range(0, 300, 30):
        for y in range(0, 450, 30):
            background(0)

def draw():
    for x in range(0, 300, 30):
       for y in range(0, 300, 30):
           rect(x,y,30,30, 10)
    if y in range(300, 450, 30):
        fill(0)
        rect(x, y, 30, 30, 10)

class Block(object):
    def __init__(self, color, shape, xpos, ypos):
        self.color = color
        self.shape = shape
        self.xpos = xpos
        self.ypos = ypos


boxcolor = [10, 15]
rows = 10
columns = 15

class Cell:
    def __init__(self, x, y, empty, value = fill(250)):
        self.x = x
        self.y = y
        self.empty = empty
        self.value = value
        if self.empty:
            self.empty = fill(0)
