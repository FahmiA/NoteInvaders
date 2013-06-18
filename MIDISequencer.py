import midi

class MIDITrackSequencer:

    def __init__(self, track, resolution):
        self._track = track
        self._resolution = resolution # Ticks per Beat (TPM)

        self._tempo = 0 # Beats per Minute (BPM) 
        self._tickMs = 0 # MS duration of one tick
        self._delayMs = -1 # MS until next event

        self._setTempo(120) # A reasonable default tempo
        self._index = 0 # Next event to look at after delayMS time

    def _setTempo(self, tempo):
        self._tempo = tempo

        microsecondsPerBeat = (60.0 * 1000000.0) / tempo
        self._tickMs = (microsecondsPerBeat / self._resolution) / 1000000.0

    def update(self, elapsedTimeSec):
        # TODO return note event(s) fired or an empty list
        firedEvents = []

        if self._index >= len(self._track):
            return firedEvents

        # TODO: Handle when elapsedTimeSec encompasses multiple events
        self._delayMs -= elapsedTimeSec
        if self._delayMs < 0:
            event = self._track[self._index]

            while event: # Get all events that occur now
                if event.name == 'Note On':
                    firedEvents.append(event)

                if self._index < len(self._track) and self._track[self._index].tick == 0:
                    self._index += 1
                    event = self._track[self._index]
                else:
                    event = None
                    self._delayMs = self._track[self._index].tick * self._tickMs

        return firedEvents
            


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

        for trackSequencer in self._trackSequencers:
            firedEvents = trackSequencer.update(elapsedTimeSec)

            for event in firedEvents:
                print str(elapsedTimeSec) + ': ' + event.name + ', ' + str(trackSequencer._index) + ', ' + str(len(trackSequencer._track))
