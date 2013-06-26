import pygame
from pygame.locals import *

from pgu import gui

class MainMenu():

    def __init__(self):
        #self._menu = gui.Form()
        self._app = gui.App()
        self._app.connect(gui.QUIT, self._app.quit, None)

        container = gui.Table(align = -1, valign = -1)
        button = gui.Button("Yay")
        button.connect(gui.CLICK, self._app.quit)
        container.add(button, 100, 100)

        self._app.init(container)

    def doEvent(self, event):
        self._app.event(event)

    def render(self):
        self._app.paint()
