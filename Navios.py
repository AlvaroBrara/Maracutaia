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
            self.tempo_descarga = 1
            self.tolerancia = 10/FPS
        elif tipo == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
            self.tempo_descarga = 2
            self.tolerancia = 5/FPS
        elif tipo == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")
            self.tempo_descarga = 3
            self.tolerancia = 5/FPS

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

destino = [(100, y_chegada), (300, y_chegada), (500, y_chegada), (700, y_chegada)]
x_chegada = [destino_x for destino_x, _ in destino]
origem = [(850, 600), (1050, 600), (1250, 600), (1450, 600)]
navio_velocidade = 2

posicoes_disponiveis = origem.copy()


def criar_navio_aleatorio():
    global posicoes_disponiveis

    if not posicoes_disponiveis:
        # Se não houver posições disponíveis, saia da função
        return

    # Escolha uma posição aleatória da lista de posições disponíveis
    x, y = random.choice(posicoes_disponiveis)
    cargo = random.choice(tipo)  # Tipo de carga aleatória
    novo_navio = navio(x, y, cargo)

    # Movimentar_Navios()
    navio_group.add(novo_navio)

    # Remova a posição escolhida da lista de posições disponíveis, se estiver lá
    if (x, y) in posicoes_disponiveis:
        posicoes_disponiveis.remove((x, y))

    if not posicoes_disponiveis:
        return None


navio_selecionado = None
def verificar_cliques(navio):
    global navio_selecionado, y_chegada

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if navio.rect.collidepoint(mouse_x, mouse_y):
        # O jogador clicou em um navio
        if navio_selecionado is None:
            navio_selecionado = navio  # Defina o navio como selecionado
        else:
            navio_selecionado = None  # Desselecione o navio se ele já estava selecionado

    # Se o jogador clicou em um berço e um navio está selecionado, posicione o navio no centro do berço
    for i, berco in enumerate(bercos_group):
        if berco.rect.collidepoint(mouse_x, mouse_y) and navio_selecionado is not None:
            if not bercos_ocupados[i]:
                navio_selecionado.rect.center = berco.rect.center
                bercos_ocupados[i] = True  # Marque o berço como ocupado
                navio_selecionado = None
    if navio.rect.collidepoint(mouse_x, mouse_y):
        # O navio foi clicado, faça-o mais claro
        navio.image.set_alpha(150)  # Define a transparência do navio (valores entre 0 e 255)

    else:
        # O navio não foi clicado, retorne ao estado normal
        navio.image.set_alpha(255)  # Restaura a transparência do navio

