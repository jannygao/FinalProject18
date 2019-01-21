import random
def setup():
    """creates the grid for the game 10x15"""
    size(300, 450)
    background(255)
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

boxSize = 30

cornerRadius = 10

colors = [
          color(255, 255, 255),
          
          color(125, 100, 250),
          
          color(100, 200, 115),
          
          color(100, 185, 250),
          
          color(100, 185, 250),
          
          color(100, 185, 250),
          
          color(50, 240, 200),
          
          color(180, 250, 60),
          
          color(15, 210, 70),
          
          color(15, 210, 70),
          
          color(15, 210, 70),
          
          color(15, 210, 70),
          
          color(35, 35, 35),
          
          color(35, 35, 35),
          
          color(255, 175, 0),
          
          color(255, 175, 0),
          
          color(230, 135, 5),
          
          color(230, 135, 5),
          
          color(220, 85, 165),
          
          color(220, 85, 165),
          
          color(180, 30, 30),
          
          color(180, 30, 30)
]


blockShapes = [
    [[1]],

    [[2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]],

    [[0, 0, 3],
     [0, 0, 3],
     [3, 3, 3]],

    [[4, 0, 0],
     [4, 0, 0],
     [4, 4, 4]],
    
    [[5, 5, 5],
     [5, 0 ,0],
     [5, 0, 0]],
    
    [[6, 6, 6],
     [0, 0, 6],
     [0, 0, 6]],

    [[7, 7, 7],
     [7, 7, 7],
     [7, 7, 7]],

    [[8, 8],
     [8, 8]],
    
    [[9, 0],
     [9, 9]],
    
    [[0, 10],
     [10, 10]],
    
    [[11, 11],
     [11, 0]],
    
    [[12, 12],
     [0, 12]],
    
    [[13, 13]],
    
    [[14],
     [14]],
    
    [[15, 15, 15]],
    
    [[16],
     [16],
     [16]],
    
    [[17, 17, 17, 17]],
    
    [[18],
     [18],
     [18],
     [18]],
    
    [[19, 19, 19, 19, 19]],
    
    [[20],
     [20],
     [20],
     [20],
     [20]]    
]

def draw():
    background(0)
    fill(255)
    for x in range(0, 300, 30):
       for y in range(0, 300, 30):
           rect(x,y,30,30, 10)
    if y in range(300, 450, 30):
        fill(0)
        rect(x, y, 30, 30, 10)
    #blockIndex = random.randint(0,19)
    #colorIndex = blockIndex + 1
    blockIndex = 5
    colorIndex = 6
    displayPiece(blockShapes[blockIndex], mouseX, mouseY, colors[colorIndex])

    
def displayPiece(piece, posX, posY, pieceColor):
    fill(pieceColor)
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == 1:
                rect(posX + j*boxSize, posY + i*boxSize, boxSize, boxSize, cornerRadius)
