import pygame

pygame.init()

display_width = 27*8  # ekran boyutu
display_height = 27*9

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pacman')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
kapaliImg = pygame.image.load('res/kapali.png')
sag_ortaImg = pygame.image.load('res/sag_orta.png')
sag_acikImg = pygame.image.load('res/sag_acik.png')
yem = pygame.image.load('res/yem.png')
duvar = pygame.image.load('res/duvar.png')

matris = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 1, 1, 0, 1],
          [1, 0, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 0, 1, 1, 1, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 0, 1, 1, 0, 1],
          [1, 0, 0, 0, 0, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1]]

offset_x = 0
offset_y = 0


def drawImg(img, x, y):
    rImg = pygame.transform.rotate(img, 90 * yon)
    gameDisplay.blit(rImg, (offset_x+x,offset_y+ y))


def statikImg(img, x, y):
    gameDisplay.blit(img, (x, y))


c = 27
x = (offset_x + c)
y = (offset_y + c)
i = 0
x_change = 0
y_change = 0
yon = 0

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            x_change = 0
            y_change = 0
            if event.key == pygame.K_LEFT:
                yon = 2
                x_change = - 3
            elif event.key == pygame.K_RIGHT:
                yon = 0
                x_change = 3
            elif event.key == pygame.K_UP:
                yon = 1
                y_change = - 3
            elif event.key == pygame.K_DOWN:
                yon = 3
                y_change = 3
    print(x,y)
    y += y_change
    x += x_change

    gameDisplay.fill(white)
    a = 0
    b = 0
    for a in range(len(matris)):
        for b in range(len(matris[0])):
            if matris[a][b] == 1:
                statikImg(duvar,c * b,c * a)
            elif matris[a][b] == 0:
                statikImg(yem,  c * b,  c * a)
    if i % 27 < 9:
        drawImg(kapaliImg, x, y)
    elif i % 27 < 18:
        drawImg(sag_ortaImg, x, y)
    else:
        drawImg(sag_acikImg, x, y)
    i += 1
    pygame.display.update()
    if i == 27: i = 0
    clock.tick(60)

pygame.quit()
quit()
