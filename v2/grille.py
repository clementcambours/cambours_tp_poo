import numpy as np
from cellule import Cellule

class Grille:
    def __init__(self, id: int, taille: int):
        self.id = id
        self.taille = taille
        self.difficulty = int(input("Choose your level: 1, 2 or 3: "))

        if self.difficulty == 1:
            self.taille = 10
        elif self.difficulty == 2:
            self.taille = 20
        elif self.difficulty == 3:
            self.taille = 30

        self.grid = np.zeros((self.taille, self.taille))  # Création de la grille
        self.cellules = [[Cellule(id_grille=self.id, taille_grille=self.taille, difficulty=self.difficulty, x=i, y=j) for j in range(self.taille)] for i in range(self.taille)]

    # # si l'on veut jouer uniquement depuis le terminal   
    # def choisir_case(self):
    #     # Demander à l'utilisateur de choisir une case (X, Y)
    #     while True:
    #         try:
    #             x = int(input(f"Choose a row (0 to {self.taille - 1}): "))
    #             y = int(input(f"Choose a column (0 to {self.taille - 1}): "))
    #             if 0 <= x < self.taille and 0 <= y < self.taille:
    #                 break
    #             else:
    #                 print(f"Invalid input! Please choose values between 0 and {self.taille - 1}.")
    #         except ValueError:
    #             print("Invalid input! Please enter integers.")
    #     print(f"You chose the cell: ({x}, c{y})")
    #     return (x, y)

    def set_visibilite(self, selected_cell):
        # Définir la visibilité de la cellule sélectionnée
        x, y = selected_cell
        self.cellules[x][y].visibilite = False  # La cellule choisie est visible

        # Calculer 5 % du nombre total de cellules à rendre visibles
        total_cells = self.taille * self.taille
        cells_to_reveal = max(1, int(total_cells * 0.05))  # Au moins une cellule

        # Récupérer les cellules voisines qui ne sont pas des bombes
        neighbors = []
        for i in range(max(0, x - 1), min(self.taille, x + 2)):  
            for j in range(max(0, y - 1), min(self.taille, y + 2)):  
                if (i, j) != (x, y) and self.grid[i, j] != 666:  # Pas la cellule choisie et pas une bombe
                    neighbors.append((i, j))

        # Rendre visibles les cellules les plus proches (5 %)
        np.random.shuffle(neighbors)  # Mélanger les voisins pour randomiser
        for cell in neighbors[:cells_to_reveal]:
            self.cellules[cell[0]][cell[1]].visibilite = True

    def update_cellule_values(self):
        # Associer les valeurs de la grille self.grid aux objets Cellule dans self.cellules
        for i in range(self.taille):
            for j in range(self.taille):
                self.cellules[i][j].value = self.grid[i, j]  # Assigner la valeur de la grille à la cellule
    
    def afficher_grille(self):
        # Associer les valeurs de la grille self.grid aux objets Cellule dans self.cellules
        self.update_cellule_values()

        # Affichage de la grille avec drapeaux, valeurs visibles et cellules non visibles
        print(self.grid)  
        for row in self.cellules:
            print(" | ".join([
                'D' if cell.flag else str(cell.value) if cell.visibilite and cell.value is not None else 'V' if cell.visibilite else 'F'
                for cell in row
            ]))  # D pour drapeau, valeur pour cellule visible, F pour non visible
        print()  # Nouvelle ligne pour séparer les affichages

    