import pygame
from fighter import Fighter

pygame.init()

#ventana del juego
ventana_ancho = 1000
ventana_altura = 600

ventana = pygame.display.set_mode((ventana_ancho, ventana_altura))
pygame.display.set_caption("ArgentinaKombat23")

#cargar imagen de fondo
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()


#funcion para llamar al fondo
def draw_bg():
    fondo_escalado = pygame.transform.scale(bg_image, (ventana_ancho, ventana_altura))
    ventana.blit(fondo_escalado, (0, 0))


#funcion para el personaje
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)



#game loop
run = True
while run:
    #llamar al fondo
    draw_bg()

    #llamar al personaje
    fighter_1.draw(ventana)
    fighter_2.draw(ventana)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

#exit pygame
pygame.quit()