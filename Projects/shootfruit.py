#pylint:disable=W0611
#pylint:disable=E0602
import pygame
import pgzrun
from random import randint

score = 0


apple = Actor("apple")

def draw():
    screen.clear()
    screen.draw.text(f"Score:{score}", topleft=(200, 200), fontsize =100)
    apple.draw()
    
def place_apple():
     apple.x = randint(10, 800)
     apple.y = randint(10, 800)
     
def on_mouse_down(pos):
   global score
   if apple.collidepoint(pos):
         print ("Good shot!")
         score = score + 1
         place_apple()
   else:
       print ("You missed!")
       quit()
   

place_apple()








pgzrun.go()