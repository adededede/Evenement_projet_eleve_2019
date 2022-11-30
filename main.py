import pygame
from pygame.locals import *

import classes.constants

from classes.player import player
from classes.scene import scene
from classes.roomscene import roomScene
from classes.mainmenu import mainMenu
from classes.textscene import textScene
from classes.text import text

#Change le mode d'affichage
def changeDisplay(width = None,height = None):
	global displayWidth
	global displayHeight
	global window
	
	if width == None:
		displayWidth = currentScene.width*currentScene.sizeFactor
	else:
		displayWidth = width
		
	if height == None:
		displayHeight = currentScene.height*currentScene.sizeFactor
	else:
		displayHeight = height
			
	if currentScene.width/currentScene.height > displayWidth/displayHeight:
		displayWidth = round(displayHeight * (currentScene.width/currentScene.height))
	else:
		displayHeight = round(displayWidth / (currentScene.width/currentScene.height))
	
	window = pygame.display.set_mode((displayWidth,displayHeight),pygame.RESIZABLE)

#Affiche l'écran	
def displayScreen(width,height,player):	
	global screen

	screen = pygame.Surface((currentScene.width,currentScene.height))
	currentScene.display(screen,player)
	surface = pygame.transform.scale(screen, (width, height))
	window.blit(surface, surface.get_rect())

#Mise en place de la scène
def setupScene(scene,fadeInTime = 0,displayTime = 0, displayText = None,sceneName = "END"):
	global currentScene
	global fadeTime
	global totalFadeTime	
	
	if displayText != None:
		currentScene = textScene(scene.width,scene.height,scene.sizeFactor,displayText,displayTime,sceneName)
	else:
		currentScene = scene
	
	changeDisplay()
	
	fadeTime = fadeInTime
	totalFadeTime = fadeInTime
	

pygame.init() #Initialisation de pygame
clock = pygame.time.Clock() #Initialisation de pygame
playerObject = player(0,0) #Objet du joueur

setupScene(mainMenu())
# setupScene(roomScene(classes.constants.ROOM_CHAMBER,playerObject))

gameRunning = True #Variable pour la boucle principale

while gameRunning:
	clock.tick(60) #On set à 60fps
	events = pygame.event.get()
	keys = pygame.key.get_pressed()
	
	#On verifie les evenements pygame
	for event in events:
		#Active le possibilité de quitter avec la crois
		if event.type == QUIT:
			gameRunning = False
		#Change la taille de l'affichage avec la taille de l'écran
		if event.type == VIDEORESIZE:
			changeDisplay(event.w,event.h)			
	
	if fadeTime > 0:
		fadeTime += -1
		displayScreen(displayWidth,displayHeight,playerObject)
		s = pygame.Surface((displayWidth,displayHeight))
		s.set_alpha(255*(fadeTime/totalFadeTime))
		s.fill((0,0,0))
		window.blit(s, (0,0))
	else:
		change = currentScene.tick(playerObject,events,keys)
		displayScreen(displayWidth,displayHeight,playerObject)
		
		if change[0] != None:
			if change[0] == "MAIN_MENU":
				setupScene(mainMenu())
				playerObject = player(0,0)
			elif change[0] == "ROOM_CHAMBER":
				setupScene(roomScene(classes.constants.ROOM_CHAMBER,playerObject),50,100,change[1],change[0])
			elif change[0] == "ROOM_CLASSROOM":
				setupScene(roomScene(classes.constants.ROOM_CLASSROOM,playerObject),50,100,change[1],change[0])
			elif change[0] == "ROOM_CHAMBER_MORNING":
				setupScene(roomScene(classes.constants.ROOM_CHAMBER_MORNING,playerObject),50,100,change[1],change[0])
			elif change[0] == "END":
				setupScene(scene(currentScene.width,currentScene.height,currentScene.sizeFactor),50,100,change[1],"END2")
			elif change[0] == "END2":
				setupScene(textScene(currentScene.width,currentScene.height,currentScene.sizeFactor,"Fin\n" + "Effort:" + str(playerObject.effort) +"\nCompetence:" + str(playerObject.competence),2000,"MAIN_MENU"),50,100,change[1],change[0])
				
	pygame.display.flip() #Met à jour l'écran