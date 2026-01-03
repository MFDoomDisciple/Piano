# Example file showing a basic pygame "game loop"
import pygame
import math
from array import array
import numpy as np
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mixer.init()

(sample_rate, format, channels) = pygame.mixer.get_init()
running = True

def gensound(note):
    freq = 65.41 * 2**(note/12)
    max = 2**15
    buf = np.zeros((sample_rate, 2), dtype=np.int16)
    sound = pygame.sndarray.make_sound(buf)
    buf = pygame.sndarray.samples(sound)
    buf[:, 0] = 0.25 * max * np.sin(2 * np.pi * freq * np.arange(sample_rate) / sample_rate)
    buf[:, 1] =  0.25 * max * np.sin(2 * np.pi * freq * np.arange(sample_rate) / sample_rate)
    return sound


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]:
        gensound(0).play() # c note
    if keys[pygame.K_x]:
        pass # d note
    if keys[pygame.K_c]:
        pass # e note
    if keys[pygame.K_v]:
        pass # f note
    if keys[pygame.K_b]:
        pass # g note
    if keys[pygame.K_n]:
        pass # a note
    if keys[pygame.K_m]:
        pass # b note
    if keys[pygame.K_COMMA]:
        pass # c note
    if keys[pygame.K_PERIOD]:
        pass # d note
    if keys[pygame.K_SLASH]:
        pass # e note
    if keys[pygame.K_s]:
        pass # c sharp note

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()