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
vache4 = vache(4,"Braford", 5100, 25, 0, "images/braford.png")
vache5 = vache(5,"Galloway Ceinturée", 25000, 50, 0, "images/galloway_ceinturee.png")
vache6 = vache(6,"Holstein", 100000, 220, 0, "images/holstein.png")
vache7 = vache(7,"Nélore", 700000, 500, 0, "images/nelore.png")

listevache = [vache1, vache2, vache3, vache4, vache5, vache6, vache7]

class recrue : 
    def __init__(self, id, prenom, nom, age, sexe, prix, clic, countnaissance, peremption, img):
        self.id = id
        self.prenom = prenom 
        self.nom = nom
        self.age = age
        self.sexe = sexe
        self.prix = prix #prix d'emploi
        self.clic = clic #capacité de clic
        self.countnaissance = countnaissance
        self.peremption = peremption #temps de vie si pas acheté
        self.img = img    

#recrue1 = recrue(1, "Johnny", 19, 10, random.randrange(10),0, 7, "images/recrue1.png")
#recrue2 = recrue(2, "Tonny", 19, 10, 1, 0, 8, "images/recrue1.png")

listerecrue = []
#laitparclic = 1
dictrecrue = {
    #1 : recrue1, 2 : recrue2
    }

listesexe = ["M", "F"]

listenom = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent",
    "Simon", "Michel", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel", "Fournier", "Girard",
    "Bonnet", "Dupont", "Lambert", "Fontaine", "Rousseau", "Vincent", "Muller", "Lefevre", "Faure", "Andre",
    "Mercier", "Blanc", "Guerin", "Boyer", "Garnier", "Chevalier", "Francois", "Legrand", "Gauthier", "Garcia",
    "Perrin", "Robin", "Clement", "Morin", "Nicolas", "Henry", "Roussel", "Mathieu", "Gautier", "Masson",
    "Marchand", "Duval", "Denis", "Dumont", "Marie", "Lemaire", "Noel", "Meyer", "Dufour", "Meunier",
    "Brun", "Blanchard", "Giraud", "Joly", "Riviere", "Lucas", "Brunet", "Gaillard", "Barbier", "Arnaud",
    "Martinez", "Gerard", "Roche", "Renard", "Schmitt", "Roy", "Leroux", "Colin", "Vidal", "Caron",
    "Picard", "Roger", "Fabre", "Aubert", "Lemoine", "Renaud", "Dumas", "Lacroix", "Olivier", "Philippe",
    "Bourgeois", "Pierre", "Benoit", "Rey", "Leclerc", "Payet", "Rolland", "Leclercq", "Guillaume", "Lecomte"]

listeprenomM = ["Aaron", "Abel", "Adam", "Adrien", "Alain", "Albert", "Alexandre", "Alexis", "Amine", "André",
    "Anthony", "Antoine", "Arnaud", "Arthur", "Baptiste", "Benjamin", "Bruno", "Cédric", "Charles", "Christian",
    "Christophe", "Clément", "Damien", "Daniel", "David", "Denis", "Dylan", "Édouard", "Elias", "Émile",
    "Enzo", "Étienne", "Fabien", "Fabrice", "Florian", "Franck", "François", "Gabriel", "Gaël", "Gaspard",
    "Georges", "Grégory", "Guillaume", "Hugo", "Ibrahim", "Isaac", "Ismaël", "Jacques", "Jean", "Jérôme",
    "Jérémy", "Jonathan", "Jordan", "Joseph", "Jules", "Julien", "Karim", "Kevin", "Léo", "Léon",
    "Louis", "Lucas", "Luc", "Ludovic", "Malik", "Marc", "Mathieu", "Mathis", "Matthieu", "Maxime",
    "Mehdi", "Michaël", "Mohamed", "Nabil", "Nicolas", "Noah", "Olivier", "Omar", "Pascal", "Paul",
    "Philippe", "Pierre", "Quentin", "Rachid", "Raphaël", "Rayane", "Romain", "Samuel", "Sébastien", "Simon",
    "Sofiane", "Stéphane", "Théo", "Thomas", "Tony", "Valentin", "Victor", "Vincent", "Yanis", "Youssef"]

listeprenomF = ["Aaliyah", "Adèle", "Agathe", "Aïcha", "Alexandra", "Alexia", "Alice", "Aline", "Amandine", "Amélie",
    "Anaïs", "Anissa", "Anna", "Anne", "Anouk", "Apolline", "Ariana", "Audrey", "Aurélie", "Aurore",
    "Aya", "Barbara", "Béatrice", "Bérénice", "Brigitte", "Camille", "Carla", "Carmen", "Caroline", "Cassandra",
    "Catherine", "Cécile", "Charlotte", "Chloé", "Christelle", "Claire", "Clara", "Claudia", "Clémence", "Colette",
    "Coralie", "Delphine", "Diane", "Éléonore", "Élisa", "Élise", "Élodie", "Emma", "Estelle", "Eva",
    "Fatima", "Florence", "Gabrielle", "Gaëlle", "Hajar", "Hélène", "Inès", "Irina", "Isabelle", "Jade",
    "Jeanne", "Jennifer", "Jessica", "Julie", "Justine", "Karima", "Khadija", "Lara", "Laura", "Léa",
    "Léna", "Lila", "Lina", "Lisa", "Louise", "Lucie", "Manon", "Margaux", "Marie", "Marina",
    "Mélanie", "Mélissa", "Myriam", "Nadia", "Naïma", "Nathalie", "Nina", "Noémie", "Nora", "Océane",
    "Pauline", "Rachel", "Sabrina", "Sarah", "Sonia", "Sophie", "Stéphanie", "Vanessa", "Victoria", "Yasmine"]

listeimageF = [
    "images/recrue10.png"
    ]

listeimageM = [
    "images/recrue1.png",
    "images/recrue2.png",
    "images/recrue3.png",
    "images/recrue4.png",
    "images/recrue5.png",
    "images/recrue6.png",
    "images/recrue7.png",
    "images/recrue8.png",
    "images/recrue9.png",
    "images/recrue11.png",
    "images/recrue12.png"
]



