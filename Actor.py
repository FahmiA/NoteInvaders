import pygame
from pygame.locals import *

from Vec2d import Vec2d

class Actor(pygame.sprite.Sprite):

    def __init__(self, image, position, maxVelocity):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self) 

        # Process the arguments
        # Reduce image size
        imageSize = image.get_rect()
        actorSize = (int(imageSize.width * 0.7), int(imageSize.height * 0.7))
        self._originalImage = pygame.transform.scale(image, actorSize) # Reduce actor size

        self.image = self._originalImage
        self.rect = self._originalImage.get_rect()
        self.rect.center = (position[0], position[1])

        self._rotation = 0; # Degrees
        self._position = Vec2d(self.rect.center)
        self._maxVelocity = maxVelocity
        self._velocity = Vec2d(0, 0)

        self._elapsedTimeSec = 0.0

    # Abstract
    def update(self, elapsedTimeSec):
        self._elapsedTimeSec = elapsedTimeSec

    def getPosition(self):
        return Vec2d(self._position)

    def setPosition(self, position):
        self._position = Vec2d(position)

    def _updatePosition(self):
        #self._velocity.rotate(self._rotation)
        self._position += self._velocity * self._elapsedTimeSec
        self.rect.center = (self._position[0], self._position[1])

    def _rotate(self, rotation):
        self._rotation = rotation

        center = self.rect.center
        self.image = pygame.transform.rotate(self._originalImage, -self._rotation)
        self.rect = self.image.get_rect()
        self.rect.center = center

    def _truncate(self, vector, maxLength):
        result = Vec2d(vector)
        if result.get_length() > maxLength:
            result = result.normalized() * maxLength
        return result

