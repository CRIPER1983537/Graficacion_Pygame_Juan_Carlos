import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Casa con Cambio de Colores")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
MARRON = (139, 69, 19)
GRIS = (128, 128, 128)

# Color inicial de la casa
color_casa = ROJO

# Posiciones y dimensiones de la casa
casa_x, casa_y = 300, 300
ancho_casa, alto_casa = 200, 150

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:  # Tecla R - Rojo
                color_casa = ROJO
                print("Color cambiado a ROJO")
            elif event.key == pygame.K_b:  # Tecla B - Azul
                color_casa = AZUL
                print("Color cambiado a AZUL")
            elif event.key == pygame.K_g:  # Tecla G - Verde
                color_casa = VERDE
                print("Color cambiado a VERDE")
            elif event.key == pygame.K_y:  # Tecla Y - Amarillo
                color_casa = AMARILLO
                print("Color cambiado a AMARILLO")
    
    # Rellenar fondo (cielo)
    screen.fill(AZUL)
    
    # Dibujar el suelo (césped)
    pygame.draw.rect(screen, VERDE, (0, casa_y + alto_casa, width, height - (casa_y + alto_casa)))
    
    # DIBUJAR LA CASA
    
    # 1. Cuerpo de la casa (rectángulo)
    cuerpo_casa = pygame.Rect(casa_x, casa_y, ancho_casa, alto_casa)
    pygame.draw.rect(screen, color_casa, cuerpo_casa)
    
    # 2. Tejado (triángulo)
    puntos_tejado = [
        (casa_x - 20, casa_y),  # Izquierda
        (casa_x + ancho_casa // 2, casa_y - 80),  # Centro arriba
        (casa_x + ancho_casa + 20, casa_y)  # Derecha
    ]
    pygame.draw.polygon(screen, MARRON, puntos_tejado)
    
    # 3. Puerta (rectángulo)
    puerta_ancho, puerta_alto = 40, 80
    puerta_x = casa_x + ancho_casa // 2 - puerta_ancho // 2
    puerta_y = casa_y + alto_casa - puerta_alto
    pygame.draw.rect(screen, MARRON, (puerta_x, puerta_y, puerta_ancho, puerta_alto))
    
    # 4. Ventanas (círculos)
    # Ventana izquierda
    ventana_izq_x = casa_x + 40
    ventana_izq_y = casa_y + 40
    pygame.draw.circle(screen, BLANCO, (ventana_izq_x, ventana_izq_y), 20)
    pygame.draw.circle(screen, NEGRO, (ventana_izq_x, ventana_izq_y), 20, 2)  # Borde
    
    # Ventana derecha
    ventana_der_x = casa_x + ancho_casa - 40
    ventana_der_y = casa_y + 40
    pygame.draw.circle(screen, BLANCO, (ventana_der_x, ventana_der_y), 20)
    pygame.draw.circle(screen, NEGRO, (ventana_der_x, ventana_der_y), 20, 2)  # Borde
    
    # 5. Chimenea (rectángulos)
    chimenea_x = casa_x + ancho_casa - 30
    chimenea_y = casa_y - 60
    pygame.draw.rect(screen, GRIS, (chimenea_x, chimenea_y, 20, 60))
    
    # Mostrar instrucciones en pantalla
    font = pygame.font.Font(None, 36)
    texto = font.render("Presiona R, G, B, Y para cambiar colores", True, BLANCO)
    screen.blit(texto, (50, 50))
    
    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()