import pygame
from pygame.locals import *

from pgu import gui

import ContentManager

class MainMenu():

    def __init__(self):
        self._isVisible = False

    def show(self):
        self._isVisible = True

    def hide(self):
        self._isVisible = False

    def isVisible(self):
        return self._isVisible

    def load(self, noteWars):
        # Create the top level widget 
        self._app = gui.Desktop()
        self._app.connect(gui.QUIT, noteWars.quit)

        # Create a table to organise our menu
        #menuTable = gui.Table(align = -1, valign = -1)
        menuTable = gui.Table()

        # Add the title banner
        bannerImage = gui.Image('media\\menu\\NoteWarsLogo.png')
        menuTable.tr() # New table row
        menuTable.td(bannerImage)

        # Add author information
        aboutText = 'A game by Fahmi for WoGaDeMo 2013'
        aboutLabel = gui.Label(aboutText)
        menuTable.tr() # New table row
        menuTable.td(aboutLabel)

        # Add instruction information
        instText = 'Use WAD to move your ship. Your ship fires with the music. Your enemies spawn with the music'
        instLabel = gui.Label(instText)
        menuTable.tr() # New table row
        menuTable.td(instLabel)

        # Add button to play a song
        song1Button = gui.Button("Play Song 1")
        song1Button.connect(gui.CLICK, noteWars.goPlayGameRound, 'media\\music\\battlefield1942')
        menuTable.tr() # New table row
        menuTable.td(song1Button)

        # Add button to play a song
        song2Button = gui.Button("Play Song 2")
        song2Button.connect(gui.CLICK, noteWars.goPlayGameRound, 'media\\music\\morrowind_dance_mix')
        menuTable.tr() # New table row
        menuTable.td(song2Button)

        # Add button to quit
        quitButton = gui.Button("Quit Game")
        quitButton.connect(gui.CLICK, noteWars.quit)
        menuTable.tr() # New table row
        menuTable.td(quitButton)

        # Add out menu to the top level widget
        self._app.init(menuTable)

        # Signify that the main menu is visible
        self._isVisible = True

    def doEvent(self, event):
        if self._isVisible:
            self._app.event(event)

    def render(self):
        if self._isVisible:
            self._app.paint()
