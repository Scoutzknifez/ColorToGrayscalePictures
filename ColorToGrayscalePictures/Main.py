import ColorToGrayscalePictures.utility.Constants as Constants
import ColorToGrayscalePictures.utility.Utils as Utils
import os


def start():
    if __name__ != '__main__':
        return

    # Send the current working directory into a global for file tracking
    Constants.initialize(os.path.dirname(__file__))
    all_conversions()


def all_conversions():
    # Get the current screen TODO most likely to accept a file
    image = Utils.take_screenshot()
    # The possible types of conversions... TODO turn into enum?
    conversions = ["grayscale", "redscale", "greenscale", "bluescale"]

    for conversion in conversions:
        # Save the converted image
        Utils.save_image(
            Utils.convert_image(
                image,      # Converted image
                conversion  # Conversion type
            ),
            Utils.get_testing_path(),   # Path where to save the image
            conversion + ".png"         # Name of the saved file
        )


start()
