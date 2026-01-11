import pygame
pygame.init()
red = (255, 0, 0)
black = (0, 0, 0)
width = 1000
height = 800
boxheight = 30
boxwidth = 30
screen = pygame.display.set_mode((width, height))
box_x = 0
box_y = 0
box_xchange = 0
box_ychange = 0

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                box_xchange -= 10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                box_xchange += 10
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                box_ychange -= 10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                box_ychange += 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                box_xchange = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                box_xchange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                box_ychange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                box_ychange = 0

    box_x += box_xchange
    box_y += box_ychange

    rect1 = pygame.Rect(box_x, box_y, boxwidth, boxheight)
    pygame.draw.rect(screen, red, rect1)
    pygame.display.update()
    screen.fill(black)
