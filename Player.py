import pygame
from pygame.locals import *

from Vec2d import Vec2d

class Player(pygame.sprite.Sprite):

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self._originalImage = image
        self.image = image
        self.rect = image.get_rect()
        self.rect.center = (500,400) # TODO: Change

        self._movementSpeed = 50 # Pixels per second
        self._rotationSpeed = 50 # Degrees per second

        self._rotation = 0; # Degrees
        self._velocity = Vec2d(0, -self._movementSpeed)

    def update(self, elapsedTimeSec):

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[K_d]:
            self._rotate(self._rotationSpeed * elapsedTimeSec)
        elif pressedKeys[K_a]:
            self._rotate(-self._rotationSpeed * elapsedTimeSec)

        if pressedKeys[K_w]:
            self.rect.center += self._velocity * elapsedTimeSec

    def _rotate(self, deltaRotation):
        self._rotation += deltaRotation
        self._velocity.rotate(deltaRotation)

        center = self.rect.center
        self.image = pygame.transform.rotate(self._originalImage, -self._rotation)
        self.rect = self.image.get_rect()
        self.rect.center = center

