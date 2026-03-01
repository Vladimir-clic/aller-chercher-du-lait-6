import tkinter as tk

from pages.menu import Menu
from pages.options import Options
from pages.param_partie import Param_partie
from pages.jeu import Jeu


class game_gui(tk.Tk) : 
    def __init__(self):

        # créer la fenêtre
        super().__init__()
        self.title("Vache à Lait 🐄")
        self.geometry("600x400")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # dictionnaire pour stocker les pages
        self.frames = {}

        # création des pages
        for Page in (Menu, Options, Param_partie, Jeu):
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

