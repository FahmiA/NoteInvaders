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
        self._isFiring = False

    def fire(self, firedFromPos, rotation):
        self._isFiring = True
        # TODO: Adjust Height

        # Adjust position
        self.rect.center = Vec2d(firedFromPos) - Vec2d(self._originalImage.get_rect().width / 2, 0).rotated(rotation)

        # Rotate
        self._rotation = rotation;
        self._rotate(rotation)

    def stop(self):
        self._isFiring = False

    def isFiring(self):
        return self._isFiring;

    def update(self, elapsedTimeSec):
        pass

    def _rotate(self, rotation):
        center = self.rect.center
        self.image = pygame.transform.rotate(self._originalImage, -rotation)
        self.rect = self.image.get_rect()
        self.rect.center = center

