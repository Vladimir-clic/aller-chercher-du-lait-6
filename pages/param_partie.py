import tkinter as tk
from game_logic import Create_caracter
from pages.jeu import Jeu

class Param_partie(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Paramètre de la partie", font=("Arial", 16))
        label.pack()

        entry = tk.Entry(self)
        entry.pack()

        # label pour afficher le résultat
        label_resultat = tk.Label(self, text="")
        label_resultat.pack()


        # fonction appelée quand on clique
        def valider():
            nom = entry.get()  # récupère ce qui est tapé

            controller.joueur = Create_caracter(nom)
            controller.show_frame(Jeu)
            
            
            

        # bouton
        tk.Button(self, text="Valider", command=valider).pack()