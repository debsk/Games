import pygame 
from random import randint

def lixo_show():
    for i in range(100):
        espaco_lixo.append([randint(1,740), randint(-2500, 0 )])

def movimento_do_lixo():
    for i in range(len(espaco_lixo)):
        if espaco_lixo[i] != [0, 0]:
            espaco_lixo[i][1] += 1
            screen.blit(lixo, [espaco_lixo[i][0], espaco_lixo[i][1]])

def colisaolixoTiro(x, y, largura, altura):
    l = False
    for i in range (len(espaco_lixo)):
        if espaco_lixo[i] != [0,0]:
            if(x + largura > espaco_lixo[i][0] and x < espaco_lixo[i][0] + 60 
            and y + altura > espaco_lixo[i][1] and y < espaco_lixo[i][1] + 60):
                espaco_lixo[i] = [0,0]
                l = True
    return l 

    
def end():
    l = l1 = False 
    # lixo tocando no chao 
    for i in range (len(espaco_lixo)):
       if espaco_lixo[i][1] + 60 > 600:
           l = True

    #lixo tocando na nave
    if colisaolixoTiro(nave_x, 600, 120, 120 ) or l :
        l1 = True
    return l1


nave_x = 340 
muni   = [[0, 0], [0, 0], [0, 0]] 
tela   = pygame.image.load("imagens/tela800X600.png")
jato   = pygame.image.load("imagens/jato120X120.png")
tiro   = pygame.image.load("imagens/bala20X40.png")
lixo   = pygame.image.load("imagens/lixo60X60.png")
time   = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
espaco_lixo = []

lixo_show()

while True:  
    time.tick(60)
    event = pygame.event.poll()
    if event.type == pygame.QUIT: 
        break 

    # movimento em x com a nave
    tecla = pygame.key.get_pressed() # pressiona a nave 
    if tecla[pygame.K_RIGHT] == 1 and nave_x + 120 < 800:
        nave_x += 5
    if tecla[pygame.K_LEFT] == 1 and nave_x > 0:
        nave_x -= 5
    
    #tiro nave
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            for i in range(len(muni)):
                if muni[i] == [0, 0]:
                   muni[i] = [nave_x + 50, 450] # altura onde o tiro  sai da nave    
                   break
     
    # colisao com o tiro 
    for i in range(len(muni)):
        if muni[i] != [0, 0]:
            if colisaolixoTiro(muni[i][0], muni[i][1], 20, 40):
                muni[i] = [0, 0]
    # colisao tiro com a borda horzontal
    for i in range(len(muni)):
         if muni[i] != [0, 0]:
            if muni[i][1] < 0:
                muni[i] = [0, 0]
    
    
    screen.blit(tela, (0, 0))

    # movimento do lixo
    movimento_do_lixo()
    # movimento da bala 
    for i in range(len(muni)): 
        if muni[i] != [0, 0]:
            screen.blit(tiro, [muni[i][0], muni[i][1]])
            muni[i][1] -= 10

    screen.blit(jato,[nave_x, 480])

    pygame.display.flip()

    if end():
        break 