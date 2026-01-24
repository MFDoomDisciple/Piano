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
pygame.mixer.set_num_channels(50)

(sample_rate, format, channels) = pygame.mixer.get_init()
print(pygame.mixer.get_init())
running = True

class Key:
    def __init__(self, note):
        # freq = 65.41 * 2**(note/12)
        freq = 65.41 * 4 * 2**(note/12)
        max = 2**15 - 1
        size = sample_rate
        buf = np.zeros((size, 2), dtype=np.int16)
        self.sound = pygame.sndarray.make_sound(buf)
        buf = pygame.sndarray.samples(self.sound)
        buf[:, 0] = (0.25 * max * np.sin(2 * np.pi * freq * np.arange(size) / sample_rate)).astype(np.int16)
        buf[:, 1] =  (0.25 * max * np.sin(2 * np.pi * freq * np.arange(size) / sample_rate)).astype(np.int16)
        self.sound.set_volume(0)
        self.sound.play(loops = -1)
    def play(self, play):
        if play:
            self.sound.set_volume(1)
        else:
            self.sound.set_volume(0)

piano_keys = [Key(i) for i in range(34)]

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
    piano_keys[0].play(keys[pygame.K_z]) # c note
    piano_keys[1].play(keys[pygame.K_s]) # c sharp
    piano_keys[2].play(keys[pygame.K_x]) # d note
    piano_keys[3].play(keys[pygame.K_d]) # d sharp
    piano_keys[4].play(keys[pygame.K_c]) # e note
    piano_keys[5].play(keys[pygame.K_v]) # f note
    piano_keys[6].play(keys[pygame.K_g]) # f sharp
    piano_keys[7].play(keys[pygame.K_b]) # g note
    piano_keys[8].play(keys[pygame.K_h]) # g sharp
    piano_keys[9].play(keys[pygame.K_n]) # a note
    piano_keys[10].play(keys[pygame.K_j]) # a sharp
    piano_keys[11].play(keys[pygame.K_m]) # b note
    piano_keys[12].play(keys[pygame.K_COMMA]) # c note
    piano_keys[13].play(keys[pygame.K_l]) # c sharp
    piano_keys[14].play(keys[pygame.K_PERIOD]) # d note
    piano_keys[16].play(keys[pygame.K_SLASH]) # e note

    piano_keys[17].play(keys[pygame.K_q]) # f note
    piano_keys[18].play(keys[pygame.K_2]) # f sharp
    piano_keys[19].play(keys[pygame.K_w]) # g note
    piano_keys[20].play(keys[pygame.K_3]) # g sharp
    piano_keys[21].play(keys[pygame.K_e]) # a note
    piano_keys[22].play(keys[pygame.K_4]) # a sharp
    piano_keys[23].play(keys[pygame.K_r]) # b note
    piano_keys[24].play(keys[pygame.K_t]) # c note
    piano_keys[25].play(keys[pygame.K_6]) # c sharp
    piano_keys[26].play(keys[pygame.K_y]) # d note
    piano_keys[27].play(keys[pygame.K_7]) # d sharp
    piano_keys[28].play(keys[pygame.K_u]) # e note
    piano_keys[29].play(keys[pygame.K_i]) # f note
    piano_keys[30].play(keys[pygame.K_9]) # f sharp
    piano_keys[31].play(keys[pygame.K_o]) # g note
    piano_keys[32].play(keys[pygame.K_0]) # g sharp
    piano_keys[33].play(keys[pygame.K_p]) # a note



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()