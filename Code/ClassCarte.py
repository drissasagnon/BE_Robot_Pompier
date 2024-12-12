import numpy as np
import ClassRobot.py as robot
import ClassManager.py as manager
import ClassFeu.py as feu 
import ClassIHM.py as IHM 
import ClassSimulateur.py as simulateur 

class carte:
    def __init__(self):
        self.taille=(2000,2000)
        self.repere =np.zeros(self.taille)
        self.coordonneerBase=self.carte[0,0]
    def chargerCarte(self):
        print(self.repere)
