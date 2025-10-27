import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trayectoria Circular")

# Colores
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Parámetros de la trayectoria circular
centro_x, centro_y = width // 2, height // 2
radio = 150
velocidad_angular = 0.02  # Radianes por frame
angulo = 0

# Rectángulo
rect_size = 40

# Bucle principal
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Calcular nueva posición en la trayectoria circular
    rect_x = centro_x + radio * math.cos(angulo) - rect_size // 2
    rect_y = centro_y + radio * math.sin(angulo) - rect_size // 2
    
    # Incrementar ángulo para el siguiente frame
    angulo += velocidad_angular
    
    # Dibujar
    screen.fill(NEGRO)
    
    # Dibujar el centro de la trayectoria
    pygame.draw.circle(screen, BLANCO, (centro_x, centro_y), 5)
    
    # Dibujar la trayectoria (círculo guía)
    pygame.draw.circle(screen, BLANCO, (centro_x, centro_y), radio, 1)
    
    # Dibujar el rectángulo
    pygame.draw.rect(screen, AZUL, (rect_x, rect_y, rect_size, rect_size))
    
    # Mostrar información
    font = pygame.font.Font(None, 36)
    info_text = font.render(f"Ángulo: {angulo:.2f} rad", True, BLANCO)
    screen.blit(info_text, (10, 10))
    
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()