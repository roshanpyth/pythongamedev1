import pgzrun,random
from time import time

WIDTH=500
LENGTH=200

#blit is used to add images in the screen
red_ball=[]
lines=[]
nom=8
nextball=0
def ball():
    for i in range(8):
        actor=Actor("ball")
        actor.pos=(random.randint(50,400),random.randint(50,200))
        red_ball.append(actor)
def draw():
    screen.blit("cricket",(0,0))
    number=1
    print(red_ball)
    for i in red_ball:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20),color="blue")
        number=number+1

def on_mouse_down(pos):
    global red_ball
    global nextball
    global lines
    if nextball<nom:
        if red_ball [nextball].collidepoint(pos):
            if nextball:
                lines.append((red_ball[nextball-1].pos, red_ball[nextball].pos))
            nextball=nextball+1
        else:
            lines=[]
            red_ball=0


ball()
print(red_ball)
pgzrun.go()