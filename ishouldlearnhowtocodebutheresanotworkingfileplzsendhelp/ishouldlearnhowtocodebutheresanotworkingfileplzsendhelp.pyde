import random
boxSize = 30
cornerRadius = 10
score = 0
blockIndex = random.randint(0,19)
colorIndex = blockIndex + 1
gridSize = 10
grid = [[0 for x in range(gridSize)]
        [0 for y in range(gridSize)]]
class Cell:
    def __init__(self, x, y, empty, value):
        self.x = x
        self.y = y
        self.empty = empty
        if self.empty:
            self.value = fill(250)
        else:
            self.value = value

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

def setup():
    """creates the grid for the game 10x15"""
    size(300, 450)
    background(255)
    for x in range(0, 300, boxSize):
        for y in range(0, 450, boxSize):
            background(0)
    for x in range(0, 300, boxSize):
       for y in range(0, 300, boxSize):
           rect(x ,y, boxSize, boxSize, cornerRadius)
    if y in range(300, 450, boxSize):
        fill(0)
        rect(x ,y, boxSize, boxSize, cornerRadius)
    textSize(45)

def draw():
    background(0)
    
    fill(255)
    for x in range(0, 300, boxSize):
        for y in range(0, 450, boxSize):
            background(0)
    for x in range(0, 300, boxSize):
       for y in range(0, 300, boxSize):
           rect(x ,y, boxSize, boxSize, cornerRadius)
    if y in range(300, 450, boxSize):
        fill(0)
        rect(x ,y, boxSize, boxSize, cornerRadius)
        
    display(grid, 0, 0)
    
    display(blockShapes[blockIndex], mouseX-boxSize/2, mouseY-boxSize/2, colors[colorIndex])
    
    fill(255, 255, 0)
    text("Score: ", 400, 650)
    text(score, 300, 700)
    text("Time: ", 100, 650)
    text(int(millis()/1000), 100, 700)
    
def mouseClicked():
    piece = blockShapes[blockIndex]
    
    gridX = int(mouseX / boxSize)
    gridY = int(mouseY / boxSize)
    
    canPlace = True
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if gridX+i >= gridSize:
                canPlace = False
            elif gridY+j >= gridSize:
                canPlace = False
            elif grid[gridX+i][gridY+j] > 0 and piece[i][j] > 0:
                canPlace = False
    if canPlace = True:
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                grid[gridX+i][gridY+j] = piece[i][j]
                
        blockIndex = random.randint(0,19)
         
    for i in range(0, gridSize):
        fullRow = True
        fullColumn = True
        for j in range(0, gridSize):
            if grid[j][i] == 0:
                fullRow = False
            if grid[i][j] == 0:
                fullColumn = False
        if fullRow = True:
            score +=1
            for j in range(0, gridSize):
                grid[j][i] = 0
        if fullColumn = True:
            score += 1
            for i in range(0, gridSize):
                grid[i][j] = 0
def display(piece, posX, posY, pieceColor):
    fill(pieceColor)
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] > 0:
                rect(posX + j*boxSize, posY + i*boxSize, boxSize, boxSize, cornerRadius)
                
