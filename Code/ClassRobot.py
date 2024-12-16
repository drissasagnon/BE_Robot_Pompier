class Robot:
    def __init__(self, idRobot, typeRobot, nom, vitesse):
        self.idRobot = idRobot            # Identifiant du robot
        self.typeRobot = typeRobot        # Type du robot
        self.nom = nom                    # Nom du robot
        self.vitesse = vitesse            # Vitesse du robot
        self.coordonnees = [0, 0]         # Position initiale (à la base)
        self.robotDispo = True            # Disponibilité du robot
        self.etat = "A la base"           # État initial
        self.etatEau = 100                # Réservoir d'eau (en %)

    def remplirReservoir(self):
        self.etatEau = 100
        self.etat = "Remplit réservoir"
        print(f"Robot {self.idRobot} remplit son réservoir d'eau.")

    def seDeplacer(self, destination):
        self.etat = "En déplacement"
        print(f"Robot {self.idRobot} se déplace vers {destination}.")
        self.coordonnees = destination  # Mise à jour de la position

    def eteindreFeu(self, coordonneesFeu, ampleurFeu):
        self.etat = "Eteint le feu"
        print(f"Robot {self.idRobot} éteint le feu à {coordonneesFeu}.")
        self.etatEau -= ampleurFeu * 10  # Consommation d'eau en fonction de l'ampleur du feu

    def retournerBase(self):
        self.etat = "Retour à la base"
        print(f"Robot {self.idRobot} retourne à la base.")
        self.coordonnees = [0, 0]  # Retour à la base

    def mae(self, coordonneesFeu, ampleurFeu):
        """Machine à États pour le robot"""
        if self.etat == "A la base":
            self.remplirReservoir()

        if self.etat == "Remplit réservoir":
            self.seDeplacer(coordonneesFeu)

        if self.etat == "En déplacement":
            print(f"Robot {self.idRobot} est arrivé au feu.")
            self.eteindreFeu(coordonneesFeu, ampleurFeu)

        if self.etat == "Eteint le feu":
            print(f"Robot {self.idRobot} a éteint le feu.")
            self.retournerBase()

        if self.etat == "Retour à la base":
            print(f"Robot {self.idRobot} est retourné à la base.")
            self.robotDispo = True
            self.etat = "A la base"  # Retour à l'état initial
