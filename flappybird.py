import pgzrun

TITLE="Flappy ball"

WIDTH=500
LENGTH=400
a=2000


class Ball():
    def __init__(self,x,y, color, radius):
        self.bx=x
        self.by=y
        self.colorx=color
        self.radius=radius
        self.vx=200
        self.vy=0
    def drawcircle(self):
        screen.draw.filled_circle((self.bx,self.by),self.radius,self.colorx)  
ball=Ball(50,40,"Red",25)
def draw():
    screen.clear()
    ball.drawcircle()
    

def update(dt):
    U=ball.vy
    ball.vy=U+a*dt
    ball.by=ball.by+(U+ball.vy)*0.5*dt

    ball.bx=ball.bx+ball.vx*dt


    if ball.by>LENGTH:
        ball.by=LENGTH
        ball.vy=-ball.vy*0.67












pgzrun.go()



    
