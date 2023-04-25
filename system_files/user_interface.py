from system_files.save_load import *
from system_files.input_handler import *
from system_files.initial_file import *
from system_files.display import *

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

    