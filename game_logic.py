from models import listejoueur, listevache, vache, joueur
import time
import threading

def Create_caracter(nomdujoueur) :

    # Génération automatique de l'id
    if len(listejoueur) == 0:
        nouvel_id = 1
    else:
        nouvel_id = max(j.id for j in listejoueur) + 1

        
    joueur1 = joueur(nouvel_id, nomdujoueur, 3, [], 1, 0)
    listejoueur.append(joueur1)

    #for j in listejoueur : 
    for v in listevache :
        joueur1.vaches.append(v)

    print(f"Profil de {joueur1.nom} créé avec l'id {joueur1.id}")
    for i in joueur1.vaches :
        print(f"Ajout de {i.nom} au joueur")
    return joueur1




def achetervache(j, v) :
    #print(f"\n\n {j.nom} part à la ferme acheter une vache \n")
    print(v.nom)
    v.nombre = v.nombre + 1

    j.argent = j.argent - v.prix
    #print(f"Après la transaction, {j.nom} à {j.argent} lacteuros")
    print(f"Vous avez acheté une {v.nom}")
                    
def test():
    print("Test réussi")

def clicpourlait(j) :
    j.lait += 1
    print(j.lait)
    print("hello")




def laitpartour(j) :
    mon_thread = threading.Thread(target=laitpermanent(j, mon_thread))
    

def laitpermanent(j, thread):  
    thread.start()  
    while j.lait < 10000 :
        for k in j.vaches :
            j.lait = j.lait + (k.lait * k.nombre)
        print(j.lait)
        time.sleep(1)

    thread.join()
    
