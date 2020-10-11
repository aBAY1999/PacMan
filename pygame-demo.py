import pygame

pygame.init()

display_width = 800             #ekran boyutu
display_height = 500

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pacman')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
kapaliImg = pygame.image.load('res/kapali.png')
sag_ortaImg = pygame.image.load('res/sag_orta.png')
sag_acikImg = pygame.image.load('res/sag_acik.png')


def car(img, x, y):
    gameDisplay.blit(img, (x, y))


x = (display_width * 0.5-12)
y = (display_height * 0.5-12)
i=0
x_change = 0
y_change = 0
while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = - 3
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 3
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = - 3
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 3
                x_change = 0
    x += x_change
    y+= y_change

    gameDisplay.fill(white)
    if i % 18 < 6:
        car(kapaliImg, x, y)
    elif i % 18 < 12:
        car(sag_ortaImg, x, y)
    else:
        car(sag_acikImg, x, y)
    i+=1
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()