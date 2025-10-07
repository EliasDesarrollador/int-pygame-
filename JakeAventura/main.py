
import  pygame
import sys

#Inicializar pygame
pygame.init()

#Configuracion de ventana
ANCHO , ALTO = 1000, 600 # Ventana tamano
PANTALLA = pygame.display.set_mode((ANCHO, ALTO)) #Creamos la ventana 
pygame.display.set_caption("Jake Adventure 🐶 ") #Titulo de la ventana 

#Colores
NEGRO = (0, 0, 0)

#Fondo
fondo = pygame.image.load("assets/images/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# FPS
FPS = 60 # Cuantos cuadros por segundo se actualiza el juego 
clock = pygame.time.Clock() #Reloj de control de control de FPS

# ==========================
#CLASE JUGADOR JAKE
# ==========================

class Jugador (pygame.sprite.Sprite):
    def __init__ (self, x, y ):
        super() .__init__()
        #Cargamos la imagen del personaje 
        self.image = pygame.load("assets/images/jake.png").convert() #
        self.image = pygame.transform.scale(self.image, (80,80)) #
        self.rect = self.image.get_rect(midbottom = (x , y)) #

        self.vel_y = 0  # Velocidad vertical ( para saltar y caer)
        self.en_suelo =  True # Bandera para  saber  si esta  tocando el suelo

# ==========================
        #Metodos 
# ==========================

        def manejar_input(self): # Metodo para manejar las entradas del teclado del jugador 
            keys = pygame.key.get_pressed() # Detecta las teclas presionadas
            if keys[pygame.K_RIGHT] : # si se presiona flecha derecha 
                self.rect.x += 5  # Mueve a jake 5 pixeles a la derecha 
            if keys[pygame.K_LEFT] : #  si se presiona la flecha izquierda
                self.rect.x  -= 5 # Mueve a jake 5 pixeles a la izquierda 
            if keys[pygame.K_SPACE] and  self.en_suelo: # si se presiona espacio y esta en el suelo
                self.vel_y =  -15 # Salta  ( Velocidad negativa  hacia arriba )
                self.en_suelo = False  #  ya no esta en el suelo

        def aplicar_gravedad(self) : # Metodo para aplicar gravedad
            self.vel_y +=  1 # Aumenta la velocidad vertical ( simula caida)
            self.rect.y += self.vel_y  #   Mueve al jugador segun velocidad
            if self.rect.bottom >= 500:  # Si toca el suelo linea y = 500
                self.rect.bottom = 500 # Lo mantiene en el suelo 
                self.en_suelo = True # Marca que esta en suelo

        def update(self) : # Metodo que se ejecuta en cada frame
            self.manejar_input() #Detecta las teclas  y nueve jugador
            self.aplicar_gravedad() #Aplica gravedad y salto
            

