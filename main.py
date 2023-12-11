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
#fonte_tempo = pygame.font.Font(None, 36)  # Define a fonte para o tempo
# Loop principal do jogo
pausa = False
rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not pausa:
                for navio in navio_group:
                    cliques(navio)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pausa = not pausa


    # Verifique o estado do jogo:
    pausa = verificar_estado_jogo()

    if not pausa:
        tempo_atual += 1 / FPS


        # Inicializando o aparecimento de navios
        if tempo_atual > tempo_para_proximo_navio:
            if len(navio_group) != len(bercos_group):
                criar_navio_aleatorio()
                tempo_para_proximo_navio = tempo_atual + random.randint(tempo_minimo, tempo_maximo)

        Movimentar_Navios()
        navio_group.update()
        tela.blit(background, (0, 0))
        bercos_group.draw(tela)
        navio_group.draw(tela)

        for navio in navio_group:
            for destino_x, destino_y in destino:
                if (navio.rect.centerx, navio.rect.centery) == (destino_x, destino_y):
                    if navio.tempo_de_espera > 0:
                        Barra_Espera(navio)
                        gerenciaPontuacao(navio, None)
                    else:
                        gerenciaPontuacao(navio, None)
                        Barra_Atraso(navio)


            for berco in bercos_group:
                if navio.rect.colliderect(berco.rect):
                    Barra_Descarga(navio)
                    gerenciaPontuacao(navio, berco)
                    # Atualize a tela
                    for i, berco in enumerate(bercos_group): #cada i recebe a posição[i] e o berço, um nome
                        if pygame.sprite.collide_rect(navio, berco):
                            if not bercos_ocupados[i]:
                                if navio.rect.center in posicoes_de_inicio:
                                    bercos_ocupados[i] = True
                                    # Ajuste da espera e remoção do navio
                            navio.tempo_descarga -= 0.01
                            if navio.tempo_descarga <=0:
                                gerenciaPontuacao(navio, berco)
                                navio_group.remove(navio)
                                bercos_ocupados[i] = False



        # Renderiza a pontuação na tela
        exibir_pontuacao()
        verificar_estado_jogo()
        #print(pontuacao_total)
        pygame.display.flip()
        relogio.tick(FPS)
    else:
        relogio.tick(0)

# Finalização do Pygame e saída do programa
pygame.mixer.music.stop()
pygame.quit()
sys.exit()
