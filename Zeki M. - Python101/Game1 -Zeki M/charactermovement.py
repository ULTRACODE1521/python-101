WIDTH = 1000
HEIGHT = 1000
alien = Actor("redstick")
alien.pos = (400,50)
box = Rect((20,20), (100,100))

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")
    alien.draw()
def update():
    if keyboard.right:
        alien.x = alien.x + 7
    elif keyboard.left:
        alien.x = alien.x - 7
    elif keyboard.up:
        alien.y = alien.y - 7
    elif keyboard.down:
        alien.y = alien.y + 7
        #box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
    if alien.colliderect(box):
        print("hit")
