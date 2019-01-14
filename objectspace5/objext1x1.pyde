def setup():
    """draws rectangle"""
    size(30, 30)
    background(250)

def draw():
    for x in range(0, 30):
       for y in range(0, 30):
           fill(227,41,41)
           rect(x, y, 30, 30, 10)
