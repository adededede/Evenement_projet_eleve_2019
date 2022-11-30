import pygame
from pygame.locals import *

import classes.constants

from .scene import scene
from .text import text
from .button import button

class mainMenu(scene):
	def __init__(self):
		scene.__init__(self,700,400,1)

		self.ObjectMenu = menu(100,230)
		self.ObjectSelpers = menuPersona(100,80)
		self.ObjectTitre = titre(25,10)

		self.buttons = [
			button(self.ObjectMenu.rect.x+30,self.ObjectMenu.rect.y+45,100,30," Histoire Géo"),
			button(self.ObjectMenu.rect.x+140,self.ObjectMenu.rect.y+45,100,30,"     Maths"),
			button(self.ObjectMenu.rect.x+250,self.ObjectMenu.rect.y+45,100,30,"    Anglais"),
			button(self.ObjectMenu.rect.x+360,self.ObjectMenu.rect.y+45,100,30,"Physique Chimie")
		]
		self.titreText = text("Etudiant Simulator",150,26,16,(0,0,0),classes.constants.PIXEL_FONT)
		self.personaText = text("Sélectionne un personnage: ",110,90,16,(0,0,0),classes.constants.PIXEL_FONT)
		self.competenceText = text("Tu disposes de 2 points de compétences, a toi de choisir ou tu souhaite avoir ",110,238,16,(0,0,0),classes.constants.PIXEL_FONT)
		self.competenceTextSuite = text("un meilleur taux de réussite: ",110,250,16,(0,0,0),classes.constants.PIXEL_FONT)
		self.autresbuttons = [
			button(self.ObjectMenu.rect.x+180,self.ObjectMenu.rect.y+120,100,30,"     Jouer")
		]

		self.compteur = 0
		#compteur du nombre de personnage sélectionné
		self.compteurP = 0

		#Creéation d'une liste de boutons personnage
		self.persona = [
			button(self.ObjectSelpers.rect.x+60,self.ObjectSelpers.rect.y+40,50,70,"persona1"),
			button(self.ObjectSelpers.rect.x+170,self.ObjectSelpers.rect.y+40,50,70,"persona2"),
			button(self.ObjectSelpers.rect.x+280,self.ObjectSelpers.rect.y+40,50,70,"persona3"),
			button(self.ObjectSelpers.rect.x+390,self.ObjectSelpers.rect.y+40,50,70,"persona4")
		]

		#self.img = [
		#	pygame.image.load('textures/J-C.jpg'),
		#	pygame.image.load('textures/J-C.jpg'),
		#	pygame.image.load('textures/J-C.jpg'),
		#	pygame.image.load('textures/J-C.jpg')
		#]



	def display(self,screen,player):
		s = pygame.Surface((screen.get_width(),screen.get_height()))
		s.fill((255,255,255))
		screen.blit(s,(0,0))
		self.ObjectMenu.display(screen)
		self.ObjectTitre.display(screen)
		self.ObjectSelpers.display(screen)
		self.titreText.display(screen)
		self.personaText.display(screen)
		self.competenceText.display(screen)
		self.competenceTextSuite.display(screen)

		for b in self.buttons:
			b.display(screen)
			textbutton = text(b.text,b.rect.x+10,b.rect.y+5)
			textbutton.display(screen)
		for b in self.autresbuttons:
			b.color = (255, 255, 96)
			b.display(screen)
			textbutton = text(b.text,b.rect.x+10,b.rect.y+5)
			textbutton.display(screen)
		for b in self.persona:
			b.display(screen)
			#monPersona = pygame.Surface((b.rect.width,b.rect.height)).convert()
			#monPersona.blit(self.img[0], (b.rect.width,b.rect.height))
			nomPersona = text(b.text,b.rect.x,b.rect.y+70)
			nomPersona.display(screen)



	def tick(self,player,events,keys):
		nextScene = [None,None]
		for event in events:
			if event.type == MOUSEBUTTONDOWN:
				#compteur de compétences attribué
				#on vérifie qu'il n'utilise pas plus de compétences que dispo
				for b in self.persona:
					if b.clickEvent(event):
						if b.state == False:
							if self.compteurP >= 1:
								b.clickEvent(event)
							else:
								self.compteurP += 1
						elif b.state == True:
							self.compteurP += -1
				for b in self.buttons:
					if b.clickEvent(event):
						if b.state == False:
							if self.compteur >= 2:
								b.clickEvent(event)
							else:
								self.compteur += 1
						elif b.state == True:
							self.compteur += -1
				for b in self.autresbuttons:
					if b.clickEvent(event):
						nextScene = ["ROOM_CHAMBER","Revision du soir"]
						for c in self.buttons:
							if c.state == False:
								if c.text == "Anglais":
									player.cptAng = True
								elif c.text == "Histoire Géo":
									player.cptHig = True
								elif c.text == "Maths":
									player.cptMaths = True
								elif c.text == "Physique Chimie":
									player.cptPC = True
							elif c.state == True:
								if c.text == "Anglais":
									player.cptAng = False
								elif c.text == "Histoire Géo":
									player.cptHig = False
								elif c.text == "Maths":
									player.cptMaths = False
								elif c.text == "Physique Chimie":
									player.cptPC = False

		return nextScene



class menu():

	def __init__(self,x=0,y=0):
		self.rect = pygame.Rect(x,y,500,100)

	def display(self,screen):
		pygame.draw.rect(screen,(192, 224, 224),self.rect)

class menuPersona():

	def __init__(self,x=0,y=0):
		self.rect = pygame.Rect(x,y,500,130)

	def display(self,screen):
		pygame.draw.rect(screen,(192, 224, 224),self.rect)


class titre():
	def __init__(self,x=0,y=0):
		self.rect = pygame.Rect(x,y,650,50)

	def display(self,screen):
		pygame.draw.rect(screen,(160, 160, 192),self.rect)
