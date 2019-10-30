#Juego de invasion espacial
import pygame, sys
import random
import os
#Variables de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0,0,0)
GREEN = (20, 248, 20)
RED = (248,20,20)
BACKGROUND_COLOR = (200,200,200)
#Clase Jugador
class Player(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self):
		super (Player, self).__init__()
		self.image = pygame.Surface((50,40))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH//2
		self.rect.bottom = HEIGHT-10
		self.speedx = 0
	#Metodos de la clase
	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT] :
			self.speedx = 5
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
		self.rect.x += self.speedx
#Clase de los enemigos
class Mob(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self):
		super(Mob, self).__init__()
		self.image = pygame.Surface((30,40))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(0,WIDTH-self.rect.width)
		self.rect.y = random.randint(-100,40)
		self.speedy = random.randrange(1,8)
		self.speedx = random.randint(-1,1)
	#Metodos de la clase
	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT+10:
			self.rect.x = random.randint(0,WIDTH-self.rect.width)
			self.rect.y = random.randint(-100,40)
			self.speedy = random.randrange(1,8)
			self.speedx = random.randint(-1,1)
#Inicializacion de pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Invasion Espacial")
clock = pygame.time.Clock()
#Grupo de Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
#Bucle de Juego
running = True
while running:
	#Mantenemos el bucle en el FPS correcto
	clock.tick(FPS)
	#Proceso de las entradas del juego
	for event in pygame.event.get():
		#Checar si se cierra la ventana
		if event.type == pygame.QUIT:
			running = False
	#Update
	all_sprites.update()
	#Dibujar o bien renderizar los objetos
	screen.fill(BLACK)
	all_sprites.draw(screen)
	#Despues de dibujar todo mostrar en pantalla
	pygame.display.flip()
#Fin del juego
pygame.quit()
sys.exit(0)