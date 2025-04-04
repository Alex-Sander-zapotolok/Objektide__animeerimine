import pygame, sys
pygame.init()


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]


screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()


ball = pygame.image.load("ball.png")


posX, posY = 0, 0
speedX = 3
speedY = 4

gameover = False
while not gameover:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True


    screen.blit(ball, (posX, posY))
    posX += speedX
    posY += speedY


    pygame.display.flip()
    screen.fill(lBlue)

pygame.quit()
sys.exit()
