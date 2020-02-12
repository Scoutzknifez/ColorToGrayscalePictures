import ColorToGrayscalePictures.utility.Constants as Constants
import os


def start():
    if __name__ != '__main__':
        return

    Constants.initialize(os.path.dirname(__file__))


start()
