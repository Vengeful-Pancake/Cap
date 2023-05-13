from system_files.save.save import *
from system_files.input_handler import *
from system_files.color import *
from system_files.initial import *

def screen_display(SCREEN):
    STATE=LOAD("STATE","cross.txt")
    if STATE == "PROGRAM":
        screen.fill(white)
        displayed_screen = pygame.transform.scale(SCREENING, (width, height))
        screen.blit(displayed_screen, (0, 0))
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, 0, width-(SCREEN_TOLERANCE*2), height/8),2)
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/8, height-(SCREEN_TOLERANCE*2)-height/4))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE,  width/8, height-(SCREEN_TOLERANCE*2)-height/4),2)
        pygame.draw.rect(screen, white, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8))
        pygame.draw.rect(screen, blue, pygame.Rect(SCREEN_TOLERANCE, height/8+SCREEN_TOLERANCE*2+height-(SCREEN_TOLERANCE*2)-height/4, width-(SCREEN_TOLERANCE*2), height/8),2)
        
    if STATE == "3DMODE":
        pass
    pygame.display.flip()

def UI(INPUT_HOLDER):
    SCREEN = LOAD('SCREEN',"config.txt")
    USER_INPUT=input(SCREEN)
    if USER_INPUT != "null" and USER_INPUT != INPUT_HOLDER:
        print (USER_INPUT)
    # if USER_INPUT == "F11":
    #     if SCREEN<3:
    #         SCREEN+=1
    #     else:
    #         SCREEN=0
    #     SAVE("SCREEN",SCREEN,"config.txt")
    INPUT_HOLDER=USER_INPUT
    screen_display(SCREEN)

    