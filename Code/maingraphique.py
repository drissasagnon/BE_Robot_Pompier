from ClassSimulateur import Simulateur
from IHM import CarteGUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    simulateur = Simulateur()
    app = CarteGUI(master=root, simulateur=simulateur)
    app.mainloop()
