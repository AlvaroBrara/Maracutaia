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
            self.tempo_descarga_inicial = 5
            self.tempo_descarga = 5
            self.tempo_de_espera_inicial = 3  # tolerancia fixa
            self.tempo_de_espera = 3 # tolerancia que muda com o tempo passado
            self.ponto = 20
            self.tempo_de_atraso_inicial = 1
            self.tempo_de_atraso = 1
        elif tipo == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
            self.tempo_descarga_inicial = 4
            self.tempo_descarga = 4
            self.tempo_de_espera = 1
            self.tempo_de_espera_inicial = 1
            self.ponto = 10
            self.tempo_de_atraso_inicial = 3
            self.tempo_de_atraso = 3
        elif tipo == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")
            self.tempo_descarga_inicial = 7
            self.tempo_descarga = 7
            self.tempo_de_espera = 2
            self.tempo_de_espera_inicial = 2
            self.ponto=30
            self.tempo_de_atraso_inicial = 1
            self.tempo_de_atraso = 1
        self.image = pygame.transform.scale(self.image, (80, 100))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x_chegada, y_chegada)
        self.cargo_tipo = tipo
        self.chegou_destino = False

tipo=['carvao', 'soda_caustica','oleo_combustivel']
y_chegada = 450

navio_group = pygame.sprite.Group()
for navio in navio_group:
    navio_esperando = navio.copy()

#tem que ajeitar a movimentação bugada e teleportar o navio diretamente para a chegada
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
            move_x = dx // distancia * navio_velocidade
            move_y = dy // distancia * navio_velocidade

            colisao_com_berco = False
            for j, berco in enumerate(bercos_group):
                if navio.rect.colliderect(berco.rect):
                    if not bercos_ocupados[j]:
                        bercos_ocupados[j] = True
                        # Atualize o dicionário destino_disponivel
                        # destino_disponivel[(destino_x, destino_y)] = True  # Marque o destino como indisponível

                    else:
                        colisao_com_berco = True
                    break

            if not colisao_com_berco:
                new_x = atual_x + move_x
                new_y = atual_y + move_y
                navio.rect.center = (new_x, new_y)
        else:
            # Se outro navio já chegou ao destino ou a distância for zero, mantenha o navio na mesma posição
            navio.rect.center = (atual_x, atual_y)
            # navio.chegou_destino = True  # Marque que o navio chegou ao destino
            # Atualize o dicionário destino_disponivel
            # destino_disponivel[(destino_x, destino_y)] = False  # Marque o destino como indisponível

destino = [(100, y_chegada), (300, y_chegada), (500, y_chegada), (700, y_chegada)]
origem = [(850, 600), (1050, 600), (1250, 600), (1450, 600)]
navio_velocidade = 2
posicoes_de_inicio = origem.copy()
# destino_disponivel = {
#     (100, y_chegada): True,
#     (300, y_chegada): True,
#     (500, y_chegada): True,
#     (700, y_chegada): True
# }





def criar_navio_aleatorio():
    global posicoes_de_inicio, navio_group, tipo

    x, y = random.choice(posicoes_de_inicio)
    cargo = 'carvao'
    novo_navio = navio(x, y, cargo)

    # Adicione o navio ao grupo
    navio_group.add(novo_navio)


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
