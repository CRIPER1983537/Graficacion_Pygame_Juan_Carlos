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

# Contador de frames
frame_count = 0
max_frames = 300

# Bucle principal
running = True
while running and frame_count < max_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Incrementar contador de frames
    frame_count += 1
    print(f"Frame: {frame_count}")
    
    # Rellenar la pantalla con el color de fondo
    screen.fill(background_color)
    
    # Actualizar la pantalla
    pygame.display.flip()

print("Programa terminado después de", frame_count, "frames")
# Salir de Pygame
pygame.quit()
sys.exit()