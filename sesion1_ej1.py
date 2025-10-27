import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi primer programa gráfico")

# Color de fondo personalizado (verde)
background_color = (0, 255, 0)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Rellenar la pantalla con el color de fondo
    screen.fill(background_color)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()