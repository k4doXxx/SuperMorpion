import random
def afficher_grille(grille): #affichage de la forme de la grille
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def debut_jeu():
    print("Bonjour bienvenue dans le Super Morpion !\n")
    print("Joueur 1 = ⭕\nJoueur 2 = ❌\n")

#création de la grille 3x3

grille = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

debut_jeu()
afficher_grille(grille)

def recommencer(): #Proposition de recommencer une nouvelle partie
    NouvellePartie = input("Voulez vous recommencer une partie? (oui/non): ")
    if NouvellePartie.lower() == "oui":
        debut_jeu()
        afficher_grille(grille)
        jouer()
    if NouvellePartie.lower() == "non":
        print("A bientôt !")


#Poser un pion dans un emplacement vide
def verifier_gagnant(grille):
    # Détection d’une ligne
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] != "-":
            return True

    # Détection d’une colonne
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] != "-":
            return True

    # Détection des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] != "-" or grille[0][2] == grille[1][1] == grille[2][0] != "-":
        return True


def jouer(): #Système de tour par tour où l'on peut poser un pion que sur un emplacemment vide
    tentative = 9
    while tentative > 0:
        print("JOUEUR 1 à vous de jouer !\n")
        ligne = int(input("Saisir une ligne (0, 1, ou 2): "))
        colonne = int(input("Saisir une colonne (0, 1, ou 2): "))
        if grille[ligne][colonne] == "-":
            grille[ligne][colonne] = "⭕"
            afficher_grille(grille)
            if verifier_gagnant(grille):
                print("Fin de la partie.\nFelicitation joueur 1 vous avez gagné !!!")
                recommencer()
                return
            tentative -=1
        else:
            print("Emplacement est occupé. Veuillez choisir un autre emplacement.\n")
            continue

        print("JOUEUR 2 à vous de jouer !")
        #L’adversaire pose un pion
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        while grille[ligne][colonne] != "-":
            ligne = random.randint(0, 2)
            colonne = random.randint(0, 2)
        grille[ligne][colonne] = "❌"
        afficher_grille(grille)
        if verifier_gagnant(grille):
            print("Fin de la partie\nFélicitation Joueur 2, vous avez gagné !")
            recommencer()
            return
        tentative -= 1

    if tentative == 0:
        print("Fin de la partie, c'est une égalité !")

jouer()


