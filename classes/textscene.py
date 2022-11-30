import pygame
from pygame.locals import *

import classes.constants

from .scene import scene
from .text import text


class textScene(scene):
	def __init__(self,width = 256,height = 256,sizeFactor=1,displayText="",time=100,nextScene = "END"):
		scene.__init__(self,width,height,sizeFactor)
		self.displayText = text(displayText,0,0,32,(255,255,255),font=classes.constants.PIXEL_FONT)
		self.time = time
		self.nextScene = nextScene
		
	def display(self,screen,player):
		pygame.draw.rect(screen,(0,0,0),pygame.Rect(0,0,self.width,self.height))
		self.displayText.display(screen)
		
	def tick(self,player,events,keys):
		ret = [None,None]
		self.time += -1
		if self.time <= 0:
			ret[0] = self.nextScene
		return ret