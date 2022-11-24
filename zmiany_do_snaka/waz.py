import pygame

pygame.init()
window = pygame.display.set_mode((1280, 720))

x = 0
y = 0


run = True
while run:
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    keys = pygame.key.get_pressed()

    speed = 5

    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    player = pygame.rect.Rect(x, y, 200, 20)



    window.fill((117, 217, 50))
    pygame.draw.rect(window, (128, 18, 224), player)
    pygame.display.update()
