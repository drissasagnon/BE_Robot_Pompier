import numpy as np 
import ClassRobot as robot
import ClassManager as manager
import ClassFeu as feu 
import ClassIHM as IHM 
import ClassSimulateur as simulateur 
import ClassCarte as carte

#simulateur.run()

if __name__ == "__main__":
    print("Hello World")
    monSimulateur = simulateur.simulateur()
    monSimulateur.lancerSimulation()
    monManager = manager.manager(monSimulateur)
    carte = carte.carte()
    feu = feu.feu()
    robot = robot.robot(carte)
    
    monSimulateur.ajouterFeu(feu)
    monSimulateur.ajouterRobot(robot)
    print(monSimulateur.listeRobot)
    monSimulateur.executerSimulation(monManager)
    
    


