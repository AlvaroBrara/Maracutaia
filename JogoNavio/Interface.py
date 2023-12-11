import pygame
import sys
from Navios import *

largura, altura = 900, 600
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
    if navio.tempo_de_atraso <= 0:
        navio.tempo_de_atraso = navio.tempo_de_atraso_inicial


pontuacao = 0


def gerenciaPontuacao(navio, berco):
    global pontuacao

    if navio.tempo_descarga <= 0:
        peso = 1  # Peso padrão

        if navio.cargo_tipo == 'carvao' and berco.tipo == 'carvao':
            peso = 2
        elif navio.cargo_tipo == 'carvao' and berco.tipo == 'soda_caustica':
            peso = 1
        elif navio.cargo_tipo == 'carvao' and berco.tipo == 'oleo_combustivel':
            peso = 0.5
        elif navio.cargo_tipo == 'soda_caustica' and berco.tipo == 'soda_caustica':
            peso = 1.5
        elif navio.cargo_tipo == 'soda_caustica' and berco.tipo == 'carvao':
            peso = 0.5
        elif navio.cargo_tipo == 'soda_caustica' and berco.tipo == 'oleo_combustivel':
            peso = 1
        elif navio.cargo_tipo == 'oleo_combustivel' and berco.tipo == 'carvao':
            peso = 0.25
        elif navio.cargo_tipo == 'oleo_combustivel' and berco.tipo == 'soda_caustica':
            peso = 1
        elif navio.cargo_tipo == 'oleo_combustivel' and berco.tipo == 'oleo_combustivel':
            peso = 1.5
        pontuacao_incremento = navio.ponto * peso
        pontuacao += pontuacao_incremento
        # print(pontuacao_incremento, pontuacao, peso)

    # Lógica para penalizar o atraso
    if navio.tempo_de_atraso <= 0.1:
        penalidade_atraso = navio.ponto // 10
        pontuacao -= penalidade_atraso

    return pontuacao


def exibir_pontuacao():
    # Exibe a pontuação na tela
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto_pontuacao, (10, 10))


# ---------------------PONTUAÇÃO DO JOGO--------------------------
pontuacao_maxima = 200
pontuacao_minima = -100


def verificar_estado_jogo():
    global rodando

    if pontuacao >= pontuacao_maxima or pontuacao <= pontuacao_minima:
        fonte_mensagem = pygame.font.Font(None, 46)  # Define a fonte para a mensagem
        if pontuacao >= pontuacao_maxima:
            mensagem = fonte_mensagem.render("Você venceu! Parabéns!", True, (255, 255, 255))
            tela.blit(mensagem, (300, 300))  # Renderiza a mensagem na tela
            pygame.mixer.music.stop()  # Pára a música tema
            pygame.mixer.music.load('win_musica.mp3')  # Carrega a música de vitória
            pygame.mixer.music.set_volume(0.45)  # volume da música
            pygame.mixer.music.play()  # reproduzir a música em um loop infinito
        elif pontuacao <= pontuacao_minima:
            mensagem = fonte_mensagem.render("Você perdeu! Tente novamente!", True, (255, 255, 255))
            tela.blit(mensagem, (200, 300))  # Renderiza a mensagem na tela
            pygame.mixer.music.stop()  # Pára a música tema
            pygame.mixer.music.load('loss_musica.mp3')  # Carrega a música de vitória
            pygame.mixer.music.set_volume(0.45)
            pygame.mixer.music.play()  # reproduzir a música sem loop
        return True
    else:
        return False
