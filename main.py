import pygame
import sys
from Navios import *
import random

pygame.init()

largura, altura = 800, 600
FPS = 60

# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("doca.png")
background = pygame.transform.scale(background, (largura, altura))


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()

navio_group = pygame.sprite.Group()
navio_group.add(navio1, navio2, navio3)

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for ship in navio_group:
                if ship.rect.collidepoint(mouse_x, mouse_y):
                    navio_group.remove(ship)


 # Move os navios em direção às posições de destino
    for i, navio in enumerate(navio_group):
        dest_x, dest_y = posição[i]
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

    navio_group.draw(tela)
    pygame.display.flip()
    tela.blit(background, (0, 0))
    relogio.tick(FPS)

