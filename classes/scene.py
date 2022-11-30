import pygame
from pygame.locals import *

class scene():
	def __init__(self,width = 256,height = 256, sizeFactor = 1):
		self.width = width
		self.height = height
		self.sizeFactor = sizeFactor
		
	def display(self,screen,player):
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,self.width,self.height))
		
	def tick(self,player,events,keys):
		return [None,None]