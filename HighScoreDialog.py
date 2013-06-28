import datetime

import pygame
from pygame.locals import *

from pgu import gui

class HighScoreDialog(gui.Dialog):

    def __init__(self, mainMenu, songName, score, message):
        self._mainMenu = mainMenu
        self._songName = songName
        self._score = score

        # Create the title
        titleLabel = gui.Label("Add your score")
        space = titleLabel.style.font.size(" ")

        # Create the document to put stuff in to
        width = 400
        height = 130
        document = gui.Document(width = width)

        # Create the description
        self._addText(message, space, document)

        # Create the user input label
        document.block(align = -1)
        userLabel = gui.Label('Name: ')
        document.add(userLabel)

        # Create the user input field
        self._userInput = gui.Input("Anonymous")
        document.add(self._userInput)

        # Add the Cancel button
        document.br(space[1])
        document.block(align = -1)
        cancelButton = gui.Button('Cancel')
        cancelButton.connect(gui.CLICK, self.close)
        document.add(cancelButton)

        # Add the Submit button
        submitButton = gui.Button('Submit')
        submitButton.connect(gui.CLICK, self._saveHighScore)
        document.add(submitButton)

        gui.Dialog.__init__(self, titleLabel, gui.ScrollArea(document, width, height))

    def _addText(self, text, space, document):
        document.block(align = -1)
        for word in text.split(' '):
            document.add(gui.Label(word))
            document.space(space)
        document.br(space[1])

    def _saveHighScore(self):
        userName = self._userInput.value
        self.close()
        with open('highscores.csv', 'a') as highScoresCSV:
            highScoresCSV.write('%s,%s,%d,%s\n' % (self._songName,
                                                 userName,
                                                 self._score,
                                                 datetime.date.today().isoformat()))
        self._mainMenu.displayHighScores()
