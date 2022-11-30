from classes.wall import wall
from classes.effectzone import effectZone
from classes.room import room
from classes.pnj import *

PIXEL_FONT = "font/Kelvetipixelnobi-2Vll.ttf"

SPRITE_ROOM_CHAMBER_NIGHT = "textures/backgrounds/room_background_night.png"
SPRITE_ROOM_CHAMBER_MORNING = "textures/backgrounds/room_background_morning.png"
SPRITE_ROOM_CLASSROOM = "textures/backgrounds/room_background_classroom.png"

#Salle de la chambre
ROOM_CHAMBER = room(
	256, #Largeur
	256, #Hauteur
	2, #Multiplicateur d'affichage
	204, #Position X du joueur
	48, #Position Y du joueur
	60, #Timer
	150, #Position X du texte
	10, #Position Y du texte
	"exhaust",
	"Il est tard", #Message de retard
	-60, #Temps maximum
	"Nuit blanche",
	"ROOM_CHAMBER_MORNING",
	"Ecrouler de sommeil",
	"ROOM_CHAMBER_MORNING",
	"Abandon des devoirs",
	"ROOM_CHAMBER_MORNING",
	"Bonne nuit de sommeil",
	"ROOM_CHAMBER_MORNING",
	SPRITE_ROOM_CHAMBER_NIGHT, #Sprite du fond
	[
		wall(0,0,10,256), #Mur de gauche
		wall(246,0,10,256), #Mur de droite
		wall(0,0,256,10), #Mur du haut
		wall(0,246,256,10), #Mur du bas
		
		wall(18,18,42,100), #Bureau
		wall(105,218,123,21), #Télévison
		wall(17,125,70,5), #Bas du lit
		wall(17,240,70,5) #Haut du lit
	], 
	[
		effectZone("study",58,18,25,100), #Zone du bureau
		effectZone("fun",136,181,75,37), #Zone de télévision	
		effectZone("rest",16,130,70,110) #Zone du lit
	]
)

ROOM_CHAMBER_MORNING = room(
	256, #Largeur
	256, #Hauteur
	2, #Multiplicateur d'affichage
	37, #Position X du joueur
	187, #Position Y du joueur
	30, #Timer
	150, #Position X du texte
	10, #Position Y du texte
	"late",
	"En retard", #Message de retard
	-60, #Temps maximum
	"Rate les cours",
	"END",
	"Rendormi",
	"END",
	"Pas le moral",
	"END",
	"Direction les cours",
	"ROOM_CLASSROOM",
	SPRITE_ROOM_CHAMBER_MORNING, #Sprite du fond
	[
		wall(0,0,10,256), #Mur de gauche
		wall(246,0,10,42), #Mur de droite (partie haute)
		wall(246,84,10,172), #Mur de droite (partie basse)
		wall(0,0,256,10), #Mur du haut
		wall(0,246,256,10), #Mur du bas
		
		wall(18,18,42,100), #Bureau
		wall(105,218,123,21), #Télévison
		wall(17,125,70,5), #Bas du lit
		wall(17,240,70,5), #Haut du lit
		wall(204,84,42,6) #Porte
	], 
	[
		effectZone("study",58,18,25,100), #Zone du bureau
		effectZone("fun",136,181,75,37), #Zone de télévision	
		effectZone("rest",16,130,70,110), #Zone du lit
		effectZone("exit",278,42,10,42) #Zone de sortie
	]
)

ROOM_CLASSROOM = room(
	256, #Largeur
	256, #Hauteur
	2,
	185, #Position X du joueur
	140, #Position Y du joueur
	60, #Timer
	150, #Position X du texte
	10, #Position Y du texte
	"extra",
	"Cours finis", #Message de retard
	-60, #Temps maximum
	"Reste en cours",
	"END",
	"Endormi en cours",
	"END",
	"Marre des cours",
	"END",
	"Retour chez soi",
	"END",
	SPRITE_ROOM_CLASSROOM, #Sprite du fond
	[
		wall(0,0,10,256), #Mur de gauche
		wall(246,0,10,42), #Mur de droite (partie haute)
		wall(246,84,10,172), #Mur de droite (partie basse)
		wall(0,0,256,10), #Mur du haut
		wall(0,246,256,10), #Mur du bas
		
		wall(34,45,91,30), #Bureau Prof
		wall(13,110,91,30), #Bureau eleve 1
		wall(13,177,91,30), #Bureau eleve 2
		wall(151,110,91,30), #Bureau eleve 3
		wall(151,177,91,30), #Bureau eleve 4
		
		wall(62,140,10,106), #Eleve 1 + eleve2
		wall(183,208,10,39), #Eleve 3
		wall(64,10,30,35) #Prof
	], 
	[
		eleve(type,10,140),
		effectZone("interract1",10,140,60,60),

		effectZone("study",151,140,95,37), #Zone de travail
		effectZone("talk",73,140,31,106), #Zone eleves 1+2
		effectZone("talk",151,207,31,39), #Zone eleve 3
		effectZone("disturb",10,10,236,122), #Zone de dérangement
		effectZone("exit",278,42,10,42) #Zone de sortie
	]
)