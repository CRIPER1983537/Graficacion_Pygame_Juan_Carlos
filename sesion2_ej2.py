import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Círculos Concéntricos")

# Colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MORADO = (255, 0, 255)

# Centro de la pantalla
centro_x, centro_y = width // 2, height // 2

# Lista de radios y colores
radios = [20, 40, 60, 80, 100]
colores = [ROJO, VERDE, AZUL, AMARILLO, MORADO]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Rellenar fondo
    screen.fill(NEGRO)
    
    # Dibujar círculos concéntricos
    for radio, color in zip(radios, colores):
        pygame.draw.circle(screen, color, (centro_x, centro_y), radio, 2)  # Grosor 2px
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()