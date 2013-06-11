import pygame
from pygame.locals import *

from Vec2d import Vec2d

class Laser(pygame.sprite.Sprite):

    def __init__(self, image):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self) 

        self._originalImage = image
        self.image = image
        self.rect = image.get_rect()

        self._rotation = 0;

    def fire(self, firedFromPos, rotation):
        #self._firedFromPos = firedFromPos
        #self._rotation = rotation

        # Adjust position
        self.rect.midleft = (firedFromPos[0], firedFromPos[1])

        # TODO: Adjust Height

        # Rotate
        self._rotation = rotation;
        self._rotate(rotation)

    def update(self, elapsedTimeSec):
        #self._rotation += 1
        #self._rotate(self._rotation)
        pass

    def _rotate(self, rotation):
        midleft = self.rect.midleft
        self.image = pygame.transform.rotate(self._originalImage, -rotation)
        self.rect = self.image.get_rect()
        self.rect.midleft = midleft

