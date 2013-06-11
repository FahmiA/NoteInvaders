import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Actor import Actor

class Enemy(Actor):

    def __init__(self, image, target):
        Actor.__init__(self, image, (100, 100), (50, 50))
        
        self._target = target

    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        self._velocity = (self._target.getPosition() - self.getPosition()).normalized()
        self._velocity *= self._maxVelocity

        self._rotation = self._velocity.get_angle() - 90
        self._rotate(0)

        self._updatePosition()


