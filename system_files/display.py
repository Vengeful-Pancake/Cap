
from system_files.color import *
import pygame
from system_files.initial_file import *
        
def screen_display(FULLSCREEN, STATE):
    clock=pygame.time.Clock()
    clock.tick(30)
    if FULLSCREEN == 0:
        width = SCREEN_WIDTH
        height = SCREEN_HEIGHT
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    elif FULLSCREEN == 1:
        width = 1920
        height = 1080
        screen = pygame.display.set_mode((width,height))
    elif FULLSCREEN == 2:
        width = 1600
        height = 900
        screen = pygame.display.set_mode((width,height))
    elif FULLSCREEN == 3:
        width = 800
        height = +600
        screen = pygame.display.set_mode((width,height))
    
    if STATE == "menu":
        screen.fill(white)
        pygame.draw.rect(screen, blue, pygame.Rect(30, 30, 60, 60))
        
    if STATE == "program":
        screen.fill(black)
        screen.fill(red)
    pygame.display.flip()
    




