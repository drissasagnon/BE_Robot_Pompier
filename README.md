# BE_Robot_Pompier

## Description

Ce programme est une simulation interactive de gestion de robots pour l'extinction de feux. Il permet de :
- Créer et gérer des robots dotés de capacités spécifiques.
- Simuler des incendies avec différents ampleurs.
- Automatiser l'assignation des robots aux feux en fonction de leur disponibilité et de leur proximité.
- Visualiser les mouvements des robots et la progression de la simulation à travers une interface graphique.

## Fonctionnalités principales

1. **Classe Robot** :
   - Gère les actions des robots, notamment le déplacement et l'extinction de feux.
   - Implémente une machine à états (MAE) pour orchestrer les étapes successives : remplissage du réservoir, déplacement, extinction et retour.

2. **Classe Feu** :
   - Gérer les caractéristiques et les comportements associés à un feu.

3. **Classe Manager** :
   - Coordonne les interactions entre les robots et les feux.
   - Affecte les robots disponibles aux feux les plus proches.
   - Calcule les distances pour optimiser les affectations.

4. **Classe Simulateur** :
   - Centralise les robots et les feux dans une simulation.
   - Offre des options de contrôle : ajouter des robots, ajouter des feux, lancer ou réinitialiser la simulation...

5. **Interface Graphique (GUI)** :
   - Permet une visualisation dynamique de la simulation.
   - Fournit des boutons pour ajouter des robots, des feux, accélérer, ralentir ou mettre en pause la simulation.
il est bien de noter que notre interface graphique est a titre indicatif et n'est pas liée au code final

## Installation

1. Clonez le dépôt ou téléchargez les fichiers sources.
2. Assurez-vous d'avoir Python 3.x installé sur votre machine.
3. Installez les dépendances nécessaires (notamment `tkinter`,`PIL`,`time`,`threading` et `Pillow` pour l'interface graphique) :
   pip install tkinter
   pip install PIL
   pip install time
   pip install threading
   pip install pillow


## Utilisation

1.1 Lancez le programme principal maingraphique si vous voulez accéder à l'interface graphique :
   python maingraphique.py
1.2 Lancez le programme principal main si vous voulez accéder au menu terminal qui affiche les états du robot:
   python main.py
 

2.1 Naviguez dans l'interface au terminal:
   - **Ajouter un robot** : Ajoutez un robot avec un ID, un type, un nom, et une vitesse.
   - **Ajouter un feu** : Placez un feu avec une position et une ampleur.
   - **Lancer la simulation** : Démarrez la simulation, observez les robots se déplacer et éteindre les feux.
   - **Quitter la simulation** : Terminez la simulation.

2.1 Naviguez dans l'interface graphique:
   - **Ajouter un robot** : Ajoutez un robot.
   - **Ajouter un feu** : Placez un feu avec la position souhaité.
   - **Lancer la simulation** : Démarrez la simulation, observez les robots se déplacer et éteindre les feux.  
   - **Contrôles de simulation** : Accélérez, ralentissez, mettez en pause ou reprenez la simulation.
   - **Quitter la simulation** : Terminez la simulation.

## Détails techniques

### Classe Robot
- **Attributs principaux** :
  - `idRobot`, `typeRobot`, `nom`, `vitesse`, `coordonnées`, `etatEau`, etc.
- **Méthodes** :
  - `remplirReservoir()`, `seDeplacer(destination)`, `eteindreFeu(coordonneesFeu, ampleurFeu)`, `retournerBase()`, `mae()`.

### Classe Manager
- **Rôles** :
  - Calculer les distances entre robots et feux.
  - Affecter les robots en fonction des feux actifs.
- **Attributs principaux** :

- **Méthodes** :
  - `calculer_distance(coordonnées)`, `trouver_feu_le_plus_proche(robot)`, `affecter_un_robot_a_un_feu(robot, feu)`, `affecterRobot()`, etc.


### Classe Simulateur
- Centralise les robots et feux.
- Coordonne la simulation globale.
- **Attributs principaux** :

- **Méthodes** :
  - `ajouterFeu(idFeu, coordonnées, ampleur)`, `ajouterRobot(robot)`, `executerSimulation()`, `accelerer_simulation()`, etc.

### Classe Feu
- **Attributs principaux** :
  - `idFeu`, `ampleur`, `coordonnées`, etc.
- **Méthodes** :
  - `eteindre()`, `sedeclencher()`.

### Classe IHM
- Interface sous terminal.
- **Attributs principaux** :
    - `simulateur`.
- **Méthodes** :
    - `menu_principal(self)`.

### Interface Graphique
- Utilise `tkinter` pour afficher les éléments visuels et les animations.
- Chargement d'une carte donnée (`carte.png`) en fond.


## Structure des fichiers

- `main.py` : programme sous terminal.
- `maingraphique.py` : programme interface graphique.
- `ClassRobot.py` : Définition de la classe `Robot`.
- `ClassManager.py` : Définition de la classe `Manager`.
- `ClassSimulateur.py` : Définition de la classe `Simulateur`.
- `ClassFeu.py` : Définition de la classe `Feu`.
- `ClassIHM.py` : Définition de la classe `IHM`pour interface sous terminal.
- `IHM.py` : Interface graphique.
- `carte.png` : fichier image de la carte.

## Améliorations possibles

- Implémenter des types de robots avec des capacités spécifiques.
- Enrichir l'interface graphique avec des statistiques sur le temps d'extinction ou de simulation.
- Améliorer l'interface graphique en améliorant les icones des Robots et Feux.
- Ajouter une gestion des pannes ou limitations des robots.
- Rendre le déplacement des robots plus réel suivant les vrais chemins de la carte.
-Lier toutes les classes existantes avec l'interface graphique pour une gestion cohérente.

## Auteurs

Programme développé par {MOEZ CHAGRAOUI, RAYEN YADIR, YASSINE ABDELILLAH et DRISSA SAGNON} .


