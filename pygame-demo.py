import pygame

pygame.init()

display_width = 27 * 8  # ekran boyutu
display_height = 27 * 9

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PacMan')

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
    gameDisplay.blit(rImg, (offset_x + x, offset_y + y))


def statikImg(img, x, y):
    gameDisplay.blit(img, (x, y))

u=0
j=0
c = 27
x = (offset_x + c)
y = (offset_y + c)
i = 0
x_change = 0
y_change = 0
yon = 0
score=0

while not crashed:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            x_change = 0
            y_change = 0
            if event.key == pygame.K_LEFT and y % c == 0:
                yon = 2
                x_change = - c
            elif event.key == pygame.K_RIGHT and y % c == 0:
                yon = 0
                x_change = c
            elif event.key == pygame.K_UP and x % c == 0:
                yon = 1
                y_change = - c
            elif event.key == pygame.K_DOWN and x % c == 0:
                yon = 3
                y_change = c
    # print(x,y)
    if (matris[int(y / c)][int((x - c) / c)]) != 1 and yon == 2:
        x += x_change
    elif (matris[int(y / c)][int((x + c) / c)]) != 1 and yon == 0:
        x += x_change
    elif (matris[int((y - c) / c)][int(x / c)]) != 1 and yon == 1:
        y += y_change
    elif (matris[int((y + c) / c)][int(x / c)]) != 1 and yon == 3:
        y += y_change

    gameDisplay.fill(white)
    a = 0
    b = 0
    for a in range(len(matris)):
        for b in range(len(matris[0])):
            if matris[a][b] == 1:
                statikImg(duvar, c * b, c * a)
            elif matris[a][b] == 0 :
                if a== y/c and b== x/c:
                    matris[a][b]= -1
                    u+=1
                    score+=100

                statikImg(yem, c * b, c * a)
    if i % 3 < 1:
        drawImg(kapaliImg, x, y)
    elif i % 3 < 2:
        drawImg(sag_ortaImg, x, y)
    else:
        drawImg(sag_acikImg, x, y)
    i += 1
    if u>j:
        print('Score:',score)
        j+=1
    pygame.display.update()
    if i == 3: i = 0
    clock.tick(5)

pygame.quit()
quit()
