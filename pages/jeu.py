import tkinter as tk
import time
import random

from game_logic import *

class Jeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller


        self.zone_boutons = tk.Frame(self)
        self.zone_boutons.pack()

        self.vache_vars = {}
        self.recrue_vars = {}

        #pour stocker les images
        self.images_cache = {}
        self.images2_cache = {}

        self.temps = 0
        self.laitpartour = 0
        self.laitparclic = 1





        #mettre des types
        self.configure(bg="#2e2e2e")


        #header pour les éléments en haut
        self.header = tk.Frame(self, bg="#040404")
        self.header.pack(fill="x")

        #footer pour les éléments en bas
        self.footer = tk.Frame(self, bg="#040404")
        self.footer.pack(fill='both', side='bottom')

        
        #body pour contenir les actions et le shop
        self.body = tk.Frame(self, bg="#2e2e2e")
        self.body.pack(expand=True, fill="both")

        self.body.columnconfigure(0, weight=1)   # actions
        self.body.columnconfigure(1, weight=4)   # market
        self.body.rowconfigure(0, weight=1)


        #action pour les éléments à gauche
        self.actions = tk.Frame(self.body, bg="#2e2e2e")
        self.actions.grid(row=0, column=0, sticky="nsew")
        
        #market pour les recrues et les vaches
        self.market = tk.Frame(self.body,  bg="#5D4FB3")
        self.market.grid(row=0, column=1, sticky="nsew")

        self.market.columnconfigure(0, weight=1)   # coworker
        self.market.columnconfigure(1, weight=3)   # shop
        self.market.rowconfigure(0, weight=1)

        
        

        #shop pour les éléments à droite
        self.shop1 = tk.Frame(self.market, bg="#252525")
        self.shop1.grid(row=0, column=1, sticky="nsew")
        #self.shop1.pack(side="right", fill="y", padx=10)

        # Canvas pour permettre le scroll
        self.shop_canvas = tk.Canvas(self.shop1, bg="#252525", highlightthickness=0)
        self.shop_canvas.pack(side="left", fill="both", expand=True)
        # Barre de scroll
        self.scrollbar_shop = tk.Scrollbar(self.shop1, orient="vertical", command=self.shop_canvas.yview)
        self.scrollbar_shop.pack(side="right", fill="y")

        self.shop_canvas.configure(yscrollcommand=self.scrollbar_shop.set)

        # Frame interne qui contiendra les boutons
        self.shop = tk.Frame(self.shop_canvas, bg="#252525")

        self.shop_canvas.create_window((0, 0), window=self.shop, anchor="nw")

        self.shop.bind(
            "<Configure>",
            lambda e: self.shop_canvas.configure(scrollregion=self.shop_canvas.bbox("all"))
        )

        #ajouter le scroll molette au shop 
        self.shop_canvas.bind(
            "<MouseWheel>",
            lambda e: self.shop_canvas.yview_scroll(int(-1*(e.delta/120)), "units")
        )


        #coworker pour les éléments à gauche du market
        self.coworker1 = tk.Frame(self.market, bg="#252525")
        self.coworker1.grid(row=0, column=0, sticky="nsew")
        #self.coworker1.pack(side="left", fill="y", padx=10)

        # Canvas pour permettre le scroll
        self.coworker_canvas = tk.Canvas(self.coworker1, bg="#252525", highlightthickness=0)
        self.coworker_canvas.pack(side="left", fill="both", expand=True)
        # Barre de scroll
        self.scrollbar_coworker = tk.Scrollbar(self.coworker1, orient="vertical", command=self.coworker_canvas.yview)
        self.scrollbar_coworker.pack(side="right", fill="y")

        self.coworker_canvas.configure(yscrollcommand=self.scrollbar_coworker.set)

        # Frame interne qui contiendra les boutons
        self.coworker = tk.Frame(self.coworker_canvas, bg="#252525")

        self.coworker_canvas.create_window((0, 0), window=self.coworker, anchor="nw")

        self.coworker.bind(
            "<Configure>",
            lambda e: self.coworker_canvas.configure(scrollregion=self.coworker_canvas.bbox("all"))
        )

        #ajouter le scroll molette au coworker 
        self.coworker_canvas.bind(
            "<MouseWheel>",
            lambda e: self.coworker_canvas.yview_scroll(int(-1*(e.delta/120)), "units")
        )





    def miseajour(self, player) : 
        self.lait_var.set("litre de lait : " + simplificateur(player.lait))
        self.argent_var.set("Argent : " + simplificateur(player.argent) + " lacteuros")
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")
        self.laitparsec_var.set("Lait/s :  " + simplificateur(self.laitpartour) + "/s")
        self.recrueclic_var.set("Lait par clic :  " + simplificateur(self.laitparclic) + " /clic")
        self.update_expiration_labels()
    



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

        label = tk.Label(self.actions, textvariable= self.lait_var, font=("Arial", 9))
        label.pack()

        #même chose pour l'argent
        self.argent_var = tk.StringVar()
        self.argent_var.set("Argent : " + str(simplificateur(player.argent)) + " lacteuros")

        label = tk.Label(self.header, textvariable= self.argent_var, font=("Arial", 16))
        label.pack()


        #lait par seconde
        self.laitparsec_var = tk.StringVar()
        self.laitparsec_var.set("Lait/s :  " + simplificateur(self.laitpartour) + "/s")

        label = tk.Label(self.actions, textvariable= self.laitparsec_var, font=("Arial", 9))
        label.pack()


        #même chose pour le temps
        self.temps_var = tk.StringVar()
        self.temps_var.set("Temps : " + str(self.temps) + " secondes")

        label = tk.Label(self.footer, textvariable= self.temps_var, font=("Arial", 9))
        label.pack()

        #update les clics par recrues
        self.recrueclic_var = tk.StringVar()
        self.recrueclic_var.set("Lait par clic :  " + simplificateur(self.laitparclic) + " /clic")

        label = tk.Label(self.actions, textvariable= self.recrueclic_var, font=("Arial", 9))
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

        #appelle des fonctions : 
        self.refresh_vache(player)
        self.refresh_coworker()
        #appel de la fonction qui actionne le lait/tour
        #self.vente_vache(player)
        #self.vente_recrute(recrue, player)
        self.start_lait_par_seconde()
        #self.apparition_aleatoire_recrue(self)



    def refresh_vache(self, player) : 

    #création d'un bouton pour chaque vaches
        for vache in player.vaches:

            #variables à mettre à jours
            var = tk.StringVar()
            var.set(f"x{simplificateur(vache.nombre)} | {simplificateur(vache.prix)} lacteuros")
            self.vache_vars[vache] = var


            frame_vache = tk.Frame(self.shop, bg="#3a3a3a", bd=1, relief="solid")
            frame_vache.pack(fill="x", pady=5, padx=5)

            #img = tk.PhotoImage(file=vache.img)
            #img = img.subsample(2,2)

            #charger les images dans images_cache si pas déjà fait
            if vache.img not in self.images_cache:
                self.images_cache[vache.img] = tk.PhotoImage(file=vache.img)

            img = self.images_cache[vache.img]


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
            )
            
            bouton_acheter.pack(side="right", padx=5)

            self.boutons_achat[vache] = bouton_acheter




    def refresh_coworker(self) : 
        
        #se vide et se reremplit
        for widget in self.coworker.winfo_children():
            widget.destroy()
        self.recrue_vars = {}
        self.expiration_labels = {}

        if not dictrecrue:
            tk.Label(
                self.coworker,
                text="Aucune recrue disponible",
                bg="#252525", fg="gray",
                font=("Arial", 10, "italic")
            ).pack(pady=20)
            return

        player = self.controller.joueur

    #création d'un bouton pour chaque recrue
        for recrue in dictrecrue.values():
            #variables à mettre à jours
            var = tk.StringVar()
            var.set(f"Engager pour {simplificateur(recrue.prix)} lacteuros")
            self.recrue_vars[recrue] = var

            frame_recrue = tk.Frame(self.coworker, bg="#3a3a3a", bd=1, relief="solid")
            frame_recrue.pack(fill="x", pady=5, padx=5)
            
            #img = tk.PhotoImage(file=recrue.img)
            #img = img.subsample(2,2)
            #charger les images dans images_cache si pas déjà fait
            if recrue.img not in self.images2_cache:
                self.images2_cache[recrue.img] = tk.PhotoImage(file=recrue.img)
            img = self.images2_cache[recrue.img]
            # image
            tk.Label(frame_recrue, image=img, bg="#3a3a3a").pack(side="left", padx=5)
            # zone texte
            info = tk.Frame(frame_recrue, bg="#3a3a3a")
            info.pack(side="left", expand=True, fill="x")

            tk.Label(
                info,
                text=recrue.nom,
                bg="#3a3a3a",
                fg="white",
                font=("Arial", 10, "bold")
            ).pack(anchor="w")
            tk.Label(
                info,
                text=f"{simplificateur(recrue.age)} age",
                bg="#3a3a3a",
                fg="lightgreen"
            ).pack(anchor="w")
            tk.Label(
                info,
                text=f"{simplificateur(recrue.clic)} par clic",
                bg="#3a3a3a",
                fg="gold"
            ).pack(anchor="w")

            # bouton acheter
            tk.Button(
                frame_recrue,
                text=f"Engager pour {recrue.prix} lacteuros",
                command=lambda r=recrue : self.engager_recrue(player, r)
            ).pack(side="right", padx=5)

            #label d'expiration avec StringVar pour pouvoir modifier la var
            expiration_var = tk.StringVar()
            expiration_var.set(f"Expire dans {recrue.peremption - recrue.countnaissance}s")
            
            #stocker la var dans le dictionnaire
            self.expiration_labels[recrue.id] = expiration_var
            
            tk.Label(info, 
                textvariable=expiration_var,
                bg="#3a3a3a", 
                fg="orange"
            ).pack(anchor="w")




    


    def clic_pour_lait(self, player):
        clicpourlait(player, self.laitparclic)
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
            

    def engager_recrue(self, player, rec):
        if player.argent >= rec.prix:
            player.argent -= rec.prix
            del dictrecrue[rec.id]
            print(f"{rec.nom} engagé !")
            self.laitparclic += rec.clic
            listerecrue.append(rec)
            self.miseajour(player)
            self.refresh_coworker()
        else:
            print("Pas assez d'argent pour engager cette recrue")



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

        self.apparition_aleatoire_recrue()

        # relance dans 1000ms (1 seconde)
        self.after(1000, self.start_lait_par_seconde)




    def apparition_aleatoire_recrue(self):
        reponse_apparition = apparition_recrue(self.temps)
        reponse_suppression = suppression_recrue()

        if reponse_apparition == True or reponse_suppression == True:
            # Recrue ajoutée ou supprimée → on recrée les widgets
            self.refresh_coworker()
        else:
            # Rien de changé → on met juste à jour les labels de temps
            self.update_expiration_labels()

    def update_expiration_labels(self):
        for id, var in self.expiration_labels.items():
            if id in dictrecrue:
                r = dictrecrue[id]
                temps_restant = r.peremption - r.countnaissance
                var.set(f"Expire dans {temps_restant}s")


