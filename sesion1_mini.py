import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cambio de Color con Tecla C")

# Colores
color_blanco = (255, 255, 255)
color_azul = (0, 0, 255)
color_actual = color_blanco  # Color inicial

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_c:  # Tecla C
                # Cambiar entre blanco y azul
                if color_actual == color_blanco:
                    color_actual = color_azul
                    print("Color cambiado a azul")
                else:
                    color_actual = color_blanco
                    print("Color cambiado a blanco")
    
    # Rellenar la pantalla con el color actual
    screen.fill(color_actual)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()