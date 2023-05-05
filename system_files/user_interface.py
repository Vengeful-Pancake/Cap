from system_files.save.save import *
from system_files.input_handler import *
from system_files.color import *

def screen_display(FULLSCREEN, STATE):
    # SCREENING = pygame.image.load("sprite\\scr.png")
    SCREEN_WIDTH=LOAD("WINDOW_WIDTH","cross.txt")
    SCREEN_HEIGHT  = LOAD("WINDOW_HEIGHT","cross.txt")
    SCREEN_TOLERANCE = 10
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
    # displayed_screen = pygame.transform.scale(SCREENING, (width, height))
    if STATE == "PROGRAM":
        # screen.blit(displayed_screen, (0, 0))
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8),2)
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/8, height-(SCREEN_TOLERANCE*2)-height/4))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/8, height-(SCREEN_TOLERANCE*2)-height/4),2)
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8),2)
        
    if STATE == "program":
        pass
    screen.convert()
    pygame.display.update()

def UI(INPUT_HOLDER):
    SCREEN = LOAD('screen',"config.txt")
    STATE = LOAD("STATE","cross.txt")
    USER_INPUT=input(SCREEN)
    # # input gamecode here
    if USER_INPUT!="null" and USER_INPUT != INPUT_HOLDER:
        print (USER_INPUT)
    if USER_INPUT == "F11":
        if SCREEN<3:
            SCREEN+=1
        else:
            SCREEN=0
        SAVE("SCREEN",SCREEN,"config.txt")
    screen_display(SCREEN, STATE)

    