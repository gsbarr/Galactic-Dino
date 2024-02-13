import pygame
import random

# Teclas
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)

# Tamaño de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# RELOJ: regula el tiempo (Framerate) en el que se ejecuta el juego
clock = pygame.time.Clock()

# Una clase jugador
# Hereda de SPRITE
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        self.surf = pygame.image.load("assets/dino.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.velocidad = 5
        self.reset_boost = 0

    def update(self, teclas):
        if teclas[K_UP]:
            self.rect.move_ip(0, -self.velocidad) #se mueve hacia arriba
        if teclas[K_DOWN]:
            self.rect.move_ip(0, self.velocidad) #hacia abajo
        if teclas[K_LEFT]:
            self.rect.move_ip(-self.velocidad, 0) #izquierda
        if teclas[K_RIGHT]:
            self.rect.move_ip(self.velocidad, 0) #derecha
        #Un boost de velocidad
        if teclas[K_SPACE]:
            if self.reset_boost == 0:
                self.velocidad = self.velocidad * 2
                self.reset_boost = 50

        # Hace que el jugador no se salga de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        # Reducimos el contador de boost
        if self.reset_boost > 0:
            self.reset_boost = self.reset_boost - 1
        else:
            self.velocidad = self.velocidad = 5


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        #self.surf = pygame.Surface((20, 10))
        #self.surf.fill((255, 255, 255))
        self.img_grande = pygame.image.load("assets/meteoro.png").convert_alpha()
        #El sprite es muy grande, así que reducimos a la mitad su tamaño
        self.surf = pygame.transform.scale(self.img_grande, (int(self.img_grande.get_width()/2), int(self.img_grande.get_height()/2))).convert_alpha()

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

        #Genera la posición del enemigo al azar
        #Viene siempre desde la derecha de la pantalla
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        #velocidad del enemigo
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        #Lo mueve constantemente hacia la derecha
        self.rect.move_ip(-self.speed, 0)
        #cuando se va para la izquierda de la pantalla, muere
        if self.rect.right < 0:
            self.kill()


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        super(Fondo, self).__init__()
        self.img = pygame.image.load("assets/parallax-mountain-bg.png").convert()
        # Hacemos que el fondo ocupe toda la pantalla
        self.surf = pygame.transform.scale(self.img, (SCREEN_WIDTH, SCREEN_HEIGHT))     

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
