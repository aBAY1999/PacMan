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


def drawImg(img, x, y):
    rImg = pygame.transform.rotate(img, 90 * yon)
    gameDisplay.blit(rImg, (x, y))


x = (display_width * 0.5-12)
y = (display_height * 0.5-12)
i=0
x_change = 0
y_change = 0
yon = 0;

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yon = 2;
                x_change = - 3
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                yon = 0;
                x_change = 3
                y_change = 0
            elif event.key == pygame.K_UP:
                yon = 1;
                y_change = - 3
                x_change = 0
            elif event.key == pygame.K_DOWN:
                yon = 3;
                y_change = 3
                x_change = 0
    x += x_change
    y+= y_change

    gameDisplay.fill(white)
    if i % 27 < 9:
        drawImg(kapaliImg, x, y)
    elif i % 27 < 18:
        drawImg(sag_ortaImg, x, y)
    else:
        drawImg(sag_acikImg, x, y)
    i+=1
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()