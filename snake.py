import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

#colors 
WHITE   = (255, 255, 255)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)

screen  = pygame.display.set_mode((600, 600)) 

clock   = pygame.time.Clock()
snake_y = snake_x = 100
food_x  = randint(10, 580)//10 *10 
food_y  = randint(10, 580)//10 *10
snake   = [(100, 100), (110,100), (120, 100), (130, 100)]

RIGHT, LEFT, UP, DOWN = 0, 1 ,2 ,3
direct  = LEFT

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((BLACK))

    # movimento da cobra      
    if event.type == KEYDOWN:
        if event.key == K_RIGHT and direct != LEFT: # a condiçao a mais eh para a cobrar nao passar por dentro dela msm 
            direct = RIGHT
        if event.key == K_LEFT and  direct != RIGHT:
            direct = LEFT
        if event.key == K_UP and direct != DOWN:
            direct = UP
        if event.key == K_DOWN and direct != UP:
            direct = DOWN
    
    #colisao com a apple
    if snake[0][0] == food_x and snake[0][1] == food_y: 
        food_x = randint(10, 580)//10 *10 
        food_y = randint(10, 580)//10 *10
        snake.append((0,0))
    
    #movendo "corpo" da cobra 
    for i in range (len(snake)-1, 0, -1):
        snake[i] = snake[i - 1]
        
    # movimento da cobra (cabeça) 
    if direct == RIGHT :
        snake[0] = (snake[0][0] + 10, snake[0][1])
    elif direct == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif direct == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif direct == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    
    #colisao com a parede                     
    if  snake[0][0]  > 590 or snake[0][1]  > 590 or snake[0][0] < 10 or snake[0][1] + 10 < 10:
        break 

    #colisao com o corpo da cobra
    for i in range (1, len(snake)):
        if snake[0] == snake[i]: 
            pygame.quit()
            sys.exit()

    #desenho da cobra
    for posicao in snake:
        pygame.draw.rect(screen, WHITE, [posicao[0], posicao[1], 10, 10])
    
    pygame.draw.rect(screen, GREEN, [food_x, food_y, 10, 10])
    pygame.draw.rect(screen, BLUE, (0, 0, 10, 600))
    pygame.draw.rect(screen, BLUE, (0, 590, 600, 10))
    pygame.draw.rect(screen, BLUE, (590, 0, 10, 600))
    pygame.draw.rect(screen, BLUE, (0, 0, 600, 10))
    pygame.display.update()

    clock.tick(10)

   