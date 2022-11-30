import random
import pygame
from pygame.locals import *
from classes.pnj import*

# Class du joueur
class player():
	# Initialisation, x et y coordonnées de base
	def __init__(self,x=0,y=0):
		#Rectangle de pygame, très utile pour les collisions, garder les coordonnées etc
		self.rect = pygame.Rect(x,y,30,30)
		self.energy = 80
		self.moral = 80
		self.work = 0
		self.effort = 0
		self.competence = 0
		self.restCounter = 0
		self.funCounter = 0
		self.studyCounter = 0
		self.talkCounter = 0
		self.disturbCounter = 0
		self.cptAng = False
		self.cptHig = False
		self.cptMaths = False
		self.cptPC = False
		self.actionText = "Inactif"

	#S'affiche sur un écran
	def display(self,screen):
		pygame.draw.rect(screen,(255,0,0),self.rect)

	#Test de zones et augmente les valeurs de manière accordée
	def testZone(self,zoneList):
		collide = self.rect.collidelistall(zoneList)
		collideType = "none"

		for i in collide:
			#Test de repos
			if zoneList[i].type == "rest":
				collideType = "rest"
				self.actionText = "Se repose"
				self.restCounter += 1
				if self.restCounter >= 50:
					self.restCounter = 0
					self.energy += random.choice([2,3])
					self.moral += 1

			#Test de loisir
			elif zoneList[i].type == "fun":
				collideType = "fun"
				self.actionText = "Joue"
				self.funCounter += 1
				if self.funCounter >= 50:
					self.funCounter = 0
					self.energy += random.choice([-1,-2])
					self.moral += random.choice([2,3,4])

			#Test d'étude
			elif zoneList[i].type == "study":
				collideType = "study"
				self.actionText ="Travaille"
				self.studyCounter += 1
				if self.studyCounter >= 50:
					self.studyCounter = 0
					self.energy += -1
					self.moral += random.choice([-1,-2])
					possibleResults = [0,1,1]
					if self.competence >= 10:
						possibleResults.append(2)
					if self.competence >= 20:
						possibleResults.append(3)
					self.work += random.choice(possibleResults)
					self.competence += random.choice([0,0,1])
					
			#Test de bavardage
			elif zoneList[i].type == "talk":
				collideType = "talk"
				self.actionText = "Bavarde"
				self.talkCounter += 1
				if self.talkCounter >= 50:
					self.talkCounter = 0
					self.energy += random.choice([0,1])
					self.moral += random.choice([1,2,3])
					self.effort += random.choice([0,-1])
			
			elif zoneList[i].type == "interact1":
						for event in events:
							if event.type == MOUSEBUTTONDOWN:
								clickEventPnj(event)
			
			else:
				collideType = zoneList[i].type

		if collideType == "none":
			self.actionText = "Inactif"

		return collideType

	def rectifValues(self):
		if self.energy > 100:
			self.energy = 100
		elif self.energy < 0:
			self.energy = 0

		if self.moral > 100:
			self.moral = 100
		elif self.moral < 0:
			self.moral = 0

		if self.work > 100:
			self.work = 100
		elif self.work < 0:
			self.work = 0

	#Change instantanément de position:
	def teleport(self,x,y):
		self.rect.x = x
		self.rect.y = y

	#Deplacement de manière général
	def movement(self,x,y,solidList):
		if self.rect.move(x,y).collidelist([s.rect for s in solidList]) == -1:
			self.rect = self.rect.move(x,y)

	# Deplacement à droite
	def moveRight(self,solidList):
		self.movement(1,0,solidList)

	# Deplacement à gauche
	def moveLeft(self,solidList):
		self.movement(-1,0,solidList)

	# Deplacement en bas
	def moveDown(self,solidList):
		self.movement(0,1,solidList)

	# Deplacement en haut
	def moveUp(self,solidList):
		self.movement(0,-1,solidList)
