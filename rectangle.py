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
      
      
while run:
    for i in pygame.event.get():
      if i.type==pygame.QUIT:
         run=False


   
         
    
