import pygame
from pygame.locals import *

from MIDISequencer import MIDISequencer
from EnemyFactory import EnemyFactory

from Laser import Laser
from Player import Player
from Enemy import Enemy

class GameDirector:
    def __init__(self, gameRound):
        self._gameRound = gameRound
        self._midiSequencer = None
        self._track = 6

        self._enemyFactory = EnemyFactory()

    def load(self, player, midiPath):
        self._enemyFactory.load(player)
        self._midiSequencer = MIDISequencer(None) #TODO: Not need for this argument
        self._midiSequencer.load(midiPath)

    def update(self, elapsedTimeSec):
        player = self._gameRound.getPlayer()

        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_0]:
            self._track = 0
        if pressedKeys[K_1]:
            self._track = 1
        if pressedKeys[K_2]:
            self._track = 2
        if pressedKeys[K_3]:
            self._track = 3
        if pressedKeys[K_4]:
            self._track = 4
        if pressedKeys[K_5]:
            self._track = 5
        if pressedKeys[K_6]:
            self._track = 6
        if pressedKeys[K_7]:
            self._track = 7
        if pressedKeys[K_8]:
            self._track = 8
        if pressedKeys[K_9]:
            self._track = 9

        notes = self._midiSequencer.update()
        for note in notes:
            if note.getTrack() == self._track:# and note.getNote() == 48:
                player.fire(note.getDurationSec())

