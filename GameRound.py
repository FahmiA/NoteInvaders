# Represents the game world for one round of game play:
#   From the birth to the death of the player.

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
        self._hudGroup = pygame.sprite.Group()

        self._score = 0
        self._lives = self.START_LIVES

    def load(self, songPath):
        # Load projectiles
        self._laser = Laser(self._windowWidth * 1.5)

        # Load player
        self._playerSpawnPos = (self._windowWidth / 2, self._windowHeight / 2)
        self._player = Player(ContentManager.load_image('media/actors/player.png'), self._laser, self._playerSpawnPos)
        self._playerGroup.add(self._player)

        # Load HUD
        fontPath = 'media/fonts/freesansbold.ttf'
        self._font = ContentManager.load_font(fontPath, 36)
        self._scoreSprite = TextSprite(self._font, pygame.Color('white'), (30, 30))
        self._livesSprite = TextSprite(self._font, pygame.Color('white'), (30, 70))
        self._livesSprite.updateText('Lives: ' + str(self._lives))
        self._hudGroup.add(self._scoreSprite, self._livesSprite)

        # Load music configuration
        #songPath = 'media/music/battlefield1942'
        #songPath = 'media/music/test'

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

        # Check for collisions
        self._checkCollisions()

        # Update game entities
        self._playerGroup.update(elapsedTimeSec)
        self._enemiesGroup.update(elapsedTimeSec)
        self._hudGroup.update(elapsedTimeSec)

        # Invoke game director
        self._gameDirector.update(elapsedTimeSec)

        # Check whether the user wants to exit the game
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_BACKSPACE]:
            self._exitRound()

    def stop(self):
        self._musicPlayer.stop()
        self._gameDirector.stop()

    def _handlePlayerDeath(self):
        self._lives -= 1

        if self._lives < 0:
            self.stop()
            self._noteWars.goToMainMenuWithLose(self._score)
        else:
            self._livesSprite.updateText('Lives: ' + str(self._lives))
            self._enemiesGroup.empty()
            self._player.setPosition(self._playerSpawnPos)

    def roundComplete(self):
        self.stop()
        self._noteWars.goToMainMenuWithWin(self._score)

    def _exitRound(self):
        self.stop()
        self._noteWars.goToMainMenu()

    def _checkCollisions(self):
        # Check collisions between laser and enemies
        collidedEnemies = []
        if self._laser.isFiring():
            for enemy in self._enemiesGroup.sprites():
                if CollisionMethods.collideLineToRect(self._laser.getFiredFromPos(),
                                                      self._laser.getFiredToPos(),
                                                      enemy.rect):
                    collidedEnemies.append(enemy)

            self._score += len(collidedEnemies) * 100
            self._scoreSprite.updateText('Score: ' + str(self._score))

            for enemy in collidedEnemies:
                enemy.kill()

        # Check collisions between player and enemies
        collidedEnemies = pygame.sprite.spritecollide(self._player, self._enemiesGroup, True, CollisionMethods.collideRectThenMask)
        if collidedEnemies:
            self._handlePlayerDeath()

    def draw(self, screen):
        self._laser.draw(screen)
        self._playerGroup.draw(screen)
        self._enemiesGroup.draw(screen)

        [text.render() for text in self._hudGroup.sprites()]
        self._hudGroup.draw(screen)
