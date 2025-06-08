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
   
    for i in red_ball:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number=number+1
ball()
pgzrun.go()