from pygame import *
from math import*
from random import *


WIDTH=1300
HEIGHT=700
VITESSE=4.7
FPS=50

white=(255,255,255)
black=(0,0,0)


init() #initialisation de pygame
fenetre=display.set_mode((WIDTH, HEIGHT)) #creation de la fenetre
clock = time.Clock()
basicfont = font.SysFont(None, 30)
police_menu = font.SysFont(None, 50)






mouse.set_cursor(*cursors.broken_x)

mixer.music.load("son/musique.mp3")
#mixer.music.play(-1)

running_jeu=True  #tant que running=True, la boucle principale tourne
running_principal=True

fond=transform.scale(image.load("images/sable.jpg"),(WIDTH,HEIGHT))
fond_menu=transform.scale(image.load("images/fond_menu.jpg"),(WIDTH,HEIGHT))
image_game_over=transform.scale(image.load("images/game_over.png"),(300,300))
image_victory=transform.scale(image.load("images/victory.png"),(344,160))
oasis=image.load("images/oasis.png")
tourelle_bleu=image.load("images/tourelle_bleu.png")
tourelle_rouge=image.load("images/tourelle_rouge.png")

son_on=transform.scale(image.load("images/son_on.png"),(70,70))
son_off=transform.scale(image.load("images/son_off.png"),(70,70))
son=False

manette_on=transform.scale(image.load("images/manette_off.png"),(70,70))
manette_off=transform.scale(image.load("images/manette_off.png"),(70,70))
manette=False


image_perso=image.load("images/BORK.PNG")
rect_perso=image_perso.get_rect()
pos_perso=[500,500]
rect_perso.topleft=(pos_perso[0],pos_perso[1])
perso_tir_cool=[0,5]
perso_degats=[1,2]
taille_bouclier_perso=0
liste_bouclier_perso=[1,1,1]
bouclier_perso=False
liste_projectile=[]
retenter=False

