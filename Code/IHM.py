import tkinter as tk
from PIL import Image, ImageTk
from time import sleep
from threading import Thread, Event
from ClassSimulateur import Simulateur
from ClassRobot import Robot
from ClassFeu import Feu

class CarteGUI(tk.Frame):
    def __init__(self, master=None, simulateur=None):
        super().__init__(master)
        self.master = master
        self.simulateur = simulateur
        self.grid()
        self.create_widgets()

        self.simulation_paused = Event()
        self.simulation_paused.set()  # L'événement est "activé"
        self.simulation_speed = 0.05  # Vitesse par défaut de la simulation
        self.robots_threads = []  # Liste pour suivre les threads des robots

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=600, height=600)
        self.canvas.grid(row=0, column=0, rowspan=6)

        self.btn_lancer_carte = tk.Button(self, text="Lancer la carte", command=self.lancer_carte)
        self.btn_lancer_carte.grid(row=0, column=1)

        self.btn_add_robot = tk.Button(self, text="Ajouter un Robot", command=self.ajouter_robot)
        self.btn_add_robot.grid(row=1, column=1)

        self.btn_add_feu = tk.Button(self, text="Ajouter un Feu", command=self.activer_ajout_feu)
        self.btn_add_feu.grid(row=2, column=1)

        self.btn_simulation = tk.Button(self, text="Lancer Simulation", command=self.lancer_simulation)
        self.btn_simulation.grid(row=3, column=1)

        self.btn_accelerer = tk.Button(self, text="Accélérer", command=self.accelerer_simulation)
        self.btn_accelerer.grid(row=4, column=1)

        self.btn_ralentir = tk.Button(self, text="Ralentir", command=self.ralentir_simulation)
        self.btn_ralentir.grid(row=5, column=1)

        self.btn_pause = tk.Button(self, text="Pause", command=self.pause_simulation)
        self.btn_pause.grid(row=6, column=1)

        self.btn_reprendre = tk.Button(self, text="Reprendre", command=self.reprendre_simulation)
        self.btn_reprendre.grid(row=7, column=1)

        self.quit = tk.Button(self, text="Quitter", command=self.master.quit)
        self.quit.grid(row=8, column=1)

        self.ajouter_feu_mode = False

    def lancer_carte(self):
        try:
            image_fond_pil = Image.open("carte.png")
            self.image_fond = ImageTk.PhotoImage(image_fond_pil)
            self.canvas.create_image(0, 0, anchor="nw", image=self.image_fond)
        except FileNotFoundError:
            print("Le fichier carte.png est introuvable.")

    def activer_ajout_feu(self):
        self.ajouter_feu_mode = True
        print("Mode ajout feu activé. Cliquez sur la carte pour placer un feu.")
        self.canvas.bind("<Button-1>", self.placer_feu)

    def placer_feu(self, event):
        if self.ajouter_feu_mode:
            x, y = event.x, event.y
            feu_id = len(self.simulateur.listeFeu) + 1
            ampleur = 5
            feu = Feu(str(feu_id), ampleur, [x, y])
            self.simulateur.ajouterFeu(feu_id, [x, y], ampleur)
            self.canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="red", tags=f"feu{feu_id}")
            print(f"Feu {feu_id} ajouté aux coordonnées ({x}, {y}).")
            self.ajouter_feu_mode = False
            self.canvas.unbind("<Button-1>")

    def ajouter_robot(self):
        robot_id = len(self.simulateur.listeRobot) + 1
        x, y = 50, 50
        robot = Robot(str(robot_id), "Type1", f"Robot{robot_id}", 1.0)
        self.simulateur.ajouterRobot(robot)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="blue", tags=f"robot{robot_id}")
        print(f"Robot {robot_id} ajouté.")

    def lancer_simulation(self):
        for robot in self.simulateur.listeRobot:
            for feu in self.simulateur.listeFeu:
                thread = Thread(target=self.deplacer_robot, args=(robot, feu))
                thread.start()
                self.robots_threads.append(thread)

    def deplacer_robot(self, robot, feu):
        robot_x, robot_y = 50, 50
        feu_x, feu_y = feu.coordonnees
        dx = feu_x - robot_x
        dy = feu_y - robot_y
        distance = (dx**2 + dy**2) ** 0.5
        dx /= distance
        dy /= distance

        while abs(robot_x - feu_x) > 5 or abs(robot_y - feu_y) > 5:
            if not self.simulation_paused.is_set():
                sleep(0.1)
                continue
            robot_x += dx * 5
            robot_y += dy * 5
            self.canvas.coords(f"robot{robot.idRobot}", robot_x - 10, robot_y - 10, robot_x + 10, robot_y + 10)
            self.master.update()
            sleep(self.simulation_speed)

        if feu in self.simulateur.listeFeu:
            self.canvas.delete(f"feu{feu.idFeu}")
            self.simulateur.listeFeu.remove(feu)

        while abs(robot_x - 50) > 5 or abs(robot_y - 50) > 5:
            if not self.simulation_paused.is_set():
                sleep(0.1)
                continue
            dx = 50 - robot_x
            dy = 50 - robot_y
            distance = (dx**2 + dy**2) ** 0.5
            dx /= distance
            dy /= distance
            robot_x += dx * 5
            robot_y += dy * 5
            self.canvas.coords(f"robot{robot.idRobot}", robot_x - 10, robot_y - 10, robot_x + 10, robot_y + 10)
            self.master.update()
            sleep(self.simulation_speed)

    def accelerer_simulation(self):
        self.simulation_speed = max(0.01, self.simulation_speed - 0.01)
        print("Simulation accélérée.")

    def ralentir_simulation(self):
        self.simulation_speed += 0.01
        print("Simulation ralentie.")

    def pause_simulation(self):
        self.simulation_paused.clear()
        print("Simulation en pause.")

    def reprendre_simulation(self):
        self.simulation_paused.set()
        print("Simulation reprise.")

if __name__ == "__main__":
    root = tk.Tk()
    simulateur = Simulateur()
    app = CarteGUI(master=root, simulateur=simulateur)
    app.mainloop()
