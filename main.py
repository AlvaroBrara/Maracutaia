import pygame
import sys
from Navios import *
from Berços import *
import pygame.font
from Interface import*
pygame.init()

# Variáveis de tempo
tempo_atual = 0
tempo_minimo = 0
tempo_maximo = 0
tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)

# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for navio in navio_group:
                    cliques(navio)

    tempo_atual += 1 / FPS

    if tempo_atual > tempo_para_proximo_navio:
        if len(navio_group) != len(bercos_group):
            criar_navio_aleatorio()  # Chama a função para criar um novo navio
            tempo_para_proximo_navio = tempo_atual + random.randint(tempo_minimo,tempo_maximo)  # Atualiza o tempo para o próximo navio

    indicenavio = 0
    Movimentar_Navios()
    navio_group.update()

    tela.blit(background, (0, 0))
    bercos_group.draw(tela)
    navio_group.draw(tela)

    for navio in navio_group:
        for destino_x, destino_y in destino:
            if (navio.rect.centerx, navio.rect.centery) == (destino_x, destino_y):
                Barra_Espera(navio)

        for berco in bercos_group:
            if navio.rect.colliderect(berco.rect):
                # repor_posicoes_disponiveis()
                Barra_Descarga(navio)

        #
        # # Atualize a tela
        # for i, berco in enumerate(bercos_group):
        #     if pygame.sprite.collide_rect(navio, berco):
        #         if not bercos_ocupados[i]:
        #             if navio.rect.center in posicoes_disponiveis:
        #                 posicoes_disponiveis.append(navio.rect.center)
        #                 bercos_ocupados[i] = True
        #
        #                 # repor_posicoes_disponiveis()
        #                 criar_navio_aleatorio()
        #                 # criar_navio_aleatorio()
        #
        #         # Ajuste da espera e remoção do navio
        #         navio.tempo_descarga -= 0.01
        #         if navio.tempo_descarga <= 0:
        #             navio_group.remove(navio)
        #             #navio.rect.center = origem[indicenavio]
        #             #navio.tempo_descarga = navio.tempo_descarga_inicial
        #             #indicenavio = (indicenavio + 1) % len(origem)
        #
        #             bercos_ocupados[i] = False
    if navio.tempo_descarga <= 0:
        navio_group.remove(navio)
    for indice, elemento in enumerate(posicoes_de_inicio):
        print(f"O elemento '{elemento}' está no índice {indice}")
    for indice, elemento in enumerate(navio_group):
        print(f"O elemento '{elemento}' está no índice {indice}")


    pygame.display.flip()
    relogio.tick(FPS)
# Finalização do Pygame e saída do programa
pygame.quit()
sys.exit()
