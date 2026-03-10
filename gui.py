import tkinter as tk

from pages.menu import Menu
from pages.options import Options
from pages.param_partie import Param_partie
from pages.jeu import Jeu
from pages.jeu_details_recrue import Jeu_details_recrue


class game_gui(tk.Tk) : 
    def __init__(self):

        # créer la fenêtre
        super().__init__()
        self.title("Vache à Lait 🐄")
        self.minsize(500,400)
        #self.geometry("500x400")

        #initialisation des conteneurs
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        #rendre le conteneur principal redimensionnable
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # dictionnaire pour stocker les pages
        self.frames = {}

        # création des pages
        for Page in (Menu, Options, Param_partie, Jeu, Jeu_details_recrue):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # afficher la première page
        self.show_frame(Menu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        # Si la page a une méthode refresh, on l'appelle
        if hasattr(frame, "refresh"):
            frame.refresh()


# lancer la boucle graphique
letstart = game_gui()
letstart.mainloop()

