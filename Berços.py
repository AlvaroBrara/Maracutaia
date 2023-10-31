import pygame

class Berco(pygame.sprite.Sprite):
    def __init__(self, x_berco, y_berco, largura, altura):
        pygame.sprite.Sprite.__init__(self)

        # Crie uma superfície retangular com a cor desejada (azul claro) e transparência
        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)
        cor_azul_claro = (173, 216, 230,)  # R, G, B, Alpha (transparência)
        pygame.draw.rect(self.image, cor_azul_claro, (0, 0, largura, altura))

        self.rect = self.image.get_rect()
        self.rect.center = (x_berco, y_berco)


y_berco = 250

x_berco = [(100, 450), (300, 450), (500, 450),(700, 450)]
# Exemplo de criação de um berço retangular azul claro
largura_berco = 100  # Largura do berço
altura_berco = 40   # Altura do berço
berco1 = Berco(100,y_berco, largura_berco, altura_berco)
berco2 = Berco(300,y_berco, largura_berco, altura_berco)
berco3 = Berco(500, y_berco, largura_berco, altura_berco)
berco4 = Berco(700, y_berco, largura_berco, altura_berco)
# Crie um grupo de berços
bercos_group = pygame.sprite.Group()
bercos_group.add(berco1, berco2, berco3, berco4)