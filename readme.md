import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
x_roxo = randint(50,600)
y_roxo = randint(50,420)
fonte = pygame.font.SysFont('comic sans', 35, True, True)
pontos = 0

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render (mensagem, True, (255,255,255), (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
    if pygame.key.get_pressed()[K_a]:
        if x > 0:
            x -= 30
    if pygame.key.get_pressed()[K_d]:
        if x < (largura - 60):
            x += 30
    if pygame.key.get_pressed()[K_w]:
        if y > 0:
            y -= 30
    if pygame.key.get_pressed()[K_s]:
        if y < (altura - 70):
            y += 30
          

    ret_roxo = pygame.draw.rect(tela,(150,0,200), (x_roxo,y_roxo,40,50))
    ret_vermelho = pygame.draw.rect(tela,(255,0,0),(x,y,40,50))

    if ret_vermelho.colliderect(ret_roxo):
        x_roxo = randint(50,600)
        y_roxo = randint(50,420)
        pontos += 1

    tela.blit(texto_formatado, (440,30))
    pygame.display.update()