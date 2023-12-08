import pygame
import sys
from Navios import *

largura, altura = 800, 600
FPS = 120
pygame.init()
# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview.png")
background = pygame.transform.scale(background, (largura, altura))

# música tema:
pygame.mixer.music.load('musica_tema.mp3')
pygame.mixer.music.set_volume(0.45)
pygame.mixer.music.play(-1)


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 36)


def Barra_Espera(navio):
    tamanho_da_barra = 100
    altura_da_barra = 25

    # Lógica para calcular o tamanho atual da barra azul
    tamanho_atual = int(tamanho_da_barra * (navio.tempo_de_espera / navio.tempo_de_espera_inicial))

    # Desenhar a barra branca (fundo)
    pygame.draw.rect(tela, (255, 255, 255), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra])

    # Desenhar a barra azul
    pygame.draw.rect(tela, (0, 0, 255), [navio.rect.x, navio.rect.y - 10, tamanho_atual, altura_da_barra])

    # Desenhar a borda
    pygame.draw.rect(tela, (0, 0, 0), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra], 2)

    # Adicione a exibição de texto indicando a tolerância
    texto = fonte.render(f"Espera: {max(0, int(navio.tempo_de_espera))} D", True, (255, 255, 255))
    tela.blit(texto, (navio.rect.x, navio.rect.y - 30))

    # Reduza a tolerância com base no tempo decorrido (assumindo que o clock.tick já está sendo usado)
    navio.tempo_de_espera -= relogio.get_rawtime() / 1000.0
    navio.tempo_de_espera = max(navio.tempo_de_espera, 0)

def Barra_Descarga(navio):
    tamanho_da_barra = 100
    altura_da_barra = 25
    # Lógica para calcular o tamanho atual da barra azul
    tamanho_atual = int(tamanho_da_barra * (navio.tempo_descarga / navio.tempo_descarga_inicial))
    # Desenhar a barra branca (fundo)
    pygame.draw.rect(tela, (255, 255, 255), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra])

    # Desenhar a barra azul
    pygame.draw.rect(tela, (0, 250, 0), [navio.rect.x, navio.rect.y - 10, tamanho_atual, altura_da_barra])

    # Desenhar a borda
    pygame.draw.rect(tela, (0, 0, 0), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra], 2)

    # Adicione a exibição de texto indicando o tempo de descarga
    texto = fonte.render(f"Descarga: {max(0, int(navio.tempo_descarga))} D", True, (255, 255, 255))
    tela.blit(texto, (navio.rect.x, navio.rect.y - 30))

    # Reduza o tempo de descarga com base no tempo decorrido (assumindo que o clock.tick já está sendo usado)
    navio.tempo_descarga -= relogio.get_rawtime() / 1000.0


def Barra_Atraso(navio):
    tamanho_da_barra = 100
    altura_da_barra = 25

    # Lógica para calcular o tamanho atual da barra azul
    tamanho_atual = int(tamanho_da_barra * (navio.tempo_de_atraso / navio.tempo_de_atraso_inicial))

    # Desenhar a barra branca (fundo)
    pygame.draw.rect(tela, (255, 255, 255), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra])

    # Desenhar a barra azul
    pygame.draw.rect(tela, (255, 255, 0), [navio.rect.x, navio.rect.y - 10, tamanho_atual, altura_da_barra])

    # Desenhar a borda
    pygame.draw.rect(tela, (0, 0, 0), [navio.rect.x, navio.rect.y - 10, tamanho_da_barra, altura_da_barra], 2)

    # Adicione a exibição de texto indicando a tolerância
    texto = fonte.render(f"Atraso: {max(0, int(navio.tempo_de_atraso))} D", True, (255, 255, 255))
    tela.blit(texto, (navio.rect.x, navio.rect.y - 30))

    # Reduza a tolerância com base no tempo decorrido (assumindo que o clock.tick já está sendo usado)
    navio.tempo_de_atraso -= relogio.get_rawtime() / 1000.0
    print(f"tempo de atraso: {navio.tempo_de_atraso}")
    if navio.tempo_de_atraso <= 0:
        navio.tempo_de_atraso = navio.tempo_de_atraso_inicial



pontuacao_total =0
pontuacao = 0


def gerenciaPontuacao(navio, berco):
    global pontuacao_total

    if navio.tempo_descarga <= 0:
        if hasattr(navio, 'tipo') and hasattr(berco, 'tipo'):
            pontuacao = navio.ponto * berco.ponto
        else:
            pontuacao = navio.ponto
        pontuacao_total = pontuacao

    # Lógica para penalizar o atraso
    if navio.tempo_de_atraso <= 0.1:
        penalidade_atraso = navio.ponto // 10
        pontuacao_total -= penalidade_atraso

    return pontuacao_total


def exibir_pontuacao():
    # Exibe a pontuação na tela
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao_total}", True, (255, 255, 255))
    tela.blit(texto_pontuacao, (10, 10))
