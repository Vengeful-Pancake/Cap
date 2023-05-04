from system_files.save_load import *
from system_files.input_handler import *
from system_files.initial_file import *
from system_files.color import *

def screen_display(FULLSCREEN, STATE):
    SCREENIMG = pygame.image.load("image\\scr.png")
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
    screen.fill(white)
    displayed_screen = pygame.transform.scale(SCREENIMG, (width, height))
    screen.blit(displayed_screen, (0, 0))
    pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8))
    pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8),2)
    pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/16, height-(SCREEN_TOLERANCE*2)-height/4))
    pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/16, height-(SCREEN_TOLERANCE*2)-height/4),2)
    pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8))
    pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8),2)
    if STATE == "menu":
        
        pygame.draw.rect(screen, blue, pygame.Rect(30, 30, 60, 60))
        # create a surface object, image is drawn on it.
    
    
    # Using blit to copy content from one surface to other
    if STATE == "program":
        screen.fill(red)
    pygame.display.flip()

def UI(INPUT_HOLDER):
    
    SCREEN = LOAD('screen')
    STATE = LOAD("state")
    USER_INPUT=input(SCREEN)
    # # input gamecode here
    if USER_INPUT != INPUT_HOLDER and USER_INPUT!="null":
        print (USER_INPUT)
    if USER_INPUT == "F11":
        if SCREEN<3:
            SCREEN+=1
        else:
            SCREEN=0
        SAVE(SCREEN)
    INPUT_HOLDER = USER_INPUT
    screen_display(SCREEN, STATE)

    