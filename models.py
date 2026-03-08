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
vache4 = vache(4,"Braford", 1200, 120, 0, "images/braford.png")
vache5 = vache(5,"Galloway Ceinturée", 15000, 500, 0, "images/galloway_ceinturee.png")
vache6 = vache(6,"Holstein", 200000, 1000, 0, "images/holstein.png")

listevache = [vache1, vache2, vache3, vache4, vache5, vache6]
