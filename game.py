"""
Import Dependecies
"""
import sys
import pygame
import random

pygame.init()

#Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

colors = [(WHITE), (BLACK), (GRAY)]

#Tetromino figures
class Figure:
    SCREEN_PLAY = r"""

HHHHHHHHH   HHHHHHHHH   HHHHHHHHH   HHHHHHHHH   HHH   HHHHHHHHH
   HHH      HHH            HHH      HHH   HHH   HHH   HHH
   HHH      HHH            HHH      HHH   HHH   HHH   HHH
   HHH      HHHHHH         HHH      HHHHHH      HHH   HHHHHHHHH
   HHH      HHHHHH         HHH      HHHHHH      HHH   HHHHHHHHH
   HHH      HHH            HHH      HHH   HHH   HHH         HHH
   HHH      HHHHHHHHH      HHH      HHH   HHH   HHH   HHHHHHHHH
   HHH      HHHHHHHHH      HHH      HHH   HHH   HHH   HHHHHHHHH

   
            P R E S S  A N Y  K E Y  T O  S T A R T
"""
    def __init__(self):
        print(self.SCREEN_PLAY)
Figure()