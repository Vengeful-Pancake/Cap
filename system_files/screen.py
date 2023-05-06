from system_files.save.save import *
import pygame

SCREENING = pygame.image.load("system_files\\sprite\\scr.png")
SCREEN_TOLERANCE = 10
STATE = LOAD("STATE","cross.txt")
SCREEN=LOAD("SCREEN", "config.txt")
if SCREEN == 0:
    screen= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
elif SCREEN == 1:
    width = 1920
    height = 1080
    screen=  pygame.display.set_mode((width,height))
elif SCREEN == 2:
    width = 1600
    height = 900
    screen=  pygame.display.set_mode((width,height))
elif SCREEN == 3:
    width = 800
    height = +600
    screen=  pygame.display.set_mode((width,height))