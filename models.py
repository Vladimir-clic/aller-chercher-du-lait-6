#initialisation de la classe joueur
class joueur :
    def __init__(self, id, nom, argent, vaches, jour, lait):
        self.id = id
        self.nom = nom
        self.argent = argent
        self.vaches = vaches
        self.jour = jour
        self.lait = lait

listejoueur = []

#initialisation de la classe vache
class vache :
    def __init__(self, id, nom, prix, lait, nombre):
        self.id = id
        self.nom = nom 
        self.prix = prix
        self.lait = lait
        self.nombre = nombre

vache1 = vache(1,"Vache normale", 3, 1, 0)
vache2 = vache(2,"Vache qualitative", 7, 2, 0)
vache3 = vache(3,"Vache d'élite", 32, 4, 0)

listevache = [vache1, vache2, vache3]
