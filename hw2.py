import pygame

pygame.init()

run=True

screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Circle")

class Circle:
    def __init__(self, color, pos, radius):
        self.color = color
        self.pos = pos
        self.radius = radius
    def draw(self):
        #ifsomethinggreyudontuse
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

my_circle = Circle((255, 0, 0), (200, 200), 50)


my_circle.draw()
pygame.display.update()
while run:
      for i in pygame.event.get():
        if i.type==pygame.QUIT:
         run=False

      

