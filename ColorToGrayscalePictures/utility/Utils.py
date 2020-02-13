import ColorToGrayscalePictures.utility.Constants as Constants
from PIL import Image
import pyautogui as auto_gui


def get_testing_path():
    return Constants.MAIN_FILE_LOCATION + "/testing/"


def save_image(image, location, name):
    image.save(location + name)


def take_screenshot():
    image = auto_gui.grab()
    save_image(image, get_testing_path(), "screenie.png")

    return Image.open(get_testing_path() + "screenie.png")


def average_pixel_color(pixel):
    return (pixel[0] + pixel[1] + pixel[2]) / 3


def convert_image(image, mode):
    image_pixels = image.load()
    data = []

    for y in range(image.size[1]):
        for x in range(image.size[0]):
            if mode == "redscale":
                pixel = (int(average_pixel_color(image_pixels[x, y])), 0, 0)
            elif mode == "greenscale":
                pixel = (0, int(average_pixel_color(image_pixels[x, y])), 0)
            elif mode == "bluescale":
                pixel = (0, 0, int(average_pixel_color(image_pixels[x, y])))
            else:
                pixel = int(average_pixel_color(image_pixels[x, y]))
            data.append(pixel)

    image = Image.new("L" if (mode == "grayscale") else "RGB", (image.size[0], image.size[1]))
    image.putdata(data)

    return image
