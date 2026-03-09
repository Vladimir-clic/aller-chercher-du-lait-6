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
        self.laitpartour = 0

        #mettre des types 1
        self.configure(bg="#2e2e2e")

        self.header = tk.Frame(self, bg="#040404")
        self.header.pack(fill="x")

        self.body = tk.Frame(self, bg="#2e2e2e")
        self.body.pack(expand=True, fill="both")

        self.actions = tk.Frame(self.body, bg="#2e2e2e")
        self.actions.pack(side="left", expand=True)




        self.shop1 = tk.Frame(self.body, bg="#252525")
        self.shop1.pack(side="right", fill="y", padx=10)

        # Canvas pour permettre le scroll
        self.shop_canvas = tk.Canvas(self.shop1, bg="#252525", highlightthickness=0)
        self.shop_canvas.pack(side="left", fill="both", expand=True)

        # Barre de scroll
        self.scrollbar = tk.Scrollbar(self.shop1, orient="vertical", command=self.shop_canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.shop_canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame interne qui contiendra les boutons
        self.shop = tk.Frame(self.shop_canvas, bg="#252525")

        self.shop_canvas.create_window((0, 0), window=self.shop, anchor="nw")

        self.shop.bind(
            "<Configure>",
            lambda e: self.shop_canvas.configure(scrollregion=self.shop_canvas.bbox("all"))
        )

    def miseajour(self, player) : 
        self.lait_var.set("litre de lait : " + simplificateur(player.lait))
        self.argent_var.set("Argent : " + simplificateur(player.argent) + " lacteuros")
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")
        self.laitparsec_var.set("Lait/s :  " + simplificateur(self.laitpartour) + "/s")
    



    def refresh(self):

        # Nettoyer anciens boutons
        for widget in self.zone_boutons.winfo_children():
            widget.destroy()

        player = self.controller.joueur

        
        self.label = tk.Label(self.header, text="Va chercher du lait " + player.nom)
        self.label.pack()


        #crée un lien entre front et back pour incrémenter player.lait en direct
        self.lait_var = tk.StringVar()
        self.lait_var.set("litre de lait : " + str(simplificateur(player.lait)))

        label = tk.Label(self.header, textvariable= self.lait_var, font=("Arial", 9))
        label.pack()

        #même chose pour l'argent
        self.argent_var = tk.StringVar()
        self.argent_var.set("Argent : " + str(simplificateur(player.argent)) + " lacteuros")

        label = tk.Label(self.header, textvariable= self.argent_var, font=("Arial", 16))
        label.pack()


        #lait par seconde
        self.laitparsec_var = tk.StringVar()
        self.laitparsec_var.set("Lait/s :  " + simplificateur(self.laitpartour) + "/s")

        label = tk.Label(self.header, textvariable= self.laitparsec_var, font=("Arial", 9))
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
            command=lambda: self.clic_pour_lait(player), 
            bd=0
        )
        self.bouton_vache.pack(pady=20)
        

    # Charger l'image
        self.img_vendre = tk.PhotoImage(file="images/vendre.png")
        self.img_vendre = self.img_vendre.subsample(4,4) #divise taille par 2
    #bouton pour vendre son lait
        tk.Button(
                self.actions,
                text="Vendre son lait",
                image=self.img_vendre,
                compound="center",   # texte au centre de l'image
                command=lambda: self.vendre_lait(player)
            ).pack()
        
    

        #liste pour garder en données les images des vaches
        self.images_vaches = []
        #variable pour refresh le bouton
        self.vache_vars = {}
        self.boutons_achat = {}

    #création d'un bouton pour chaque vaches
        for vache in player.vaches:

            #variables à mettre à jours
            var = tk.StringVar()
            var.set(f"x{simplificateur(vache.nombre)} | {simplificateur(vache.prix)} lacteuros")
            self.vache_vars[vache] = var


            frame_vache = tk.Frame(self.shop, bg="#3a3a3a", bd=1, relief="solid")
            frame_vache.pack(fill="x", pady=5, padx=5)

            masque = tk.Frame(frame_vache, bg="black")

            img = tk.PhotoImage(file=vache.img)
            #img = img.subsample(2,2)

            if not hasattr(self, "images_vaches"):
                self.images_vaches = []

            self.images_vaches.append(img)

            # image
            tk.Label(frame_vache, image=img, bg="#3a3a3a").pack(side="left", padx=5)

            # zone texte
            info = tk.Frame(frame_vache, bg="#3a3a3a")
            info.pack(side="left", expand=True, fill="x")

            tk.Label(
                info,
                text=vache.nom,
                bg="#3a3a3a",
                fg="white",
                font=("Arial", 10, "bold")
            ).pack(anchor="w")

            tk.Label(
                info,
                text=f"{simplificateur(vache.lait)} lait/sec",
                bg="#3a3a3a",
                fg="lightgreen"
            ).pack(anchor="w")

            tk.Label(
                info,
                textvariable=var,
                bg="#3a3a3a",
                fg="gold"
            ).pack(anchor="w")

            # bouton acheter
            bouton_acheter = tk.Button(
                frame_vache,
                text="Acheter",
                command=lambda v=vache: self.acheter_vache(player, v)
            ).pack(side="right", padx=5)

            self.boutons_achat[vache] = bouton_acheter

            if player.argent < vache.prix:
                tk.Button().config(state="disabled")
            else:
                self.boutons_achat[vache].config(state="normal")


            if player.argent < vache.prix * 0.5:
                masque.place(relwidth=1, relheight=1)
            else : 
                masque.place_forget()

        #appel de la fonction qui actionne le lait/tour
        self.start_lait_par_seconde()


    def clic_pour_lait(self, player):
        clicpourlait(player)
        self.miseajour(player)


    def vendre_lait(self, player):
        vendrelait(player)
        self.miseajour(player)



    def acheter_vache(self, player, vache):
        if player.argent >= vache.prix :
            achetervache(player, vache)  # backend

            # Mise à jour du bouton correspondant
            self.vache_vars[vache].set(
                f"x {simplificateur(vache.nombre)} | {simplificateur(vache.prix)} lacteuros")

        elif player.argent < vache.prix :
            print(f"tu n'as pas assez d'argent pour acheter une {vache.nom}")
            


        # Mise à jour lait/argent si besoin
        self.miseajour(player)






    def start_lait_par_seconde(self):
        player = self.controller.joueur
        self.laitpartour = 0

        #compter le lait par tour
        for v in player.vaches:
            self.laitpartour +=  v.lait * v.nombre
        player.lait += self.laitpartour

        #incrémente le temps de 1
        self.temps += 1
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")
        print(f"temps = {str(self.temps)}")


        self.miseajour(player)
        print(f"Tu as gagné {simplificateur(self.laitpartour)} litre de lait")

        # relance dans 1000ms (1 seconde)
        self.after(1000, self.start_lait_par_seconde)


