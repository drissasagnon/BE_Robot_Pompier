from ClassManager import Manager
from ClassFeu import Feu
from ClassRobot import Robot
import time

class Simulateur:
    def __init__(self):
        self.listeFeu = []
        self.listeRobot = []

    def ajouterFeu(self, idFeu, coordonnees, ampleur):
        feu = Feu(idFeu, ampleur, coordonnees)
        self.listeFeu.append(feu)
        print(f"Feu {idFeu} ajouté avec succès aux coordonnées {coordonnees} avec une ampleur de {ampleur}.")

    def ajouterRobot(self, robot):
        self.listeRobot.append(robot)

    def executerSimulation(self): 
        print("Simulation lancée...")
        while any(feu.ampleur > 0 for feu in self.listeFeu):
            for robot in self.listeRobot:
                # Trouver le premier feu actif
                feu_actif = next((feu for feu in self.listeFeu if feu.ampleur > 0), None)
                if feu_actif:
                    robot.mae(feu_actif.coordonnees, feu_actif.ampleur)
                    # Éteindre le feu
                    feu_actif.eteindre()
                    # Retirer le feu de la liste une fois éteint
                    if feu_actif.ampleur == 0:
                        self.listeFeu.remove(feu_actif)
                        print(f"Feu {feu_actif.idFeu} complètement éteint et retiré de la liste.")
        print("Simulation terminée.")

    def accelerer_simulation(self):
        """Accélère la simulation en réduisant la vitesse."""
        self.simulation_speed = max(0.01, self.simulation_speed - 0.01)
        print("Simulation accélérée.")

    def ralentir_simulation(self):
        """Ralentit la simulation en augmentant la vitesse."""
        self.simulation_speed += 0.01
        print("Simulation ralentie.")

    def pause_simulation(self):
        """Met la simulation en pause."""
        self.simulation_paused.clear()  # Désactive l'événement, ce qui met la simulation en pause
        print("Simulation en pause.")

    def reprendre_simulation(self):
        """Reprend la simulation après une pause."""
        self.simulation_paused.set()  # Active l'événement, ce qui reprend la simulation
        print("Simulation reprise.")

    def reinitialiser_simulation(self):
        """Réinitialise les feux et robots à leur état initial."""
        # Réinitialiser les positions des robots
        for i, robot in enumerate(self.listeRobot):
            robot.coordonneerRobot = self.initial_robot_positions[i]
            print(f"Robot {robot.idRobot} réinitialisé à sa position initiale.")

        # Réinitialiser l'ampleur des feux
        for i, feu in enumerate(self.listeFeu):
            feu.ampleur = self.initial_feu_ampleur[i]
            print(f"Feu {feu.idFeu} réinitialisé à son ampleur initiale.")

        print("Simulation réinitialisée.")