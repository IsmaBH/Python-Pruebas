#Juego de invasion espacial
#Sprite graphics: Copyright 2016 David Thompson <davet@gnu.org>
#Background image artwork from game "Gagian" by Alksander Kowalczyk, Retrocade.net
#Licensed under: Attribution 4.0 Internacional (CC BY 4.0) https://creativecommons.org/licenses/by/4.0/
import pygame, sys
import random
import os
#Variables de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0,0,0)
RED = (200,20,20)
WHITE = (248,248,248)
BACKGROUND_COLOR = (200,200,200)
ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
#Funciones del juego
def draw_score(surf,text,size,pos):
	font = pygame.font.Font(font_name,size)
	text_surface = font.render(text,True,WHITE)
	text_shadow = font.render(text, True, RED)
	text_rect = text_surface.get_rect()
	text_rect.midtop = pos
	text_shadow_pos = [text_rect.x+2,text_rect.y+2]
	surf.blit(text_shadow, text_shadow_pos)
	surf.blit(text_surface, text_rect)
#Clase Jugador
class Player(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self):
		super (Player, self).__init__()
		self.image = player_img
		self.rect = self.image.get_rect()
		self.radius = 14
		#pygame.draw.circle(self.image,RED,self.rect.center,self.radius, 3)
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
	def shoot(self):
		bullet = Bullet(self.rect.centerx,self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
#Clase de los enemigos
class Mob(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self):
		super(Mob, self).__init__()
		self.image = random.choice(enemy_images)
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width*0.45)
		#pygame.draw.circle(self.image,RED,self.rect.center,self.radius, 3)
		self.rect.x = random.randint(0,WIDTH-self.rect.width)
		self.rect.y = random.randint(-100,-40)
		self.speedy = random.randrange(1,8)
		self.speedx = random.randint(-1,1)
	#Metodos de la clase
	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT+10:
			self.rect.x = random.randint(0,WIDTH-self.rect.width)
			self.rect.y = random.randint(-100,-40)
			self.speedy = random.randrange(1,8)
			self.speedx = random.randint(-1,1)
class Bullet(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self, x , y):
		super(Bullet, self).__init__()
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10
	def update(self):
		self.rect.y += self.speedy
#Inicializacion de pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Invasion Espacial")
clock = pygame.time.Clock()
#Carga de imagenes
background = pygame.image.load(os.path.join(ASSETS_DIR, "starfield.png")).convert_alpha()
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(ASSETS_DIR,"player.png")).convert_alpha()
enemy_files = ['enemy1.png','enemy2.png','enemy3.png']
enemy_images = []
for img_file in enemy_files:
	enemy_images.append(pygame.image.load(os.path.join(ASSETS_DIR,img_file)).convert_alpha())
bullet_img = pygame.image.load(os.path.join(ASSETS_DIR,"bullet.png")).convert_alpha()
#Grupo de Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
#Variable de puntuacion
score = 0
#Fuente para la puntuacion
font_name = pygame.font.match_font('arial')
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
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
	#Update
	all_sprites.update()
	#Comprobacion de colisiones con los mob
	hits = pygame.sprite.spritecollide(player,mobs,False, pygame.sprite.collide_circle)
	if hits:
		running = False
	#Comprobacion de colision de un bullet con mob
	hits = pygame.sprite.groupcollide(mobs,bullets,True, True)
	for hit in hits:
		score += 25
		m = Mob()
		all_sprites.add(m)
		mobs.add(m)
	#Dibujar o bien renderizar los objetos
	screen.fill(BLACK)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)
	draw_score(screen,str(score), 18, (WIDTH//2,10))
	#Despues de dibujar todo mostrar en pantalla
	pygame.display.flip()
#Fin del juego
pygame.quit()
sys.exit(0)