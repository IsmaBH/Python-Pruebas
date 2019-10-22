#Juego de coches y obstaculo
import pygame, sys
#Variables
ANCHO_V = 640
ALTURA_V = 480
choque = False
BLACK = (0,0,0)
WHITE = (255,255,255)
SKY_BLUE = (20,51,220)
#Inicializacion de las variables de ventana
pygame.init()
canvas = pygame.display.set_mode((ANCHO_V,ALTURA_V))
pygame.display.set_caption("Introduccion a Pygame")
#Bucle de juego
while not choque:
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			choque = True
	canvas.fill(SKY_BLUE)
	pygame.display.update()
#Final del programa
pygame.quit()
sys.exit(0)