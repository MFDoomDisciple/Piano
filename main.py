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
print(pygame.mixer.get_init())
running = True

def gensound(note):
    # freq = 65.41 * 2**(note/12)
    freq = 65.41 * 4 * 2**(note/12)
    max = 2**15
    buf = np.zeros((sample_rate, 2), dtype=np.int16)
    sound = pygame.sndarray.make_sound(buf)
    buf = pygame.sndarray.samples(sound)
    buf[:, 0] = (0.25 * max * np.sin(2 * np.pi * freq * np.arange(sample_rate) / sample_rate)).astype(np.int16)
    buf[:, 1] =  (0.25 * max * np.sin(2 * np.pi * freq * np.arange(sample_rate) / sample_rate)).astype(np.int16)
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
        gensound(2).play() # d note
    if keys[pygame.K_c]:
        gensound(4).play() # e note
    if keys[pygame.K_v]:
        gensound(5).play() # f note
    if keys[pygame.K_b]:
        gensound(7).play() # g note
    if keys[pygame.K_n]:
        gensound(9).play() # a note
    if keys[pygame.K_m]:
        gensound(11).play() # b note
    if keys[pygame.K_COMMA]:
        gensound(12).play() # c note
    if keys[pygame.K_PERIOD]:
        gensound(14).play() # d note
    if keys[pygame.K_SLASH]:
        gensound(16).play() # e note
    if keys[pygame.K_s]:
        gensound(1).play() # c sharp
    if keys[pygame.K_d]:
        gensound(3).play() # d sharp
    if keys[pygame.K_g]:
        gensound(6).play() # f sharp
    if keys[pygame.K_h]:
        gensound(8).play() # g sharp
    if keys[pygame.K_j]:
        gensound(10).play() # a sharp

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()