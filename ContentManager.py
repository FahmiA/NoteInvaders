import os

import pygame
from pygame.locals import *

def load_image(name, colorkey = -1):
    """
    Loads an image.
    name = relative file path to image.
    colorkey = Determines transparent colour:
                * None for no transparency
                * -1 for top-left pixel to be transparent colour (default)
                * transparent colour
    """
    fullname = os.path.join('.', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image#, image.get_rect()

def load_font(fontPath, fontSize):
    font = None

    if pygame.font:
        font = pygame.font.Font(fontPath, fontSize)

    return font

