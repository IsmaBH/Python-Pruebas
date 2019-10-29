#Juego del pong
import pygame, sys

#Inicializamos la libreria
pygame.init()
#Variables de la ventana
ANCHO_V = 800
ALTURA_V = 600
running = 1
BACKGROUND_COLOR = (200,200,200)
tiempo = pygame.time.Clock()
#Variables para las palas y la pelota
BALL_RADIUS = 20
L_POLE_COLOR = (20,51,220)
R_POLE_COLOR = (148,62,100)
B_COLOR = (100, 200, 80)
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
LEFT = False
RIGHT = True
LINES_COLOR = (0,0,0)
#Funciones
def draw_Field():
	pygame.draw.line(canvas, LINES_COLOR, (ANCHO_V//2,0), (ANCHO_V//2, ALTURA_V), 1)
	pygame.draw.line(canvas, LINES_COLOR, (PAD_WIDTH,0), (PAD_WIDTH,ALTURA_V), 1)
	pygame.draw.line(canvas, LINES_COLOR, ((ANCHO_V-PAD_WIDTH),0), ((ANCHO_V-PAD_WIDTH),ALTURA_V), 1)
def draw_Poles():
	pygame.draw.rect(canvas, L_POLE_COLOR, (0,ALTURA_V//2 - HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT))
	pygame.draw.rect(canvas, R_POLE_COLOR, (ANCHO_V-(PAD_WIDTH-1),ALTURA_V//2-HALF_PAD_HEIGHT, PAD_WIDTH, PAD_HEIGHT))
def draw_Ball():
	pygame.draw.circle(canvas, B_COLOR, (ANCHO_V//2,ALTURA_V//2), BALL_RADIUS)
#Creacion de la ventana
canvas = pygame.display.set_mode((ANCHO_V,ALTURA_V))
pygame.display.set_caption("PONG")
#Bucle de Juego
while running:
	#Lista de eventos del juego
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
	#Se dibuja el plano de juego
	canvas.fill(BACKGROUND_COLOR)
	draw_Field()
	draw_Poles()
	draw_Ball()
	pygame.display.update()
	tiempo.tick(60)
#Final del programa
pygame.quit()
sys.exit(0)