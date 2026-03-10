#initialisation de la classe joueur
import random

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
    def __init__(self, id, nom, prix, lait, nombre, img):
        self.id = id
        self.nom = nom 
        self.prix = prix
        self.lait = lait
        self.nombre = nombre
        self.img = img


vache1 = vache(1,"Charolaise", 10, 1, 0, "images/charolaise.png")
vache2 = vache(2,"Limousine", 100, 3, 0, "images/limousine.png")
vache3 = vache(3,"Blanc-Bleu-Belge", 700, 10, 0, "images/blanc_bleu_belge.png")
vache4 = vache(4,"Braford", 15000, 25, 0, "images/braford.png")
vache5 = vache(5,"Galloway Ceinturée", 250000, 50, 0, "images/galloway_ceinturee.png")
vache6 = vache(6,"Holstein", 1000000, 120, 0, "images/holstein.png")
vache7 = vache(7,"Nélore", 50000000, 300, 0, "images/nelore.png")

listevache = [vache1, vache2, vache3, vache4, vache5, vache6, vache7]

class recrue : 
    def __init__(self, id, nom, age, prix, clic, countnaissance, peremption, img):
        self.id = id
        self.nom = nom 
        self.age = age
        self.prix = prix #prix d'emploi
        self.clic = clic #capacité de clic
        self.countnaissance = countnaissance
        self.peremption = peremption #temps de vie si pas acheté
        self.img = img    

recrue1 = recrue(1, "Johnny", 19, 10, random.randrange(10),0, 7, "images/recrue1.png")
recrue2 = recrue(2, "Tonny", 19, 10, 1, 0, 8, "images/recrue1.png")

listerecrue = []
#laitparclic = 1
dictrecrue = {1 : recrue1, 2 : recrue2}



