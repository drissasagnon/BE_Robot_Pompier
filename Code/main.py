from ClassSimulateur import Simulateur
from ClassIHM import IHM

# Créer une instance du simulateur
simulateur = Simulateur()

# Passer l'instance du simulateur à IHM
ihm = IHM(simulateur)

# Lancer le menu principal
ihm.menu_principal()
