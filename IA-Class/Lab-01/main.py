#Ejecucion principal
import pygame,sys
from player import *
from map import *
import random
import os

#Variables Globales
WINDOW_WIDTH = 800
WINDOW_HEIGTH = 600
FPS = 60
#Inicio del juego
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGTH))
pygame.display.set_caption("Laberinto")
clock = pygame.time.Clock()
#Bucle de Juego
running = True
while running:
  #Mantenemos el bucle en el FPS correcto
  clock.tick(FPS)
  maze = Maze()
  maze.draw(screen)
  #Proceso de las entradas del juego
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  pygame.display.update()