#Archivo del mapa
import pygame,sys
import random
import os
#Globales
BLACK = (0,0,0)
GREY = (128,128,128)
WHITE = (248,248,248)
#Clase que representa un muro
class Wall(object):
	"""docstring for Wall"""
	def __init__(self, arg):
		super(Wall, self).__init__()
		self.arg = arg

#Clase del mapa
class Maze:
  """docstring for Maze"""
  def __init__(self):
    super(Maze, self).__init__()
    self.m = 10
    self.n = 8
    self.maze = [1,1,1,1,1,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,1,1,
    0,0,0,0,0,0,0,0,1,1,
    0,1,1,1,1,1,1,0,1,1,
    0,1,0,0,0,0,0,0,1,1,
    0,1,0,1,1,1,1,0,1,1,
    0,0,0,0,0,0,0,0,1,1,
    1,1,1,1,1,1,1,1,1,]

  def draw(self,surf):
    bx = 0
    by = 0
    for i in range(0,self.m*self.n):
      if self.maze[bx+(by*self.m)] == 1:
        rect = pygame.Rect(bx*44,by*44,40,40)
        pygame.draw.rect(surf,GREY,rect)
      elif self.maze[bx+(by*self.m)] == 0:
        rect = pygame.Rect(bx*44,by*44,40,40)
        pygame.draw.rect(surf,WHITE,rect)
      bx = bx + 1
      if bx > self.m-1:
        bx = 0
        by = by + 1