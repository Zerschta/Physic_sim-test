"""   
     -----Conways Game of Life-----
        Rules:
        
Any live cell with fewer than two live neighbors dies
Any live cell with two or three live neighbors lives on to the next generation
Any live cell with more than three live neighbors dies
Any dead cell with exactly three live neighbors becomes a live cell

     Neighbors:
        C = Cell
        N = Neighbors

        N N N
        N C N
        N N N

"""

import pygame
from math import *
import numpy as np