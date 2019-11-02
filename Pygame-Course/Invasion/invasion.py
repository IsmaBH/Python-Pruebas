#Juego de invasion espacial
#Sprite graphics: Copyright 2016 David Thompson <davet@gnu.org>
#Background image artwork from game "Gagian" by Alksander Kowalczyk, Retrocade.net
#Licensed under: Attribution 4.0 Internacional (CC BY 4.0) https://creativecommons.org/licenses/by/4.0/
#www.bfxr.net for sounds
#Background music by SketchyLogic
#Licensed under: Attribution completely optional CC0 1.0 Universal (CC0 1.0)
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
GREEN = (20,220,20)
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
def new_mob():
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
def draw_health_bar(surf,x,y,valor):
	if valor < 0:
		valor = 0
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (valor/100)*BAR_LENGHT
	fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
	outer_rect = pygame.Rect(x,y,BAR_LENGHT,BAR_HEIGHT)
	pygame.draw.rect(surf,RED,outer_rect)
	pygame.draw.rect(surf,GREEN,fill_rect)
	pygame.draw.rect(surf,WHITE,outer_rect,2)
def draw_lives(surf,x,y,n_lives,img):
	for i in range(n_lives):
		img_rect = img.get_rect()
		img_rect.x = x+20*i
		img_rect.y = y
		surf.blit(img,img_rect)
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
		self.health = 100
		self.lives = 3
		self.hidden = False
		self.hide_timer = pygame.time.get_ticks()
	#Metodos de la clase
	def update(self):
		if self.hidden and pygame.time.get_ticks() - self.hide_timer > 2000:
			self.hidden = False
			self.rect.centerx = WIDTH//2
			self.rect.bottom = HEIGHT -10
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
		snd_shoot.play()
		bullet = Bullet(self.rect.centerx,self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
	def hide(self):
		self.hidden = True
		self.hide_timer = pygame.time.get_ticks()
		self.rect.y = HEIGHT +200
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
		self.last_shot = pygame.time.get_ticks()
		self.shot_delay = random.randint(2000,4000)
	#Metodos de la clase
	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT+10:
			self.rect.x = random.randint(0,WIDTH-self.rect.width)
			self.rect.y = random.randint(-100,-40)
			self.speedy = random.randrange(1,8)
			self.speedx = random.randint(-1,1)
		now = pygame.time.get_ticks()
		if now - self.last_shot > self.shot_delay:
			self.shoot()
	def shoot(self):
		self.last_shot = pygame.time.get_ticks()
		bullet = EnemyBullet(self.rect.centerx,self.rect.bottom)
		all_sprites.add(bullet)
		enemy_bullets.add(bullet)
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
class Explosion(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self, center, size):
		super(Explosion, self).__init__()
		self.size = size
		self.image = explosion_anim[self.size][0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_delay = 50 #Son milisegundos
	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_delay:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim[self.size]):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.size][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center
class EnemyBullet(pygame.sprite.Sprite):
	#Metodo init de la clase
	def __init__(self,x,y):
		super(EnemyBullet, self).__init__()
		self.image = enemy_bullet_img
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width * 0.3)
		self.rect.top = y
		self.rect.centerx = x
		self.speedy = 5
	def update(self):
		self.rect.y += self.speedy
#Inicializacion de pygame
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Invasion Espacial")
clock = pygame.time.Clock()
#Carga de imagenes
background = pygame.image.load(os.path.join(ASSETS_DIR, "starfield.png")).convert_alpha()
background_rect = background.get_rect()
player_img = pygame.image.load(os.path.join(ASSETS_DIR,"player.png")).convert_alpha()
player_mini_img = pygame.transform.scale(player_img,(16,16))
enemy_files = ['enemy1.png','enemy2.png','enemy3.png']
enemy_images = []
for img_file in enemy_files:
	enemy_images.append(pygame.image.load(os.path.join(ASSETS_DIR,img_file)).convert_alpha())
bullet_img = pygame.image.load(os.path.join(ASSETS_DIR,"bullet.png")).convert_alpha()
enemy_bullet_img = pygame.image.load(os.path.join(ASSETS_DIR,"enemy_bullet.png")).convert_alpha()
#Carga de imagenes para las explosiones
explosion_anim = {}
explosion_anim['big'] = []
explosion_anim['small'] = []
for i in range(3):
	filename = 'explosion'+str(i)+'.png'
	img = pygame.image.load(os.path.join(ASSETS_DIR,filename)).convert_alpha()
	img_big = pygame.transform.scale(img,(32,32))
	explosion_anim['big'].append(img_big)
	explosion_anim['small'].append(img)
explosion_anim['player'] = explosion_anim['big'][0:3]
explosion_anim['player'].append(explosion_anim['big'][1])
explosion_anim['player'].append(explosion_anim['big'][0])
#Carga de Sonidos
snd_shoot = pygame.mixer.Sound(os.path.join(ASSETS_DIR,'Laser_Shoot.wav'))
snd_shoot.set_volume(0.05)
snd_explosions = []
snd_files = ["Explosion.wav","Explosion2.wav","Explosion3.wav"]
for snd_file in snd_files:
	snd = pygame.mixer.Sound(os.path.join(ASSETS_DIR,snd_file))
	snd.set_volume(0.04)
	snd_explosions.append(snd)
snd_player_explosion = pygame.mixer.Sound(os.path.join(ASSETS_DIR,"explosion_player.wav"))
snd_player_explosion.set_volume(0.1)
pygame.mixer.music.load(os.path.join(ASSETS_DIR,"Venus.wav"))
pygame.mixer.music.set_volume(0.1)
#Grupo de Sprites
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
	new_mob()
#Variable de puntuacion
score = 0
#Fuente para la puntuacion
font_name = pygame.font.match_font('arial')
#Play background music forever
pygame.mixer.music.play(loops = -1)
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
	hits = pygame.sprite.spritecollide(player,mobs,True, pygame.sprite.collide_circle)
	for hit in hits:
		snd_explosions[0].play()
		expl = Explosion(hit.rect.center,'small')
		all_sprites.add(expl)
		player.health -= 25
		new_mob()
		if player.health <= 0:
			snd_player_explosion.play()
			death_explosion = Explosion(player.rect.center,'player')
			all_sprites.add(death_explosion)
			player.lives -= 1
			player.health = 100
			player.hide()
	#Comprobacion de colision de un bullet con mob
	hits = pygame.sprite.groupcollide(mobs,bullets,True, True)
	for hit in hits:
		random.choice(snd_explosions).play()
		expl = Explosion(hit.rect.center,'big')
		all_sprites.add(expl)
		score += 25
		new_mob()
	#Comprobacion de colison de un bullet con el player
	hits = pygame.sprite.spritecollide(player,enemy_bullets,True,pygame.sprite.collide_circle)
	for hit in hits:
		expl = Explosion(hit.rect.center,'small')
		all_sprites.add(expl)
		player.health -= 15
		if player.health <= 0:
			snd_player_explosion.play()
			death_explosion = Explosion(player.rect.center,'player')
			all_sprites.add(death_explosion)
			player.lives -= 1
			player.health = 100
			player.hide()
	if player.lives == 0 and death_explosion.alive():
		running = False
	#Dibujar o bien renderizar los objetos
	screen.fill(BLACK)
	screen.blit(background, background_rect)
	all_sprites.draw(screen)
	draw_score(screen,str(score), 18, (WIDTH//2,10))
	draw_health_bar(screen,5,5,player.health)
	draw_lives(screen,WIDTH - 54,10,player.lives,player_mini_img)
	#Despues de dibujar todo mostrar en pantalla
	pygame.display.flip()
#Fin del juego
pygame.quit()
sys.exit(0)