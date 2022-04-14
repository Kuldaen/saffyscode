#pylint:disable=W0621
#pylint:disable=E0602
import pygame
import pgzrun
from pgzhelper import *
from random import randint

WIDTH = 1600
HEIGHT = 800

game_over = False


dots = [ ]
lines = [ ]

next_dot = 0
time_remaining = 20

 
for dot in range(0, 10):
    actor = Actor("dot")
    actor.scale = 5
    actor.pos = randint (20, WIDTH - 20), \
    randint(20, HEIGHT - 20)
    dots.append(actor)
    
    
    
    
def draw():
    screen.fill("black")
    number = 1
    
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 60), fontsize=40)
        dot.draw()
        number = number + 1
        
    for line in lines:
        screen.draw.line(line[0], line[1], (200, 0, 0))
        
    screen.draw.text("Time left:"+str(time_remaining), topleft = (1500, 40), fontsize=100)
    
    if game_over:
        screen.fill("white")
        screen.draw.text("Game Over", topleft=(200, 200,), fontsize=100)
        
def on_mouse_down(pos):
        global next_dot
        global lines
        if dots[next_dot].collidepoint(pos):
            if next_dot > 0:
                lines.append((dots[next_dot-1].pos, dots[next_dot].pos))
            next_dot = next_dot + 1
        else:
                lines= [ ]
                next_dot = 0
                


pgzrun.go()


