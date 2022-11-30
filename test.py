import pygame
from pygame.locals import *

from classes.constants import *

from classes.player import player
from classes.wall import wall
from classes.text import text
from classes.effectzone import effectZone
from classes.room import room
from classes.roomscene import roomScene
from classes.mainmenu import mainMenu
from classes.pnj import *

#Change le mode d'affichage
def changeDisplay(width = None,height = None):
	global displayWidth
	global displayHeight
	global window
	
	if width == None:
		displayWidth = currentScene.width
	else:
		displayWidth = width
		
	if height == None:
		displayHeight = currentScene.height
	else:
		displayHeight = height
			
	if currentScene.width/currentScene.height > displayWidth/displayHeight:
		displayWidth = round(displayHeight * (currentScene.width/currentScene.height))
	else:
		displayHeight = round(displayWidth / (currentScene.width/currentScene.height))
	
	window = pygame.display.set_mode((displayWidth,displayHeight),pygame.RESIZABLE)

#Affiche l'écran	
def displayScreen(width,height,player):	
	surface = pygame.Surface((currentScene.width,currentScene.height))
	currentScene.display(surface,player)
	surface = pygame.transform.scale(surface, (width, height))
	window.blit(surface, surface.get_rect())

#Mise en place de la scène
def setupScene(scene):
	global currentScene
	
	currentScene = scene
	
	changeDisplay()
	
try:
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
			
		change = currentScene.tick(playerObject,events,keys)
		displayScreen(displayWidth,displayHeight,playerObject)
		
		if change[0] != None:
			if change[0] == "MAIN_MENU":
				setupScene(mainMenu())
				playerObject = player(0,0)
			elif change[0] == "ROOM_CHAMBER":
				setupScene(roomScene(ROOM_CLASSROOM,playerObject))
				for d in ROOM_CLASSROOM.zones:
					a = effectZone("interract",d.rect.x,d.rect.y)
				collide = ROOM_CLASSROOM.zones[0].rect.collidelistall(ROOM_CLASSROOM.zones)
				collideType = "none"

				for i in collide:
				#Test si player est dans la zone d'interaction
					if ROOM_CLASSROOM.zones[i].type == "interact1":
						for event in events:
							if event.type == MOUSEBUTTONDOWN:
								for p in ROOM_CLASSROOM.zones:
									if p.clickEventPnj(event):
										print("clic")

				
				
			print(change[1])
					
		pygame.display.flip() #Met à jour l'écran
	
except Exception as e:
	print(e)
	wait = input()