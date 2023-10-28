import pygame
import random
class navio(pygame.sprite.Sprite):
    def __init__(self, x, y, cargo_type):
        pygame.sprite.Sprite.__init__(self)  # Inicializa a classe base

        # Carregue as imagens dos navios
        if cargo_type == "carvao":
            self.image = pygame.image.load("navio_carvao.png")

        elif cargo_type == "soda_caustica":
            self.image = pygame.image.load("navio_soda_caustica.png")
        elif cargo_type == "oleo_combustivel":
            self.image = pygame.image.load("navio_oleo_combustivel.png")
        self.image = pygame.transform.scale(self.image, (80, 80))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.cargo_type = cargo_type

cargo_type=['carvao', 'soda_caustica','oleo_combustivel']

# Agora você pode criar instâncias dos três tipos de navios
navio1 = navio(850, 600, random.choice(cargo_type))
navio2 = navio(1050, 600, random.choice(cargo_type))
navio3 = navio(1250, 600, random.choice(cargo_type))
navio4 = navio(1450,600, random.choice(cargo_type))
navio_group = pygame.sprite.Group()


navio_group = pygame.sprite.Group()
navio_group.add(navio1, navio2, navio3, navio4)

origem = [(100, 450), (300, 450), (500, 450),(700, 450)]
navio_velocidade =2

chegada = [(850, 600), (1050, 600), (1250, 600), (1450, 600)]

posicoes_disponiveis = chegada.copy()


def criar_navio_aleatorio():
    if not posicoes_disponiveis:
        return None
    # Escolha uma posição aleatória da lista de posições disponíveis
    x, y = random.choice(posicoes_disponiveis)
    cargo = random.choice(cargo_type)  # Tipo de carga aleatória
    novo_navio = navio(x, y, cargo)
    navio_group.add(novo_navio)

    # Remova a posição escolhida da lista de posições disponíveis, se estiver lá
    if (x, y) in posicoes_disponiveis:
        posicoes_disponiveis.remove((x, y))
#
# criar_navio_aleatorio()
#
