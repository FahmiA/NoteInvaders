import os
import sys

import pygame
from pygame.locals import *
from pygame.compat import geterror

from Player import Player

# Check essential resources
if not pygame.font:
    print ('Warning, fonts disabled')
if not pygame.mixer:
    print ('Warning, sound disabled')

def load_image(name, colorkey=None):
    fullname = os.path.join('.', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image#, image.get_rect()

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

    # Create the player
    playerImage = load_image('media\\actors\\player_test.png')
    player = Player(playerImage)

    playerGroup = pygame.sprite.GroupSingle(player)

    # Start the game loop
    clock = pygame.time.Clock()
    elapsedTimeMs = 0
    elapsedTimeSec = 0
    going = True

    while going:
        elapsedTimeMs = clock.tick(60) # Limit to 60 frames per second
        elapsedTimeSec = 1.0 / elapsedTimeMs

        # Listen to window events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        playerGroup.update(elapsedTimeSec)

        # Render the game state
        screen.blit(background, (0, 0))
        playerGroup.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    # And we're off!
    pygame.init()

    main()

    pygame.quit()
