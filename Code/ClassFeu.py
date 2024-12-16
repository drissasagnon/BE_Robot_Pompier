class Feu:
    def __init__(self, idFeu, ampleur, coordonnees):
        if not isinstance(ampleur, (int, float)) or ampleur <= 0:
            raise ValueError("L'ampleur du feu doit être un entier ou un flottant positif.")
        if not isinstance(coordonnees, list) or len(coordonnees) != 2:
            raise ValueError("Les coordonnées doivent être une liste de deux éléments.")
        self.idFeu = idFeu
        self.ampleur = ampleur
        self.coordonnees = coordonnees

    def seDeclencher(self):
        print(f"Le feu {self.idFeu} s'est déclenché aux coordonnées {self.coordonnees}.")

    def eteindre(self):
        self.ampleur = 0
        print(f"Le feu {self.idFeu} a été éteint.")
