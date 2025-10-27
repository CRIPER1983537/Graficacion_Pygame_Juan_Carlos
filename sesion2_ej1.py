import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tablero de Ajedrez")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

# Tamaño del tablero y casillas
filas, columnas = 8, 8
tam_casilla = width // columnas

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
    screen.fill(GRIS)
    
    # Dibujar tablero de ajedrez
    for fila in range(filas):
        for columna in range(columnas):
            # Alternar colores
            if (fila + columna) % 2 == 0:
                color = BLANCO
            else:
                color = NEGRO
            
            # Dibujar casilla
            rect = pygame.Rect(
                columna * tam_casilla,
                fila * tam_casilla,
                tam_casilla,
                tam_casilla
            )
            pygame.draw.rect(screen, color, rect)
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()