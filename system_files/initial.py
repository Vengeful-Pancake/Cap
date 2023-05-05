import pygame
from system_files.save.save import SAVE

pygame.init()

screen = pygame.display.set_mode()
WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
clock = pygame.time.Clock()
pygame.display.set_caption('Title')
icon = pygame.image.load("system_files\\sprite\\icon.ico")
pygame.display.set_icon(icon)

#saved data for cross communication
data={
    "WINDOW_HEIGHT" : WINDOW_HEIGHT,
    "WINDOW_WIDTH" : WINDOW_WIDTH,
    "STATE" : "PROGRAM"
}
SAVE("",data,"cross.txt")
