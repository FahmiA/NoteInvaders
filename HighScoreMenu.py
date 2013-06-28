import pygame
from pygame.locals import *

from pgu import gui

import ContentManager

class HighScoreMenu:
    def __init__(self, mainMenu, noteWars):
        self._mainMenu = mainMenu
        self._noteWars = noteWars
        self._isVisible = False

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
        highScoreTable = gui.Table()

        # Add the table header
        highScoreTable.tr()
        highScoreTable.td(gui.Label("Song"))
        highScoreTable.td(gui.Label("Name"))
        highScoreTable.td(gui.Label("Score"))
        highScoreTable.td(gui.Label("Date"))
        
        # Load high scores into table
        highScores = self._loadHighScores()
        for highScore in highScores:
            highScoreTable.tr()
            highScoreTable.td(gui.Label(highScore[0]))
            highScoreTable.td(gui.Label(highScore[1]))
            highScoreTable.td(gui.Label(str(highScore[2])))
            highScoreTable.td(gui.Label(highScore[3]))

        # Add a back button
        backButton = gui.Button("Return to main menu")
        backButton.connect(gui.CLICK, self._displayMainMenu)
        highScoreTable.tr() # New table row
        highScoreTable.td(backButton, colspan = 4)

        # Add the menu to the top level widget
        self._app.init(highScoreTable)

        # Signify that the high score menu is visible
        self._isVisible = True

    def _loadHighScores(self):
        highScores = []

        # Load high scores from file
        with open('highscores.csv', 'r') as highScoresCSV:
            for row in highScoresCSV:
                parts = row.split(',')
                songName = parts[0].strip()
                userName = parts[1].strip()
                score = int(parts[2].strip())
                date = parts[3].strip()
                highScores.append([songName, userName, score, date])

        # Sort by score in descending order
        highScores = sorted(highScores, key=lambda tuble:tuble[2], reverse = True)

        # Take the top 20 scores
        highScores = highScores[:20]
        
        # Return the high score
        return highScores

    def _displayMainMenu(self):
        self._isVisible = False
        self._mainMenu.show()

    def doEvent(self, event):
        if self._isVisible:
            self._app.event(event)

    def render(self):
        if self._isVisible:
            self._app.paint()
