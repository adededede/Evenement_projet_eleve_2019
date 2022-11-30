import pygame
from pygame.locals import *

#Class de murs
class wall():
	#Initialisation, coord x,y ainsi que largeur et hauteur
	def __init__(self,x=0,y=0,width=10,height=10):
		self.rect = pygame.Rect(x,y,width,height)