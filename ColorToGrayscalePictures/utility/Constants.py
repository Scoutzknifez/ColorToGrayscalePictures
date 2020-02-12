import ctypes

# Globals
MAIN_FILE_LOCATION = ''
SCREENSIZE = 0, 0


def initialize(main_file):
    global MAIN_FILE_LOCATION
    MAIN_FILE_LOCATION = main_file

    global SCREENSIZE
    SCREENSIZE = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

