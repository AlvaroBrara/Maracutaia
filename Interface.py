import pygame
import sys
from Navios import*
largura, altura = 800, 600
FPS = 120
pygame.init()
# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview.png")
background = pygame.transform.scale(background, (largura, altura))

#música tema:
pygame.mixer.music.load('musica_tema.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


def venceu(pontuacao,vencer)->int:
    if pontuacao>=vencer:

        # Muda a música para a música de vitória
        pygame.mixer.music.stop()
        pygame.mixer.music.load('win_musica.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        # Define a fonte e renderiza o texto
        fonte_vitoria = pygame.font.Font(None, 48)
        texto_vitoria = fonte_vitoria.render("Você venceu!", True, (255, 255, 255))

        # Posiciona o texto no centro da tela
        texto_rect = texto_vitoria.get_rect(center=(largura / 2, altura / 2))

        # Desenha o texto na tela
        tela.blit(texto_vitoria, texto_rect)

        # Atualiza a tela
        pygame.display.flip()




def perdeu(pontuacao,perder)->int:
    if pontuacao<=perder:

        # Muda a música para a música de derrota
        pygame.mixer.music.stop()
        pygame.mixer.music.load('loss_musica.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        # Define a fonte e renderiza o texto
        fonte_derrota = pygame.font.Font(None, 48)
        texto_derrota = fonte_derrota.render("Você perdeu!", True, (255, 255, 255))

        # Posiciona o texto no centro da tela
        texto_rect = texto_derrota.get_rect(center=(largura / 2, altura / 2))

        # Desenha o texto na tela
        tela.blit(texto_derrota, texto_rect)

        # Atualiza a tela
        pygame.display.flip()




# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()

fonte = pygame.font.Font(None, 36)

def renderizar_pontuacao(pontuacao):
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, (255, 255, 255))
    tela.blit(texto_pontuacao, (10, 10))  # Ajuste as coordenadas conforme necessário
def Barra_Espera(navio,pontuacao, pausa):
    tamanho_da_barra = 100
    altura_da_barra = 25
    if not pausa:
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
        #print(f"Tempo_de_espera: {navio.tempo_de_espera}")
        navio.tempo_de_espera = max(navio.tempo_de_espera, 0)
        if navio.tempo_de_espera<=0 and not navio.pontos_contados:
            if navio.cargo_tipo == "carvao":
                pontuacao-=1*navio.ponto_carvao
            if navio.cargo_tipo == "soda_caustica":
                pontuacao-=1*navio.ponto_soda
            if navio.cargo_tipo == "oleo_combustivel":
                pontuacao-=1*navio.ponto_oleo
            navio.pontos_contados=True
        return pontuacao
    else:
        navio.tempo_de_espera += relogio.get_rawtime()*2/ 1000.0
        print(f"Tempo_de_espera: {navio.tempo_de_espera}")
        return pontuacao, navio.tempo_de_espera

def Barra_Descarga(navio,pontuacao,pausa):
    tamanho_da_barra = 100
    altura_da_barra = 25
    if not pausa:
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
        if navio.tempo_descarga <= 0 and not navio.pontos_contados:
            if navio.cargo_tipo == "carvao":
                pontuacao +=1*navio.ponto_carvao
            elif navio.cargo_tipo == "soda_caustica":
                pontuacao +=1* navio.ponto_soda
            elif navio.cargo_tipo == "oleo_combustivel":
                pontuacao +=1* navio.ponto_oleo
            navio.pontos_contados = True  # Marca os pontos como contados
        return pontuacao
