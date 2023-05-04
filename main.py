from system_files.user_interface import *
from system_files.input_handler import *
from system_files.initial_file import *

def main():
    
    pygame.init()
    clock=pygame.time.Clock()
    clock.tick(60)
    
    while RUNNING:
        UI(INPUT_HOLDER)

if __name__ == "__main__":    
    main()