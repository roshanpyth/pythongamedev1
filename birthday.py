import pygame
import time

pygame.init()
run=True

screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Birthday")

imag_store=pygame.image.load("C:/Users/cyrus/Py game module 1/gamdev2/birthday.jpg")

store=pygame.transform.scale(imag_store,(500,400))

while run:
    screen.blit(imag_store,(0,0))
    pygame.display.update()
    time.sleep(5)







