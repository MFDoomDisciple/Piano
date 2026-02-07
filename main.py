# Example file showing a basic pygame "game loop"
import pygame
import math
from array import array
import numpy as np
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
scale = 1.5
surface = pygame.Surface((1280/scale, 720/scale))
clock = pygame.time.Clock()

pygame.mixer.init()
pygame.mixer.set_num_channels(50)

(sample_rate, format, channels) = pygame.mixer.get_init()
print(pygame.mixer.get_init())
running = True

c_f = pygame.image.load("c_f.png").convert_alpha()
d_g_a = pygame.image.load("d_g_a.png").convert_alpha()
e_b = pygame.image.load("e_b.png").convert_alpha()
black_key = pygame.image.load("black_key.png").convert_alpha()

class Key:
    def __init__(self, note, texture, pos):
        self.texture = texture
        self.pos = pos
        # freq = 65.41 * 2**(note/12)
        freq = 65.41 * 4 * 2**(note/12)
        max = 2**15 - 1
        size = sample_rate
        buf = np.zeros((size, 2), dtype=np.int16)
        self.sound = pygame.sndarray.make_sound(buf)
        buf = pygame.sndarray.samples(self.sound)
        volume = 0.25 * max * 65/freq
        buf[:, 0] = (volume * np.sin(2 * np.pi * freq * np.arange(size) / sample_rate)).astype(np.int16)
        buf[:, 1] =  (volume * np.sin(2 * np.pi * freq * np.arange(size) / sample_rate)).astype(np.int16)
        self.sound.set_volume(0)
        self.sound.play(loops = -1)
    def play(self, play):
        if play:
            self.sound.set_volume(1)
        else:
            self.sound.set_volume(0)
    def draw(self):
        surface.blit(self.texture, self.pos)

piano_keys = [
    Key(0,c_f, (0,50)),
    Key(1,black_key, (30,50)),
    Key(2,d_g_a, (40,50)),
    Key(3,black_key, (70,50)),
    Key(4,e_b, (80,50)),
    Key(5,c_f, (120,50)),
    Key(6,black_key, (150,50)),
    Key(7,d_g_a, (160,50)),
    Key(8,black_key, (190,50)),
    Key(9,d_g_a, (200,50)),
    Key(10,black_key, (230,50)),
    Key(11,e_b, (240,50)),
    Key(12,c_f, (280,50)),
    Key(13,black_key, (310,50)),
    Key(14,d_g_a, (320,50)),
    Key(15,black_key, (350,50)),
    Key(16,e_b, (360,50)),

    Key(17,c_f, (400,50)),
    Key(18,black_key, (430,50)),
    Key(19,d_g_a, (440,50)),
    Key(20,black_key, (470,50)),
    Key(21,d_g_a, (480,50)),
    Key(22,black_key, (510,50)),
    Key(23,e_b, (520,50)),
    Key(24,c_f, (560,50)),
    Key(25,black_key, (590,50)),
    Key(26,d_g_a, (600,50)),
    Key(27,black_key, (630,50)),
    Key(28,e_b, (640,50)),
    Key(29,c_f, (680,50)),
    Key(30,black_key, (710,50)),
    Key(31,d_g_a, (720,50)),
    Key(32,black_key, (750,50)),
    Key(33,d_g_a, (760,50)),
]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    surface.fill("purple")

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
    # piano_keys[29].play(keys[pygame.K_i]) # f note
    # piano_keys[30].play(keys[pygame.K_9]) # f sharp
    # piano_keys[31].play(keys[pygame.K_o]) # g note
    # piano_keys[32].play(keys[pygame.K_0]) # g sharp
    # piano_keys[33].play(keys[pygame.K_p]) # a note

    for key in piano_keys:
        key.draw()
    pygame.transform.scale(surface,(1280, 720), screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()