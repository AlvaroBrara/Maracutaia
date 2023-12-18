import os
from Interface import *
import pygame
import sys





def obter_nome_jogador():
    nome = input("Digite seu nome: ")
    return nome

def salvar_pontuacao_com_nome(nome, pontuacao, tempo_jogo):
    # Nome do arquivo que será usado para armazenar as pontuações
    arquivo_pontuacoes = "pontuacoes.txt"

    # Adiciona a nova pontuação ao arquivo
    with open(arquivo_pontuacoes, 'a') as file:
        # Escreve no arquivo no formato "nome, pontuacao, pontos, tempo em segundos"
        file.write(f"{nome},{pontuacao}:pontos, {tempo_jogo//1000}:segundos\n")



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
pontuacao_maxima = 20
pontuacao_minima = -100


def exibir_tempo(tempo_jogo):
    # Exibe o tempo na tela
    tempo_jogo += relogio.get_rawtime()
    texto_tempo = fonte.render(f"Tempo: {tempo_jogo // 1000}", True, (255, 255, 255))
    tela.blit(texto_tempo, (750, 10))
    return tempo_jogo
def verificar_estado_jogo():
    global rodando, pausa

    # texto_tempo = exibir_tempo()

    if pontuacao >= pontuacao_maxima or pontuacao <= pontuacao_minima:
        fonte_mensagem = pygame.font.Font(None, 46)  # Define a fonte para a mensagem
        if pontuacao >= pontuacao_maxima:
            mensagem = fonte_mensagem.render(f"Você venceu! Parabéns! Seu tempo é de: {pygame.time.get_ticks()//1000} segundos", True, (255, 255, 0))
            tela.blit(mensagem, (70, 350))  # Renderiza a mensagem na tela
            pygame.mixer.music.stop()  # Pára a música tema
            pygame.mixer.music.load('win_musica.mp3')  # Carrega a música de vitória
            pygame.mixer.music.set_volume(0.45)  # volume da música
            pygame.mixer.music.play()  # reproduzir a música em um loop infinito
        elif pontuacao <= pontuacao_minima:
            mensagem = fonte_mensagem.render(f"Você Perdeu! Que Peninha! Você durou: {pygame.time.get_ticks()//1000} segundos", True,
                                             (255, 0, 255))
            tela.blit(mensagem, (75, 300))  # Renderiza a mensagem na tela
            pygame.mixer.music.stop()  # Pára a música tema
            pygame.mixer.music.load('loss_musica.mp3')  # Carrega a música de vitória
            pygame.mixer.music.set_volume(0.45)
            pygame.mixer.music.play()  # reproduzir a música sem loop
        return True
    else:
        return False


