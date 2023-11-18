from Movimentação import*
from Interface import*
pygame.init()


#intervalo entre barcos
tempo_minimo = 0
tempo_maximo = 3
tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
tempo_atual = 0

# quantidade_atual =100
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
    print(tempo_atual)
    if tempo_atual >= tempo_para_proximo_navio:
        criar_navio_aleatorio()
        tempo_para_proximo_navio = random.randint(tempo_minimo, tempo_maximo)
        tempo_atual = 0

    Movimentar_Navios()

    # Desenhe os navios e as barras
    tela.blit(background, (0, 0))
    bercos_group.draw(tela)
    navio_group.draw(tela)
    decrimento = 1
    for navio in navio_group:
        for destino_x, destino_y in destino:
            if (navio.rect.centerx, navio.rect.centery) == (destino_x, destino_y):
                Barra_Espera(navio)

    for navio in navio_group:
        for berco in bercos_group:
            if navio.rect.colliderect(berco.rect):
                Barra_Descarga(navio)
    # Atualize a tela
    pygame.display.flip()

    # Controle de FPS
    relogio.tick(FPS)