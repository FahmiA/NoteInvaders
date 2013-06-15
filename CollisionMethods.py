import pygame
from pygame.locals import *

from Laser import Laser
from Player import Player

def collideLineToRect(lineSprite, rectSprite):
    # TODO: Optimise by using a linne collision algorithm (not pixel collision like this)
    return pygame.sprite.collide_mask(lineSprite, rectSprite)
