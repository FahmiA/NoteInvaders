import pygame
from pygame.locals import *

from Vec2d import Vec2d

from Actor import Actor
from Laser import Laser

class Player(Actor):

    def __init__(self, image, laser, position):
        Actor.__init__(self, image, position, 100)

        self._laser = laser

        self._rotationSpeed = 100 #Degrees per second
        self._fireDurationSec = 0

    def fire(self, durationSec):
        self._fireDurationSec = durationSec

    def update(self, elapsedTimeSec):
        Actor.update(self, elapsedTimeSec)

        # Handle mouse rotation
        mousePos = pygame.mouse.get_pos()
        angleToMouse = (Vec2d(mousePos) - self.getPosition()).get_angle() - 90
        self._rotate(angleToMouse)

        # Handle keyboard movement
        pressedKeys = pygame.key.get_pressed()
        self._velocity = Vec2d(0, 0)
        if pressedKeys[K_w]:
            self._velocity.y -= 1.0
        if pressedKeys[K_s]:
            self._velocity.y += 1.0
        if pressedKeys[K_a]:
            self._velocity.x -= 1.0
        if pressedKeys[K_d]:
            self._velocity.x += 1.0
        self._velocity = self._truncate(self._velocity * self._maxVelocity, self._maxVelocity)
        self._updatePosition()

        # Handle firing laser
        if self._fireDurationSec > 0:
            self._laser.fire(self.rect.center, self._rotation)
            self._fireDurationSec -= elapsedTimeSec
        else:
            self._laser.stop()

