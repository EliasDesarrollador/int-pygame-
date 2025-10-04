

import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego Pygame sabado haku")


# Clase Jugador
class Jugador:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 5
        self.size = 50

    # Método de la clase Jugador
    def mover(self, direccion):
        if direccion == "izquierda":
            self.x -= self.velocidad
        elif direccion == "derecha":
            self.x += self.velocidad
        elif direccion == "arriba":
            self.y -= self.velocidad
        elif direccion == "abajo":
            self.y += self.velocidad

        # Limitar el movimiento del jugador dentro de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - self.size:
            self.x = ANCHO - self.size

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - self.size:
            self.y = ALTO - self.size

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.size, self.size))


# Clase Enemigo
class Enemigo:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = 3
        self.size = 50

    def mover(self):
        self.x += random.choice([-self.velocidad, self.velocidad])
        self.y += random.choice([-self.velocidad, self.velocidad])

        # Limitar el movimiento dentro de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x > ANCHO - self.size:
            self.x = ANCHO - self.size

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - self.size:
            self.y = ALTO - self.size

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.size, self.size))


def main():
    jugador = Jugador(375, 275, (255, 0, 0))  # Rojo
    enemigo = Enemigo(100, 100, (0, 0, 255))  # Azul

    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Obtener las teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador.mover("izquierda")
        if teclas[pygame.K_RIGHT]:
            jugador.mover("derecha")
        if teclas[pygame.K_UP]:
            jugador.mover("arriba")
        if teclas[pygame.K_DOWN]:
            jugador.mover("abajo")

        enemigo.mover()

        # Verificar colisión (rectángulos simples)
        if (
            jugador.x < enemigo.x + enemigo.size
            and jugador.x + jugador.size > enemigo.x
            and jugador.y < enemigo.y + enemigo.size
            and jugador.y + jugador.size > enemigo.y
        ):
            print("¡Colisión!")
            corriendo = False

        # Dibujar
        pantalla.fill((0, 0, 0))  # Fondo negro
        jugador.dibujar(pantalla)
        enemigo.dibujar(pantalla)
        pygame.display.flip()

        reloj.tick(30)  # 30 FPS

    pygame.quit()


if __name__ == '__main__':
    main()