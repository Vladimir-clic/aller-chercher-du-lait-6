import tkinter as tk
from pages.options import Options
from pages.param_partie import Param_partie

class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = tk.Label(self, text="Bienvenue dans Vache à Lait", font=("Arial", 16))
        label.pack()

        tk.Button(
            self,
            text="Nouvelle partie",
            command=lambda: controller.show_frame(Param_partie)).pack()
        
        tk.Button(
            self,
            text="Options",
            command=lambda: controller.show_frame(Options)
        ).pack()