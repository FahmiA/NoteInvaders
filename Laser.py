import pygame
from pygame.locals import *

from Vec2d import Vec2d

class Laser:

    def __init__(self, length):
        self._length = length
        self._outerThickness = 20 # pixels
        self._innerThickness = 7 # pixels

        self._firedFromPos = Vec2d(0, 0)
        self._firedToPos = Vec2d(0, 0)

        self._outerColour = pygame.Color('#670da0ff')
        self._innerColour = pygame.Color('#9840cfff')

        self._isFiring = False

    def fire(self, firedFromPos, rotation):
        self._firedFromPos = Vec2d(firedFromPos)
        self._firedToPos = (self._firedFromPos * Vec2d(0, self._length)).rotated(rotation)

        self._isFiring = True

    def stop(self):
        self._isFiring = False

    def isFiring(self):
        return self._isFiring;

    def getFiredFromPos(self):
        return self._firedFromPos

    def getFiredToPos(self):
        return self._firedToPos

    def update(self, elapsedTimeSec):
        # Nothing to update
        pass

    def draw(self, screen):
        if self._isFiring:
            # Draw the outer line
            pygame.draw.line(screen, self._outerColour, self._firedFromPos, self._firedToPos, self._outerThickness)
            # Draw the inner line
            pygame.draw.line(screen, self._innerColour, self._firedFromPos, self._firedToPos, self._innerThickness)


