import pygame
import time

pygame.init()
run=True

screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Birthday")

imag_store=pygame.image.load("C:/Users/cyrus/Py game module 1/gamdev2/birthday.jpg")

store=pygame.transform.scale(imag_store,(500,400))

imag_store2=pygame.image.load("C:/Users/cyrus/Py game module 1/gamdev2/birthday.png")
store2=pygame.transform.scale(imag_store2,(500,400))

imag_store3=pygame.image.load("C:/Users/cyrus/Py game module 1/gamdev2/birthday1.jpg")
store3=pygame.transform.scale(imag_store3,(500,400))
#blit is used to add

while run:
    screen.blit(store,(0,0))
    Font=pygame.font.SysFont("Times New Roman",30)
    text=Font.render("Happy Birthday Bro",True,"Red")
    screen.blit(text,(140,150))
    pygame.display.update()
    time.sleep(2)
    screen.blit(store2,(0,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(store3,(0,0))
    pygame.display.update()
    time.sleep(2)








#    screen.blit(imag_store2,(0,0))
   # pygame.display.update()
 #   time.sleep(5)



#while run:
 #   screen.blit(imag_store3,(0,0))
  #  pygame.display.update()
   # time.sleep(5)







