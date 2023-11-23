import pygame
import random
from Berços import *
from Interface import *
class navio(pygame.sprite.Sprite):
    def __init__(self, x_chegada, y_chegada, tipo, ):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe base
        # Carregue as imagens dos navios
        if tipo == "carvao":
            self.image = pygame.image.load("navio_carvao.png")
            self.tempo_descarga_inicial = 10
            self.tempo_descarga = 10
            self.tempo_de_espera_inicial = 10 #tolerancia fixa
            self.tempo_de_espera = 10 #tolerancia que muda com o tempo passado
        elif tipo == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
            self.tempo_descarga_inicial = 10
            self.tempo_descarga = 10
            self.tempo_de_espera = 5
            self.tempo_de_espera_inicial = 5
        elif tipo == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")
            self.tempo_descarga_inicial = 10
            self.tempo_descarga = 10
            self.tempo_de_espera = 7
            self.tempo_de_espera_inicial = 7


        self.image = pygame.transform.scale(self.image, (80, 100))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x_chegada, y_chegada)
        self.cargo_tipo = tipo

tipo=['carvao', 'soda_caustica','oleo_combustivel']
y_chegada = 450
# Agora você pode criar instâncias dos três tipos de navios
# navio1 = navio(850, 600, random.choice(tipo))
# navio2 = navio(1050, 600, random.choice(cargo_type))
# navio3 = navio(1250, 600, random.choice(cargo_type))
# navio4 = navio(1450,600, random.choice(cargo_type))
navio_group = pygame.sprite.Group()
navio_esperando = navio_group.copy()
navios_em_porto= pygame.sprite.Group()
#
#
# navio_group.add(navio1)
#
# y_berco = 250
# x_chegada = 1
# x_berco = 100


def Movimentar_Navios():
    global x_chegada, y_chegada

    for i, navio in enumerate(navio_group): #compara num-navios com o numero de destinos disponíveis
        i = i % len(destino)
        destino_x, destino_y = destino[i]
        atual_x, atual_y = navio.rect.center
        dx = destino_x - atual_x
        dy = destino_y - atual_y
        distancia = ((dx ** 2) + (dy ** 2)) ** 0.5

        if distancia > 0:
            move_x = dx / distancia * navio_velocidade
            move_y = dy / distancia * navio_velocidade

            # Verifique a colisão com o berço atual e desative o movimento se houver colisão
            colisao_com_berco = False
            for j, berco in enumerate(bercos_group):
                if navio.rect.colliderect(berco.rect):
                    if not bercos_ocupados[j]:
                        bercos_ocupados[j] = True  # Marque o berço como ocupado

                    else:
                        colisao_com_berco = True
                    break

            if not colisao_com_berco:
                new_x = atual_x + move_x
                new_y = atual_y + move_y
                navio.rect.center = (new_x, new_y)


# def repor_posicoes_disponiveis():
#     global posicoes_disponiveis,navio_esperando
#
#     # Crie uma lista para armazenar as posições com navios
#     posicoes_com_navios = [navio.rect.center for navio in navio_esperando]
#
#     # Remova as posições de navios das posições disponíveis
#     posicoes_disponiveis = [posicao for posicao in posicoes_disponiveis if posicao not in posicoes_com_navios]

destino = [(100, y_chegada), (300, y_chegada), (500, y_chegada), (700, y_chegada)]
# x_chegada = [destino_x for destino_x, _ in destino]
origem = [(850, 600), (1050, 600), (1250, 600), (1450, 600)]
navio_velocidade = 2
posicoes_de_inicio = origem.copy()


def criar_navio_aleatorio():
    global posicoes_de_inicio, navio_group, tipo

    # for berco in bercos_ocupados:
    #     if berco == True:
    #         repor_posicoes_disponiveis()


    # if not posicoes_disponiveis:
    #     return  # Se não houver posições disponíveis, saia da função

    x, y = random.choice(posicoes_de_inicio)
    cargo = random.choice(tipo)
    novo_navio = navio(x, y, cargo)

    # Adicione o navio ao grupo
    navio_group.add(novo_navio)

    # # Remova a posição escolhida da lista de posições disponíveis, se estiver lá
    # if (x, y) in posicoes_disponiveis:
    #     posicoes_disponiveis.remove((x, y))







navio_selecionado = None
def cliques(navio):
    global navio_selecionado

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Verifica se o navio está no destino e se o mouse foi clicado
    for destino_x, destino_y in destino:
        if (navio.rect.collidepoint(mouse_x, mouse_y) and
                (navio.rect.centerx, navio.rect.centery) == (destino_x, destino_y) and
                pygame.mouse.get_pressed()[0]):
            # O jogador clicou em um navio no destino
            if navio_selecionado is None:
                navio_selecionado = navio  # Defina o navio como selecionado
                # Altere a transparência do navio selecionado
                navio_selecionado.image.set_alpha(150)
            else:
                navio_selecionado.image.set_alpha(255)  # Restaura a transparência do navio desselecionado
                navio_selecionado = None  # Desselecione o navio
            break  # Saia do loop, pois o navio está no destino e foi clicado

    # Se o jogador clicou em um berço e um navio está selecionado, posicione o navio no centro do berço
    for i, berco in enumerate(bercos_group):
        if berco.rect.collidepoint(mouse_x, mouse_y) and navio_selecionado is not None:
            if not bercos_ocupados[i]:
                navio_selecionado.rect.center = berco.rect.center
                bercos_ocupados[i] = True  # Marque o berço como ocupado
                navio_selecionado.image.set_alpha(255)  # Restaura a transparência do navio ao movê-lo para um berço
                navio_selecionado = None
                break  # Saia do loop, pois o navio foi movido para um berço
