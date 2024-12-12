import numpy as np
import ClassRobot.py as robot
import ClassFeu.py as feu 
import ClassIHM.py as IHM 
import ClassSimulateur.py as simulateur 
import ClassCarte.py as carte

class manager:
    def __init__(self):
      feu.nbFeu=len(simulateur.listeFeu)

def affecter(simulateur.listeRobot, simulateur.listeFeu):
    # Function to assign robots to fires based on the number of robots and fires
    def calculer_distance(coordonneer1, coordonneer2):
        return np.sqrt((coordonneer2[0] - coordonneer1[0]) ** 2 + (coordonneer2[1] - coordonneer1[1]) ** 2)

    def affecter_un_robot_a_un_feu(robot, feu):
        """Assign a robot to a fire"""
        robot['assigned'] = True
        print(f"Robot {robot['coordonneerRobot']} affecté au feu {feu['coordonneerFeu']}")

    def trouver_feu_le_plus_proche(robot, simulateur.listeFeu):
        min_distance = float('inf')
        nearest_feu = None
        for feu in simulateur.listeFeu:
            distance = calculer_distance(robot['coordonneerRobot'], feu['coordonneerFeu'])
            if distance < min_distance:
                min_distance = distance
                nearest_feu = feu
        return nearest_feu

    def trouver_robot_le_plus_proche(feu, simulateur.listeRobot):
        min_distance = float('inf')
        nearest_robot = None
        for robot in simulateur.listeRobot:
            if not robot['assigned']:  # Only consider unassigned robots
                distance = calculer_distance(robot['coordonneerRobot'], feu['coordonneerFeu'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_robot = robot
        return nearest_robot
    num_robots = len(simulateur.listeRobot)
    num_feux = len(simulateur.listeFeu)

    # Cas 1: Equal number of robots and fires
    if num_robots == num_feux:
        for robot, feu in zip(simulateur.listeRobot, simulateur.listeFeu):
            affecter_un_robot_a_un_feu(robot, feu)
    
    # Cas 2: More fires than robots
    elif num_feux > num_robots:
        for i in range(num_robots):
            nearest_feu = trouver_feu_le_plus_proche(simulateur.listeRobot[i], simulateur.listeFeu)
            affecter_un_robot_a_un_feu(simulateur.listeRobot[i], nearest_feu)

    # Cas 3: More robots than fires
    else:  # More robots than fires
        for feu in simulateur.listeFeu:
            nearest_robot = trouver_robot_le_plus_proche(feu, simulateur.listeRobot)
            affecter_un_robot_a_un_feu(nearest_robot, feu)
                
        # Assign remaining robots to the nearest fires
        remaining_robots = [robot for robot in simulateur.listeRobot if not robot['assigned']]
        for robot in remaining_robots:
            nearest_feu = trouver_feu_le_plus_proche(robot, simulateur.listeFeu)
            affecter_un_robot_a_un_feu(robot, nearest_feu)
    print("L'affectation des robots aux feux est terminée.")
    
    def calculerDistancebymanager(self):
        LISTE=[]
        MATRICEDISTANCE=np.zeros(len(simulateur.listeFeu),len(simulateur.listeRobot))
        for i in range(len(simulateur.listeFeu)):
            for j in range(len(simulateur.listeRobot)):
                TF=simulateur.listeFeu[i]
                TR=simulateur.listeRobot[j]
                CoorF=TF[1]
                CoorR=TR[2]
                Dij=np.sqrt((CoorF[0]-CoorR[0])**2+(CoorF[1]-CoorR[1])**2)
                MATRICEDISTANCE[i][j]= Dij
                LISTE=LISTE.append(Dij)
        return MATRICEDISTANCE