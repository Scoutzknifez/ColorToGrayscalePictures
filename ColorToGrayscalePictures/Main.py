import ColorToGrayscalePictures.utility.Constants as Constants
import ColorToGrayscalePictures.utility.Utils as Utils
import os


def start():
    if __name__ != '__main__':
        return

    Constants.initialize(os.path.dirname(__file__))
    all_conversions()


def all_conversions():
    image = Utils.take_screenshot()
    conversions = ["grayscale", "redscale", "greenscale", "bluescale"]

    for conversion in conversions:
        Utils.save_image(
            Utils.convert_image(
                image,
                conversion
            ),
            Utils.get_testing_path(),
            conversion + ".png"
        )


start()
