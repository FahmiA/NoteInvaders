import os
import sys

import pygame
from pygame.locals import *

# Check essential resources
if not pygame.font:
    print ('Warning, fonts disabled')
if not pygame.mixer:
    print ('Warning, sound disabled')

def main():
    # Create the screen
    screen = pygame.display.set_mode((1280, 720)) # 720p
    pygame.display.set_caption('Game Title TBD')

    # Create the bckground
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    # Display the background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Start the game loop
    clock = pygame.time.Clock()
    going = True

    while going:
        # Listen to window events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        # Update the game state

        # Render the gape state

        pygame.display.flip()


if __name__ == '__main__':
    # And we're off!
    pygame.init()

    main()

    pygame.quit()
