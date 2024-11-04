

#######################################################################################
#######################################################################################
#######################################################################################

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from grille import Grille
from user import User
from bomb import Bomb
from chiffreInd import ChiffreInd

class InterfaceGraphique(QtWidgets.QWidget):
    def __init__(self, grille: Grille, user: User):
        super().__init__()
        self.grille = grille
        self.user = user
        self.first_click = True  # Variable pour gérer le premier clic
        self.elapsed_time = 0  # Variable pour le temps écoulé
        self.timer = QtCore.QTimer()  # Timer pour le chronomètre
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Démineur')
        self.setGeometry(100, 100, 600, 600)
        
        self.layout = QtWidgets.QGridLayout(self)

        self.timer.timeout.connect(self.update_timer)  # Connexion du timer à la méthode update_timer
        self.timer.start(1000)  # Mettre à jour toutes les secondes

        self.time_label = QtWidgets.QLabel("Temps écoulé : 0s")  # Label pour afficher le temps
        self.layout.addWidget(self.time_label, 0, 0)  

        self.buttons = {}
        for x in range(self.grille.taille):
            for y in range(self.grille.taille):
                button = QtWidgets.QPushButton()
                button.setFixedSize(60, 60)
                button.clicked.connect(lambda checked, x=x, y=y: self.cell_clicked(x, y))
                button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                button.customContextMenuRequested.connect(lambda pos, x=x, y=y: self.show_context_menu(pos, x, y))
                self.layout.addWidget(button, x + 1, y)  # Décalage de la grille pour laisser place au label
                self.buttons[(x, y)] = button

        # Initialiser la grille avec des cellules à zéro
        for x in range(self.grille.taille):
            for y in range(self.grille.taille):
                self.grille.cellules[x][y].value = 0  
                self.grille.cellules[x][y].visibilite = False  

    def update_timer(self):
        self.elapsed_time += 1  
        self.time_label.setText(f"Temps écoulé : {self.elapsed_time}s")  # Mise à jour le label

    def cell_clicked(self, x, y):
        if self.first_click:
            # Au premier clic, choisir une cellule sûre et placer les bombes
            self.first_click = False
            safe_cell = (x, y)
            Bomb.place_bomb(self.grille.grid, safe_cell)
            grille.set_visibilite(safe_cell)
            self.place_chiffres()

        # Gérer le clic gauche pour révéler une case
        if not self.grille.cellules[x][y].visibilite:
            self.user.cleanCase(self.grille, x, y)
            if self.detectLoose(x, y):
                self.show_message("Vous êtes tombé sur une bombe ! Partie terminée.")
                self.close()
            elif self.detectWin():
                self.show_message(f"Félicitations ! Vous avez gagné la partie en {self.elapsed_time} secondes.")  # Afficher le temps final
                self.close()
            else:
                self.update_cell_display(x, y)

    def place_chiffres(self):
        # Placer les chiffres indicateurs sur la grille
        for i in range(self.grille.taille):
            for j in range(self.grille.taille):
                if self.grille.grid[i, j] != 666:  # Si ce n'est pas une bombe
                    chiffre = ChiffreInd(grille.id, grille.taille, grille.difficulty, i, j, chiffre_id=(i * grille.taille + j))
                    chiffre.place_number(self.grille.grid)
                    self.grille.grid[i, j] = chiffre.value  # Attribuer la valeur calculée à la grille

    def show_context_menu(self, pos, x, y):
        menu = QtWidgets.QMenu(self)
        
        if self.grille.cellules[x][y].flag:
            remove_flag_action = menu.addAction("Retirer drapeau")
            remove_flag_action.triggered.connect(lambda: self.remove_flag(x, y))
        else:
            place_flag_action = menu.addAction("Placer drapeau")
            place_flag_action.triggered.connect(lambda: self.place_flag(x, y))

        menu.exec_(self.mapToGlobal(pos))

    def remove_flag(self, x, y):
        self.user.removeFlag(self.grille, x, y)
        self.update_cell_display(x, y)

    def place_flag(self, x, y):
        self.user.placeFlag(self.grille, x, y)
        self.update_cell_display(x, y)

    def detectLoose(self, x, y):
        return self.grille.grid[x][y] == 666  # Vérifie si la cellule révélée est une bombe

    def detectWin(self):
        return all(cell.visibilite for row in self.grille.cellules for cell in row if cell.value != 666)

    def show_message(self, message):
        QMessageBox.information(self, "Info", message)

    def update_cell_display(self, x, y):
        for i in range(self.grille.taille):
            for j in range(self.grille.taille):
                cell = self.grille.cellules[i][j]
                button = self.buttons[(i, j)]

                if cell.visibilite:
                    button.setText(str(cell.value) if cell.value != 666 else "B")
                    button.setEnabled(False)
                else:
                    button.setText("F" if cell.flag else "")
                    button.setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Initialisation d'une grille et d'un utilisateur
    grille = Grille(id=1, taille=10)
    user = User(user_id=1, name="Player", score=[])
    
    # Création de l'interface graphique
    interface = InterfaceGraphique(grille, user)

    interface.show()
    sys.exit(app.exec_())
