import pygame
import sys
from Navios import*
largura, altura = 1200, 800
FPS = 120
pygame.init()
# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview.png")
background = pygame.transform.scale(background, (largura, altura))


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 36)

def Barra(navio):
    tamanho_da_barra = 100
    altura_da_barra = 25

    # Lógica para calcular o tamanho atual da barra azul
    tamanho_atual = int(tamanho_da_barra * (navio.tolerancia / navio.tolerancia_inicial))

    # Desenhar a barra branca (fundo)
    pygame.draw.rect(tela, (255, 255, 255), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra])

    # Desenhar a barra azul
    pygame.draw.rect(tela, (0, 0, 255), [navio.rect.x, navio.rect.y - 10, tamanho_atual, altura_da_barra])

    # Desenhar a borda
    pygame.draw.rect(tela, (0, 0, 0), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra], 2)

        # Adicione a exibição de texto indicando a tolerância
    texto = fonte.render(f"Tolerância: {max(0, int(navio.tolerancia))} D", True, (255, 255, 255))
    tela.blit(texto, (navio.rect.x, navio.rect.y - 30))

    # Reduza a tolerância com base no tempo decorrido (assumindo que o clock.tick já está sendo usado)
    navio.tolerancia -= relogio.get_rawtime() / 1000.0