def setup():
    """creates the grid for the game"""
    size(300, 420)
    background(250)
    for x in range(0, 300, 30):
        for y in range(0, 420, 30):
            background(0)

boxcolor = [10, 14]

def draw():
    for x in range(0, 300, 30):
       for y in range(0, 300, 30):
           rect(x,y,30,30, 10)
    if y in range(300, 420, 30):
        fill(0)
        rect(x, y, 30, 30, 10)
