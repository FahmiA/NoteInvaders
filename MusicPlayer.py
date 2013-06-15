import pygame
from pygame.locals import *

class MusicPlayer:

    def __init__(self):
        pass

    def load(self, midiPath):
        freq = 44100 # audio CD quality
        bitsize = -16 # unsigned 16 bit
        channels = 2 # 1 is mono, 2 is stereo
        buffer = 1024 # number of samples

        pygame.mixer.init(freq, bitsize, channels, buffer)

        loadSuccess = False
        try:
            pygame.mixer.music.load(midiPath)
            loadSuccess = True
        except pygame.error:
            print 'Could not load MIDI file:', midiPath

        return loadSuccess

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def update(self, elapsedTimeSec):
        pass
