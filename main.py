from Navios import *
from Interface import*
pygame.init()

# Variáveis de tempo
tempo_atual = 0
tempo_minimo = 1
tempo_maximo = 3
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
    disponibilidade = destinos_ocupados.count(False)
    if tempo_atual > tempo_para_proximo_navio:
        if len(navio_group) != disponibilidade:
            criar_navio_aleatorio()  # Chama a função para criar um novo navio
            tempo_para_proximo_navio = tempo_atual + random.randint(tempo_minimo, tempo_maximo)  # Atualiza o tempo para o próximo navio
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
                Barra_Descarga(navio)

                # Atualize a tela
                for i, berco in enumerate(bercos_group):
                    if pygame.sprite.collide_rect(navio, berco):
                        if not bercos_ocupados[i]:
                            if navio.rect.center in posicoes_de_inicio:
                                bercos_ocupados[i] = True
                        if navio.tempo_descarga <= 0:
                            navio_group.remove(navio)
                            bercos_ocupados[i] = False
    print(disponibilidade)

    pygame.display.flip()
    relogio.tick(FPS)
# Finalização do Pygame e saída do programa
pygame.quit()
sys.exit()
