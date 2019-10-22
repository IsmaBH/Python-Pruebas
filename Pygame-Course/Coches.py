#Juego de coches y obstaculo
import pygame, sys
import random
#Variables para el coche
ANCHO_V = 800
ALTURA_V = 600
choque = False
BLACK = (0,0,0)
WHITE = (255,255,255)
SKY_BLUE = (20,51,220)
incremento_x = 0;
imagen_coche = pygame.image.load("racecar.png")
x = (ANCHO_V - imagen_coche.get_width()) // 2
y = (ALTURA_V - imagen_coche.get_height())
tiempo = pygame.time.Clock()
#Variables para los bloques del juego
bloque_velocidad = 7
bloque_alto = 100
bloque_ancho = 100
bloque_inicio_y = -bloque_alto
bloque_inicio_x = random.randint(0,ANCHO_V - bloque_ancho)
bloque_color = BLACK
#Funciones del juego
def dibujaCoche(pos_x,pos_y):
	canvas.blit(imagen_coche, (pos_x,pos_y))
#Funciones para el bloque
def bloque(bloque_x, bloque_y, bloque_ancho, bloque_alto, color):
	pygame.draw.rect(canvas,color,(bloque_x,bloque_y, bloque_ancho, bloque_alto))
#Inicializacion de las variables de ventana
pygame.init()
canvas = pygame.display.set_mode((ANCHO_V,ALTURA_V))
pygame.display.set_caption("Introduccion a Pygame")
#Bucle de juego
while not choque:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			choque = True
		if evento.type ==pygame.KEYDOWN:
			if evento.key == pygame.K_LEFT:
				incremento_x = -5
			if evento.key == pygame.K_RIGHT:
				incremento_x = 5;
		if evento.type == pygame.KEYUP:
			if (evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT):
				incremento_x = 0
	#Se debe comprobar los limites de la pantalla
	if (x + incremento_x >= 0) and (x + imagen_coche.get_width() + incremento_x < ANCHO_V) :
		x = x + incremento_x
	#Actualiza la posicion del bloque
	bloque_inicio_y += bloque_velocidad
	#Comprobamos los limites
	if bloque_inicio_y > ALTURA_V:
	 	bloque_inicio_y = -bloque_alto
	 	bloque_inicio_x = random.randint(0,ANCHO_V - bloque_ancho)
	#Se dibuja el plano de juego
	canvas.fill(SKY_BLUE)
	#Aqui se dibuja el bloque
	bloque(bloque_inicio_x,bloque_inicio_y,bloque_ancho,bloque_alto, bloque_color)
	dibujaCoche(x,y)
	pygame.display.update()
	tiempo.tick(50)
#Final del programa
pygame.quit()
sys.exit(0)