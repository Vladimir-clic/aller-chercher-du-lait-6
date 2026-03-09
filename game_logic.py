from models import *
import time
import threading
import random

def test():
    print("Test réussi")



def Create_caracter(nomdujoueur) :

    # Génération automatique de l'id
    if len(listejoueur) == 0:
        nouvel_id = 1
    else:
        nouvel_id = max(j.id for j in listejoueur) + 1

        
    joueur1 = joueur(nouvel_id, nomdujoueur, 0, [], 1, 0)
    listejoueur.append(joueur1)

    #for j in listejoueur : 
    for v in listevache :
        joueur1.vaches.append(v)

    print(f"Profil de {joueur1.nom} créé avec l'id {joueur1.id}")
    for i in joueur1.vaches :
        print(f"Ajout de {i.nom} au joueur")
    return joueur1




def achetervache(j, v) :
    
    #on ajoute une vache
    v.nombre = v.nombre + 1

    #on retire l'argent
    j.argent = j.argent - v.prix

    #on incrémente le prix de la vache
    v.prix += round(v.prix/2)


    #témoin console
    print("------------------------------------------")
    print(f"Vous avez acheté une {v.nom}")
    print(f"{v.nom} x {v.nombre}")
    print(f"Le prix de {v.nom} à augmenté de {v.prix}, elle coute maintenant {v.prix}")
    print(f"le joueur à {j.argent} lacteuros")
    print("------------------------------------------")




def clicpourlait(j) :
    j.lait += 1
    print("+ 1")


def vendrelait(j):
    j.argent += j.lait
    j.lait = 0

def simplificateur(argent):
    strargent = str(argent)
    listechiffre = list(strargent)

    if len(listechiffre) > 6:
        for i in range(5):
            del listechiffre[-1]
        listechiffre.append(listechiffre[-1])
        listechiffre[-2] = ","

        nombre = ''.join(listechiffre)
        return(nombre + " M")
    
    elif len(listechiffre) > 3:
        for i in range(2):
            del listechiffre[-1]

        listechiffre.append(listechiffre[-1])
        listechiffre[-2] = ","
        nombre = ''.join(listechiffre)
        return(nombre + " k")

    elif len(listechiffre) <= 3 :
        nombre = ''.join(listechiffre)
        return(nombre)


#création aléatoire et disparition de recrue

def apparition_recrue(self, player):
    listesecondes = len(player.temps)
    if listesecondes[-1] == random.randrange(15) :
        recruealeatoire = recrue(1, "Johnny", 19, 10, random.randrange(10), 5, "images/recrue1.png")

    
    
