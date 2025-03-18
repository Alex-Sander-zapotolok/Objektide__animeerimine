import pygame
import sys

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")

clock = pygame.time.Clock()

taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    screen.blit(taust, (0, 0))
    screen.blit(punane_auto, (297.5, 391))
    pygame.display.flip()

pygame.quit()
sys.exit()