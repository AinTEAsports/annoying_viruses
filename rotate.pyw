from pynput.keyboard import Listener
import rotatescreen
import random

screen = rotatescreen.get_primary_display()


options = {
    '0' : screen.set_landscape,
    '90' : screen.set_portrait,
    '180' : screen.set_landscape_flipped,
    '270' : screen.set_portrait_flipped,
}


def random_rotate(key):
    rotation = random.choice(list(options.keys()))
    options[rotation]()


with Listener(on_press=random_rotate) as listener:
    listener.join()
    pass
