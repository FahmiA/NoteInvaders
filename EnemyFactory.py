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

        self._enemyImageArrow = ContentManager.load_image('media\\actors\\enemy_arrow.png')
        self._enemyImageTooth = ContentManager.load_image('media\\actors\\enemy_tooth.png')
        self._enemyImageV = ContentManager.load_image('media\\actors\\enemy_v.png')

    def createArrow(self):
        enemy = Enemy(self._enemyImageArrow, self._player)
        return enemy

    def createTooth(self):
        enemy = Enemy(self._enemyImageTooth, self._player)
        return enemy

    def createV(self):
        enemy = Enemy(self._enemyImageV, self._player)
        return enemy
