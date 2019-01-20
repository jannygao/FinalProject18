import random
def setup():
    """creates the grid for the game"""
    size(300, 450)
    background(250)
    for x in range(0, 300, 30):
        for y in range(0, 450, 30):
            background(0)
    for x in range(0, 300, 30):
       for y in range(0, 300, 30):
           rect(x,y,30,30, 10)
    if y in range(300, 450, 30):
        fill(0)
        rect(x, y, 30, 30, 10)

            

        
class Cell:
    def __init__(self, x, y, empty, value):
        self.x = x
        self.y = y
        self.empty = empty
        if self.empty:
            self.value = fill(250)
        else:
            self.value = value
  
