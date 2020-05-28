import pygame

BLACK, WHITE, BROWN = (0, 0, 0), (255, 255, 255), (139, 69, 19)
position = [0, 0]
x1, y1 = 380, 380
x2, y2 = 250, 260
pygame.init()
#audio = pygame.mixer.Sound("musica/colisão.ogg")
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Colisão")
clock = pygame.time.Clock()

while True:
    clock.tick(30)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    position[0], position[1] = x1, y1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y1 -= 10
        if event.key == pygame.K_DOWN:
            y1 += 10
        if event.key == pygame.K_RIGHT:
            x1 += 10
        if event.key == pygame.K_LEFT:
            x1 -= 10
    
    if ((x1 < x2 + 100) and (x1 + 40 > x2) 
    and (y1 < y2 + 80) and (y1 + 40 > y2)):
        #audio.play()
        x1, y1 = position[0], position[1]
    
    screen.fill(BROWN)
    pygame.draw.rect(screen, WHITE, [x2, y2, 100, 80])
    pygame.draw.rect(screen, BLACK, [x1, y1, 40, 40])
    pygame.display.flip()
