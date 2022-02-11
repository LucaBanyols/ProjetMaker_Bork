from init_variable import *
from pygame import *
from math import*
from random import *
import os
import webbrowser

class projectile():  #la classe projectile
    def __init__ (self,pos_depart,pos_visee,vitesse,cible,degat,taille,couleur1,couleur2): #initialisation de l'objet avec tout ses arguments

        D=distance(pos_depart,pos_visee)                                  #)
        self.vitesseX=((pos_visee[0]-pos_depart[0])*vitesse)/D            #)--- a l'aide d'un calcul, on donne la vitesseX et le vitesseY du projectile
        self.vitesseY=((pos_visee[1]-pos_depart[1])*vitesse)/D            #)    pour que leurs somme vectorielle soit egale a vitesse dans la direction choisie

        self.position=pos_depart     #)
        self.cible=cible             #)--- on attribue les arguments a l'objet
        self.degat=degat             #)
        self.taille=taille           #)

        self.couleur1=couleur1          #)--- attribution des couleurs au projectile
        self.couleur2=couleur2          #)

    def update(self):  #on definit une fonction specifique a la classe. Son but sera de modifier la position du projectile selon sa vitesse
        self.position[0]=self.vitesseX+self.position[0]
        self.position[1]=self.vitesseY+self.position[1]

        if self.position[0]>WIDTH or self.position[1]>HEIGHT or self.position[0]<0 or self.position[1]<0: #si le projectile sort de l'image, on le supprime
            liste_projectile.remove(self) #suppression du projectile. En l'enlevant de la liste, on retire son seul point d'acces et il est supprime.



class Boss():  #la classe du boss sert a acceder beaucoup plus facilement a toute les caracteristiques du boss
    def __init__(self): #chaque self signifie que l'on donne une varible directement à l'objet
        self.image=image.load("images/squealer.PNG")   #on charge son image
        self.rect=self.image.get_rect()   #on cree le "rect" du boss. il se presente sous la forme (posX, posY, Largeur, Hauteur). Cela nous permet d'acceder facilement a son milieu avec rect.center par exemple
        self.pos=[200,200]                #la position du boss (haut gauche de l'image)
        self.rect.topleft=(self.pos[0],self.pos[1]) #on change la position du rect pour qu'il coincide avec celle du boss
        self.vitesse=7 #sa vitesse
        self.pos_visee=[0,0] #position vers laquelle le boss veux se deplacer
        self.vitesseX=0 #vitesse du boss sur l'axe X
        self.vitesseY=0 #vitesse du boss sur l'axe Y
        self.vie=[4000,4000] #vie du boss. la premiere partie sera celle qui diminue, la deuxieme sert a se rappeler de la vie max

        self.cool_tir3=[0,31,6] #le cooldown (temps d'attente) entre chaque tir. [0] sera le compteur qui partira de [1] vers 0. Si il est inferieur a [2], un projectile est tire.
        self.cool_tir1=[0,35,3] # Il y a plusieurs listes, une pour chaque type de tir
        self.cool_tir2=[0,60,45] # ^^^^^^
        self.cool_tir4=[0,10,7] #^^^^^^
        self.tir_random_cible=[0,0] #cible du tir aleatoire
        self.spe2_on=False #sert a savoir si on affiche les effets de la spe2
        self.spe3_on=False #^^^^^^
        self.spe4_on=False #^^^^^^
        self.spe5_on=False #^^^^^^
        self.spe6_on=False #^^^^^^
        self.angle_spe4=0 #angle de rotation de la spe4
        self.sens_angle=1 #sens de rotation de la spe4
        self.vitesse_rotation=0.025 #la vitesse de rotation des lasers de la spe4
        self.liste_spe5=[[randint(15,WIDTH-15),randint(15,HEIGHT-15)]] #on donne les coordonees d'une tourelle bleu a la spe5 car il faut toujour au moins une tourelle
        self.liste_spe6=[] #liste qui contiendra les tourelles rouges de la spe6

        self.compteur_phase=0 #les actions du boss sont divises en phases. Ce compteur augmente de 1 a chaque fin de phase pour qu'on sache a quelle phase on se trouve

        self.liste_cooldown=[200,200,80,300,100,400,50,80,1500,50,100] #chaque phase dure un certain temps. Ce temps est sauvegarde dans cette liste (c'est ici le nombre d'images qu'on compte)
        self.liste_phase=[ #C'est ici qu'on determine les actions de chaque phase. liste_phase contient des listes de fonction.
                           #A chaque frame, le boss effectuera chaque action dans la liste. Quand on change de phase, on passe a la liste suivante

        [self.trouver_visee,self.tir3,self.va_pos_visee],
        [self.tir2],
        [self.spe2_init],
        [self.spe2,self.va_pos_visee2],
        [], #par exemple, ici le boss ne fera rien
        [self.spe3_init,self.va_pos_visee2],
        [self.spe3_stop,self.vise_mid],
        [self.spe4_init1],
        [self.spe4_init2,self.tir4],
        [self.spe4_stop],
        [self.tir3] #ici il ne fera que tirer sur le perso
        ]

        self.compteur_cooldown=self.liste_cooldown[self.compteur_phase] #on attribue au compteur la valeur correspondant a la phase 1
        self.liste_action=self.liste_phase[self.compteur_phase][:] #([:] = copie de la liste) Liste action represente toutes les actions a effectuer et change a chaque phase




    def update(self):
        """ fonction appelee a chaque frame pour actualiser toutes les actions du boss"""
        for action in self.liste_action: #pour chaque actions dans liste_action, on active la fonction correspondante
            action()
        self.compteur_cooldown-=1 #on diminue le temps d'activation de la phase de 1


        if self.compteur_cooldown==0: #si le compteur attein 0, on change de phase
            self.compteur_phase+=1 #on augmente le compteur de phase de 1
            if self.compteur_phase>=len(self.liste_cooldown): #si le compteur depasse la nombre de phases, il redevient 0
                self.compteur_phase=0

            self.compteur_cooldown=self.liste_cooldown[self.compteur_phase] #puis on modifie le cooldown et liste_action en consequence pour qu'ils correspondent a la phase
            self.liste_action=self.liste_phase[self.compteur_phase][:] #([:] = copie de la liste)




    def va_pos_visee(self): #fonction de deplacement du boss. il va se deplacer  vers une position donnee
        """ actualise la position du boss, si la cible est atteinte, trouve une nouvelle cible
            si il se dirige trop vers le perso, trouve une nouvelle cible"""
        self.pos[0]+=self.vitesseX #pour ca, on ajoute a sa position sa vitesse en X et en Y
        self.pos[1]+=self.vitesseY
        self.rect.topleft=(self.pos[0],self.pos[1]) #on replace le rect pour qu'il corresponde

        d1=int(distance([rect_perso.centerx,rect_perso.centery],[self.rect.centerx,self.rect.centery])) #
        d2=int(distance(self.pos_visee,[self.rect.centerx,self.rect.centery]))                          #
        if d2!=0:                                                                                       #
            z=d1/d2                                                                                     #   Calcul qui permet de trouver la position du point
            X=self.pos_visee[0]-self.rect.centerx                                                       #   etant le plus proche du perso situe sur la droite
            Y=self.pos_visee[1]-self.rect.centery                                                       #   que forme la position du boss et sa position visee
            pos=[int(self.rect.centerx+X*z),int(self.rect.centery+Y*z)]                                 #
        else:                                                                                           #
            pos=[0,0]                                                                                   #


        if distance([self.rect.centerx,self.rect.centery],self.pos_visee)<=self.vitesse or (distance([self.rect.centerx,self.rect.centery],[rect_perso.centerx,rect_perso.centery])>200 and distance(pos,[rect_perso.centerx,rect_perso.centery])<200):
            #si la distance entre le boss et la position visee est inferieure a sa vitesse ou si le point trouve auparavant est trop proche du perso , on change de position visee
            self.liste_action.append(self.trouver_visee) #pour cela, il suffit d'ajouter a la liste d'action une fonction qui trouve une nouvelle cible

    def vise_mid(self): #fonction qui donne le milieu de l'ecran pour position visee
        """ vise le milieu de la fenetre et active wait_va_pos()"""
        self.pos_visee=[WIDTH//2,HEIGHT//2]
        D=distance([self.rect.centerx,self.rect.centery],self.pos_visee)
        if D!=0:
            self.vitesseX=((self.pos_visee[0]-self.rect.centerx)*self.vitesse)/D
            self.vitesseY=((self.pos_visee[1]-self.rect.centery)*self.vitesse)/D

        self.liste_action.append(self.wait_va_pos) #on ajoute a la liste_action la fonction wait_va_pos qui est la suite logique de cette fonction
        self.liste_action.remove(self.vise_mid) #etant donne que cette action ne s'active qu'une fois, on l'enleve de la liste_action

    def wait_va_pos(self): #deplace le boss vers une position en bloquant le cooldown jusqu'a ce qu'il l'atteigne
        """ va vers la position choisie en bloquant le cooldown jusqu'a ce qu'elle l'atteigne"""
        self.pos[0]+=self.vitesseX
        self.pos[1]+=self.vitesseY
        self.rect.topleft=(self.pos[0],self.pos[1])
        if distance([self.rect.centerx,self.rect.centery],self.pos_visee) >=self.vitesse:
            self.compteur_cooldown+=1
        else:
            self.liste_action.remove(self.wait_va_pos) #supperssion de la fonction de la liste_action

    def va_pos_visee2(self):
        """ comme va_pos_visee mais avec la moitie de la vitesse"""
        self.pos[0]+=self.vitesseX/2
        self.pos[1]+=self.vitesseY/2
        self.rect.topleft=(self.pos[0],self.pos[1])

        d1=int(distance([rect_perso.centerx,rect_perso.centery],[self.rect.centerx,self.rect.centery])) #
        d2=int(distance(self.pos_visee,[self.rect.centerx,self.rect.centery]))                          #
        if d2!=0:                                                                                       #
            z=d1/d2                                                                                     #   Calcul qui permet de trouver la position du point
            X=self.pos_visee[0]-self.rect.centerx                                                       #   etant le plus proche du perso situe sur la droite
            Y=self.pos_visee[1]-self.rect.centery                                                       #   que forme la position du boss et sa position visee
            pos=[int(self.rect.centerx+X*z),int(self.rect.centery+Y*z)]                                 #
        else:                                                                                           #
            pos=[0,0]                                                                                   #

        if distance([self.rect.centerx,self.rect.centery],self.pos_visee)<=self.vitesse or (distance([self.rect.centerx,self.rect.centery],[rect_perso.centerx,rect_perso.centery])>200 and distance(pos,[rect_perso.centerx,rect_perso.centery])<200):
            #si la distance entre le boss et la position visee est inferieure a sa vitesse ou si le point trouve auparavant est trop proche du perso , on change de position visee
            self.liste_action.append(self.trouver_visee) #pour cela, il suffit d'ajouter a la liste d'action une fonction qui trouve une nouvelle cible



    def trouver_visee(self):
        """ trouve une position aleatoire vers laquelle se deplacer et calcule la vitesse X et Y necesaire pour s'y rendre"""
        self.pos_visee=[randint(0,WIDTH),randint(0,HEIGHT)]
        D=distance([self.rect.centerx,self.rect.centery],self.pos_visee)

        self.vitesseX=((self.pos_visee[0]-self.rect.centerx)*self.vitesse)/D
        self.vitesseY=((self.pos_visee[1]-self.rect.centery)*self.vitesse)/D

        self.liste_action.remove(self.trouver_visee)


    def tir1(self):
        """ tire quelques petits projectiles au degats faibles """
        if self.cool_tir1[0]:
            self.cool_tir1[0]-=1
        else:
            self.cool_tir1[0]=randint(self.cool_tir1[1]-5,self.cool_tir1[1]+5)
        if self.cool_tir1[0]<self.cool_tir1[2]:
            tirer([self.rect.centerx,self.rect.centery],[rect_perso.centerx,rect_perso.centery],"perso",8,randint(2,4),5,(160,0,25),white)

    def tir2(self):
        """ tire de longues salves de petits projectiles rapide sur le perso"""
        if self.cool_tir2[0]:
            self.cool_tir2[0]-=1
        else:
            self.cool_tir2[0]=self.cool_tir2[1]
        if self.cool_tir2[0]<self.cool_tir2[2]:
            tirer([self.rect.centerx,self.rect.centery],[rect_perso.centerx,rect_perso.centery],"perso",10,randint(1,3),3,(140,0,0),black)

    def tir3(self): #selon le cooldown tirer_perso, on tire ou non un projectile sur perso puis on diminue le cooldown
        """ Tire de gros et lents projectiles noirs"""
        if self.cool_tir3[0]:
            self.cool_tir3[0]-=1
        else:
            self.cool_tir3[0]=randint(self.cool_tir3[1]-5,self.cool_tir3[1]+5)
        if self.cool_tir3[0]<self.cool_tir3[2]:
            tirer([self.rect.centerx,self.rect.centery],[rect_perso.centerx,rect_perso.centery],"perso",1.5,randint(2,4),40,(0,0,25),white)


    def tir4(self):
        """ tire une petite salve de projectiles a une position aleatoire"""
        if self.cool_tir4[0]:
            self.cool_tir4[0]-=1
        else:
            self.cool_tir4[0]=self.cool_tir4[1]
            self.tir_random_cible=[randint(0,WIDTH),randint(0,HEIGHT)]
        if self.cool_tir4[0]<self.cool_tir4[2]:
            tirer([self.rect.centerx,self.rect.centery],[self.tir_random_cible[0],self.tir_random_cible[1]],"perso",4.5,1,5,(225,100,0),white)


    def spe1_init(self):
        """ on trouve le sens et le'angle de depart selon lequel on tirera"""
        self.angle_spe4=0.1*randint(0,62)
        self.sens_angle=1-2*randint(0,1)
        self.liste_action.append(self.spe1)
        self.liste_action.remove(self.spe1_init)

    def spe1(self):
        """ on tire deux projectiles selon un angle qui tourne autour du boss."""
        self.angle_spe4+=0.02*self.sens_angle
        tirer([self.rect.centerx,self.rect.centery],[self.rect.centerx+100*cos(self.angle_spe4),self.rect.centery+100*sin(self.angle_spe4)],"perso",5,1,8,(0,100,255),white)
        tirer([self.rect.centerx,self.rect.centery],[self.rect.centerx+100*cos(self.angle_spe4+pi),self.rect.centery+100*sin(self.angle_spe4+pi)],"perso",5,1,8,(0,100,255),white)


    def spe2_init(self): #spe2 a besoin d'etre initialise pour activer l'affichage de la safe-zone et determiner sa position
        """ Trouve une position pour l'oasis et active son affichage"""
        self.spe2_on=True
        self.zone_spe2=[randint(0,WIDTH-150),randint(0,HEIGHT-150)]
        self.liste_action.remove(self.spe2_init)



    def spe2(self): #on cree de nombreux projectiles allant partout sauf dans la safe-zone
        """ Des projectiles arrivent de tout les cotés mais évitent l'oasis"""
        cibleX=choice([randint(0,self.zone_spe2[0]),randint(self.zone_spe2[0]+150,WIDTH)])
        cibleY=choice([randint(0,self.zone_spe2[1]),randint(self.zone_spe2[1]+150,HEIGHT)])
        direction= randint(0,4)
        if direction==0:
            tirer([0,cibleY],[1,cibleY],"perso",10,randint(3,6),8,(181, 140, 54),(108, 79, 36))
        elif direction==1:
            tirer([WIDTH,cibleY],[0,cibleY],"perso",10,randint(3,6),8,(181, 140, 54),(108, 79, 36))
        elif direction==2:
            tirer([cibleX,0],[cibleX,1],"perso",10,randint(3,6),8,(181, 140, 54),(108, 79, 36))
        elif direction==3:
            tirer([cibleX,HEIGHT],[cibleX,0],"perso",10,randint(3,6),8,(181, 140, 54),(108, 79, 36))

    def spe2_stop(self): #on desactive l'affichage de la safe-zone
        """ on desactive l'affichage de l'oasiss"""
        self.spe2_on=False
        self.liste_action.remove(self.spe2_stop)



    def spe3_init(self):
        """ on initialise les deux cercles, on active l'affichage et les degats et on remplis une liste de coordones et taille de boules de poison seulement visuelles"""
        self.taille_rond1=0
        self.taille_rond2=WIDTH
        self.spe3_on=True
        self.liste_action.append(self.spe3)
        self.liste_action.remove(self.spe3_init)
        self.liste_boule_poison=[]
        for i in range(100):
            self.liste_boule_poison.append([randint(0,WIDTH),randint(0,HEIGHT),randint(5,20)])

    def spe3(self):
        """ Deux cercles se forment autour du boss. Il faut rester entre les deux pour ne pas prendre de dommages.
            on augmente la taille du plus petit cercle et diminue celle du grand jusqu'a ce qu'ils atteignent leurs taille minimum"""
        if self.taille_rond1<200:
            self.taille_rond1+=2
        elif self.taille_rond2>500:
            self.taille_rond2-=4

    def spe3_stop(self):
        """ on desactive l'affichage et les degats de la spe3"""
        self.spe3_on=False
        self.liste_action.remove(self.spe3_stop)



    def spe4_init1(self):
        """ on active une image inoffencive des rayons, on trouve leurs sens et leur angle de depart"""
        self.spe4_on=1
        self.angle_spe4=0.1*randint(0,62)
        self.sens_angle=1-2*randint(0,1)
        self.liste_action.remove(self.spe4_init1)

    def spe4_init2(self):
        """ on active les vrais rayons et on ajoute a la liste d'action la spe4"""
        self.spe4_on=2
        self.liste_action.remove(self.spe4_init2)
        self.liste_action.append(self.spe4)

    def spe4(self):
        """ 4 rayons tournent dans un sens aleatoire de plus en plus vite."""
        if self.compteur_cooldown>self.liste_cooldown[self.compteur_phase]*5/6: #pendant le premier sixieme du temps, les rayons vont a une vitesse constante
            self.angle_spe4+=self.sens_angle*self.vitesse_rotation*0.15

        elif self.compteur_cooldown>self.liste_cooldown[self.compteur_phase]/3: #jusqu'a ce qu'il ne reste qu'un tier du temps, les rayons accelerent
            self.angle_spe4+=self.sens_angle*self.vitesse_rotation*((self.liste_cooldown[self.compteur_phase]-self.compteur_cooldown)/self.liste_cooldown[self.compteur_phase])

        else:
            self.angle_spe4+=self.sens_angle*self.vitesse_rotation*0.66 #ils vont ensuite a une vitesse constante

    def spe4_stop(self):
        """ on desactive l'affichage de la spe4"""
        self.spe4_on=False
        self.liste_action.remove(self.spe4_stop)



    def spe5_init(self):
        """ On active l'affichage des tourelles bleues et on en rajoute une avec des coordonees aleatoires"""
        self.spe5_on=True
        self.liste_spe5.append([randint(15,WIDTH-15),randint(15,HEIGHT-15)])
        self.liste_action.remove(self.spe5_init)

    def spe5(self):
        """ Pour chaque tourelle bleue, celle ci a 1 chance sur 100 de tirer sur une autre tourelle bleu aleatoire"""
        for i in range(len(self.liste_spe5)):
            if randint(0,100)==0:
                tourelle_visee=randint(0,(len(self.liste_spe5)-1)//2)
                if i%2==0:
                    tirer(self.liste_spe5[i],self.liste_spe5[2*tourelle_visee-1],"perso",5,6,8,(0, 101, 166),(73, 167, 194))
                else:
                    tirer(self.liste_spe5[i],self.liste_spe5[2*tourelle_visee],"perso",5,6,8,(0, 101, 166),(73, 167, 194))

    def spe5_stop(self):
        """ on vide la liste des tourelles bleues (tout en en laissant une)  et on desactive la spe5"""
        liste_spe5=[[randint(15,WIDTH-15),randint(15,HEIGHT-15)]]
        self.spe5_on=False
        self.liste_action.remove(self.spe5_stop)



    def spe6_init(self):
        """ On active l'affichage des tourelles rouge et on en rajoute une avec des coordonees aleatoires."""
        self.spe6_on=True
        self.liste_spe6.append([randint(15,WIDTH-15),randint(15,HEIGHT-15)])
        self.liste_action.remove(self.spe6_init)

    def spe6(self):
        """ Pour chaque tourelle rouge, celle ci a 1 chance sur 100 de tirer sur le perso"""
        for i in range(len(self.liste_spe6)):
            if randint(0,100)==0:
                tirer(self.liste_spe6[i],[rect_perso.centerx,rect_perso.centery],"perso",5,6,8,(221, 66, 25),(182, 88, 61))

    def spe6_stop(self):
        """ on vide la liste des tourelles rouges et on desactive la spe6"""
        liste_spe6=[]
        self.spe6_on=False
        self.liste_action.remove(self.spe6_stop)



    def regen(self):
        """ le boss regagne 5pv si sa vie n'est pas au max"""
        self.vie[0]+=5
        if self.vie[0]>self.vie[1]:
            self.vie[0]=self.vie[1]






def distance(d1,d2):
    """ retourne la distance entre deux coordonees """
    distance=sqrt((d1[0]-d2[0])**2+(d1[1]-d2[1])**2)
    return(distance)

def perso_update(pos_perso):
    """ on recupere les informations donnes par l'utilisateur ayant un rapport avec le perso
        avec, on actualise sa position et son tir."""
    keys = key.get_pressed()
    if keys[K_d]+keys[K_a]+keys[K_w]+keys[K_s]>1:
        facteur=1/sqrt(2)
    else:
        facteur=1
    if keys[K_d]:
        pos_perso[0] = pos_perso[0] + VITESSE * facteur

        if pos_perso[0]+rect_perso.width>WIDTH:
            pos_perso[0]=WIDTH-rect_perso.width

    if keys[K_a]:
        pos_perso[0] = pos_perso[0] - VITESSE * facteur

        if pos_perso[0]<0:
            pos_perso[0]=0

    if keys[K_w]:
        pos_perso[1] = pos_perso[1] - VITESSE * facteur

        if pos_perso[1]<0:
            pos_perso[1]=0

    if keys[K_s]:
        pos_perso[1] = pos_perso[1] + VITESSE * facteur

        if pos_perso[1]+rect_perso.height>HEIGHT:
            pos_perso[1]=HEIGHT-rect_perso.height

    if manette:
        if mon_joystick.get_axis(0)>0.15 or mon_joystick.get_axis(0)<-0.15:
            pos_perso[0] = pos_perso[0] + VITESSE*mon_joystick.get_axis(0)


        if mon_joystick.get_axis(1)>0.15 or mon_joystick.get_axis(1)<-0.15:
            pos_perso[1] = pos_perso[1] + VITESSE*mon_joystick.get_axis(1)

        if mon_joystick.get_button(5) == True or mon_joystick.get_axis(2)<-0.1:
                perso_tirer([rect_perso.centerx,rect_perso.centery],[rect_perso.centerx+mon_joystick.get_axis(4),rect_perso.centery+mon_joystick.get_axis(3)])

    if mouse.get_pressed()[0]:
                perso_tirer([rect_perso.centerx,rect_perso.centery],mouse.get_pos())



def tirer(pos_depart,pos_visee,cible,vitesse,degat,taille,couleur1,couleur2):
    """ cree un projectile avec les caracteristiques voulues"""
    if pos_depart != pos_visee : #on ne peux pas tirer sans direction
        liste_projectile.append (projectile(pos_depart[:],pos_visee[:],vitesse,cible,degat,taille,couleur1,couleur2))


def menu_echap():

    menu_running=True
    retenter=False
    running_jeu=True
    global running_jeu
    global running_principal
    global son
    global manette
    text_menu_1 = police_menu.render(("Reprendre"), True, (0,0,0))
    rect1=Rect(WIDTH//2-120,HEIGHT//2-190,240,50)

    text_menu_2 = police_menu.render(("  Quitter"), True, (0,0,0))
    rect2=Rect(WIDTH//2-120,HEIGHT//2+130,240,50)

    text_menu_3 = police_menu.render(("     Aide"), True, (0,0,0))
    rect3=Rect(WIDTH//2-120,HEIGHT//2-50,240,50)

    text_menu_4 = police_menu.render(("     Menu"), True, (0,0,0))
    rect4=Rect(WIDTH//2-120,HEIGHT//2+10,240,50)

    text_menu_7 = police_menu.render(("  Réesayer"), True, (0,0,0))
    rect7=Rect(WIDTH//2-120,HEIGHT//2+70,240,50)

    rect5=Rect(WIDTH//2-90,HEIGHT//2-130,70,70)

    rect6=Rect(WIDTH//2+30,HEIGHT//2-130,70,70)

    while menu_running:
        for evenement in event.get():
            if evenement.type == KEYDOWN:

                if evenement.key == K_ESCAPE:
                    menu_running=False
            if evenement.type== QUIT :
                running_jeu=False
                running_principal=False
                menu_running=False
            if evenement.type == MOUSEBUTTONUP:
                if rect1.collidepoint(mouse.get_pos()):
                    menu_running=False
                elif rect2.collidepoint(mouse.get_pos()):
                    running_jeu=False
                    running_principal=False
                    menu_running=False
                elif rect3.collidepoint(mouse.get_pos()):
                    webbrowser.open("html\\site_1.html")
                elif rect4.collidepoint(mouse.get_pos()):
                    running_jeu=False
                    menu_running=False
                elif rect7.collidepoint(mouse.get_pos()):
                    running_jeu=False
                    menu_running=False
                    retenter=True
                elif rect5.collidepoint(mouse.get_pos()):
                    if son:
                        mixer.music.stop()
                        son=False
                    else:
                        mixer.music.play(-1)
                        son=True
                elif rect6.collidepoint(mouse.get_pos()):
                    if manette:
                        manette=False

                    else:
                        nb_joysticks = joystick.get_count()

                        #On compte les joysticks
                        nb_joysticks = joystick.get_count()
                        #Et on en crée un s'il y a en au moins un

                        if nb_joysticks > 0 :
                            mon_joystick = joystick.Joystick(0)

                            mon_joystick.init()
                            manette=True

        draw.rect(fenetre,(255,255,255),(WIDTH//2-145,HEIGHT//2-215,290,410))
        draw.rect(fenetre,(0,0,0),(WIDTH//2-140,HEIGHT//2-210,280,400))
        draw.rect(fenetre,(255,255,255),rect1)
        draw.rect(fenetre,(255,255,255),rect2)
        draw.rect(fenetre,(255,255,255),rect3)
        draw.rect(fenetre,(255,255,255),rect4)
        draw.rect(fenetre,(255,255,255),rect7)

        if son:
            fenetre.blit(son_on,(WIDTH//2-90,HEIGHT//2-130))
        else:
            fenetre.blit(son_off,(WIDTH//2-90,HEIGHT//2-130))

        if manette:
            fenetre.blit(manette_on,(WIDTH//2+30,HEIGHT//2-130))
        else:
            fenetre.blit(manette_off,(WIDTH//2+30,HEIGHT//2-130))



        fenetre.blit(text_menu_1,(WIDTH//2-90,HEIGHT//2-183,240,50))

        fenetre.blit(text_menu_2,(WIDTH//2-90,HEIGHT//2+137,240,50))

        fenetre.blit(text_menu_3,(WIDTH//2-90,HEIGHT//2-43,240,50))

        fenetre.blit(text_menu_4,(WIDTH//2-90,HEIGHT//2+17,240,50))

        fenetre.blit(text_menu_7,(WIDTH//2-90,HEIGHT//2+77,240,50))

        display.flip()
    return(running_principal,running_jeu,retenter)

def menu_principal():

    global son
    global manette
    running_jeu=True
    running_principal=True
    menu_principal_running=True
    rectjouer=Rect(int(WIDTH*0.05),(int(HEIGHT*0.05+230)),355,90)
    rectniveau=Rect(int(WIDTH*0.05),(int(HEIGHT*0.05+330)),355,90)

    rectnivmoins=Rect(int(WIDTH*0.05+44),(int(HEIGHT*0.05+355)),45,45)

    rectnivnombre=Rect(int(WIDTH*0.05+int(355/3)),(int(HEIGHT*0.05+355)),int(355/3),int(90/2))

    rectnivplus=Rect(int(WIDTH*0.05+266),(int(HEIGHT*0.05+355)),45,45)

    rectson=Rect(int(WIDTH*0.05+53),(int(HEIGHT*0.05+435)),70,70)
    rectmanette=Rect(int(WIDTH*0.05+231),(int(HEIGHT*0.05+435)),70,70)

    recthistoire=Rect(int(WIDTH*0.05),(int(HEIGHT*0.05+520)),355,90)
    rectquitter=Rect(int(WIDTH*0.05),(int(HEIGHT*0.05+620)),355,90)

    text_jouer=police_menu.render(("              Jouer"), True, (0,200,0))
    text_nivnombre=police_menu.render(("niveau 0"), True, (0,0,0))
    text_nivmoins=police_menu.render(("  -"), True, (200,0,0))
    text_nivplus=police_menu.render((" +"), True, (0,200,0))
    text_histoire=police_menu.render(("           Histoire"), 0, (0,0,0))
    text_quitter=police_menu.render(("            Quitter"), True, (255, 124, 126))

    liste_niveau=["niveau 0","niveau 1","niveau 2","niveau 3","niveau 4","  hell"," heaven","  meca"]

    i=0
    while menu_principal_running==True :
        for evenement in event.get():
            if evenement.type== QUIT :
                menu_principal_running=False
                running_principal=False
                running_jeu=False

            if evenement.type == MOUSEBUTTONUP:
                if rectjouer.collidepoint(mouse.get_pos()):
                    menu_principal_running=False


                if rectnivmoins.collidepoint(mouse.get_pos()):
                    i=i-1
                    if i<0:
                        i=0
                    text_nivnombre=police_menu.render((str(liste_niveau[i])), True, (0,0,0))

                if rectnivplus.collidepoint(mouse.get_pos()):
                    i=i+1
                    if i>7:
                        i=7
                    text_nivnombre=police_menu.render(str(liste_niveau[i]), True, (0,0,0))

                if recthistoire.collidepoint(mouse.get_pos()):
                    webbrowser.open("html\\site_2.html")

                if rectquitter.collidepoint(mouse.get_pos()):
                    running_principal=False
                    running_jeu=False
                    menu_principal_running=False

                if rectson.collidepoint(mouse.get_pos()):
                    if rectson.collidepoint(mouse.get_pos()):
                        if son:
                            mixer.music.stop()
                            son=False
                        else:
                            mixer.music.play(-1)
                            son=True

                if rectmanette.collidepoint(mouse.get_pos()):
                    if manette:
                        manette=False
                    else:
                        nb_joysticks = joystick.get_count()
                        nb_joysticks = joystick.get_count()
                    if nb_joysticks > 0 :
                        mon_joystick = joystick.Joystick(0)
                        mon_joystick.init()
                        manette=True

        fenetre.blit(fond_menu,(0,0))
        draw.rect(fenetre,(1, 134, 0),(rectjouer),0)
        draw.rect(fenetre,(1, 104, 0),(rectjouer),4)

        draw.rect(fenetre,(255,255,255),(rectniveau),0)
        draw.rect(fenetre,(0,0,0),(rectniveau),4)

        draw.rect(fenetre,(255, 101, 108),(rectnivmoins),3)

        draw.rect(fenetre,(104, 255, 108),(rectnivplus),3)

        draw.rect(fenetre,(255,255,255),(recthistoire),0)
        draw.rect(fenetre,(0,0,0),(recthistoire),4)


        draw.rect(fenetre,(207, 57, 58),(rectquitter),0)
        draw.rect(fenetre,(111, 0, 8),(rectquitter),4)

        fenetre.blit(text_jouer,(rectjouer.left,rectjouer.top+25,0,0))
        fenetre.blit(text_nivnombre,(rectnivnombre))
        fenetre.blit(text_nivmoins,(rectnivmoins))
        fenetre.blit(text_nivplus,(rectnivplus))
        fenetre.blit(text_histoire,(recthistoire.left,recthistoire.top+25,0,0))
        fenetre.blit(text_quitter,(rectquitter.left,rectquitter.top+25,0,0))

        draw.rect(fenetre,(124, 126, 250),(int(WIDTH*0.05),(int(HEIGHT*0.05+425)),355,90))
        draw.rect(fenetre,(74, 76, 150),(int(WIDTH*0.05),(int(HEIGHT*0.05+425)),355,90),4)
        if son:
            fenetre.blit(son_on,(rectson))
        else:
            fenetre.blit(son_off,(rectson))
        if manette:
            fenetre.blit(manette_on,(rectmanette))
        else:
            fenetre.blit(manette_off,(rectmanette))
            display.flip()

    return(i,running_principal,running_jeu)

def menu_game_over(gagner):
    menu_running=True
    retenter=False
    global running_jeu
    global running_principal

    text_menu_retenter = police_menu.render(("Réessayer"), True, (255,255,255))
    rectretenter=Rect(WIDTH//4-120,HEIGHT//5,240,50)

    text_menu_menu = police_menu.render(("    Menu"), True, (255,255,255))
    rectmenu=Rect(WIDTH//2-120,HEIGHT//5,240,50)

    text_menu_quitter = police_menu.render(("   Quitter"), True, (255,255,255))
    rectquitter=Rect(3*WIDTH//4-120,HEIGHT//5,240,50)


    while menu_running:
        for evenement in event.get():

            if evenement.type== QUIT :
                running_jeu=False
                running_principal=False
                menu_running=False

            if evenement.type == MOUSEBUTTONUP:

                if rectretenter.collidepoint(mouse.get_pos()):
                    menu_running=False
                    running_jeu=False
                    retenter=True

                elif rectmenu.collidepoint(mouse.get_pos()):
                    running_jeu=False
                    menu_running=False

                elif rectquitter.collidepoint(mouse.get_pos()):
                    running_jeu=False
                    running_principal=False
                    menu_running=False


        draw.rect(fenetre,(0,0,0),rectretenter)
        draw.rect(fenetre,(100,100,100),rectretenter,4)

        draw.rect(fenetre,(0,0,0),rectmenu)
        draw.rect(fenetre,(100,100,100),rectmenu,4)

        draw.rect(fenetre,(0,0,0),rectquitter)
        draw.rect(fenetre,(100,100,100),rectquitter,4)

        fenetre.blit(text_menu_retenter,(WIDTH//4-90,HEIGHT//5+10))

        fenetre.blit(text_menu_menu,(WIDTH//2-90,HEIGHT//5+10))

        fenetre.blit(text_menu_quitter,(3*WIDTH//4-90,HEIGHT//5+10))

        if gagner:
            fenetre.blit(image_victory,(WIDTH//2-170,HEIGHT//2-150))
        else:
            fenetre.blit(image_game_over,(WIDTH//2-150,HEIGHT//2-150))

        display.flip()

    return(retenter,running_principal,running_jeu)


def perso_tirer(pos1,pos2):
    """ fonction qui actualise le cooldown du tir du personnage et tire si il atteint 0"""


    if perso_tir_cool[0]!=0:
        perso_tir_cool[0]-=1
    else:
        tirer(pos1,pos2,"boss",12,randint(perso_degats[0],perso_degats[1]),5,white,black)
        perso_tir_cool[0]=perso_tir_cool[1]

def wait_input():
    """ fige le jeu jusqu'a qu'on appuie sur une touche ou la souris"""
    continuer = True
    while continuer:
        for evenement in event.get():
            if evenement.type==KEYDOWN or evenement.type==MOUSEBUTTONDOWN or evenement.type==JOYBUTTONDOWN or evenement.type==JOYAXISMOTION:
                continuer=False









