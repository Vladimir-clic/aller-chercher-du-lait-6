import tkinter as tk


class Options(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue dans les options (le bouton marche pas)", font=("Arial", 16))
        label.pack()

        tk.Button(
            self,
            text="Retour", 
            #command=Menu
            ).pack()