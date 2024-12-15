import numpy as np
import ClassManager as manager
import ClassFeu as feu 
import ClassIHM as IHM 
import ClassSimulateur as simulateur 
import ClassCarte as carte

class robot:
    def __init__(self, carte):
        self.coordonneeRobot = [carte.coordonneeBase[0], carte.coordonneeBase[1]]
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
        self.feuAssigned = None 
        
    def eteindreFeu(self,feu) :
        while(feu.ampleurFeu>0) :
            if feu.coordonneeFeu == self.coordonneeRobot:
                self.etatEau=self.etatEau-1
                feu.ampleurFeu=feu.ampleurFeu -1 
                T=('F',feu.coordonneeFeu)
                simulateur.listeFeu= simulateur.listeFeu.remove(T)
                print("Le feu est éteint")
            else :
                a=np.rand(0,1)
                if a==0 :
                    ampleurFeu=ampleurFeu-1
                else :
                    ampleurFeu=ampleurFeu+1
        
    def seDeplacer(self,feu):
        if (feu.coordonneeFeu(0)-self.coordonneeRobot(0))<0 and (feu.coordonneeFeu(1)-self.coordonneeRobot(1))<0 and len(feu.listeFeu)>0:
            self.coordonneeRobot[0]=self.coordonneeRobot[0]-self.constante
            self.coordonneeRobot[1]=self.coordonneeRobot[1]-self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneeRobot[0],self.coordonneeRobot[1])=='R'
        elif (feu.coordonneeRobot(0)-self.coordonneeRobot(0))>0 and (feu.coordonneeRobot(1)-self.coordonneeRobot(1))>0 and len(feu.listeFeu)>0:
            self.coordonneeRobot[0]=self.coordonneeRobot[0]+self.constante
            self.coordonneeRobot[1]=self.coordonneeRobot[1]+self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneeRobot[0],self.coordonneeRobot[1])=='R'
        elif (feu.coordonneeFeu(0)-self.coordonneeRobot(0))<0 and (feu.coordonneerFeu(1)-self.coordonneeRobot(1))>0 and len(feu.listeFeu)>0:   
            self.coordonneeRobot[0]=self.coordonneeRobot[0]-self.constante
            self.coordonneeRobot[1]=self.coordonneeRobot[1]+self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneeRobot[0],self.coordonneeRobot[1])=='R'
        elif (feu.coordonneeFeu(0)-self.coordonneeRobot(0))>0 and (feu.coordonneeFeu(1)-self.coordonneeRobot(1))<0 and len(feu.listeFeu)>0:
            self.coordonneeRobot[0]=self.coordonneeRobot[0]+self.constante
            self.coordonneeRobot[1]=self.coordonneeRobot[1]-self.constante
            self.etat == "en déplacement"
            carte.carte(self.coordonneeRobot[0],self.coordonneeRobot[1])=='R'

    def calculerDistance(self,feu):
        self.distance = ((feu.coordonneeFeu[0]-self.coordonneeRobot[0])**2+(feu.coordonneeFeu[1]-self.coordonneeRobot[1])**2)**0.5
        print("Le robot calcule la distance")
        return self.distance
    
    def remplirReservoir(self):
        if self.etatEau==0:
            self.etatEau=50
        print("Le robot se rempli")

    def estDevantFeu(self,feu) :
        if self.calculerDistance(self, feu)<1 :
            return True
    def getDispo(self):
        return self.robotDispo
    
    def setFeuAssigned(self, feu):
        self.feuAssigned = feu

    def mae(self, feu, nouvelle_mission=None):
            if self.etat == "a la base":
                print("État : À la base")
                if self.etatEau < 2:
                    self.remplirReservoir()  # Le remplissage est géré ici
                if feu.coordonneeFeu is not None:  # Une mission est disponible
                    self.calculerDistance(feu)
                    self.etat = "en attente de mission"

            elif self.etat == "en attente de mission":
                print("État : En attente de mission")
                if feu.coordonneeFeu is not None:  # Une mission est confirmée
                    print("Nouvelle mission reçue !")
                    self.calculerDistance(feu)
                    self.etat = "en déplacement"

            elif self.etat == "en déplacement":
                print("État : En déplacement")
                if feu.coordonneeFeu is not None:  # Se déplacer vers le feu
                    self.seDeplacer(feu)
                    if self.estDevantFeu(feu):  # Vérifier si arrivé à destination
                        print("Robot arrivé à destination.")
                        self.etat = "extinction du feu"

            elif self.etat == "extinction du feu":
                print("État : Extinction du feu")
                if feu.coordonneeFeu is not None and feu.ampleurFeu is not None:  # Si à proximité du feu
                    self.eteindreFeu(feu)  # Éteindre le feu
                    if self.etatEau == 0:  # Si le réservoir est vide
                        self.etat = "retour à la base"
                    else:  # Si encore du stock, retourner à l'état initial
                        self.etat = "a la base"

            """elif self.etat == "retour à la base":
                print("État : Retour à la base")
                self.seDeplacer([0, 0])  # Retourner aux coordonnées de la base
                if nouvelle_mission and self.etatEau >= 1:  # Nouvelle mission en chemin
                    print("Nouvelle mission reçue pendant le retour à la base !")
                    feu_coordonnees = nouvelle_mission  # Mise à jour des coordonnées pour la nouvelle mission
                    self.calculerDistance(feu_coordonnees)
                    self.etat = "en déplacement"
                elif self.coordonneeRobot == [0, 0]:  # Si arrivé à la base
                    print("Robot est arrivé à la base.")
                    self.etat = "a la base"  # Passer à l'état "a la base" """