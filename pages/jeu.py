import tkinter as tk


class Jeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text=f"Bienvenue le jeu", font=("Arial", 16))
        label.pack()