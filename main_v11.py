from init_variable import *
from pygame import *
from math import*
from random import *
from classe_fonction_V3 import *





while running_principal:


    boss=Boss() #on cree un objet de la classe Boss qu'on appelle boss
    running_jeu=True
    if not retenter:
        niveau,running_principal,running_jeu=menu_principal()
    else:
        retenter=0


    #en fonction du niveau choisit, on modifie de nombreuses caracteristique
    if niveau==0:
        vie_perso=[700,700]
        perso_tir_cool=[0,4]
        VITESSE=8.5
        perso_degats[:]=[14,16]
        liste_bouclier_perso=[1,1,1,1,1,1,1,1]

        boss.vitesse=3.5
        boss.vie=[2000,2000]
        boss.image=transform.scale(image.load("images/squealer.PNG"),(150,194))
        boss.rect=boss.image.get_rect()
        boss.cool_tir3=[0,100,3]
        boss.cool_tir2=[0,100,10]
        boss.cool_tir4=[0,50,4]
        boss.vitesse_rotation=0.007

        boss.liste_cooldown=[150,60,200,60,240,350,200,120,100,60,600,60,90,900,70,120]
        boss.liste_phase=[

        [boss.tir2,boss.va_pos_visee],
        [boss.va_pos_visee],
        [boss.tir3,boss.va_pos_visee],
        [],
        [boss.tir2],
        [boss.spe2_init],
        [boss.spe2,boss.va_pos_visee2],
        [],
        [boss.spe2_stop,boss.tir3,boss.va_pos_visee],
        [],
        [boss.spe3_init,boss.va_pos_visee2],
        [boss.spe3_stop,boss.vise_mid],
        [boss.spe4_init1],
        [boss.spe4_init2,boss.tir4],
        [boss.spe4_stop],
        [boss.tir2]

        ]

    elif niveau==1:
        vie_perso=[250,250]
        perso_tir_cool=[0,4]
        VITESSE=8.5
        perso_degats[:]=[12,14]
        liste_bouclier_perso=[1,1,1,1,1]

        boss.vitesse=5
        boss.vie=[2500,2500]
        boss.image=transform.scale(image.load("images/squealer.PNG"),(150,194))
        boss.rect=boss.image.get_rect()
        boss.cool_tir3=[0,70,3]
        boss.cool_tir2=[0,75,10]
        boss.cool_tir4=[0,35,4]
        boss.vitesse_rotation=0.01

        boss.liste_cooldown=[150,60,200,60,240,200,200,120,100,60,600,60,90,900,70,120]
        boss.liste_phase=[[boss.tir1,boss.va_pos_visee],[boss.va_pos_visee],[boss.tir3,boss.va_pos_visee],[],[boss.tir2],[boss.spe2_init],[boss.spe2,boss.va_pos_visee2],[],[boss.spe2_stop,boss.tir3,boss.va_pos_visee],[],[boss.spe3_init,boss.va_pos_visee2],[boss.spe3_stop,boss.vise_mid],[boss.spe4_init1],[boss.spe4_init2,boss.tir4],[boss.spe4_stop],[boss.tir2]]


    elif niveau==2:
        vie_perso=[150,150]
        perso_tir_cool=[0,5]
        VITESSE=8
        perso_degats[:]=[11,13]

        boss.vitesse=7
        boss.vie=[3000,3000]
        boss.image=transform.scale(image.load("images/squealer.PNG"),(110,142))
        boss.rect=boss.image.get_rect()
        boss.cool_tir3=[0,40,5]
        boss.cool_tir2=[0,60,40]
        boss.cool_tir4=[0,19,7]
        boss.vitesse_rotation=0.021

        boss.liste_cooldown=[30,200,30,240,100,200,60,100,600,50,80,900,40,70,120]
        boss.liste_phase=[[boss.va_pos_visee],[boss.tir3,boss.va_pos_visee],[],[boss.tir2],[boss.spe2_init],[boss.spe2,boss.va_pos_visee2],[boss.spe2_stop],[boss.tir3,boss.va_pos_visee],[boss.spe3_init,boss.va_pos_visee2],[boss.spe3_stop,boss.vise_mid],[boss.spe4_init1],[boss.spe4_init2,boss.tir4],[boss.spe4_stop],[boss.regen,boss.tir1],[boss.tir2]]

    elif niveau==3:
        vie_perso=[100,100]
        perso_tir_cool=[0,5]
        VITESSE=7.8
        perso_degats[:]=[10,12]
        liste_bouclier_perso=[1,1]

        boss.vie=[4000,4000]
        boss.vitesse=7.5
        boss.image=transform.scale(image.load("images/squealer.PNG"),(100,129))
        boss.rect=boss.image.get_rect()
        boss.cool_tir3=[0,35,7]
        boss.cool_tir2=[0,60,45]
        boss.cool_tir4=[0,13,7]

        boss.liste_cooldown=[200,30,240,90,180,60,100,500,50,80,600,40,120,120]
        boss.liste_phase=[[boss.tir3,boss.va_pos_visee],[],[boss.tir2],[boss.spe2_init],[boss.spe2,boss.va_pos_visee],[boss.spe2_stop],[boss.tir3,boss.va_pos_visee],[boss.spe3_init,boss.va_pos_visee2,boss.tir4],[boss.spe3_stop,boss.vise_mid,boss.tir3],[boss.spe4_init1],[boss.spe4_init2,boss.tir4],[boss.spe4_stop,boss.tir3],[boss.tir2,boss.va_pos_visee2],[boss.regen,boss.va_pos_visee2,boss.tir1]]

    elif niveau==4:
        fond=transform.scale(image.load("images/sable.jpg"),(WIDTH,HEIGHT))
        vie_perso=[50,50]
        perso_tir_cool=[0,3]
        VITESSE=8
        perso_degats[:]=[8,10]
        liste_bouclier_perso=[1]

        boss.vitesse=7.75
        boss.image=transform.scale(image.load("images/squealer.PNG"),(100,129))
        boss.rect=boss.image.get_rect()
        boss.vie=[5000,5000]
        boss.cool_tir3=[0,30,12]
        boss.cool_tir2=[0,58,47]
        boss.cool_tir4=[0,9,5]
        boss.vitesse_rotation=0.027

        boss.liste_cooldown=[200,240,90,180,70,120,500,50,50,600,40,120]
        boss.liste_phase=[[boss.tir3,boss.va_pos_visee],[boss.tir2,boss.va_pos_visee2],[boss.spe2_init,boss.va_pos_visee,boss.va_pos_visee2],[boss.spe2,boss.spe2,boss.va_pos_visee],[boss.spe2_stop],[boss.tir3,boss.tir3,boss.tir2],[boss.spe3_init,boss.va_pos_visee2,boss.tir4],[boss.vise_mid,boss.tir3],[boss.spe4_init1,boss.tir4],[boss.spe4_init2,boss.tir4],[boss.spe4_stop,boss.tir3],[boss.spe3_stop,boss.tir2,boss.va_pos_visee2]]

    elif niveau==5:
        fond=transform.scale(image.load("images/hell.jpg"),(WIDTH,HEIGHT))
        vie_perso=[13,13]
        perso_tir_cool=[0,3]
        VITESSE=9
        perso_degats[:]=[7,9]
        liste_bouclier_perso=[1]


        boss.image=transform.scale(image.load("images/squealer.PNG"),(75,97))
        boss.rect=boss.image.get_rect()
        boss.vitesse=8.25
        boss.vie=[6666,6666]
        boss.cool_tir3=[0,2,1]
        boss.cool_tir2=[0,68,58]
        boss.cool_tir4=[0,9,9]
        boss.vitesse_rotation=0.029

        boss.liste_cooldown=[200,240,60,90,130,120,30,500,50,50,600,40,200,120]
        boss.liste_phase=[[boss.tir3,boss.va_pos_visee],[boss.tir2,boss.va_pos_visee],[boss.spe2_init,boss.spe1_init],[boss.spe2_init,boss.va_pos_visee,boss.va_pos_visee2],[boss.spe2,boss.spe2,boss.va_pos_visee],[boss.spe2_stop,boss.tir3,boss.tir3,boss.tir2],[boss.spe2_stop,boss.tir3,boss.tir3,boss.tir2,boss.tir1],[boss.spe3_init,boss.va_pos_visee2,boss.tir4,boss.tir4],[boss.vise_mid,boss.tir3,boss.tir1],[boss.spe4_init1,boss.tir4,boss.tir4],[boss.spe4_init2,boss.tir4,boss.tir4],[boss.spe4_stop,boss.tir3],[boss.spe1_init,boss.tir1,boss.tir4],[boss.spe3_stop,boss.tir2,boss.va_pos_visee2,boss.regen]]

        fond=transform.scale(image.load("images/hell.jpg"),(WIDTH,HEIGHT))

    elif niveau==6:
        vie_perso=[1,1]
        perso_tir_cool=[0,3]
        VITESSE=9
        perso_degats[:]=[8,10]
        liste_bouclier_perso=[1,1]


        boss.image=transform.scale(image.load("images/squealer.PNG"),(75,97))
        boss.rect=boss.image.get_rect()
        boss.vitesse=4.5
        boss.vie=[3333,3333]
        boss.cool_tir3=[0,25,1]
        boss.cool_tir2=[0,68,58]
        boss.cool_tir4=[0,9,9]

        boss.liste_cooldown=[100,100,20,100,20,100,60,100,10,100,10,100,10,100,2,60,100,10,100,10,60,10,100,80]
        boss.liste_phase=[[boss.vise_mid,boss.regen],[boss.spe1_init],[boss.tir3],[boss.spe1_init,boss.tir1],[boss.tir1],[boss.spe1_init,boss.tir1],[boss.va_pos_visee2,boss.tir1],[boss.spe1_init],[],[boss.spe1_init],[boss.tir3],[boss.spe1_init],[],[boss.spe1_init],[boss.vise_mid],[boss.va_pos_visee2],[boss.spe1_init],[],[boss.spe1_init],[],[boss.spe1_init,boss.spe1],[],[boss.spe1_init],[boss.spe3_init]]

        fond=transform.scale(image.load("images/heaven.jpg"),(WIDTH,HEIGHT))

    elif niveau==7:
        vie_perso=[100,100]
        perso_tir_cool=[0,3]
        VITESSE=9
        perso_degats[:]=[6,8]
        liste_bouclier_perso=[1,1]


        boss.image=transform.scale(image.load("images/squealer.PNG"),(150,194))
        boss.rect=boss.image.get_rect()
        boss.vitesse=4.5
        boss.vie=[4826,4826]
        boss.cool_tir3=[0,25,1]
        boss.cool_tir2=[0,68,58]
        boss.cool_tir4=[0,9,9]
        boss.vitesse_rotation=0.024

        boss.liste_cooldown=[50,50,100,300,50,100,500,100]
        boss.liste_phase=[[boss.regen],[],[boss.spe5_init,boss.spe6_init],[boss.spe5,boss.spe6,boss.va_pos_visee],[boss.spe5,boss.spe6,boss.vise_mid,boss.spe4_init1],[],[boss.spe4_init2,boss.spe5,boss.spe6],[boss.spe4_stop]]

        fond=transform.scale(image.load("images/meca.jpg"),(WIDTH,HEIGHT))

    if running_jeu:
        boss.compteur_cooldown=boss.liste_cooldown[boss.compteur_phase]
        boss.liste_action=boss.liste_phase[boss.compteur_phase][:]
        boss.rect.topleft=(boss.pos[0],boss.pos[1])
        boss.pos_visee=[boss.rect.centerx,boss.rect.centery]
        bouclier_perso=False
        liste_projectile[:]=[]




        fenetre.blit(fond, (0,0))
        fenetre.blit(image_perso, rect_perso.topleft)
        fenetre.blit(boss.image, boss.rect.topleft)

        draw.rect(fenetre,(0,50,0),(20,HEIGHT-50,302,20))
        draw.rect(fenetre,(0,150,0),(21,HEIGHT-49,int(300*vie_perso[0]/vie_perso[1]),18))
        text_vie1 = basicfont.render(str(vie_perso[0])+"/"+str(vie_perso[1]), True, (50,100,50))
        fenetre.blit(text_vie1,(135,HEIGHT-49,20,20))


        draw.rect(fenetre,(50,0,0),(99,20,WIDTH-198,22))
        draw.rect(fenetre,(150,0,0),(100,21,int((WIDTH-200)*boss.vie[0]/boss.vie[1]),20))
        text_vie2 = basicfont.render(str(boss.vie[0])+"/"+str(boss.vie[1]), True, (100,60,60))
        fenetre.blit(text_vie2,(WIDTH//2-10,22,20,20))

        for point in range (len(liste_bouclier_perso)):

            draw.circle(fenetre,(150, 215, 255),(25+25*point,HEIGHT-70),10)
            draw.circle(fenetre,(255,255,255),(25+25*point,HEIGHT-70),9)




        display.flip()
        wait_input()



    while running_jeu:

        clock.tick(FPS)
        for evenement in event.get():
            if evenement.type == KEYDOWN:

                if evenement.key == K_ESCAPE:
                    running_principal,running_jeu,retenter=menu_echap()
                if evenement.key == K_SPACE:
                    for i in range(len(liste_bouclier_perso)-1,-1,-1):
                        if liste_bouclier_perso[i]==1:
                            bouclier_perso=True
                            liste_bouclier_perso[i]=0
                            taille_bouclier_perso=6
                            break

            if evenement.type== QUIT :
                running_jeu=False
                running_principal=False



        perso_update(pos_perso)
        rect_perso.topleft=(pos_perso[0],pos_perso[1])

        boss.update()



        for projectile in liste_projectile:
            projectile.update()



        fenetre.blit(fond, (0,0))

        if boss.spe2_on:
            fenetre.blit(oasis,(boss.zone_spe2[0],boss.zone_spe2[1]))

        if boss.spe5_on==True:
            for pos in boss.liste_spe5:
                fenetre.blit(tourelle_bleu,(pos[0]-15,pos[1]-15))

        if boss.spe6_on==True:
            for pos in boss.liste_spe6:
                fenetre.blit(tourelle_rouge,(pos[0]-15,pos[1]-15))

        fenetre.blit(image_perso, rect_perso.topleft)
        fenetre.blit(boss.image, boss.rect.topleft)



        for projectile in liste_projectile:
            draw.circle(fenetre,projectile.couleur1,(int(projectile.position[0]),int(projectile.position[1])),projectile.taille)
            draw.circle(fenetre,projectile.couleur2,(int(projectile.position[0]),int(projectile.position[1])),projectile.taille,2)


            if distance(projectile.position,rect_perso.center)<projectile.taille+rect_perso.width/2 and projectile.cible=="perso":
                vie_perso[0]-=projectile.degat
                liste_projectile.remove(projectile)
            if projectile.cible=="boss" and boss.rect.collidepoint(projectile.position[0],projectile.position[1]):
                liste_projectile.remove(projectile)
                boss.vie[0]-=projectile.degat

        if boss.spe3_on:

            for boule in boss.liste_boule_poison:
                d=distance([boule[0],boule[1]],[boss.rect.centerx,boss.rect.centery])
                if d<boss.taille_rond1-boule[2] or d>boss.taille_rond2+boule[2]:
                    draw.circle(fenetre,(19, 205, 105),(boule[0],boule[1]),boule[2])
            if boss.taille_rond1>10:
                draw.circle(fenetre,(225, 223, 0),(boss.rect.centerx,boss.rect.centery),boss.taille_rond1,10)
            draw.circle(fenetre,(254, 223, 0),(boss.rect.centerx,boss.rect.centery),boss.taille_rond2,10)

            if distance([rect_perso.centerx,rect_perso.centery],[boss.rect.centerx,boss.rect.centery])+(rect_perso.width/2)>boss.taille_rond2 or distance([rect_perso.centerx,rect_perso.centery],[boss.rect.centerx,boss.rect.centery])-(rect_perso.width/2)<boss.taille_rond1:
                if not randint(0,4):
                    vie_perso[0]-=1

        if boss.spe4_on==1:
            x=boss.rect.centerx
            y=boss.rect.centery


            for facteur_pi in range(0,4):
                add_angle=facteur_pi*pi/2
                draw.circle(fenetre,(200,100,200),(boss.rect.centerx,boss.rect.centery),100,3)
                draw.line(fenetre,(200,100,200),(x+100*cos(boss.angle_spe4+add_angle),y+100*sin(boss.angle_spe4+add_angle)),(x+1000*cos(boss.angle_spe4+add_angle),y+1000*sin(boss.angle_spe4+add_angle)),3)


        elif boss.spe4_on==2:
            draw.circle(fenetre,(255,100,0),(boss.rect.centerx,boss.rect.centery),100,15)
            draw.circle(fenetre,(155,0,0),(boss.rect.centerx,boss.rect.centery),95,3)
            x=boss.rect.centerx
            y=boss.rect.centery
            d=int(distance([rect_perso.centerx,rect_perso.centery],[x,y]))
            if d-rect_perso.width/2 <100:
                vie_perso[0]-=1

            for facteur_pi in range(0,4):
                add_angle=facteur_pi*pi/2

                draw.line(fenetre,(255,100,0),(x+100*cos(boss.angle_spe4+add_angle),y+100*sin(boss.angle_spe4+add_angle)),(x+1000*cos(boss.angle_spe4+add_angle),y+1000*sin(boss.angle_spe4+add_angle)),15)
                draw.line(fenetre,(155,0,0),(x+95*cos(boss.angle_spe4+add_angle),y+95*sin(boss.angle_spe4+add_angle)),(x+1000*cos(boss.angle_spe4+add_angle),y+1000*sin(boss.angle_spe4+add_angle)),3)

                if distance([x+d*cos(boss.angle_spe4+add_angle),y+d*sin(boss.angle_spe4+add_angle)],[rect_perso.centerx,rect_perso.centery])-rect_perso.width/2<0:
                    vie_perso[0]-=1





        draw.rect(fenetre,(0,50,0),(20,HEIGHT-50,302,20))
        draw.rect(fenetre,(0,150,0),(21,HEIGHT-49,int(300*vie_perso[0]/vie_perso[1]),18))

        text_vie1 = basicfont.render(str(vie_perso[0])+"/"+str(vie_perso[1]), True, (50,100,50))
        fenetre.blit(text_vie1,(135,HEIGHT-49,20,20))


        draw.rect(fenetre,(50,0,0),(99,20,WIDTH-198,22))
        draw.rect(fenetre,(150,0,0),(100,21,int((WIDTH-200)*boss.vie[0]/boss.vie[1]),20))

        text_vie2 = basicfont.render(str(boss.vie[0])+"/"+str(boss.vie[1]), True, (100,60,60))
        fenetre.blit(text_vie2,(WIDTH//2-10,22,20,20))

        if bouclier_perso==True:
            draw.circle(fenetre,(150, 215, 255),rect_perso.center,taille_bouclier_perso,5)
            taille_bouclier_perso+=15

            for projectile in liste_projectile:
                if distance(rect_perso.center,projectile.position)<taille_bouclier_perso+projectile.taille:
                    if projectile.cible=="perso":
                        liste_projectile.remove(projectile)

            if taille_bouclier_perso>200:
                bouclier_perso=False

        for point in range (len(liste_bouclier_perso)):

            if liste_bouclier_perso[point]==1:
                draw.circle(fenetre,(150, 215, 255),(25+25*point,HEIGHT-70),10)
                draw.circle(fenetre,(255,255,255),(25+25*point,HEIGHT-70),9)
            else:
                draw.circle(fenetre,(0, 0, 0),(25+25*point,HEIGHT-70),10)
                draw.circle(fenetre,(100,100,100),(25+25*point,HEIGHT-70),9)

        if manette:
            draw.circle(fenetre,(50,0,0),(round(rect_perso.centerx+mon_joystick.get_axis(4)*100),round(rect_perso.centery+mon_joystick.get_axis(3)*100)),7)
            draw.line(fenetre,(150,0,0),(-3+round(rect_perso.centerx+mon_joystick.get_axis(4)*100),3+round(rect_perso.centery+mon_joystick.get_axis(3)*100)),((3+round(rect_perso.centerx+mon_joystick.get_axis(4)*100)),-3+round(rect_perso.centery+mon_joystick.get_axis(3)*100)),3)
            draw.line(fenetre,(150,0,0),(3+round(rect_perso.centerx+mon_joystick.get_axis(4)*100),3+round(rect_perso.centery+mon_joystick.get_axis(3)*100)),((-3+round(rect_perso.centerx+mon_joystick.get_axis(4)*100)),-3+round(rect_perso.centery+mon_joystick.get_axis(3)*100)),3)



        display.flip()

        if vie_perso[0]<=0:
            retenter,running_principal,running_jeu=menu_game_over(False)
        if boss.vie[0]<=0:
            retenter,running_principal,running_jeu=menu_game_over(True)


quit()
