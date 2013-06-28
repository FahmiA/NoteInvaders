import pygame
from pygame.locals import *

import ContentManager

from Enemy import Enemy

# TODO: Give enemies different behaviours (use the behaviour/command pattern).
class EnemyFactory:

    def __init__(self):
        pass

    def load(self, player):
        self._player = player

        self._enemy1Image= ContentManager.load_image('media\\actors\\enemy1.png')
        self._enemy2Image= ContentManager.load_image('media\\actors\\enemy2.png')
        self._enemy3Image = ContentManager.load_image('media\\actors\\enemy3.png')

    def createEnemy1(self):
        enemy = Enemy(50, self._enemy1Image, self._player)
        return enemy

    def createEnemy2(self):
        enemy = Enemy(60, self._enemy2Image, self._player)
        return enemy

    def createEnemy3(self):
        enemy = Enemy(70, self._enemy3Image, self._player)
        return enemy
