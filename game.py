import pgzrun, random

WIDTH=500
LENGTH=500

score=0
gameover=False
character1=Actor("virat")
character2=Actor("ball")
character1.pos=65,70
character2.pos=50,300
def draw():
    screen.blit("indiaflag",(0,0))
    character1.draw()
    character2.draw()


    screen.draw.text("Your score:"+str(score),topleft=(0,0),color="Grey")
    if gameover==True:
        screen.fill("Red")
        screen.draw.text("gameover:",topleft=(0,0),color="Grey")


def virat():
    character2.y=random.randint(50,450)
    character2.x=random.randint(50,450)


def update():
    global score
    if keyboard.left:
        character1.x=character1.x-8
    if keyboard.right:
        character1.x=character1.x+8
    if keyboard.up:
        character1.y=character1.y-8
    if keyboard.down:
        character1.y=character1.y+8
    ballcollected=character1.colliderect(character2)
    if ballcollected:
        score=score+10  
        

def timeup ():
    global gameover
    gameover=True

clock.schedule(timeup,60.0)



pgzrun.go()

  