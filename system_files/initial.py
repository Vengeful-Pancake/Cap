import pygame
from system_files.save.save import SAVE

pygame.init()

screen= pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
clock = pygame.time.Clock()
pygame.display.set_caption('Title')
icon = pygame.image.load("system_files\\sprite\\icon.ico")
pygame.display.set_icon(icon)
RUNNING=1
width = 1920
height = 1080

SCREENING = pygame.image.load("system_files\\sprite\\scr.png")
SCREEN_TOLERANCE = 10

#saved data for cross communication

data={
    "WINDOW_HEIGHT" : WINDOW_HEIGHT,
    "WINDOW_WIDTH" : WINDOW_WIDTH,
    "STATE" : "PROGRAM",
    "SCREEN" : 100
}
SAVE("",data,"cross.txt")
