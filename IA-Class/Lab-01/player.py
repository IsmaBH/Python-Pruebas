#Archivo del Jugador
import pygame,sys
import random
import os
#Globales
BLACK = (0,0,0)
GREY = (128,128,128)
WHITE = (248,248,248)
#Clase del jugador
class Player:
  """docstring for Player"""
  def __init__(self):
    super(Player, self).__init__()
    self.x = 44
    self.y = 44
    self.speed = 1
  #Methods
  def moveRight(self):
    self.x = self.x + self.speed
  def moveLeft(self):
    self.x = self.x - self.speed
  def moveUp(self):
    self.y = self.y - self.speed
  def moveDown(self):
    self.y = self.y + self.speed