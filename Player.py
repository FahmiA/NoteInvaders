import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Actor import Actor
from Laser import Laser

class Player(Actor):

    def __init__(self, image, laser):
        Actor.__init__(self, image, (500, 500), (0, 100))

        self._laser = laser

        self._rotationSpeed = 100 #Degrees per second

    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        pressedKeys = pygame.key.get_pressed()

        # Handle rotation
        if pressedKeys[K_d]:
            self._rotate(self._rotationSpeed)
        elif pressedKeys[K_a]:
            self._rotate(-self._rotationSpeed)

        # Handle Movement
        if pressedKeys[K_w]:
            self._velocity = self._maxVelocity.rotated(self._rotation)
        else:
            self._velocity = Vec2d(0, 0)
        self._updatePosition()

        # Handle firing laser
        if pressedKeys[K_SPACE]:
            self._laser.fire(self.rect.center, self._rotation - 90)
        else:
            self._laser.stop()
