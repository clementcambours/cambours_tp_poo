from cellule import Cellule 
import numpy as np

class Bomb(Cellule):
    def __init__(self, id_grille: bool, taille_grille: list, difficulty: int, x: int, y: int, bomb_id: int):
        super().__init__(id_grille, taille_grille, difficulty, x, y)
        self.id = bomb_id

    @staticmethod
    def place_bomb(grid, safe_cell):
        # Calcul du nombre de bombes en fonction de la difficulté (10% des cases)
        n = int(grid.shape[0] * grid.shape[1] * 10 / 100)

        # Créer une liste de toutes les cases sauf la case choisie
        all_cells = [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1])]
        all_cells.remove(safe_cell)  

        # Choisir des bombes parmi les autres cases
        bomb_indices = np.random.choice(len(all_cells), size=n, replace=False)
        bomb_coords = [all_cells[i] for i in bomb_indices]

        # Placer les bombes dans la grille
        for coord in bomb_coords:
            grid[coord] = 666  # 666 représente une bombe

