from models import listejoueur, listevache, vache, joueur

class Create_caracter :
    def __init__(self, nomdujoueur):     

        # Génération automatique de l'id
        if len(listejoueur) == 0:
            nouvel_id = 1
        else:
            nouvel_id = max(j.id for j in listejoueur) + 1

        
        joueur1 = joueur(nouvel_id, nomdujoueur, 3, [], 1, 0)
        listejoueur.append(joueur1)

        for j in listejoueur : 
            for v in listevache :
                j.vaches.append(v)

        print(f"Profil de {joueur1.nom} créé avec l'id {joueur1.id}")
        for i in joueur1.vaches :
            print(f"Ajout de {i.nom} au joueur")
        