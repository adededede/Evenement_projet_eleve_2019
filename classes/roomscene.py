import pygame
from pygame.locals import *

import classes.constants
from .pnj import *


from .scene import scene
from .text import text

class roomScene(scene):
	def __init__(self,room,player):
		self.room = room
		scene.__init__(self,self.room.width,self.room.height,self.room.sizeFactor)
		self.timer = room.timer
		self.overtime = False
		self.subSeconds = 0
		
		player.teleport(self.room.playerX,self.room.playerY)
		if player.energy < 10:
			player.energy = 10
		if player.moral < 10:
			player.moral = 10
			
		player.rectifValues()
		
		self.timerText = text("Temps: <value>",self.room.textX,self.room.textY+10,16,(255,255,255),classes.constants.PIXEL_FONT,"Désactivé")
		if self.timer != None:
			self.timerText.value = f"{self.timer:.1f}"
			
		self.actionText = text("<value>",self.room.textX,self.room.textY,16,(255,255,0),classes.constants.PIXEL_FONT,player.actionText)	
		self.moralText = text("Moral: <value>%",self.room.textX,self.room.textY+20,16,(255,255,255),classes.constants.PIXEL_FONT,player.moral)
		self.energyText = text("Energie: <value>%",self.room.textX,self.room.textY+30,16,(255,255,255),classes.constants.PIXEL_FONT,player.energy)
		self.workText =text("Travail: <value>%",self.room.textX,self.room.textY+40,16,(255,255,255),classes.constants.PIXEL_FONT,player.work)
		self.timeText = text(self.room.timeText,self.room.textX,self.room.textY+50,16,(255,100,100),classes.constants.PIXEL_FONT)
		
		
	def display(self,screen,player):
		surface = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
		self.room.displayBackground(surface)
		
		player.display(surface)
		
		if self.overtime:
			s = pygame.Surface((80,65))
		else:
			s = pygame.Surface((80,55))
		s.set_alpha(128)
		s.fill((0,0,0))
		surface.blit(s, (self.room.textX-5,self.room.textY))
		
		self.timerText.display(surface)
		self.moralText.display(surface)
		self.energyText.display(surface)
		self.workText.display(surface)
		self.actionText.display(surface)
		
		if self.overtime:
			self.timeText.display(surface)
		
		screen.blit(surface,(0,0))
		
	def tick(self,player,events,keys):
		nextScene = [None,None]
	
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			player.moveRight(self.room.walls)
		if keys[pygame.K_LEFT] or keys[pygame.K_q]:
			player.moveLeft(self.room.walls)
		if keys[pygame.K_UP] or keys[pygame.K_z]:
			player.moveUp(self.room.walls)
		if keys[pygame.K_DOWN] or keys[pygame.K_s]:
			player.moveDown(self.room.walls)
		
		if self.timer != None:
			self.subSeconds += 1
		#Augmente le timer de 0.1 toutes les 6 frames
			if self.subSeconds >= 6:
				self.subSeconds = 0
				self.timer = round(self.timer-0.1,1)
				self.timerText.value = f"{self.timer:.1f}" #Et me à jour l'affichage du timer
				if self.timer < 0:
					self.timerText.color = (255,100,100)
					self.overtime = True
					
				else:
					self.timerText.color = (255,255,255)
					self.overtime = False
					
		if self.overtime:
			if self.room.timeType == "exhaust":
				if self.timer % 1 == 0 and self.subSeconds == 0:
					player.energy += -1
			elif self.room.timeType == "late":
				if self.timer % 2 == 0 and self.subSeconds == 0:
					player.moral += -1
					player.effort += -1
		
		collideType = player.testZone(self.room.zones)
		player.rectifValues()
		self.moralText.value = player.moral
		self.energyText.value = player.energy
		self.workText.value = player.work
		
		if collideType == "disturb" and self.overtime == False:
			player.actionText = "Derange"
			player.disturbCounter += 1
			if player.disturbCounter >= 50:
				player.disturbCounter = 0
				player.effort += -3
			
		self.actionText.value = player.actionText
		
		if self.moralText.value <= 20:
			self.moralText.color = (255,100,100)
		else:
			self.moralText.color = (255,255,255)
		
		if self.energyText.value <= 20:
			self.energyText.color = (255,100,100)
		else:
			self.energyText.color = (255,255,255)
		
		if collideType =="interract1":
			for event in events:
				if event.type == MOUSEBUTTONDOWN:
					if eleve().clickEventpnj(event):
						print("hello")
					
		if collideType == "exit":
			nextScene[0] = self.room.exitScene
			nextScene[1] = self.room.exitMessage
		elif self.timer <= -60:
			nextScene[0] = self.room.timeScene
			nextScene[1] = self.room.timeMessage
		elif player.energy <= 0:
			nextScene[0] = self.room.energyScene
			nextScene[1] = self.room.energyMessage
		elif player.moral <= 0:
			nextScene[0] = self.room.moralScene
			nextScene[1] = self.room.moralMessage
		elif self.overtime:
			if self.room.timeType == "exhaust" and collideType == "rest":
				nextScene[0] = self.room.exitScene
				nextScene[1] = self.room.exitMessage
				player.moral += 30
				player.energy += 50
				
		if nextScene[0] != None and self.room.timeType == "late":
			player.effort += round(((player.work-50)/100)*40)
			player.work = 0
				
		if nextScene[0] == "END":
			if self.room.timeType == "extra":
				player.competence += round(((player.work-50)/100)*20)
			else:
				player.effort += -100
		
		return nextScene