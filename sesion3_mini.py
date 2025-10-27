import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rastro de Movimiento Avanzado")

# Colores
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AMARILLO = (255, 255, 0)

# Rectángulo principal
rect_size = 40
rect_x = width // 2 - rect_size // 2
rect_y = height // 2 - rect_size // 2
velocidad = 5

# Sistema de rastro
rastro = []
max_rastro = 100
radio_circulo = 6
rastro_color = ROJO
modo_arcoiris = False

# Bucle principal
clock = pygame.time.Clock()
running = True

def color_arcoiris(progreso):
    """Genera un color del arcoíris basado en el progreso (0-1)"""
    r = int(255 * (1 - abs(progreso * 6 - 3) / 3))
    g = int(255 * (1 - abs(progreso * 6 - 2) / 3))
    b = int(255 * (1 - abs(progreso * 6 - 4) / 3))
    return (max(0, min(255, r)), max(0, min(255, g)), max(0, min(255, b)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_c:  # Limpiar rastro
                rastro.clear()
            elif event.key == pygame.K_r:  # Cambiar modo arcoíris
                modo_arcoiris = not modo_arcoiris
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                max_rastro = min(200, max_rastro + 10)
            elif event.key == pygame.K_MINUS:
                max_rastro = max(10, max_rastro - 10)
    
    # Obtener teclas presionadas
    keys = pygame.key.get_pressed()
    
    # Movimiento
    if keys[pygame.K_LEFT]:
        rect_x -= velocidad
    if keys[pygame.K_RIGHT]:
        rect_x += velocidad
    if keys[pygame.K_UP]:
        rect_y -= velocidad
    if keys[pygame.K_DOWN]:
        rect_y += velocidad
    
    # Verificar límites
    rect_x = max(0, min(rect_x, width - rect_size))
    rect_y = max(0, min(rect_y, height - rect_size))
    
    # Agregar posición actual al rastro
    centro_x = rect_x + rect_size // 2
    centro_y = rect_y + rect_size // 2
    rastro.append((centro_x, centro_y))
    
    # Limitar el tamaño del rastro
    if len(rastro) > max_rastro:
        rastro.pop(0)
    
    # Dibujar
    screen.fill(NEGRO)
    
    # Dibujar el rastro
    for i, (x, y) in enumerate(rastro):
        progreso = i / len(rastro) if len(rastro) > 0 else 0
        
        if modo_arcoiris:
            color = color_arcoiris(progreso)
        else:
            # Fade del color base
            alpha = int(255 * progreso)
            color = (min(255, rastro_color[0] * alpha // 255), 
                    min(255, rastro_color[1] * alpha // 255), 
                    min(255, rastro_color[2] * alpha // 255))
        
        radio = int(radio_circulo * (0.3 + 0.7 * progreso))
        pygame.draw.circle(screen, color, (x, y), radio)
    
    # Dibujar el rectángulo principal
    pygame.draw.rect(screen, VERDE, (rect_x, rect_y, rect_size, rect_size))
    pygame.draw.circle(screen, BLANCO, (centro_x, centro_y), 3)
    
    # Mostrar información
    font = pygame.font.Font(None, 24)
    info_lines = [
        f"Rastro: {len(rastro)}/{max_rastro}",
        "C: Limpiar rastro",
        "R: Modo arcoíris",
        "+/-: Ajustar tamaño rastro",
        "Flechas: Mover"
    ]
    
    for i, line in enumerate(info_lines):
        texto = font.render(line, True, BLANCO)
        screen.blit(texto, (10, 10 + i * 25))
    
    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()