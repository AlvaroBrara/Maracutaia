import pygame
import sys
from Navios import *
from Berços import *


pygame.init()

largura, altura = 1200, 600
FPS = 120

# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview.png")
background = pygame.transform.scale(background, (largura, altura))


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()



tempo_minimo = 0
tempo_maximo = 3
tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
tempo_atual = 0


# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Verifique se o botão esquerdo do mouse foi clicado
                for navio in navio_group:
                    verificar_cliques(navio)

    tempo_atual += 1 / FPS  # Tempo desde o último quadro
    #
    #Se o tempo atual ultrapassar o tempo para o próximo navio, crie um novo navio
    if tempo_atual >= tempo_para_proximo_navio:
        criar_navio_aleatorio()
       # Reinicie o temporizador para o próximo navio
        tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
        tempo_atual = 0

    if y_chegada != y_berco:
         Movimentar_Navios()

# Atualize os navios
    navio_group.update()

    # Renderize os navios e a tela de fundo
    tela.blit(background, (0, 0))
    bercos_group.draw(tela)
    navio_group.draw(tela)
    pygame.display.flip()

    relogio.tick(FPS)
