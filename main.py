import pygame

pygame.init()

ventana_ancho = 1000
ventana_altura = 600

screen = pygame.display.set_mode((ventana_ancho, ventana_altura))
pygame.display.set_caption("ArgentinaKombat23")

run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False