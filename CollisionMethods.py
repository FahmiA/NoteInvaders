import pygame
from pygame.locals import *

from Laser import Laser
from Player import Player

def collideLineToRect(lineSprite, rectSprite):
    # TODO: Optimise by using a line collision algorithm (not pixel collision like this)
    return pygame.sprite.collide_mask(lineSprite, rectSprite)
    #laserStartPoint = lineSprite.rect.center + Vec2d(lineSprite._originalImage.get_rect().width / 2, 0).rotated(lineSprite._rotation)
    #laserEndPoint = lineSprite.rect.center - Vec2d(lineSprite._originalImage.get_rect().width / 2, 0).rotated(lineSprite._rotation)

    #return linesCollide(laserStartPoint, laserEndPoint, rectSprite.bottomleft



def linesCollide(line1p1, line1p2, line2p1, line2p2):
    # Source: http://python.6.x6.nabble.com/Python-Line-Intersection-td1508591.html
    x1, y1, x2, y2 = line1p1[0], line1p1[1], line1p2[0], line1p2[1]
    x3, y3, x4, y5 = line2p1[0], line2p1[1], line2p2[0], line2p2[1]

    try:
        denom = float((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
        y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom
    except ZeroDivisionError:
        return False
    return True



