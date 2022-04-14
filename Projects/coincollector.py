#pylint:disable=E0602
import pygame
import pgzrun
from pgzhelper import *
from random import randint
from gamehelper import *

WIDTH = 400
HEIGHT = 400
score = 0

game_over = False

control_buttons = create_control_buttons()

fox = Actor("fox")
fox.scale = 1
fox.pos = 100, 100

coin = Actor("coin")
coin.scale = 3
coin.pos = randint(200, 1400), randint(200, 1000)

def time_up():
    global game_over
    game_over = True

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    draw_control_buttons(control_buttons)
    screen.draw.text("Score: " +str(score), topleft=(10, 10), fontsize=60)
    
    
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " +str(score), topleft=(10, 10), fontsize=60)
    
def on_mouse_down(pos):
   (upbutton, downbutton, leftbutton, rightbutton) = control_buttons
   if upbutton.collidepoint(pos):
       fox.move_left(dist=40)
   if downbutton.collidepoint(pos):
       fox.move_right(dist=40)
   if leftbutton.collidepoint(pos):
       fox.move_back(dist=40)
   if rightbutton.collidepoint(pos):
       fox.move_forward(dist=40)
       
def move_coin():
          
          coin.pos = randint(200, 1400), randint(200, 1000)
          
 
          
               
def update():
          global score
          coin_collected = fox.colliderect(coin)
          
          if coin_collected:
                        score = score + 10
                        move_coin()
                        
clock.schedule(time_up, 20.0)
move_coin
                        
          
   
    
   
   
    
























pgzrun.go()