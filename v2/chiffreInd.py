from cellule import Cellule
import numpy as np

class ChiffreInd(Cellule):
    def __init__(self, id_grille: bool, taille_grille: list, difficulty: int, x: int, y: int, chiffre_id: int):
        super().__init__(id_grille, taille_grille, difficulty, x, y)
        self.id = chiffre_id
        self.value = 0

    def place_number(self, grid):
        # Compter le nombre de bombes parmi les voisins
        bomb_count = 0
        for x in range(max(0, self.X - 1), min(grid.shape[0], self.X + 2)):  
            for y in range(max(0, self.Y - 1), min(grid.shape[1], self.Y + 2)):  
                if (x, y) != (self.X, self.Y) and grid[x, y] == 666:  
                    bomb_count += 1
        self.value = bomb_count  # Attribuer le nombre de bombes



   