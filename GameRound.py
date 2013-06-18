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
import CollisionMethods
from MusicPlayer import MusicPlayer
from MIDISequencer import MIDISequencer

from Laser import Laser
from Player import Player
from Enemy import Enemy

class GameRound:

    def __init__(self):
        self._enemiesGroup = pygame.sprite.Group()
        self._enemyDelaySec = 3.0
        self._enemyElapsedDelaySec = 0.0

        self._playerGroup = pygame.sprite.GroupSingle()
        self._projectilesGroup = pygame.sprite.Group()

        self._maxEnemies = 1 # TODO: For debugging only

    def load(self):
        # Load projectiles
        self._laser = Laser(ContentManager.load_image('media\\projectiles\\laser.png'))
        self._projectilesGroup.add(self._laser)

        # Load player
        self._player = Player(ContentManager.load_image('media\\actors\\player.png'), self._laser)
        self._playerGroup.add(self._player)

        # Load enemies
        self._enemyImage = ContentManager.load_image('media\\actors\\enemy_arrow.png')

        # Load music
        self._musicPlayer = MusicPlayer()
        self._musicPlayer.load('media\\music\\mary.mid')
        self._musicPlayer.play()

        self._midiSequencer = MIDISequencer(None)
        self._midiSequencer.load('python-midi-0.2.3/mary.mid')

    def update(self, elapsedTimeSec):
        self._enemyElapsedDelaySec += elapsedTimeSec

        if len(self._enemiesGroup) < self._maxEnemies and self._enemyElapsedDelaySec > self._enemyDelaySec:
            self._enemyElapsedDelaySec = 0.0
            enemy = Enemy(self._enemyImage, self._player)
            self._enemiesGroup.add(enemy)

        if self._laser.isFiring():
            self._laser.add(self._projectilesGroup)
        else:
            self._laser.kill()

        self._checkCollisions()

        self._playerGroup.update(elapsedTimeSec)
        self._projectilesGroup.update(elapsedTimeSec)
        self._enemiesGroup.update(elapsedTimeSec)

        self._midiSequencer.update(elapsedTimeSec)

    def _checkCollisions(self):
        # Check collisions between projectiles and enemies
        collidedEnemies = pygame.sprite.spritecollide(self._laser, self._enemiesGroup, True, CollisionMethods.collideLineToRect)

    def draw(self, screen):
        self._projectilesGroup.draw(screen)
        self._playerGroup.draw(screen)
        self._enemiesGroup.draw(screen)

