import random
def setup():
    """creates the grid for the game 10x15"""
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

rows, columns = 10, 15

blockShapes = [
    [[1]],

    [[2, 2, 2],
     [2, 2, 2],
     [2, 2, 2],

    [[0, 0, 3],
     [0, 0, 3],
     [3, 3, 3]],

    [[4, 0, 0],
     [4, 0, 0],
     [4, 4, 4]],

    [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]],
    
    [[7, 0],
     [7, 7]],
    
    [[0, 8],
     [8, 8]],
    
    [[9, 9]],
    
    [[10, 10, 10]],
    
    [[11, 11, 11, 11]],
    
    [[12, 12, 12, 12, 12]]
    
    
]
