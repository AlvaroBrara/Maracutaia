import pygame
import sys
from Navios import *
from Berços import *
import pygame.font
from Interface import*
pygame.init()



tempo_minimo = 0
tempo_maximo = 3
tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
tempo_atual = 0

fonte = pygame.font.Font(None, 36)
# Loop principal do jogo
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for navio in navio_group:
                    verificar_cliques(navio)

    tempo_atual += 1 / FPS

    if tempo_atual >= tempo_para_proximo_navio:
        criar_navio_aleatorio()
        tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
        tempo_atual = 0

    indicenavio = 0
    Movimentar_Navios()

    navio_group.update()

    tela.blit(background, (0, 0))
    bercos_group.draw(tela)
    navio_group.draw(tela)

    for i, berco_ocupado in enumerate(bercos_ocupados):
        if berco_ocupado:
            for navio in navio_group:
                if navio.rect.collidepoint(navio.rect.center) and navio.tolerancia > 0:
                    # Desenha a barra de espera (retângulo colorido proporcional à tolerância)
                    pygame.draw.rect(tela, (0, 255, 0),
                                     [navio.rect.x, navio.rect.y - 10, int(navio.tolerancia * 10), 5])
                    navio.tolerancia -= 0.01  # Diminui a tolerância ao longo do tempo

                    # Adicione a exibição de texto indicando a tolerância
                    texto = fonte.render(f"Tolerância: {int(navio.tolerancia * 100)}%", True, (255, 255, 255))
                    tela.blit(texto, (navio.rect.x, navio.rect.y - 30))

    pygame.display.flip()

    relogio.tick(FPS)