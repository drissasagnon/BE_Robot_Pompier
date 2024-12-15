import numpy as np
import ClassRobot as robot
import ClassManager as manager
import ClassFeu as feu 
import ClassIHM as IHM 
import ClassSimulateur as simulateur 

class carte:
    def __init__(self):
        self.taille = (2000,2000)
        self.repere = np.zeros(self.taille)
        self.coordonneeBase = [0, 0]#self.carte[0,0]

    def chargerCarte(self):
        print(self.repere)
