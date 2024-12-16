from ClassRobot import Robot
class IHM:
    def __init__(self, simulateur):
        self.simulateur = simulateur

    def menu_principal(self):
        while True:
            print("\n--- Menu Principal ---")
            print("1. Ajouter un robot")
            print("2. Ajouter un feu")
            print("3. Lancer la simulation")
            print("4. Quitter")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                idRobot = input("Entrez l'ID du robot : ")
                typeRobot = input("Type du robot : ")
                nom = input("Nom du robot : ")
                vitesse = float(input("Vitesse du robot : "))
                robot = Robot(idRobot, typeRobot, nom, vitesse)
                self.simulateur.ajouterRobot(robot)
                print(f"Robot {idRobot} ajouté avec succès.")

            elif choix == "2":
                idFeu = input("Entrez l'ID du feu : ")
                x = float(input("Coordonnée X du feu : "))
                y = float(input("Coordonnée Y du feu : "))
                ampleur = float(input("Ampleur du feu : "))
                self.simulateur.ajouterFeu(idFeu, [x, y], ampleur)

            elif choix == "3":
                self.simulateur.executerSimulation()

            elif choix == "4":
                print("Quitter le programme.")
                break

            else:
                print("Choix invalide. Veuillez réessayer.")
