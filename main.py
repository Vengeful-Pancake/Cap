from system_files.initial import *
from system_files.user_interface import *
from dhandler.d_scanner import *


def main():
    
    INPUT_HOLDER=""
    while RUNNING:
        UI(INPUT_HOLDER)
        d_scan()


if __name__ == "__main__":    
    main()
