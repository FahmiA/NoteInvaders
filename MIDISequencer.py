import pygame
from pygame.locals import *
from pygame.compat import geterror

import midi

class MIDITrackSequencer:

    def __init__(self, track, resolution, defaultTempo):
        self._track = track
        self._resolution = resolution / 1000.0 # Ticks per Beat (TPM)

        self._tempo = 0 # Beats per Minute (BPM) 
        self._tickMs = 0 # MS duration of one tick
        self._delayMs = -1 # MS until next event

        self._setTempo(defaultTempo)
        self._index = 0 # Next event to look at after delayMS time
        self._totalTimeMs = 0

    def _setTempo(self, tempo):
        self._tempo = tempo

        microsecondsPerBeat = (60.0 * 1000000.0) / tempo
        self._tickMs = (microsecondsPerBeat / self._resolution) / 1000000.0

    def getTickMS(self):
        return self._tickMs

    def update(self, elapsedTimeMS):
        self._totalTimeMs += elapsedTimeMS
        firedEvents = []

        if self._index >= len(self._track):
            return firedEvents

        event = self._track[self._index]
        #print self._totalTimeMs
        while event and event.tick * self._tickMs < self._totalTimeMs:
            if event.name == 'Note On':
                #print str(event.tick * self._tickMs) + ' < ' + str(self._totalTimeMs)
                self._handleNoteOn(event, firedEvents)
            elif event.name == 'Note Off':
                self._handleNoteOff()
            elif event.name == 'Set Tempo':
                self._handleTempoChange(event)

            if self._index < len(self._track) - 1:
                self._index += 1
                event = self._track[self._index]
            else:
                event = None

        return firedEvents

    def _handleNoteOn(self, event, firedEvents):
        firedEvents.append(event)

    def _handleNoteOff(self):
        pass # TODO: Implement

    def _handleTempoChange(self, event):
        self._setTempo(event.get_bpm())
        print 'Tempo changed to: ' + event.get_bpm()
            
class Note:
    def __init__(self, note, track, durationSec):
        self._note = note
        self._track = track
        self._durationSec = durationSec

    def getNote(self):
        return self._note

    def getTrack(self):
        return self._track

    def getDurationSec(self):
        return self._durationSec

class MIDISequencer:

    def __init__(self, defaultTempo):
        self._defaultTempo = defaultTempo
        self._prevTimeMs = None # Time in Ms of last frame

    def load(self, midiPath):
        self._midiPattern = midi.read_midifile(midiPath)
        self._midiPattern.make_ticks_abs()
        self._index = 0

        # Load the tracks
        self._trackSequencers = []
        for i in range(1, len(self._midiPattern)):
            sequencer = MIDITrackSequencer(self._midiPattern[i], self._midiPattern.resolution, self._defaultTempo)
            self._trackSequencers.append(sequencer)

    def getElapsedRealTime(self):
        currentTimeMs = pygame.time.get_ticks()
        if self._prevTimeMs == None:
            self._prevTimeMs = currentTimeMs
        elapsedTimeMs = currentTimeMs - self._prevTimeMs
        self._prevTimeMs = currentTimeMs

        return elapsedTimeMs

    def update(self):
        elapsedTimeMs = self.getElapsedRealTime()

        firedNotes = []
        for i in range(0, len(self._trackSequencers)):
            trackEvents = self._trackSequencers[i].update(elapsedTimeMs)
            tickSec = self._trackSequencers[i].getTickMS() * 1000.0

            for event in trackEvents:
                note = Note(event.data[0], i, 0.2) # TODO: Look for note off event!!!
                firedNotes.append(note)

        return firedNotes
