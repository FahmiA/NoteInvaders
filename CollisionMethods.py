import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Laser import Laser
from Player import Player

def collideLineToRect(lineStartPoint, lineEndPoint, targetRect):
    # Check line intersection against line and all edges of rect
    return linesCollide(lineStartPoint, lineEndPoint, targetRect.bottomleft, targetRect.topleft) or \
           linesCollide(lineStartPoint, lineEndPoint, targetRect.topleft, targetRect.topright) or \
           linesCollide(lineStartPoint, lineEndPoint, targetRect.topright, targetRect.bottomright) or \
           linesCollide(lineStartPoint, lineEndPoint, targetRect.bottomright, targetRect.bottomleft)
           
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




