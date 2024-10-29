import pygame
import random
pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
by = SCREEN_HEIGHT/2 - 25
bx = SCREEN_WIDTH/2 - 25
ph = 150
pw = 50
px = 150
py = 465
px2 = 1770
py2 = 465
svx = 20 #random.randint(-15,15)
svy = random.randint(-5,5)
svs = 0
if svx < 5:
    svx = svx + 8
if svx > 0 and svx < svy:
    svs = svy
    svy = svx
    svx = svs
elif svx < 0 and svy < svx:
    svs = svy
    svy = svx
    svx = svs
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect((px, py, pw, ph))
player2 = pygame.Rect((px2, py2, pw, ph))
topborder = pygame.Rect((0,0,SCREEN_WIDTH,10))
lborder = pygame.Rect((0,0,10,SCREEN_HEIGHT))
rborder = pygame.Rect((1910,0,10,SCREEN_HEIGHT))
botborder = pygame.Rect((0,1070,SCREEN_WIDTH,10))
ball = pygame.Rect((bx,by,pw,pw))
screen.fill((0,0,0))

run = True

while run:
    px = player.x + 1/2 * pw
    py = player.y + 1/2 * pw
    key = pygame.key.get_pressed()
    if key[pygame.K_s] == True:
        player.move_ip(0,20)
    if key[pygame.K_w] == True:
        player.move_ip(0, -20)
    
    px2 = player2.x + 1/2 * pw
    py2 = player2.y + 1/2 * pw
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN] == True:
        player2.move_ip(0,20)
    if key[pygame.K_UP] == True:
        player2.move_ip(0, -20)

    bx = ball.x + 1/2 * pw
    by = ball.y + 1/2 * pw

    ball.move_ip(svx,svy)


    if ball.colliderect(player):
        if svx < 0:
            svx = svx * -1 + .2
        else:
            svx = svx * -1 - .2
        svy = svy + random.randint(-10,10)
    if ball.colliderect(player2):
        if svx < 0:
            svx = svx * -1 + .2
        else:
            svx = svx * -1 - .2
        svy = svy + random.randint(-10,10)
    if ball.colliderect(topborder):
        svy = svy * -1
    if ball.colliderect(botborder):
        svy = svy * -1
    if ball.colliderect(lborder):
        pygame.quit()
    if ball.colliderect(rborder):
        pygame.quit()
    
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), player)
    pygame.draw.rect(screen, (255,255,255), player2)
    pygame.draw.rect(screen, (0,0,0), topborder)
    pygame.draw.rect(screen, (0,0,0), botborder)
    pygame.draw.rect(screen, (0,0,0), lborder)
    pygame.draw.rect(screen, (0,0,0), rborder)
    pygame.draw.rect(screen, (255,255,255), ball)
    clock.tick(30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    print(svx)

    pygame.display.update()

pygame.quit()