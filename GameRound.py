# Represents the game world for one round of game play:
#   From the birth to the death of the player.
#
# Concepts:
# - Manager Player
# - Manage and spawn enemies, including "orchestration"
# - Handle score
# - Handle background?

import pygame
from pygame.locals import *

import ContentManager
from Player import Player

class GameRound:

    def __init__(self):
        pass

    def load(self):
        self._player = Player(ContentManager.load_image('media\\actors\\player.png'))
        self._playerGroup = pygame.sprite.GroupSingle(self._player)

    def update(self, elapsedTimeSec):
        self._playerGroup.update(elapsedTimeSec)

    def draw(self, screen):
        self._playerGroup.draw(screen)

