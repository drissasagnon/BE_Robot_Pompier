import numpy as np
import ClassRobot as robot
import ClassManager as manager
import ClassIHM as IHM 
import ClassSimulateur as simulateur 
import ClassCarte as carte


class feu:
    def __init__(self):
        self.idFeu= 0
        self.coordonneeFeu = None
        self.ampleur = 20
        self.etat = "actif"
        self.assigned = False

    def seDeclencher(self):
        carte.carte(self.coordonneeFeu)== 'Feu'
        print("Un feu s'est declenche")
        
    def eteindre(self):
        if self.ampleur==0 :
            simulateur.listeFeu.remove(Feu)

