import pgzrun

TITLE="Flappy bird"

WIDTH=500
LENGTH=400

class Ball():
    def __init__(self,x,y, color, radius):
        self.bx=x
        self.by=y
        self.colorx=color
        self.radius=radius
        self.vx=200
        self.vy=0

