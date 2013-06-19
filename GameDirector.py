from MIDISequencer import MIDISequencer

from Laser import Laser
from Player import Player
from Enemy import Enemy

class GameDirector:
    def __init__(self, gameRound):
        self._gameRound = gameRound
        self._midiSequencer = None

    def load(self, midiPath):
        self._midiSequencer = MIDISequencer(None) #TODO: Not need for this argument
        self._midiSequencer.load(midiPath)

    def update(self, elapsedTimeSec):
        player = self._gameRound.getPlayer()

        notes = self._midiSequencer.update(elapsedTimeSec)
        for note in notes:
            #if note.getTrack() == 2:# and note.getNote() == 48:
            player.fire(0.2)

