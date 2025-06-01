import pgzrun,random
from time import time

WIDTH=500
LENGTH=200
#blit is used to add images in the screen
satlist=[]
lines=[]
nom=8
nextsat=0
def satelite():
    for i in range(8):
        actor=Actor("satelite")
        actor.pos=(random.randint(50,400),random.randint(50,200))
        satlist.append(actor)
def draw():
    screen.blit("starysky",(0,0))
    number=1
    for i in satlist:
        i.draw()
        screen.draw.text(str(number),(i.pos[0],i.pos[1]+20))
        number=number+1
        #str, what ever value u put in it, it will be converted to strong

def on_mouse_down(pos):
    if nextsat<nom:
        if satlist [nextsat].collidepoint(pos):
            if nextsat:
                lines.append((satlist[nextsat-1].pos, satlist[nextsat].pos))





satelite()
#this is calling

pgzrun.go()