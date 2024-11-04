class Cellule:
    def __init__(self, id_grille: bool, taille_grille: int, difficulty: int, x: int, y: int, visibilite: bool = False, flag: bool = False):
        self.id_grille = id_grille
        self.taille_grille = taille_grille
        self.difficulty = difficulty
        self.X = x
        self.Y = y
        self.visibilite = visibilite  
        self.flag = flag  
        self.value = None 



