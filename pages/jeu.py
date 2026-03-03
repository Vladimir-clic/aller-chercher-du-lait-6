import tkinter as tk
import time

from game_logic import *

class Jeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller


        self.zone_boutons = tk.Frame(self)
        self.zone_boutons.pack()

        self.vache_vars = {}
        self.temps = 0

        self.configure(bg="#2e2e2e")

        self.header = tk.Frame(self, bg="#040404")
        self.header.pack(fill="x")

        self.body = tk.Frame(self, bg="#2e2e2e")
        self.body.pack(expand=True, fill="both")

        self.shop = tk.Frame(self.body, bg="#252525")
        self.shop.pack(side="right", fill="y", padx=10)

        self.actions = tk.Frame(self.body, bg="#2e2e2e")
        self.actions.pack(side="left", expand=True)

        


    def refresh(self):

        # Nettoyer anciens boutons
        for widget in self.zone_boutons.winfo_children():
            widget.destroy()

        player = self.controller.joueur

        
        self.label = tk.Label(self.header, text="Bienvenue dans le jeu " + player.nom)
        self.label.pack()


        #crée un lien entre front et back pour incrémenter player.lait en direct
        self.lait_var = tk.StringVar()
        self.lait_var.set("litre de lait : " + str(player.lait))

        label = tk.Label(self.header, textvariable= self.lait_var, font=("Arial", 9))
        label.pack()

        #même chose pour l'argent
        self.argent_var = tk.StringVar()
        self.argent_var.set("Argent : " + str(player.argent) + " lacteuros")

        label = tk.Label(self.header, textvariable= self.argent_var, font=("Arial", 9))
        label.pack()

        #même chose pour le temps
        self.temps_var = tk.StringVar()
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")

        label = tk.Label(self.header, textvariable= self.temps_var, font=("Arial", 9))
        label.pack()

        


    #bouton pour obtenir du lait
        self.vache_img = tk.PhotoImage(file="images/vache1.png")

        self.bouton_vache = tk.Button(
            self.actions,
            image=self.vache_img,
            command=lambda: clicpourlait(player),
            bd=0
        )
        self.bouton_vache.pack(pady=20)
        

    #bouton pour vendre son lait
        tk.Button(
                self.actions,
                text="Vendre son lait",
                #command=achetervache(player, vache)
                command=lambda: self.vendre_lait(player)
            ).pack()
        
    




    #création d'un bouton pour chaque vaches
        for vache in player.vaches:

            #créer un lien entre back et front
            var = tk.StringVar()
            var.set(f"{vache.nom} (x {vache.nombre}) : {vache.prix} lacteuros")

            self.vache_vars[vache] = var

            tk.Button(
                self.shop,
                textvariable=var,
                command=lambda v=vache : self.acheter_vache(player, v)
            ).pack()

        #appel de la fonction qui actionne le lait/tour
        self.start_lait_par_seconde()


    def vendre_lait(self, player):
        vendrelait(player)

        # Mise à jour lait/argent si besoin
        self.lait_var.set("litre de lait : " + str(player.lait))
        self.argent_var.set("Argent : " + str(player.argent) + " lacteuros")
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")



    def acheter_vache(self, player, vache):
        if player.argent >= vache.prix :
            achetervache(player, vache)  # backend

            # Mise à jour du bouton correspondant
            self.vache_vars[vache].set(f"{vache.nom} (x {vache.nombre}) : {vache.prix} lacteuros")

        elif player.argent < vache.prix :
            print("tu n'as pas assez d'argent")


        # Mise à jour lait/argent si besoin
        self.lait_var.set("litre de lait : " + str(player.lait))
        self.argent_var.set("Argent : " + str(player.argent) + " lacteuros")
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")






    def start_lait_par_seconde(self):
        player = self.controller.joueur
        #incrémentation de lait par tour à 0
        self.laitpartour = 0

        #compter le lait par tour
        for v in player.vaches:
            self.laitpartour +=  v.lait * v.nombre
        player.lait += self.laitpartour

        #incrémente le temps de 1
        self.temps += 1
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")
        print(f"temps = {self.temps}")


        self.lait_var.set("litre de lait : " + str(player.lait))
        print(f"Tu as gagné {self.laitpartour} litre de lait")

        # relance dans 1000ms (1 seconde)
        self.after(1000, self.start_lait_par_seconde)

    