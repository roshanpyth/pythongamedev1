import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Rectangle")

run=True

class Rectangle():
   def __init__(self,color,dimension):
      self.rectanglecolor=color
      self.dimension=dimension
   def draw(self):
      pygame.draw.rect(screen,self.rectanglecolor,self.dimension,5)
rectangle1=Rectangle("Green",(20,50,40,70))


rectangle2=Rectangle("Orange",(50,150,40,70))





      

while run:
    for i in pygame.event.get():
      if i.type==pygame.QUIT:
         run=False
      elif i.type==pygame.MOUSEBUTTONDOWN:
         rectangle1.draw()
         pygame.display.update()
         rectangle2.draw()
         pygame.display.update()




   
         
    
