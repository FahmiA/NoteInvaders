# Represents the game world for one round of game play:
#   From the birth to the death of the player.
#
# Concepts:
# - Manager Player
# - Manage and spawn enemies, including "orchestration"
# - Handle score
# - Handle background?

import random

import pygame
from pygame.locals import *

import ContentManager
import CollisionMethods
from MusicPlayer import MusicPlayer
from GameDirector import GameDirector

from Laser import Laser
from Player import Player
from Enemy import Enemy

class GameRound:

    def __init__(self, windowWidth, windowHeight):
        self._windowWidth = windowWidth
        self._windowHeight = windowHeight

        self._enemiesGroup = pygame.sprite.Group()
        self._enemyDelaySec = 3.0
        self._enemyElapsedDelaySec = 0.0

        self._playerGroup = pygame.sprite.GroupSingle()
        self._projectilesGroup = pygame.sprite.Group()

    def load(self):
        # Load projectiles
        self._laser = Laser(ContentManager.load_image('media\\projectiles\\laser.png'))
        self._projectilesGroup.add(self._laser)

        # Load player
        self._player = Player(ContentManager.load_image('media\\actors\\player.png'), self._laser)
        self._playerGroup.add(self._player)

        # Load music
        midiPath = 'media\\music\\morrowind_dance_mix'

        self._gameDirector = GameDirector(self)
        self._gameDirector.load(self._player, midiPath)

        self._musicPlayer = MusicPlayer()
        self._musicPlayer.load(midiPath + '.mid')
        self._musicPlayer.play()

    def spawnEnemy(self, enemy):
        spawnSide = int(random.uniform(0, 4))
        spawnDistance = random.random()
        spawnX = 0
        spawnY = 0

        if spawnSide == 0: # Left side
            spawnX = 0
            spawnY = self._windowHeight * spawnDistance
        elif spawnSide == 1: # Top side
            spawnX = self._windowWidth * spawnDistance
            spawnY = 0
        elif spawnSide == 2: # Right side
            spawnX = self._windowWidth
            spawnY = self._windowHeight * spawnDistance
        else: # Bottom side
            spawnX = self._windowWidth * spawnDistance
            spawnY = self._windowHeight

        enemy.setPosition((spawnX, spawnY))
        self._enemiesGroup.add(enemy)

    def update(self, elapsedTimeSec):
        self._enemyElapsedDelaySec += elapsedTimeSec

        if self._laser.isFiring():
            self._laser.add(self._projectilesGroup)
        else:
            self._laser.kill()

        self._checkCollisions()

        self._playerGroup.update(elapsedTimeSec)
        self._projectilesGroup.update(elapsedTimeSec)
        self._enemiesGroup.update(elapsedTimeSec)

        self._gameDirector.update(elapsedTimeSec)

    def _checkCollisions(self):
        # Check collisions between projectiles and enemies
        collidedEnemies = pygame.sprite.spritecollide(self._laser, self._enemiesGroup, True, CollisionMethods.collideLineToRect)

    def draw(self, screen):
        self._projectilesGroup.draw(screen)
        self._playerGroup.draw(screen)
        self._enemiesGroup.draw(screen)

