import numpy as np
import ClassManager.py as manager
import ClassFeu.py as feu 
import ClassIHM.py as IHM 
import ClassSimulateur.py as simulateur 
import ClassCarte.py as carte

class robot:
    def __init__(self):
        self.coordonneerRobot = [carte.coordonnerBase[0],carte.coordonnerBase[1]]
        self.vitesse = 0
        self.idRobot = 0
        self.etat = "a la base"
        self.etatEau = 50
        self.robotDispo = True
        self.typeRobot = ""
        self.constante = 1
        self.distance=0 
        self.constante=1   
        self.nbRobot= 0    
        
    def eteindreFeu(self) :
        while(feu.ampleurFeu>0) :
            if feu.coordonneerFeu== self.coordonnerRobot:
                self.etatEau=self.etatEau-1
                feu.ampleurFeu=feu.ampleurFeu -1 
                T=('F',feu.coordonnerFeu)
                simulateur.listeFeu= simulateur.listeFeu.remove(T)
                print("Le feu est éteint")
            else :
                a=np.rand(0,1)
                if a==0 :
                    ampleurFeu=ampleurFeu-1
                else :
                    ampleurFeu=ampleurFeu+1
        
    def seDeplacer(self):
        if (feu.coordonneerFeu(0)-self.coordonnerRobot(0))<0 and (feu.coordonneerFeu(1)-self.coordonnerRobot(1))<0 and len(feu.listeFeu)>0:
            self.coordonneerRobot[0]=self.coordonneerRobot[0]-self.constante
            self.coordonneerRobot[1]=self.coordonneerRobot[1]-self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneerRobot[0],self.coordonneerRobot[1])=='R'
        elif (feu.coordonneerFeu(0)-self.coordonnerRobot(0))>0 and (feu.coordonneerFeu(1)-self.coordonnerRobot(1))>0 and len(feu.listeFeu)>0:
            self.coordonneerRobot[0]=self.coordonneerRobot[0]+self.constante
            self.coordonneerRobot[1]=self.coordonneerRobot[1]+self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneerRobot[0],self.coordonneerRobot[1])=='R'
        elif (feu.coordonneerFeu(0)-self.coordonnerRobot(0))<0 and (feu.coordonneerFeu(1)-self.coordonnerRobot(1))>0 and len(feu.listeFeu)>0:   
            self.coordonneerRobot[0]=self.coordonneerRobot[0]-self.constante
            self.coordonneerRobot[1]=self.coordonneerRobot[1]+self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneerRobot[0],self.coordonneerRobot[1])=='R'
        elif (feu.coordonneerFeu(0)-self.coordonnerRobot(0))>0 and (feu.coordonneerFeu(1)-self.coordonnerRobot(1))<0 and len(feu.listeFeu)>0:
            self.coordonneerRobot[0]=self.coordonneerRobot[0]+self.constante
            self.coordonneerRobot[1]=self.coordonneerRobot[1]-self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneerRobot[0],self.coordonneerRobot[1])=='R'

    def calculerDistance(self):
        self.distance = np.sqrt((feu.coordonneerFeu[0]-self.coordonneerRobot[0])**2+(feu.coordonneerFeu[1]-self.coordonneerRobot[1])**2)
        print("Le robot calcule la distance")

    def remplirReservoir(self):
        if self.stockFeu==0:
            self.stockFeu=2
        print("Le robot se rempli")
    def estDevantFeu(self) :
        if self.calculerDistance(self)<1 :
            return True
        
    def mae(self, feu_coordonnees=None, ampleurFeu=None, nouvelle_mission=None):
            if self.etat == "a la base":
                print("État : À la base")
                if self.stockFeu < 2:
                    self.remplirReservoir()  # Le remplissage est géré ici
                if feu_coordonnees is not None:  # Une mission est disponible
                    self.calculerDistance(feu_coordonnees)
                    self.etat = "en attente de mission"

            elif self.etat == "en attente de mission":
                print("État : En attente de mission")
                if feu_coordonnees is not None:  # Une mission est confirmée
                    print("Nouvelle mission reçue !")
                    self.calculerDistance(feu_coordonnees)
                    self.etat = "en déplacement"

            elif self.etat == "en déplacement":
                print("État : En déplacement")
                if feu_coordonnees is not None:  # Se déplacer vers le feu
                    self.seDeplacer(feu_coordonnees)
                    if self.estDevantFeu(coordonneerRobot,feu_coordonnees):  # Vérifier si arrivé à destination
                        print("Robot arrivé à destination.")
                        self.etat = "extinction du feu"

            elif self.etat == "extinction du feu":
                print("État : Extinction du feu")
                if feu_coordonnees is not None and ampleurFeu is not None:  # Si à proximité du feu
                    self.eteindreFeu(feu_coordonnees, ampleurFeu)  # Éteindre le feu
                    if self.stockFeu == 0:  # Si le réservoir est vide
                        self.etat = "retour à la base"
                    else:  # Si encore du stock, retourner à l'état initial
                        self.etat = "a la base"

            elif self.etat == "retour à la base":
                print("État : Retour à la base")
                self.seDeplacer([0, 0])  # Retourner aux coordonnées de la base
                if nouvelle_mission and self.stockFeu >= 1:  # Nouvelle mission en chemin
                    print("Nouvelle mission reçue pendant le retour à la base !")
                    feu_coordonnees = nouvelle_mission  # Mise à jour des coordonnées pour la nouvelle mission
                    self.calculerDistance(feu_coordonnees)
                    self.etat = "en déplacement"
                elif self.coordonneerRobot == [0, 0]:  # Si arrivé à la base
                    print("Robot est arrivé à la base.")
                    self.etat = "a la base"  # Passer à l'état "a la base"
