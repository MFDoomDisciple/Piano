# Example file showing a basic pygame "game loop"
import pygame
import math
from array import array
import numpy as np
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1250, 720), pygame.RESIZABLE)
scale = 1.5
surface = pygame.Surface((1250/scale, 720/scale))
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

pygame.font.init()
font = pygame.font.SysFont(None, 35)

class Key:
    def __init__(self, note, texture, pos, key_char, key_code):
        self.texture = texture
        self.pos = pos
        self.black = texture == black_key
        self.key_code = key_code
        self.text_surface = font.render(key_char, True, (255, 255, 255) if self.black else (0,0,0)) # White text
        # freq = 65.41 * 2**(note/12)
        freq = 65.41 * 4 * 2**(note/12)
        max = 2**15 - 1
        size = sample_rate
        buf = np.zeros((size, 2), dtype=np.int16)
        self.sound = pygame.sndarray.make_sound(buf)
        buf = pygame.sndarray.samples(self.sound)
        volume = 0.25 * max * 65/freq
        wave = np.sin(2 * np.pi * freq * np.arange(size) / sample_rate) 
        for i in range(5):
            k = i * 2 + 3
            wave += np.sin(2 * np.pi * k* freq * np.arange(size) / sample_rate) / k

        buf[:, 0] = (volume * wave).astype(np.int16)
        buf[:, 1] =  (volume * wave).astype(np.int16)
        self.sound.set_volume(0)
        self.sound.play(loops = -1)
    def play(self, keys):
        if keys[self.key_code]:
            self.sound.set_volume(1)
        elif keys[pygame.K_SPACE]:
            self.sound.set_volume(max(0 ,self.sound.get_volume() - 0.01))
        else:
            self.sound.set_volume(0)
    def draw(self):
        dy = 0 if self.sound.get_volume() < 1 else 10
        surface.blit(self.texture, (self.pos[0], self.pos[1] + dy))
        surface.blit(self.text_surface, (self.pos[0] + (self.texture.get_width() - self.text_surface.get_width()) / 2, self.pos[1] + self.texture.get_height() - 35 + dy))

y = 150
piano_keys = [
    Key(0,c_f, (0,y), "Z", pygame.K_z),
    Key(1,black_key, (30,y), "S", pygame.K_s),
    Key(2,d_g_a, (40,y), "X", pygame.K_x),
    Key(3,black_key, (70,y), "D", pygame.K_d),
    Key(4,e_b, (80,y), "C", pygame.K_c),
    Key(5,c_f, (120,y), "V", pygame.K_v),
    Key(6,black_key, (150,y), "G", pygame.K_g),
    Key(7,d_g_a, (160,y), "B", pygame.K_b),
    Key(8,black_key, (190,y), "H", pygame.K_h),
    Key(9,d_g_a, (200,y), "N", pygame.K_n),
    Key(10,black_key, (230,y), "J", pygame.K_j),
    Key(11,e_b, (240,y), "M", pygame.K_m),
    Key(12,c_f, (280,y), ",", pygame.K_COMMA),
    Key(13,black_key, (310,y), "L", pygame.K_l),
    Key(14,d_g_a, (320,y), ".", pygame.K_PERIOD),
    Key(15,black_key, (350,y), ";", pygame.K_SEMICOLON),
    Key(16,e_b, (360,y), "/", pygame.K_SLASH),

    Key(17,c_f, (400,y), "Q", pygame.K_q),
    Key(18,black_key, (430,y), "2", pygame.K_2),
    Key(19,d_g_a, (440,y), "W", pygame.K_w),
    Key(20,black_key, (470,y), "3", pygame.K_3),
    Key(21,d_g_a, (480,y), "E", pygame.K_e),
    Key(22,black_key, (510,y), "4", pygame.K_4),
    Key(23,e_b, (520,y), "R", pygame.K_r),
    Key(24,c_f, (560,y), "T", pygame.K_t),
    Key(25,black_key, (590,y), "6", pygame.K_6),
    Key(26,d_g_a, (600,y), "Y", pygame.K_y),
    Key(27,black_key, (630,y), "7", pygame.K_7),
    Key(28,e_b, (640,y), "U", pygame.K_u),
    Key(29,c_f, (680,y), "I", pygame.K_i),
    Key(30,black_key, (710,y), "9", pygame.K_9),
    Key(31,d_g_a, (720,y), "O", pygame.K_o),
    Key(32,black_key, (750,y), "0", pygame.K_0),
    Key(33,d_g_a, (760,y), "P", pygame.K_p),
    Key(34,black_key, (790,y), "-", pygame.K_MINUS),
    Key(35,e_b, (800,y), "[", pygame.K_LEFTBRACKET),
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
    for key in piano_keys:
        key.play(keys)

    for key in piano_keys:
        if not key.black:
            key.draw()
    for key in piano_keys:
        if key.black:
            key.draw()
    pygame.transform.scale(surface,screen.get_size(), screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()