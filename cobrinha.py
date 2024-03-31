import pygame 
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 700
height = 550
x = 0
y = 0
xm = randint(50,650)
ym = randint(50,500)
veloc = 10
p = 0
x_controle = veloc
y_controle = 0
fonte = pygame.font.SysFont('comic sans', 35, True, False)

tela = pygame.display.set_mode((width,height))
nome = pygame.display.set_caption('Cobrinha')
relogio = pygame.time.Clock()
lista_cobra = []
comp_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
  for xey in lista_cobra:
    pygame.draw.rect(tela,(50,255,0),(xey[0],xey[1], 30,30))

def reiniciar_jogo():
  global p, comp_inicial, x, y, xm, ym, lista_cabeça, lista_cobra, morreu
  p = 0
  comp_inicial = 5
  x = 0
  y = 0
  xm = randint(50,650)
  ym = randint(50,500)
  lista_cabeça = []
  lista_cobra = []
  morreu = False

while True:
    tela.fill((255,255,255))
    relogio.tick(25)
    texto = f'Pontos:{p}'
    formatado = fonte.render(texto, True, (0,0,0),(255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

    if event.type == KEYDOWN:
     if event.key == K_RIGHT:
       if x_controle == -veloc:
         pass
       else:
         if x < 670:
          x_controle = +veloc
          y_controle = 0
     if event.key == K_LEFT:
       if x_controle == veloc:
         pass
       else:
         if x > 5:
          x_controle = -veloc
          y_controle = 0
     if event.key == K_UP:
       if y_controle == veloc:
         pass
       else:
         if y > 5:
          x_controle = 0
          y_controle = -veloc
     if event.key == K_DOWN:
       if y_controle == -veloc:
         pass
       else:
         if y < 520:
          x_controle = 0
          y_controle = +veloc
    x += x_controle
    y += y_controle

    cobra = pygame.draw.rect(tela,(50,255,0),(x,y,30,30))
    maçã = pygame.draw.rect(tela,(255,0,0),(xm,ym,20,20))

    if cobra.colliderect(maçã):
       xm = randint(50,650)
       ym = randint(50,500)
       p += 1
       comp_inicial += 1


    lista_cabeça = []
    lista_cabeça.append(x)
    lista_cabeça.append(y)
    lista_cobra.append(lista_cabeça)


    if lista_cobra.count(lista_cabeça) > 1:
      fonte2 = pygame.font.SysFont('comic sans', 20, True, True)
      mensagem = 'GAME OVER! Pressione a tecla A para jogar novamente.'
      texto_formatado = fonte2.render(mensagem, True, (0,0,0))
      ret_texto = texto_formatado.get_rect()
      morreu = True
      while morreu:
        tela.fill((255,255,255))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            quit()
          if event.type == KEYDOWN:
            if event.key == K_a:
              reiniciar_jogo()

        ret_texto.center = (width//2,height//2)
        tela.blit(texto_formatado, ret_texto)
        pygame.display.update()

    if x > width:
      x = 0
    if x < 0:
      x = width
    if y < 0:
      y = height
    if y > height:
      y = 0


    if len(lista_cobra) > comp_inicial:
       del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    tela.blit(formatado,(500,30))
    pygame.display.update()

