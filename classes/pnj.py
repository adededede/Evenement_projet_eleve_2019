import pygame
from pygame.locals import *
from classes.effectzone import *
from classes.constants import *
from classes.room import *

SPRITE_ROOM_CLASSROOM = "textures/backgrounds/room_background_classroom.png.png"

class eleve():
	def __init__(self,type="eleve",x=0,y=0):
		self.bavard = False
		self.travailleur = False
		self.aidant = False
		self.rect = pygame.Rect(x,y,30,30)
		self.sprite = SPRITE_ROOM_CLASSROOM
		self.type = type
		self.testzone = 0
	def display(self,screen):
  		screen.blit(self.sprite,(self.rect.x,self.rect.y))
	def clickEventpnj(self,event):
		clicked = False
		x, y = event.pos
		if self.rect.collidepoint(x,y):
			clicked = True
			if self.state == True:
				self.state = False
			else:
				return clicked


class prof():
	def __init__(self,x=0,y=0,text="Prof"):
		self.matiere = text
		self.rect = pygame.Rect(x,y,30,30)
		self.app = 0

