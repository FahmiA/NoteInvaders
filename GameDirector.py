import json

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
        
        self._stopped = False

        self._enemyFactory = EnemyFactory()

    def load(self, player, songPath):
        self._player = player
        self._enemyFactory.load(player)

        with open(songPath + '.json', 'r') as songInfoJSON:
            self._songInfo = json.load(songInfoJSON)

        defaultTempo = float(self._songInfo.get('defaultTempo', 120)) # A reasonable default tempo
        self._midiSequencer = MIDISequencer(defaultTempo)
        self._midiSequencer.load(songPath + '.mid')

    def stop(self):
        self._stopped = True

    def update(self, elapsedTimeSec):
        if self._stopped:
            return

        pressedKeys = pygame.key.get_pressed()

        notes = self._midiSequencer.update()
        for noteEvent in notes:
            track = str(noteEvent.getTrack())
            note = noteEvent.getNote()

            # Player
            trackNotes = self._songInfo['playerFireEvents'].get(track, [])
            if note in trackNotes or -1 in trackNotes:
                self._player.fire(noteEvent.getDurationSec())

            # Enemy: Arrow
            arrowNotes = self._songInfo['arrowSpawnEvents'].get(track, [])
            if note in arrowNotes or -1 in arrowNotes:
                enemy = self._enemyFactory.createArrow()
                self._gameRound.spawnEnemy(enemy)

            toothNotes = self._songInfo['toothSpawnEvents'].get(track, [])
            if note in toothNotes or -1 in toothNotes:
                enemy = self._enemyFactory.createTooth()
                self._gameRound.spawnEnemy(enemy)

            vNotes = self._songInfo['vSpawnEvents'].get(track, [])
            if note in vNotes or -1 in vNotes:
                enemy = self._enemyFactory.createV()
                self._gameRound.spawnEnemy(enemy)
