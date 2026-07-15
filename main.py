import pgzrun
 

def draw():
    screen.blit("back", (0, 0))
    mario.draw()


def update():
    pass

WIDTH = 1280
HEIGHT = 720

mario = Actor("mario_right")
mario.x = 300
mario.y = 200

pgzrun.go()