# Biblioteca Pygame
import pygame

import random

from clases import *


# Inicializa el juego
pygame.init()

# Crea la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creamos un evento de PYGAME
# Un evento es un código que se ejecuta cada X tiempo 
NUEVOENEMIGO = pygame.USEREVENT + 1
pygame.time.set_timer(NUEVOENEMIGO, 250) # aparece cada 250 ms

# Instancia el jugador. Todavía es solamente un cuadrado
player = Player()
# Crea el fondo
fondo = Fondo()

# Crea un conjunto de enemigos
enemigos = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)



# Variable para mantener un LOOP
running = True

# Main loop
while running:

    # Loop de eventos
    for event in pygame.event.get():
        # Evento de fin de programa
        if event.type == pygame.QUIT:
            running = False
        # Evento de presionar una tecla
        if event.type == KEYDOWN:
            # Tecla de salida
            if event.key == K_ESCAPE:
                running = False
        # Crear un nuevo enemigo es un evento, así que va en este loop
        if event.type == NUEVOENEMIGO:
            #Este if se ejecuta cada vez que se activa el evento (250ms)
            # Creamos el nuevo enemigo
            new_enemy = Enemy()
            enemigos.add(new_enemy)
            all_sprites.add(new_enemy)
            
            
    ## Controlador de jugador
    ## Capturamos tecla que se presiona
    teclas = pygame.key.get_pressed()

    # Actualizamos el movimiento de los sprites
    player.update(teclas)
    enemigos.update()



    # Limpiamos la pantalla de negro
    screen.fill((0, 0, 0))

    # Dibujamos todos los sprites
    screen.blit(fondo.surf, (0,0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)


    # Verificamos por colisiones (Si algún enemigo colisionó con el jugador)
    if pygame.sprite.spritecollideany(player, enemigos):
        # Una colisión mata al jugador
        player.kill()
        # Y termina el loop
        running = False

    # Actualizamos la pantalla
    pygame.display.flip()

    # Configuramos que el Framerate = 30
    # Esto significa que la velocidad del juego va a estar fijada en 30 pantallas por segundo
    clock.tick(60)

# Termina el programa
pygame.quit()