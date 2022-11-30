import pygame
from pygame.locals import *

import classes.constants

#Class de text
class text():
	#Initialisation avec text et coordonnées x et y
	def __init__(self,text="",x=0,y=0,size=16,color=(0,0,0),font=classes.constants.PIXEL_FONT,value=0):
		self.text = text.split("\n")
		self.value = value
		self.x = x
		self.y = y
		self.size = size
		self.color = color
		self.font = pygame.font.Font(font,size)
	
	#Affichage
	def display(self,screen):
		bonusY = 0
		for i in range(len(self.text)):
			screen.blit(self.font.render(self.text[i].replace("<value>",str(self.value)), False, self.color),(self.x,self.y + bonusY))
			bonusY += self.size*(10/16)