import pygame
from pygame.locals import *

from Actor import Actor
from Vec2d import Vec2d

class Player(Actor):

    def __init__(self, image):
        Actor.__init__(self, image, (500, 500))
        self._maxVelocity[0] = 0

    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        pressedKeys = pygame.key.get_pressed()

        if pressedKeys[K_d]:
            self._rotate(self._rotationSpeed)
        elif pressedKeys[K_a]:
            self._rotate(-self._rotationSpeed)

        if pressedKeys[K_w]:
            self._velocity = Vec2d(self._maxVelocity)
        else:
            self._velocity = Vec2d(0, 0)


        self._updatePosition()
