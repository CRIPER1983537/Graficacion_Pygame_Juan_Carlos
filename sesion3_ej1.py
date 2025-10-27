import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movimiento Automático con Límites")

# Colores
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Rectángulo
rect_size = 50
rect_x = width // 2 - rect_size // 2
rect_y = height // 2 - rect_size // 2
rect_color = VERDE

# Velocidad y dirección automática
velocidad_x = random.choice([-4, -3, 3, 4])
velocidad_y = random.choice([-4, -3, 3, 4])

# Contador de frames en rojo
frames_rojo = 0
max_frames_rojo = 15  # Mantener rojo por 15 frames

# Contador de rebotes
rebotes = 0

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
            elif event.key == pygame.K_r:  # Reiniciar posición
                rect_x = width // 2 - rect_size // 2
                rect_y = height // 2 - rect_size // 2
                velocidad_x = random.choice([-4, -3, 3, 4])
                velocidad_y = random.choice([-4, -3, 3, 4])
                rebotes = 0
                rect_color = VERDE
                frames_rojo = 0
    
    # Movimiento automático
    rect_x += velocidad_x
    rect_y += velocidad_y
    
    # Verificar límites y cambiar dirección
    en_borde = False
    
    if rect_x <= 0:
        rect_x = 0
        velocidad_x = abs(velocidad_x)
        en_borde = True
        rebotes += 1
    elif rect_x >= width - rect_size:
        rect_x = width - rect_size
        velocidad_x = -abs(velocidad_x)
        en_borde = True
        rebotes += 1
    
    if rect_y <= 0:
        rect_y = 0
        velocidad_y = abs(velocidad_y)
        en_borde = True
        rebotes += 1
    elif rect_y >= height - rect_size:
        rect_y = height - rect_size
        velocidad_y = -abs(velocidad_y)
        en_borde = True
        rebotes += 1
    
    # Manejar cambio de color
    if en_borde:
        rect_color = ROJO
        frames_rojo = max_frames_rojo
    elif frames_rojo > 0:
        frames_rojo -= 1
        if frames_rojo == 0:
            rect_color = VERDE
    
    # Dibujar
    screen.fill(NEGRO)
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_size, rect_size))
    
    # Mostrar información
    font = pygame.font.Font(None, 36)
    info_text = font.render(f"Rebotes: {rebotes}", True, BLANCO)
    screen.blit(info_text, (10, 10))
    
    velocidad_text = font.render(f"Velocidad: ({velocidad_x}, {velocidad_y})", True, BLANCO)
    screen.blit(velocidad_text, (10, 50))
    
    posicion_text = font.render(f"Posición: ({rect_x}, {rect_y})", True, BLANCO)
    screen.blit(posicion_text, (10, 90))
    
    instrucciones = font.render("R: Reiniciar  ESC: Salir", True, BLANCO)
    screen.blit(instrucciones, (10, height - 40))
    
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()