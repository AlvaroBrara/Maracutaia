import pygame

class Berco(pygame.sprite.Sprite):
    def __init__(self, x_berco, y_berco, largura, altura, tipo):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((largura, altura), pygame.SRCALPHA)

        self.tipo = tipo  # Adicione o atributo 'tipo'

        if tipo == 'carvao':
            cor = (255, 0, 0, 128)  # Vermelho com transparência
        elif tipo == 'soda_caustica':
            cor = (0, 0, 255, 128)  # Azul com transparência
        elif tipo == 'oleo_combustivel':
            cor = (255, 255, 0, 128)  # Amarelo com transparência
        else:
            # Lógica para tipos desconhecidos (pode ser ajustada conforme necessário)
            cor = (100, 100, 100, 100)  # Cor padrão com transparência

        pygame.draw.rect(self.image, cor, (0, 0, largura, altura))

        self.rect = self.image.get_rect()
        self.rect.center = (x_berco, y_berco)

tipo=['carvao', 'soda_caustica','oleo_combustivel']
y_berco = 250

x_berco = [(100, 450), (300, 450), (500, 450),(700, 450)]

# Exemplo de criação de um berço retangular azul claro
largura_berco = 100  # Largura do berço
altura_berco = 40   # Altura do berço
berco1 = Berco(100,y_berco, largura_berco, altura_berco, 'carvao')
berco2 = Berco(300,y_berco, largura_berco, altura_berco, 'soda_caustica')
berco3 = Berco(500, y_berco, largura_berco, altura_berco,'oleo_combustivel')
berco4 = Berco(700, y_berco, largura_berco, altura_berco,'carvao')
# Crie um grupo de berços
bercos_group = pygame.sprite.Group()
bercos_group.add(berco1, berco2, berco3, berco4)

bercos_ocupados = [False, False, False, False]
