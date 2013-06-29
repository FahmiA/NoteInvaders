import pygame
from pygame.locals import *

from pgu import gui

import ContentManager

from HighScoreMenu import HighScoreMenu
from HighScoreDialog import HighScoreDialog

class MainMenu():

    def __init__(self, noteWars):
        self._noteWars = noteWars
        self._isVisible = False
        self._highScoreMenu = HighScoreMenu(self, noteWars)

    def show(self):
        self._isVisible = True

    def hide(self):
        self._isVisible = False

    def isVisible(self):
        return self._isVisible

    def load(self):
        # Create the top level widget 
        self._app = gui.Desktop()
        self._app.connect(gui.QUIT, self._noteWars.quit)

        # Create a table to organise our menu
        menuTable = gui.Table()

        # Add the title banner
        bannerImage = gui.Image('media/menu/NoteWarsLogo.png')
        menuTable.tr() # New table row
        menuTable.td(bannerImage)

        # Add author information
        sentenceWordLength = 10
        aboutText = 'A game by Fahmi for WoGaDeMo 2013'
        self._displayText(menuTable, aboutText, 10)

        # Add instruction information
        instText = 'Use WASD to move your ship and your mouse to aim. Your ship fires with the music. Your enemies spawn with the music'
        self._displayText(menuTable, instText, 10)

        # Add button to play a song
        song1Button = gui.Button("Play Song: Battlefield1942")
        song1Button.connect(gui.CLICK, self._noteWars.goPlayGameRound, 'media/music/battlefield1942')
        menuTable.tr() # New table row
        menuTable.td(song1Button)

        # Add button to play a song
        song2Button = gui.Button("Play Song: Morrowind Dance Mix")
        song2Button.connect(gui.CLICK, self._noteWars.goPlayGameRound, 'media/music/morrowind_dance_mix')
        menuTable.tr() # New table row
        menuTable.td(song2Button)

        # Add button to play a song
        song3Button = gui.Button("Play Song: Deus Ex Theme")
        song3Button.connect(gui.CLICK, self._noteWars.goPlayGameRound, 'media/music/Deus_Ex_Theme')
        menuTable.tr() # New table row
        menuTable.td(song3Button)

        # Add button to view high scores
        highScoresButton = gui.Button("High Scores")
        highScoresButton.connect(gui.CLICK, self.displayHighScores)
        menuTable.tr() # New table row
        menuTable.td(highScoresButton)

        # Add button to quit
        quitButton = gui.Button("Quit Game")
        quitButton.connect(gui.CLICK, self._noteWars.quit)
        menuTable.tr() # New table row
        menuTable.td(quitButton)

        # Add the menu to the top level widget
        self._app.init(menuTable)

        # Signify that the main menu is visible
        self._isVisible = True

    def _displayText(self, menuTable, text, sentenceWordLimit):
        words = text.split(' ')
        sentence = ''
        for i in range(0, len(words)):
            if i % sentenceWordLimit == 0:
                menuTable.tr()
                if i > 0:
                    menuTable.td(gui.Label(sentence))
                    sentence = ''

            sentence += words[i] + ' '

        menuTable.tr()
        menuTable.td(gui.Label(sentence))

    def displayHighScores(self):
        self._isVisible = False
        self._highScoreMenu.load()

    def addHighScore(self, songName, score, message):
        highScoreDialog = HighScoreDialog(self, songName, score, message)
        highScoreDialog.open()

    def doEvent(self, event):
        if self._isVisible:
            self._app.event(event)
        elif self._highScoreMenu.isVisible():
            self._highScoreMenu.doEvent(event)

    def render(self):
        if self._isVisible:
            self._app.paint()
        elif self._highScoreMenu.isVisible():
            self._highScoreMenu.render()
