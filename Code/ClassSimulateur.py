import numpy as np
import ClassRobot.py as robot
import ClassManager.py as manager
import ClassFeu.py as feu 
import ClassIHM.py as IHM 
import ClassCarte.py as carte

class simulateur:
    def __init__(self):
        vitesseSimu = 1
        self.listeFeu = []
        self.listeRobot = []
    def executerSimulation() :
        while(len(simulateur.listeFeu)>0):
            manager.affecter(robot,feu)
            robot.mae()

    def lancerSimulation(self):
        print("La simulation est lancee")

    def ajouterFeu(self):
        self.listeFeu=self.listeFeu.append(('F',feu.coordonnerFeu))
        print("Un feu est ajoute")

    def ajouterRobot(self):
        self.listeRobot=self.listeRobot.append(('R',robot.id, robot.coordonnerRobot))
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
    