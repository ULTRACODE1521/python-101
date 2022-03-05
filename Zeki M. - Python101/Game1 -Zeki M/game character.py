#this is my first game
WIDTH = 500
HEIGHT = 500

alien = Actor('ninja')
alien.x=300
alien.y-50

def draw():
    screen.clear()
    alien.draw()
