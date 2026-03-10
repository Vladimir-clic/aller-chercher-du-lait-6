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




def clicpourlait(j, laitparclic) :
    for recrue in listerecrue:
        j.lait+= recrue.clic
    j.lait += 1
    print(f"+ {laitparclic}")


def vendrelait(j):
    j.argent += j.lait
    j.lait = 0


#pas parfait, à continuer
def simplificateur_temps(temps):

    minutes = int(temps/60)
    
    if minutes < 1 :
        return str(temps) + "s"
    else :
        return str(minutes) + "min"
    


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
def apparition_recrue(temps):
    chiffre = temps % 10
    randomnumber = random.randrange(10)
    print(f"nombre aléatoire : {randomnumber} contre {chiffre}")
    if chiffre == random.randrange(10) :

        print("création d'une recrue")
        
        if len(dictrecrue) == 0:
            id = 1
        else :
            id = max(dictrecrue.keys()) + 1

        randomrecrue = recrue(id, #id
                              "Randomrecrue", #prenom
                              listenom[random.randrange(len(listenom))], #nom
                              random.randint(18,60), #age
                              listesexe[random.randint(0,1)], #sexe
                              random.randrange(1000), #prix
                              random.randrange(10), #clic
                              0, #countnaissance
                              random.randint(10, 30), #péremption
                              "none") #image
        
        if randomrecrue.sexe == "M" :
            randomrecrue.prenom = listeprenomM[random.randrange(len(listeprenomM))]
            randomrecrue.img = listeimageM[random.randrange(len(listeimageM))]

        elif randomrecrue.sexe == "F" :
            randomrecrue.prenom = listeprenomF[random.randrange(len(listeprenomF))]
            randomrecrue.img = listeimageF[random.randrange(len(listeimageF))]

        
        print(f"Recrue {randomrecrue.nom} avec l'id {randomrecrue.id}")
        dictrecrue[randomrecrue.id] = randomrecrue
        reponse = True

    else:
        reponse = False
    return reponse
    

def suppression_recrue():
    suppression_effectuee = False
    for id in list(dictrecrue):
        r = dictrecrue[id]
        if r.countnaissance >= r.peremption:
            del dictrecrue[id]
            suppression_effectuee = True

        else:
            r.countnaissance += 1
    return suppression_effectuee
    