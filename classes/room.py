import pygame
from pygame.locals import *

class room():
	#Initialisation
	def __init__(self,width,height,sizeFactor,playerX,playerY,timer,textX,textY,timeType,timeText,timeOut,timeMessage,timeScene,energyMessage,energyScene,moralMessage,moralScene,exitMessage,exitScene,sprite,walls,zones):
		self.width = width
		self.height = height
		self.sizeFactor = sizeFactor
		self.walls = walls
		self.zones = zones
		self.playerX = playerX
		self.playerY = playerY
		self.timer = timer
		self.sprite = pygame.image.load(sprite)
		self.textX = textX
		self.textY = textY
		self.timeType = timeType
		self.timeText = timeText
		self.timeOut = timeOut
		self.timeMessage = timeMessage
		self.timeScene = timeScene
		self.energyMessage = energyMessage
		self.energyScene = energyScene
		self.moralMessage = moralMessage
		self.moralScene = moralScene
		self.exitMessage = exitMessage
		self.exitScene = exitScene
	
	#Affiche le fond de la salle
	def displayBackground(self,screen,backgroundColor = (255,255,255)):
		surface = pygame.Surface((self.width,self.height))
		surface.fill(backgroundColor)
		surface.blit(self.sprite,(0,0))
			
		# for z in self.zones:
			# s = pygame.Surface((z.rect.width,z.rect.height))
			# s.set_alpha(128)
			# s.fill((150,20,150))
			# surface.blit(s, (z.rect.x,z.rect.y))
			
		# for w in self.walls:
			# s = pygame.Surface((w.rect.width,w.rect.height))
			# s.set_alpha(128)
			# s.fill((20,150,20))
			# surface.blit(s, (w.rect.x,w.rect.y))
			
		screen.blit(surface,(0,0))