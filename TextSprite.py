import pygame
from pygame.locals import *

class TextSprite(pygame.sprite.Sprite):

    def __init__(self, font, colour, position):
        pygame.sprite.Sprite.__init__(self)

        self._font = font
        self._colour = colour
        self._position = position
        self._text = 'Blank text'

        # The dirty flag indicates that the text has changed and the font must be re-rendered
        self._dirty = True

    def updateText(self, text):
        if text:
            self._text = text
            self._dirty = True

    def render(self):
        if self._dirty:
            self.image = self._font.render(self._text, True, self._colour)
            self.rect = self.image.get_rect()
            self.rect.topleft = self._position
            self._dirty = False
