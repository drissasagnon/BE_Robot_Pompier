class Carte:
    def __init__(self, taille):
        self.taille = taille
        self.repere = [[0] * taille for _ in range(taille)]

    def chargerCarte(self):
        """
        Charge une carte simple.
        """
        print("Carte chargée avec succès.")
