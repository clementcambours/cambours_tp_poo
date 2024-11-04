from grille import Grille
from bomb import Bomb
from chiffreInd import ChiffreInd
from user import User

# Création d'un utilisateur


    # deroulement jeu 

# Création d'un utilisateur
user1 = User(user_id=1, name=str, score=[])
# Exemple d'utilisation :
grille = Grille(id=1, taille=20)  # Niveau 2 (grille de taille 20x20)
safe_cell = grille.choisir_case()  # L'utilisateur choisit une case
Bomb.place_bomb(grille.grid, safe_cell, grille.difficulty)  # Les bombes sont placées en excluant cette case
grille.set_visibilite(safe_cell)  # Attribuer la visibilité à la cellule choisie et ses voisines
# Placer les chiffres pour chaque cellule (ici, on le fait pour toutes les cellules de la grille)
for i in range(grille.taille):
    for j in range(grille.taille):
        if grille.grid[i, j] != 666:  # Si ce n'est pas une bombe
            chiffre = ChiffreInd(grille.id, grille.taille, grille.difficulty, i, j, chiffre_id=(i * grille.taille + j))
            chiffre.place_number(grille.grid)
            grille.grid[i, j] = chiffre.value  # Attribuer la valeur calculée à la grille
# Afficher la grille avant de placer un drapeau
print("Grille avant de placer le drapeau :")
grille.update_cellule_values()
grille.afficher_grille()


user1.jeu(grille)



