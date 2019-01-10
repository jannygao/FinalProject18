def setup():
    """creates the grid for the game"""
    size(300, 300)
    background(250)
    boxcolor = [10, 10]

def draw():
   for x in range(0, 300, 30):
       for y in range(0, 300, 30):
           rect(x,y,30,30)
