import numpy as np
import ClassRobot.py as robot
import ClassManager.py as manager
import ClassIHM.py as IHM 
import ClassSimulateur.py as simulateur 
import ClassCarte.py as carte


class feu:
    def __init__(self):
        self.idFeu= 0
        self.coordonneerFeu = None
        self.ampleur = 20

    def seDeclencher(self):
        carte.carte(self.coordonneerFeu)== 'Feu'
        print("Un feu s'est declenche")
    def eteindre(self):
        if self.ampleur==0 :
            simulateur.listeFeu.remove(Feu)

