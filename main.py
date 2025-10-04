
import pygame
import random

#Inicializar Pygame
pygame.init()

#Definir dimensiones de la pantalla
ANCHO =800
ALTO = 600
#Crear la pantalla
pantalla = pygame.display.set_modo( ANCHO , ALTO )


pygame.display.set_caption("Juego Pygame sabado haku")


#Creamos  la clase  jugador 
class Jugador :

    #sel.x = atributo  de la clase 
    def __init__(self , x , y,  color ):
        self.x = x
        self.y =y 
        self.color = color
        self.velocidad = 5

# Metodo de la clase jugador 
        def mover (self, direccion ):
            if direccion  == "izquierda":
                self.x -= self.velocidad
            elif direccion == "derecha":
                sefl.x += self.velocidad
            elif direccion == "arriba":
                self.y -= self.velocidad
            elif direccion == "abajo":
                self.y += self.velocidad
        
        #lLimitar  el movimiento  del jugador  dentro de la pantalla
        if  self.x < 0:
            self .x  =0
        elif  self.x   > ANCHO  -50 :  # ( 50  es el tamano del jugador en pixeles)
            self.x = ANCHO - 50 

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - 50:
            self.y = ALTO - 50

def dibujar (self, pantalla):
#dibujar el 

    pygame.draw.rect(pantalla, self.color, (self.x , self.y  , 50  , 50))


    #Creamos la clase  Enemigo 
    class Enemigo :
        def __init__(self , x , y ,color):
            self.x = x 
            self.y = y 
            self.color = color 
            self.velocidad = 3

            def  mover (self):
                self.x += random .choice ([-self.velocidad , self.velocidad])
                self.y += random .choice ([-self.velocidad , self.velocidad])
            
                    #lLimitar  el movimiento  del jugador  dentro de la pantalla
        if  self.x < 0:
            self .x  =0
        elif  self.x   > ANCHO  -50 :  # ( 50  es el tamano del jugador en pixeles)
            self.x = ANCHO - 50 

        if self.y < 0:
            self.y = 0
        elif self.y > ALTO - 50:
            self.y = ALTO - 50

    def dibujar (self , pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x , self.y  , 50  , 50))




        jugador = Jugador (375, 275 , (255, 0 , 0 ))  # Mediante RGB
        enemigo = Enemigo (100 , 100 ,(0 ,0 ,255))  # Enemigo en azul 


        #BUCLE PRINCIPAL 
        corriendo = True
        while corriendo :
            