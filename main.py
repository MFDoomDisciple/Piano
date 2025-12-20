# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True




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
        pass # c note
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