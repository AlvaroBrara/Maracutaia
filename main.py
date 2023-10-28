import pygame
import sys
from Navios import *
from Berços import *

pygame.init()

largura, altura = 800, 600
FPS = 60

# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview1.png")
background = pygame.transform.scale(background, (largura, altura))


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()



tempo_minimo = 15
tempo_maximo = 30
tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
tempo_atual = 0



# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tempo_atual += 1 / FPS  # Tempo desde o último quadro

    # Se o tempo atual ultrapassar o tempo para o próximo navio, crie um novo navio
    if tempo_atual >= tempo_para_proximo_navio:
        criar_navio_aleatorio()

        # Reinicie o temporizador para o próximo navio
        tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
        tempo_atual = 0
    for i, navio in enumerate(navio_group):
        # Use o operador de módulo para garantir que o índice esteja dentro dos limites da lista posição
        i = i % len(origem)
        dest_x, dest_y = origem[i]  # Use posicao em vez de posição
        current_x, current_y = navio.rect.center
        dx = dest_x - current_x
        dy = dest_y - current_y
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia > 0:
            # Calcule a quantidade a ser movida nesta iteração
            move_x = dx / distancia * navio_velocidade
            move_y = dy / distancia * navio_velocidade

            # Atualize a posição do navio
            new_x = current_x + move_x
            new_y = current_y + move_y
            navio.rect.center = (new_x, new_y)


    # Atualize os navios
    navio_group.update()

    # Renderize os navios e a tela de fundo
    tela.blit(background, (0, 0))
    navio_group.draw(tela)
    pygame.display.flip()

    relogio.tick(FPS)