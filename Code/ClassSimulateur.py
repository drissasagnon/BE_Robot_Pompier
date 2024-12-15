import numpy as np
import ClassRobot as robot
import ClassManager as manager
import ClassFeu as feu 
import ClassIHM as IHM 
import ClassCarte as carte
import time as time

class simulateur:
    def __init__(self):
        self.vitesseSimu = 1
        self.listeFeu = []
        self.listeRobot = []

    def executerSimulation(self, manager) :
        i = 0
        while(len(self.listeFeu)>0):
            time.sleep(self.vitesseSimu)
            manager.affecter_robot(self)
            for r in self.listeRobot:
                r.mae()

    def lancerSimulation(self):
        print("La simulation est lancee")

    def ajouterFeu(self, feu):
        self.listeFeu.append(feu)
        print("Un feu est ajoute")
        print(self.listeFeu[0])

    def ajouterRobot(self, robot):
        self.listeRobot.append(robot)
        print("Un robot est ajoute")
    
    def lireCarte(self):
        print("La carte est lue")
    
    def arreterSimulation(self):
        print("La simulation est arretee")
    
    def pauseSimulation(self):
        print("La simulation est en pause")
    
    def reprendreSimulation(self):
        print("La simulation est reprise")

    def reintialiserSimulation(self):
        print("La simulation est reinitialisee")
    