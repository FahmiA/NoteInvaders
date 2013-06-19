import midi

class MIDITrackSequencer:

    def __init__(self, track, resolution):
        self._track = track
        self._resolution = resolution / 4000.0 # Ticks per Beat (TPM)

        self._tempo = 0 # Beats per Minute (BPM) 
        self._tickMs = 0 # MS duration of one tick
        self._delayMs = -1 # MS until next event

        self._setTempo(120) # A reasonable default tempo
        self._index = 0 # Next event to look at after delayMS time

    def _setTempo(self, tempo):
        self._tempo = tempo

        microsecondsPerBeat = (60.0 * 1000000.0) / tempo
        self._tickMs = (microsecondsPerBeat / self._resolution) / 1000000.0
        #print 'Tempo:', self._tickMs

    def getTickMS(self):
        return self._tickMs

    def update(self, elapsedTimeMS):
        # TODO return note event(s) fired or an empty list
        firedEvents = []

        if self._index >= len(self._track):
            return firedEvents

        # TODO: Handle when elapsedTimeMS encompasses multiple events
        self._delayMs -= elapsedTimeMS
        if self._delayMs <= 0:
            event = self._track[self._index]

            # Get all events tkat occur now
            while event:
                if event.name == 'Note On':
                    firedEvents.append(event)

                event = None
                if self._index < len(self._track) - 1:
                    if self._track[self._index].tick < elapsedTimeMS:
                        self._index += 1
                        event = self._track[self._index]
                    else:
                        self._delayMs = self._track[self._index].tick * self._tickMs
                        #print self._delayMs
                        self._index += 1


        return firedEvents
            
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

    def __init__(self, gameDirector):
        self._gameDirector = gameDirector

    def load(self, midiPath):
        self._midiPattern = midi.read_midifile(midiPath)
        self._index = 0

        # Load the tracks
        self._trackSequencers = []
        for i in range(1, len(self._midiPattern)):
            sequencer = MIDITrackSequencer(self._midiPattern[i], self._midiPattern.resolution)
            self._trackSequencers.append(sequencer)

    def update(self, elapsedTimeSec):

        elapsedTimeMS = elapsedTimeSec * 1000.0
        firedNotes = []
        for i in range(0, len(self._trackSequencers)):
            trackEvents = self._trackSequencers[i].update(elapsedTimeMS)
            tickSec = self._trackSequencers[i].getTickMS() * 1000.0

            for event in trackEvents:
                note = Note(event.data[0], i, event.tick * tickSec) # TODO: Look for note off event!!!
                firedNotes.append(note)

        return firedNotes
