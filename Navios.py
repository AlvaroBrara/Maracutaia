import pygame
import random
from Berços import *
class navio(pygame.sprite.Sprite):
    def __init__(self, x_chegada, y_chegada, tipo):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe base

        # Carregue as imagens dos navios
        if tipo == "carvao":
            self.image = pygame.image.load("navio_carvao.png")

        elif tipo == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
        elif tipo == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")

        self.image = pygame.transform.scale(self.image, (100, 100))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x_chegada, y_chegada)
        self.cargo_tipo = tipo
        self.movimento = Movimentar_Navios()
        # self.origem = origem
        # self.chegada = chegada
tipo=['carvao', 'soda_caustica','oleo_combustivel']
y_chegada = 600
# Agora você pode criar instâncias dos três tipos de navios
# navio1 = navio(850, 600, random.choice(tipo))
# navio2 = navio(1050, 600, random.choice(cargo_type))
# navio3 = navio(1250, 600, random.choice(cargo_type))
# navio4 = navio(1450,600, random.choice(cargo_type))
navio_group = pygame.sprite.Group()
#
#
# navio_group.add(navio1)
#
# y_berco = 250
# x_chegada = 1
# x_berco = 100
def Movimentar_Navios():
    global x_chegada, y_chegada
    for i, navio in enumerate(navio_group):
            # Use o operador de módulo para garantir que o índice esteja dentro dos limites da lista destino
            i = i % len(destino)
            destino_x, destino_y = destino[i]

            atual_x, atual_y = navio.rect.center
            dx = destino_x - atual_x
            dy = destino_y - atual_y
            distancia = ((dx ** 2) + (dy ** 2)) ** 0.5

            if distancia > 0:
                # Calcule a quantidade a ser movida nesta iteração
                move_x = dx / distancia * navio_velocidade
                move_y = dy / distancia * navio_velocidade

                # Atualize a posição do navio
                x_chegada[i] = atual_x + move_x
                y_chegada = atual_y + move_y
                navio.rect.center = (x_chegada, y_chegada)

                return x_chegada[i], y_chegada

    return None

destino = [(100, 450), (300, 450), (500, 450), (700, 450)]
x_chegada = [destino_x for destino_x, _ in destino]
origem = [(850, 600), (1050, 600), (1250, 600), (1450, 600)]
navio_velocidade = 2

posicoes_disponiveis = origem.copy()


def criar_navio_aleatorio():
    if not posicoes_disponiveis:
        return None
    # Escolha uma posição aleatória da lista de posições disponíveis
    x, y = random.choice(posicoes_disponiveis)
    cargo = random.choice(tipo)  # Tipo de carga aleatória
    novo_navio = navio(x, y, cargo)
    # Movimentar_Navios()
    navio_group.add(novo_navio)
    # Remova a posição escolhida da lista de posições disponíveis, se estiver lá
    if (x, y) in posicoes_disponiveis:
        posicoes_disponiveis.remove((x, y))


navio_selecionado = None
def verificar_cliques(navio):
    global  navio_selecionado, y_chegada

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if navio.rect.collidepoint(mouse_x, mouse_y):
        # O jogador clicou em um navio
        if navio_selecionado is None:
            navio_selecionado = navio  # Defina o navio como selecionado
        else:
            navio_selecionado = None  # Desselecione o navio se ele já estava selecionado

    # Se o jogador clicou em um berço e um navio está selecionado, posicione o navio no centro do berço
    for berco in bercos_group:
        if berco.rect.collidepoint(mouse_x, mouse_y) and navio_selecionado is not None:
            navio_selecionado.rect.center = berco.rect.center
            navio_selecionado = None
            y_chegada = y_berco


    if navio.rect.collidepoint(mouse_x, mouse_y):
        # O navio foi clicado, faça-o mais claro
        navio.image.set_alpha(150)  # Define a transparência do navio (valores entre 0 e 255)

    else:
        # O navio não foi clicado, retorne ao estado normal
        navio.image.set_alpha(255)  # Restaura a transparência do navio

