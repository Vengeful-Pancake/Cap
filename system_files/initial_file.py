import os
import pygame
import tkinter as tk
from system_files.save_load import LOAD


TKINTER = tk.Tk()
RUNNING = 1
SCREEN_WIDTH = TKINTER.winfo_screenwidth()
SCREEN_HEIGHT = TKINTER.winfo_screenheight()
path = os.getcwd()
SCREEN_TOLERANCE = 10
INPUT_HOLDER = "null"
FS_HOLDER = ""
