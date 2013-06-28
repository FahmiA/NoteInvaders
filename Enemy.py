import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Actor import Actor

class Enemy(Actor):

    def __init__(self, image, target):
        Actor.__init__(self, image, (100, 100), 50)
        
        self._target = target


    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        desiredVelocity = (self._target.getPosition() - self.getPosition()).normalized()
        desiredVelocity *= self._maxVelocity

        steering = desiredVelocity - self._velocity
        steering = self._truncate(steering, 8)
        steering = steering / 10

        self._velocity = self._truncate(self._velocity + steering, self._maxVelocity)

        rotation = self._velocity.get_angle() - 90
        self._rotate(rotation)

        self._updatePosition()


