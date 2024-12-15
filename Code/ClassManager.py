import numpy as np
import ClassRobot as robot
import ClassFeu as feu 
import ClassIHM as IHM 
import ClassSimulateur as simulateur 
import ClassCarte as carte

class manager:
    def __init__(self, simulateur):
        self.nbRobot=len(simulateur.listeRobot)
        self.nbFeu=len(simulateur.listeFeu)
        self.listeRobotsDispo=[]
        self.listeFeuxActifs=[]
        self.matriceDistance=2000*np.array(np.ones((self.nbRobot,self.nbFeu)))

 
    def affecter(self):
        # Affectation 
        print("Affectation en cours ...")
        
    def calculer_distance(self,coordonneer1, coordonneer2):
        return np.sqrt((coordonneer2[0] - coordonneer1[0]) ** 2 + (coordonneer2[1] - coordonneer1[1]) ** 2)


    def trouver_feu_le_plus_proche(self, robot, simulateur):
        min_distance = float('inf')
        nearest_feu = None
        for feu in simulateur.listeFeu:
            distance = self.calculer_distance(robot, feu)
            if distance < min_distance:
                min_distance = distance
                nearest_feu = feu
        return nearest_feu

    def trouver_robot_le_plus_proche(self, feu, simulateur):
        min_distance = float('inf')
        nearest_robot = None
        for robot in simulateur.listeRobot:
            if not robot['assigned']:  # Only consider unassigned robots
                distance = self.calculer_distance(robot['coordonneerRobot'], feu['coordonneerFeu'])
                if distance < min_distance:
                    min_distance = distance
                    nearest_robot = robot
        return nearest_robot
    
    def affecter_robot(self, simulateur):
        for f in simulateur.listeFeu:
            #if f.getEtat() == "actif":
                self.listeFeuxActifs.append(f)
        for r in simulateur.listeRobot:
            if r.getDispo() == True:
                self.listeRobotsDispo.append(r)
        for i, r in enumerate(self.listeRobotsDispo):
            for j, f in enumerate(self.listeFeuxActifs):
                self.matriceDistance[i,j] = r.calculerDistance(f)
        
        self.assignerRobot()
        
    def assignerRobot(self):
        for i in range(len(self.listeRobotDispo)):
            distanceMin = np.min(self.matriceDistance[i,:])
            indexFeu = np.argmin(self.matriceDistance[i,:])
            if self.listeFeuxActifs[indexFeu].getEtat() == "actif" and self.listeFeuxActifs[indexFeu].getAssigned() == False:
                self.listeRobotDispo[i].setFeuAssigne(self.listeFeuxActifs[indexFeu])
                self.listeRobotDispo[i].setDispo(False)
                self.listeFeuxActifs[indexFeu].setAssigned(True)
                print(f"Le robot {self.listeRobotDispo[i].getId()} est affecté au feu {self.listeFeuxActifs[indexFeu].getId()}")
        

    """
    def affecter_un_robot_a_un_feu(self, simulateur):
        
        #robot['assigned'] = True
        #print(f"Robot {robot['coordonneerRobot']} affecté au feu {feu['coordonneerFeu']}")

        num_robots = len(simulateur.listeRobot)
        num_feux = len(simulateur.listeFeu)

        # Cas 1: Equal number of robots and fires
        if num_robots == num_feux:
            for robot, feu in zip(simulateur.listeRobot, simulateur.listeFeu):
                self.affecter_un_robot_a_un_feu(robot, feu)
        
        # Cas 2: More fires than robots
        elif num_feux > num_robots:
            for i in range(num_robots):
                nearest_feu = self.trouver_feu_le_plus_proche(simulateur.listeRobot[i], simulateur.listeFeu)
                self.affecter_un_robot_a_un_feu(simulateur.listeRobot[i], nearest_feu)

        # Cas 3: More robots than fires
        else:  # More robots than fires
            for feu in simulateur.listeFeu:
                nearest_robot = self.trouver_robot_le_plus_proche(feu, simulateur.listeRobot)
                self.affecter_un_robot_a_un_feu(nearest_robot, feu)
                    
            # Assign remaining robots to the nearest fires
            remaining_robots = [robot for robot in simulateur.listeRobot if not robot['assigned']]
            for robot in remaining_robots:
                nearest_feu = self.trouver_feu_le_plus_proche(robot, simulateur.listeFeu)
                self.affecter_un_robot_a_un_feu(robot, nearest_feu)
        print("L'affectation des robots aux feux est terminée.")
    """

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