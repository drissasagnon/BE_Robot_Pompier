from ClassManager import Manager
from ClassFeu import Feu
from ClassRobot import Robot

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
