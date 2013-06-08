import pygame
from pygame.locals import *

from Actor import Actor
from Vec2d import Vec2d

class Enemy(Actor):

    def __init__(self, image, target):
        Actor.__init__(self, image, (100, 100))
        
        self._target = target

    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        self._velocity = (self._target.getPosition() - self._position).normalized()
        self._velocity *= self._maxVelocity

        #self._rotation = self._position.get_angle_between(self._target.getPosition())
        #self._rotate(0)

        self._updatePosition()


