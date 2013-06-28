import sys

import pygame
from pygame.locals import *
from pygame.compat import geterror

from MainMenu import MainMenu

import ContentManager
from Player import Player
from GameRound import GameRound

# Check essential resources
if not pygame.font:
    print ('Warning, fonts disabled')
if not pygame.mixer:
    print ('Warning, sound disabled')

class NoteWars:

    def __init__(self):
        self._running = False
        self._currentSongName = ''
        self._mainMenu = MainMenu(self)
        self._gameRound = None

    def loadResources(self):
        # Create the screen
        self._screen = pygame.display.set_mode((1280, 720)) # 720p
        pygame.display.set_caption('Note Wars')

        # Create the bckground
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self._background.fill((0, 0, 0))

        # Load the main menu
        self._mainMenu.load()

        self._running = True

    def run(self):
        # Start the game loop
        clock = pygame.time.Clock()
        elapsedTimeMs = 0
        elapsedTimeSec = 0

        while self._running:
            elapsedTimeMs = clock.tick(60) # Limit to 60 frames per second
            elapsedTimeSec = 1.0 / elapsedTimeMs

            # Listen to window events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self._running = False
                else:
                    # The main menu will listen to the remaining events
                    self._mainMenu.doEvent(event)

            # Update the game state
            if self._gameRound:
                self._gameRound.update(elapsedTimeSec)

            # Render the game
            self._screen.blit(self._background, (0, 0))
            self._mainMenu.render()
            if self._gameRound:
                self._gameRound.draw(self._screen)

            # Show the new frame
            pygame.display.flip()

    def quit(self):
        self._running = False

    def goToMainMenuWithLose(self, score):
        self._gameRound.stop()
        self._gameRound = None
        self._mainMenu.show()

        self._mainMenu.addHighScore(self._currentSongName, score, 'You were killed :(')

    def goToMainMenuWithWin(self, score):
        self._gameRound.stop()
        self._gameRound = None
        self._mainMenu.show()

        self._mainMenu.addHighScore(self._currentSongName, score, 'You survived :)')

    def goPlayGameRound(self, songPath):
        self._currentSongName = songPath.split('/')[-1]
        self._currentSongName = self._currentSongName.replace('_', ' ')
        self._gameRound = GameRound(self, self._screen.get_width(), self._screen.get_height())
        self._gameRound.load(songPath)
        self._mainMenu.hide()


if __name__ == '__main__':
    # And we're off!
    pygame.init()

    noteWars = NoteWars()
    noteWars.loadResources()
    noteWars.run()

    pygame.quit()
