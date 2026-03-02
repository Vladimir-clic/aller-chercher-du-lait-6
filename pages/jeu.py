import tkinter as tk
from game_logic import *

class Jeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        self.label = tk.Label(self, text="Bienvenue dans le jeu")
        self.label.pack()

        self.zone_boutons = tk.Frame(self)
        self.zone_boutons.pack()


    def refresh(self):

        # Nettoyer anciens boutons
        for widget in self.zone_boutons.winfo_children():
            widget.destroy()

        player = self.controller.joueur

        #crée un lien entre front et back
        self.lait_var = tk.StringVar()
        self.lait_var.set("litre de lait : " + str(player.lait))

        label = tk.Label(self, textvariable= self.lait_var, font=("Arial", 16))
        label.pack()

        tk.Button(
                self.zone_boutons,
                text="Vendre lait",
                #command=achetervache(player, vache)
                command=lambda: test2(player)
            ).pack()
        



        for vache in player.vaches:
            tk.Button(
                self.zone_boutons,
                text=vache.nom,
                command=lambda: achetervache(player, vache)
            ).pack()