#Juego del pong
import pygame, sys
import random
#Inicializamos la libreria
pygame.init()
#Variables de la ventana
ANCHO_V = 800
ALTURA_V = 600
running = 1
BACKGROUND_COLOR = (200,200,200)
tiempo = pygame.time.Clock()
text_font = pygame.font.SysFont("Arial",48)
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
PADDLE_SPEED = 4
LINES_COLOR = (0,0,0)
SCORE_1_POS = (ANCHO_V//2 - 70, 50)
SCORE_2_POS = (ANCHO_V//2 + 50, 50)
#Funciones
def draw_Text(texto, position, color):
	global canvas
	superficie = text_font.render(texto, True, color)
	canvas.blit(superficie, position)
def new_Game():
	global pala_1_pos, pala_2_pos, pala_1_incremento_y, pala_2_incremento_y, score_1, score_2
	pala_1_pos = [0,ALTURA_V//2 - HALF_PAD_HEIGHT]
	pala_2_pos = [ANCHO_V-(PAD_WIDTH-1),ALTURA_V//2-HALF_PAD_HEIGHT]
	pala_1_incremento_y = 0;
	pala_2_incremento_y = 0;
	score_1 = 0
	score_2 = 0
	lanza_bola(random.choice([RIGHT,LEFT]))
def lanza_bola(direccion):
	global ball_pos, ball_vel
	x_dir = random.randint(2,4)
	if direccion == LEFT:
		x_dir = -x_dir
	ball_pos = [ANCHO_V//2,ALTURA_V//2]
	ball_vel = [x_dir, random.randint(-3,-1)]
def key_down(tecla):
	global pala_1_incremento_y, pala_2_incremento_y
	if tecla == pygame.K_w:
		pala_1_incremento_y = -PADDLE_SPEED
	if tecla == pygame.K_s:
		pala_1_incremento_y = PADDLE_SPEED
	if tecla == pygame.K_UP:
		pala_2_incremento_y = -PADDLE_SPEED
	if tecla == pygame.K_DOWN:
		pala_2_incremento_y = PADDLE_SPEED
def key_up(tecla):
	global pala_1_incremento_y, pala_2_incremento_y
	if tecla == pygame.K_w or tecla == pygame.K_s:
		pala_1_incremento_y = 0
	if tecla == pygame.K_UP or tecla == pygame.K_DOWN:
		pala_2_incremento_y = 0
def draw_Field():
	#Linea que dibuja el centro del campo
	pygame.draw.line(canvas, LINES_COLOR, (ANCHO_V//2,0), (ANCHO_V//2, ALTURA_V), 1)
	#Linea del jugador isquierdo
	pygame.draw.line(canvas, LINES_COLOR, (PAD_WIDTH,0), (PAD_WIDTH,ALTURA_V), 1)
	#Linea del jugador derecho
	pygame.draw.line(canvas, LINES_COLOR, ((ANCHO_V-PAD_WIDTH),0), ((ANCHO_V-PAD_WIDTH),ALTURA_V), 1)
	#Dibujamos los marcadores
	draw_Text(str(score_1), SCORE_1_POS, L_POLE_COLOR)
	draw_Text(str(score_2), SCORE_2_POS, R_POLE_COLOR)
def draw_Poles():
	#Actualizamos los datos
	global pala_1_pos, pala_2_pos
	pala_1_pos[1] += pala_1_incremento_y
	pala_2_pos[1] += pala_2_incremento_y
	pygame.draw.rect(canvas, L_POLE_COLOR, (pala_1_pos[0],pala_1_pos[1], PAD_WIDTH, PAD_HEIGHT))
	pygame.draw.rect(canvas, R_POLE_COLOR, (pala_2_pos[0],pala_2_pos[1], PAD_WIDTH, PAD_HEIGHT))
def draw_Ball():
	global score_1, score_2
	#Control de la pelota en el limite derecho
	if ball_pos[0] + BALL_RADIUS > ANCHO_V - PAD_WIDTH:
		if ball_pos[1] + BALL_RADIUS < pala_2_pos[1] or ball_pos[1] - BALL_RADIUS > pala_2_pos[1] + PAD_HEIGHT:
			score_1 += 1
			lanza_bola(LEFT)
		else:
			ball_vel[0] = -ball_vel[0] * 1.1
	#Control de la pelota en el limite izquierdo
	if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
			if ball_pos[1] + BALL_RADIUS < pala_1_pos[1] or ball_pos[1] - BALL_RADIUS > pala_1_pos[1] + PAD_HEIGHT:
					score_2 += 1
					lanza_bola(RIGHT)
			else:
				ball_vel[0] = -ball_vel[0] * 1.1
	#Se actualizan los datos
	ball_pos[0] = ball_pos[0] + ball_vel[0]
	ball_pos[1] = ball_pos[1] +ball_vel[1]
	#Comprobamos los limites inferior y superior y hacemos el rebote
	if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= ALTURA_V-BALL_RADIUS:
		ball_vel[1] = -ball_vel[1]
	pygame.draw.circle(canvas, B_COLOR,(int(ball_pos[0]),int(ball_pos[1])), BALL_RADIUS)
#Creacion de la ventana
canvas = pygame.display.set_mode((ANCHO_V,ALTURA_V))
pygame.display.set_caption("PONG")
new_Game()
#Bucle de Juego
while running:
	#Lista de eventos del juego
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			pygame.quit()
			sys.exit(0)
		if evento.type == pygame.KEYDOWN:
			key_down(evento.key)
		if evento.type == pygame.KEYUP:
			key_up(evento.key)
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