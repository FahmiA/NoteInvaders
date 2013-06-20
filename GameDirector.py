from MIDISequencer import MIDISequencer

from Laser import Laser
from Player import Player
from Enemy import Enemy
import pygame
from pygame.locals import *

class GameDirector:
    def __init__(self, gameRound):
        self._gameRound = gameRound
        self._midiSequencer = None
        self._track = 0

    def load(self, midiPath):
        self._midiSequencer = MIDISequencer(None) #TODO: Not need for this argument
        self._midiSequencer.load(midiPath)

    def update(self, elapsedTimeSec):
        player = self._gameRound.getPlayer()

        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[K_e]:
            self._track -= 1
            print self._track
        if pressedKeys[K_r]:
            self._track += 1
            print self._track

        notes = self._midiSequencer.update()
        for note in notes:
            if note.getTrack() == self._track:# and note.getNote() == 48:
                player.fire(note.getDurationSec())

