#this is my first game
WIDTH = 500
HEIGHT = 500

alien = Actor('alien')
alien.x=0
alien.y-50

def draw():
    screen.clear()
    alien.draw()

ninja = Actor('ninja')
ninja.x=0
ninja.y-50

def draw():
    screen.clear()
    ninja.draw()