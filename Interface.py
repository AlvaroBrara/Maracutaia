import pygame
import sys

largura, altura = 1200, 800
FPS = 120

# tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Alocação de Berço")
background = pygame.image.load("Topview.png")
background = pygame.transform.scale(background, (largura, altura))


# Relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()
