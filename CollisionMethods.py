import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Laser import Laser
from Player import Player

def collideLineToRect(lineSprite, rectSprite):
    # Get start and end points of line
    laserStartPoint = lineSprite.rect.center + Vec2d(lineSprite._originalImage.get_rect().width / 2, 0).rotated(lineSprite._rotation)
    laserEndPoint = lineSprite.rect.center - Vec2d(lineSprite._originalImage.get_rect().width / 2, 0).rotated(lineSprite._rotation)

    # Check line intersection against line and all edges of rect
    rect = rectSprite.rect
    return linesCollide(laserStartPoint, laserEndPoint, rect.bottomleft, rect.topleft) or \
           linesCollide(laserStartPoint, laserEndPoint, rect.topleft, rect.topright) or \
           linesCollide(laserStartPoint, laserEndPoint, rect.topright, rect.bottomright) or \
           linesCollide(laserStartPoint, laserEndPoint, rect.bottomright, rect.bottomleft)
           
def ccw(A, B, C):
    # Source: http://www.bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def linesCollide(A,B,C,D):
    # Source: http://www.bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def collideRectThenMask(spriteA, spriteB):
    """
    Checks if two sprites collide by first doing cheap rect collision,
    then doing expensive mask (per-pixel) collision if their rects collide.
    """
    collide = False
    if pygame.sprite.collide_rect(spriteA, spriteB):
        collide = pygame.sprite.collide_mask(spriteA, spriteB)
    return collide




