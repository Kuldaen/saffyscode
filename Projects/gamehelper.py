#pylint:disable=W0611
#pylint:disable=W0401
import pygame
import pgzrun
from pgzhelper import *

def create_control_buttons():
    upbutton = Actor("dot")
    upbutton.scale = 5
    upbutton.pos = 1600, 825

    downbutton = Actor("dot")
    downbutton.scale = 5
    downbutton.pos = 1600, 1025
  
    leftbutton = Actor("dot")
    leftbutton.scale = 5
    leftbutton.pos = 1500, 925

    rightbutton = Actor("dot")
    rightbutton.scale = 5
    rightbutton.pos = 1700, 925
    
    return (upbutton, downbutton, leftbutton, rightbutton)
    
def draw_control_buttons(control_buttons):
    for button in control_buttons:
        button.draw()   
    