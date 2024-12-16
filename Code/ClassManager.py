class Manager:
    def __init__(self, liste_robot, liste_feu):
        self.liste_robot = liste_robot
        self.liste_feu = liste_feu

    @staticmethod
    def calculer_distance(coord1, coord2):
        """Calcule la distance euclidienne entre deux coordonnées."""
        return ((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2) ** 0.5

    def trouver_feu_le_plus_proche(self, robot):
        """Trouve le feu le plus proche pour un robot donné."""
        min_distance = float('inf')
        nearest_feu = None
        for feu in self.liste_feu:
            distance = self.calculer_distance(robot.coordonnees, feu.coordonnees)
            if distance < min_distance:
                min_distance = distance
                nearest_feu = feu
        return nearest_feu

    def trouver_robot_le_plus_proche(self, feu):
        """Trouve le robot disponible le plus proche d’un feu donné."""
        min_distance = float('inf')
        nearest_robot = None
        for robot in self.liste_robot:
            if robot.robotDispo:  # Vérifie si le robot est disponible
                distance = self.calculer_distance(robot.coordonnees, feu.coordonnees)
                if distance < min_distance:
                    min_distance = distance
                    nearest_robot = robot
        return nearest_robot

    def affecter_un_robot_a_un_feu(self, robot, feu):
        """Assigne un robot à un feu et le fait agir."""
        print(f"Assignation du feu {feu.idFeu} au robot {robot.idRobot}.")
        robot.mae(feu.coordonnees, feu.ampleur)
        feu.eteindre()
        print(f"Feu {feu.idFeu} complètement éteint.")
        self.liste_feu.remove(feu)

    def affecterRobot(self):
        num_robots = len(self.liste_robot)
        num_feux = len(self.liste_feu)

        # Cas 1: Nombre égal de robots et de feux
        if num_robots == num_feux:
            for robot, feu in zip(self.liste_robot, self.liste_feu):
                if robot.robotDispo:
                    self.affecter_un_robot_a_un_feu(robot, feu)

        # Cas 2: Plus de feux que de robots
        elif num_feux > num_robots:
            for robot in self.liste_robot:
                if robot.robotDispo:
                    nearest_feu = self.trouver_feu_le_plus_proche(robot)
                    if nearest_feu:
                        self.affecter_un_robot_a_un_feu(robot, nearest_feu)

        # Cas 3: Plus de robots que de feux
        else:
            for feu in self.liste_feu:
                nearest_robot = self.trouver_robot_le_plus_proche(feu)
                if nearest_robot:
                    self.affecter_un_robot_a_un_feu(nearest_robot, feu)

            # Robots restants sans mission
            remaining_robots = [robot for robot in self.liste_robot if robot.robotDispo]
            for robot in remaining_robots:
                nearest_feu = self.trouver_feu_le_plus_proche(robot)
                if nearest_feu:
                    self.affecter_un_robot_a_un_feu(robot, nearest_feu)

        print("L'affectation des robots aux feux est terminée.")
