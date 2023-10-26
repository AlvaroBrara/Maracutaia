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

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.cargo_type = cargo_type

cargo_type=['carvao', 'soda_caustica','oleo_combustivel']

# Agora você pode criar instâncias dos três tipos de navios
navio1 = navio(850, 600, random.choice(cargo_type))
navio2 = navio(1050, 600, random.choice(cargo_type))
navio3 = navio(1250, 600, random.choice(cargo_type))

navio_group = pygame.sprite.Group()

#
# def criar_navio(x, y, cargo_type):
#     novo_navio = random.choice(navio_group)
#     navio_group.add(novo_navio)

ship_spawn_time = pygame.time.get_ticks()
current_time = 10000

posição = [(200, 490), (400, 520), (600, 550)]
navio_velocidade =2




