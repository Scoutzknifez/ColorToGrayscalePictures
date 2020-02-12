import ColorToGrayscalePictures.utility.Constants as Constants
import ColorToGrayscalePictures.utility.Utils as Utils
import os


def start():
    if __name__ != '__main__':
        return

    Constants.initialize(os.path.dirname(__file__))
    Utils.save_image(
        Utils.convert_image(
            Utils.take_screenshot()
        ),
        Utils.get_testing_path(),
        "converted.png"
    )


start()
