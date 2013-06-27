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
from TextSprite import TextSprite
from MusicPlayer import MusicPlayer
from GameDirector import GameDirector

from Laser import Laser
from Player import Player
from Enemy import Enemy

class GameRound:

    START_LIVES = 3

    def __init__(self, noteWars, windowWidth, windowHeight):
        self._noteWars = noteWars
        self._windowWidth = windowWidth
        self._windowHeight = windowHeight

        self._enemiesGroup = pygame.sprite.Group()
        self._enemyDelaySec = 3.0
        self._enemyElapsedDelaySec = 0.0

        self._playerGroup = pygame.sprite.GroupSingle()
        self._projectilesGroup = pygame.sprite.Group()
        self._hudGroup = pygame.sprite.Group()

        self._score = 0
        self._lives = self.START_LIVES

    def load(self, songPath):
        # Load projectiles
        self._laser = Laser(ContentManager.load_image('media\\projectiles\\laser.png'))
        self._projectilesGroup.add(self._laser)

        # Load player
        self._player = Player(ContentManager.load_image('media\\actors\\player.png'), self._laser)
        self._playerGroup.add(self._player)

        # Load HUD
        self._font = ContentManager.load_font(36)
        self._scoreSprite = TextSprite(self._font, pygame.Color('black'), (30, 30))
        self._livesSprite = TextSprite(self._font, pygame.Color('black'), (30, 70))
        self._livesSprite.updateText('Lives: ' + str(self._lives))
        self._hudGroup.add(self._scoreSprite, self._livesSprite)

        # Load music configuration
        #midiPath = 'media\\music\\battlefield1942'
        #midiPath = 'media\\music\\morrowind_dance_mix'

        # Load game director
        self._gameDirector = GameDirector(self)
        self._gameDirector.load(self._player, songPath)

        # Load music
        self._musicPlayer = MusicPlayer()
        self._musicPlayer.load(songPath + '.mid')
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
        self._hudGroup.update(elapsedTimeSec)

        self._gameDirector.update(elapsedTimeSec)

    def stop(self):
        self._musicPlayer.stop()

    def _handlePlayerDeath(self):
        self._lives -= 1

        if self._lives < 0:
            self._gameDirector.stop()
            self._noteWars.goToMainMenu()
        else:
            self._livesSprite.updateText('Lives: ' + str(self._lives))
            self._enemiesGroup.empty()

    def _checkCollisions(self):
        # Check collisions between projectiles and enemies
        if self._laser.isFiring():
            collidedEnemies = pygame.sprite.spritecollide(self._laser, self._enemiesGroup, True, CollisionMethods.collideLineToRect)

            self._score += len(collidedEnemies) * 100
            self._scoreSprite.updateText('Score: ' + str(self._score))

        # Check collisions between player and enemies
        collidedEnemies = pygame.sprite.spritecollide(self._player, self._enemiesGroup, True, CollisionMethods.collideRectThenMask)
        if collidedEnemies:
            self._handlePlayerDeath()

    def draw(self, screen):
        self._projectilesGroup.draw(screen)
        self._playerGroup.draw(screen)
        self._enemiesGroup.draw(screen)

        [text.render() for text in self._hudGroup.sprites()]
        self._hudGroup.draw(screen)
