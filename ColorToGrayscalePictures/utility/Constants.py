import ctypes

# Globals
MAIN_FILE_LOCATION = ''     # Keeps track of where the main root program file is
SCREENSIZE = 0, 0           # The screen size we are working with


def initialize(main_file):
    global MAIN_FILE_LOCATION
    MAIN_FILE_LOCATION = main_file

    global SCREENSIZE
    SCREENSIZE = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

