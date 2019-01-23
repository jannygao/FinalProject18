import random #so the chosen blocks will be randomly selected
import copy #easily copy stuff for the list later
boxSize = 30 #just setting a standard variable for the size of my boxes
cornerRadius = 10 #setting a standard radius for the boxes
blockIndex = random.randint(0,19) #establishes the numbers to randomly select as the index to randomly choose a block
gridSize = 10 #establishing how big my grid is
grid = [[0 for j in range(gridSize)] for i in range(gridSize)] #defining the size of my grid

colors = [#making a list holding all the colors for each object
          color(255, 255, 255),
          
          color(125, 100, 250),
          
          color(50, 240, 200),
          
          color(100, 185, 250),
          
          color(100, 185, 250),
          
          color(100, 185, 250),
          
          color(100, 185, 250),
          
          color(50, 240, 200),
          
          color(40, 255, 100),
          
          color(10, 225, 160),
          
          color(10, 225, 160),
          
          color(10, 225, 160),
          
          color(10, 225, 160),
          
          color(255, 175, 0),
          
          color(255, 175, 0),
          
          color(252, 162, 43),
          
          color(252, 162, 43),
          
          color(252, 71, 129),
          
          color(252, 71, 129),
          
          color(180, 30, 30),
          
          color(180, 30, 30)
]

blockShapes = [ #making a list holding all the possible blocks placed in multiple orientations
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

    [[7, 7, 7], #put this block in twice to make it harder to win
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

class Piece:
    #creates class that holdes the blocks
    def __init__(self, blockIndex):
        self.blockIndex = blockIndex
    
    def getBlocks(self):
        return blockShapes[self.blockIndex]
    
    def randomize(self):
        self.blockIndex = random.randint(0,19)
    

currentBlock = Piece(blockIndex)

def setup():
    """creates the grid for the game 10x10"""
    size(300, 300) #screen window size
    background(255) #color of the background of screen
    for x in range(0, 300, boxSize): #establishing the grid
        for y in range(0, 300, boxSize):
            background(0)
    for x in range(0, 300, boxSize):
       for y in range(0, 300, boxSize):
           rect(x ,y, boxSize, boxSize, cornerRadius)
    textSize(45)

def draw():
    """was a predefined function but used to display game"""
    background(255) #just setting a value to draw and the background
    fill(255) #establishing the box colors to be drawn
    for x in range(0, 300, boxSize): #redraws the grid each time
        for y in range(0, 300, boxSize):
            background(0)
    for x in range(0, 300, boxSize):
       for y in range(0, 300, boxSize):
           rect(x ,y, boxSize, boxSize, cornerRadius)
    
    display(grid, 0, 0) #shows the grid and the change

    display(currentBlock.getBlocks(), mouseX-boxSize/2, mouseY-boxSize/2) #shows the block being moved around
    
      
def mouseClicked():
    #predefined function
    """lets the block be moved around and appended into the grid space"""
    #need to put the variables here because i need them defined locally so that it will run through
    global currentBlock
    global grid
    score = 0
    piece = blockShapes[blockIndex] #establishing the current piece
    #defines where the mouse is and which box is being referenced
    gridX = (mouseX / boxSize)
    gridY = (mouseY / boxSize)
    
    canPlace = True #assumming that the block can fit
    for i in range(len(currentBlock.getBlocks())):
        #checks if block can fit
        for j in range(len(currentBlock.getBlocks()[0])):
            if gridX+j >= gridSize:
                canPlace = False
            elif gridY+i >= gridSize:
                canPlace = False
            elif grid[gridY+i][gridX+j] > 0 and currentBlock.getBlocks()[i][j] > 0:
                canPlace = False
    if canPlace == True:
        for i in range(len(currentBlock.getBlocks())):
            for j in range(len(currentBlock.getBlocks()[0])):
                if currentBlock.getBlocks()[i][j] > 0:
                   #adding pieces to the grid if they fit
                    print(grid)
                    print(currentBlock.getBlocks())
                    grid[gridY+i][gridX+j] = currentBlock.getBlocks()[i][j]
                
        currentBlock.randomize()
        
#checks for completed rows and clears them    
    tempGrid = copy.deepcopy(grid)
    for i in range(0, gridSize):
        fullRow = True
        fullColumn = True
        for j in range(0, gridSize):
            if grid[i][j] == 0:
                fullRow = False
            if grid[j][i] == 0:
                fullColumn = False
        if fullRow == True:
            score += 1
            for j in range(0, gridSize):
                tempGrid[i][j] = 0
        if fullColumn == True:
            score += 1
            for j in range(0, gridSize):
                tempGrid[j][i] = 0
    grid = tempGrid #places the grid used to hold the row and column so both can be wiped together in the grid space being viewed

    youLoser = True
    #checking all squares if block can be placed
    for gridX in range(0, gridSize):
        for gridY in range(0, gridSize):
            playGame = True
            #checking if block can be placed
            for i in range(len(currentBlock.getBlocks())):
                for j in range(len(currentBlock.getBlocks()[0])):
                    if gridX+j >= gridSize:
                        playGame = False
                    elif gridY+i >= gridSize:
                        playGame = False
                    elif grid[gridY+i][gridX+j] > 0 and currentBlock.getBlocks()[i][j] > 0:
                        playGame = False
            if playGame == True:
                    #so game wasnt lost yet and it keeps going
                    youLoser = False
                    
    if youLoser == True:
        grid = [[0 for j in range(gridSize)] for i in range(gridSize)]
        #wiping the whole thing to restart
          
def display(piece, posX, posY):
    """show the object in the location on the grid specified"""
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] > 0:
                fill(colors[piece[i][j]])
                rect(posX + j*boxSize, posY + i*boxSize, boxSize, boxSize, cornerRadius)
