import pygame
from system_files.save.save import SAVE

pygame.init()

screen = pygame.display.set_mode()

WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()

pygame.display.set_caption('Title')

# pygame.display.set_icon("sprite\\icon.ico")

#saved data for cross communication
data={
    "WINDOW_HEIGHT" : WINDOW_HEIGHT,
    "WINDOW_WIDTH" : WINDOW_WIDTH,
    "STATE" : "PROGRAM"
}
SAVE("",data,"cross.txt")
