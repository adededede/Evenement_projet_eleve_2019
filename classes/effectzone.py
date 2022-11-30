import pygame
from pygame.locals import *

#Class des zone d'effets
class effectZone():
	#Initialisation, type, coord x,y, largeur, hauteur et couleur
	def __init__(self,type = "default",x=0,y=0,width=10,height=10):
		self.type = type
		self.rect = pygame.Rect(x,y,width,height)