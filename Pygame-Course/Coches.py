#Juego de coches y obstaculo
import pygame, sys
#Variables
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
#Funciones del juego
def dibujaCoche(pos_x,pos_y):
	canvas.blit(imagen_coche, (pos_x,pos_y))
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
	x = x + incremento_x
	canvas.fill(SKY_BLUE)
	dibujaCoche(x,y)
	pygame.display.update()
	tiempo.tick(50)
#Final del programa
pygame.quit()
sys.exit(0)