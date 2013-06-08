import pygame
from pygame.locals import *

from Vec2d import Vec2d

class Actor(pygame.sprite.Sprite):

    def __init__(self, image, position):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self) 

        # Process the arguments
        self._originalImage = image
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (position[0], position[1])

        self._rotationSpeed = 50 # Degrees per second

        self._rotation = 0; # Degrees
        self._position = Vec2d(self.rect.center)
        self._maxVelocity = Vec2d(50, 50)
        self._velocity = Vec2d(0, 0)

        self._elapsedTimeSec = 0.0

    # Abstract
    def update(self, elapsedTimeSec):
        self._elapsedTimeSec = elapsedTimeSec

    def getPosition(self):
        return Vec2d(self._position)

    def _updatePosition(self):
        self._velocity.rotate(self._rotation)
        self._position += self._velocity * self._elapsedTimeSec
        self.rect.center = (self._position[0], self._position[1])

    def _rotate(self, deltaRotation):
        self._rotation += deltaRotation * self._elapsedTimeSec

        center = self.rect.center
        self.image = pygame.transform.rotate(self._originalImage, -self._rotation)
        self.rect = self.image.get_rect()
        self.rect.center = center

