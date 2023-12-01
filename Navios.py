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
            self.tempo_descarga_inicial = 3
            self.tempo_descarga = 3
            self.tempo_de_espera_inicial = 10 #tolerancia fixa
            self.tempo_de_espera = 10 #tolerancia que muda com o tempo passado
        elif tipo == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
            self.tempo_descarga_inicial = 3
            self.tempo_descarga = 3
            self.tempo_de_espera = 5
            self.tempo_de_espera_inicial = 5
        elif tipo == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")
            self.tempo_descarga_inicial = 3
            self.tempo_descarga = 3
            self.tempo_de_espera = 7
            self.tempo_de_espera_inicial = 7


        self.image = pygame.transform.scale(self.image, (80, 100))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x_chegada, y_chegada)
        self.cargo_tipo = tipo
        # self.velocidade =2
tipo=['carvao', 'soda_caustica','oleo_combustivel']
y_chegada = 450
navio_group = pygame.sprite.Group()
navio_esperando = navio_group.copy()
navios_em_porto= pygame.sprite.Group()
velocidade_navio = 2

def criar_navio_aleatorio():
    global posicoes_de_inicio, navio_group, tipo

    x, y = random.choice(posicoes_de_inicio)
    cargo = random.choice(tipo)
    novo_navio = navio(x, y, cargo)

    # Adicione o navio ao grupo
    navio_group.add(novo_navio)


destinos_ocupados = [False, False, False, False]

navio_velocidade = 2
destino = [(100, y_chegada), (300, y_chegada), (500, y_chegada), (700, y_chegada)]
origem = [(850, 600)]
posicoes_de_inicio = origem.copy()

def Movimentar_Navios():
    global x_chegada, y_chegada, navio_velocidade, destinos_ocupados

    for i, navio in enumerate(navio_group):
        i = i % len(destino)
        destino_x, destino_y = destino[i]
        atual_x, atual_y = navio.rect.center
        dx = destino_x - atual_x
        dy = destino_y - atual_y
        distancia = ((dx ** 2) + (dy ** 2)) ** 0.5

        if distancia > 0:
            if not destinos_ocupados[i]:
                move_x = dx / distancia * navio_velocidade
                move_y = dy / distancia * navio_velocidade

                colisao_com_berco = False
                for j, berco in enumerate(bercos_group):
                    if navio.rect.colliderect(berco.rect):
                        if not bercos_ocupados[j]:
                            bercos_ocupados[j] = True
                        else:
                            colisao_com_berco = True
                        break

                if not colisao_com_berco:
                    new_x = atual_x + move_x
                    new_y = atual_y + move_y
                    navio.rect.center = (new_x, new_y)
        else:
            destinos_ocupados[i] = True

navio_selecionado = None
def cliques(navio):
    global navio_selecionado,destino

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
                destinos_ocupados[i] = False
                break  # Saia do loop, pois o navio foi movido para um berço
