import pygame
from pygame.locals import *

# Class du bouton
class button():
	def __init__(self,x=0,y=0,width=10,height=10,text=""):

		self.rect = pygame.Rect(x,y,width,height)
		#état du bouton
		self.color = (192,32,32) #rouge
		self.state = True
		self.text = text
		#get le centre du rectangle
		#rectTitle = text.get_rect(center=screen.get_rect().center)

	#Affichage
	def display(self,screen):
		pygame.draw.rect(screen,self.color,self.rect)

	def clickEvent(self,event):
		clicked = False
		x, y = event.pos
		if self.rect.collidepoint(x,y):
			clicked = True
			if self.state == True:
				self.color = (32, 160, 96) #vert
				self.state = False

			else:
				self.color = (192,32,32) #rouge
				self.state = True
		return clicked
