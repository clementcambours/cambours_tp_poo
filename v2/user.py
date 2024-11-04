 
from grille import Grille

class User:
    def __init__(self, user_id: int, name: str, score: list):
        self.id = user_id
        self.name = input("pseudo : ")
        self.score = score
        self.grilles = []  # Liste de grilles associées à l'utilisateur

    def placeFlag(self, grille: Grille, x: int, y: int):
        # Placer le drapeau à l'emplacement donné
        grille.cellules[x][y].flag = True
        print(f"Drapeau placé à la cellule ({x}, {y})")

        # Afficher la grille avec le drapeau
        print("Grille mise à jour :")
        grille.update_cellule_values()
        grille.afficher_grille()

    def removeFlag(self, grille: Grille, x: int, y: int):
        # Retirer le drapeau à l'emplacement donné
        if grille.cellules[x][y].flag:
            grille.cellules[x][y].flag = False
            print(f"Drapeau enlevé à la cellule ({x}, {y})")
        else:
            print(f"Aucun drapeau n'est présent à la cellule ({x}, {y})")

        # Afficher la grille après avoir retiré le drapeau
        print("Grille mise à jour après avoir retiré le drapeau :")
        grille.update_cellule_values()
        grille.afficher_grille()

    def cleanCase(self, grille: Grille, x: int, y: int):
        # Rendre la cellule visible
        if not grille.cellules[x][y].visibilite:
            grille.cellules[x][y].visibilite = True
            print(f"La cellule ({x}, {y}) est maintenant visible.")
        else:
            print(f"La cellule ({x}, {y}) est déjà visible.")
        return x, y  # On retourne les coordonnées pour vérification dans la boucle de jeu
    
    