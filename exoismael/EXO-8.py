def afficher_pyramide(n):
    # Vérifier si l'entrée est un entier positif
    if not isinstance(n, int) or n <= 0:
        print("Veuillez entrer un entier positif.")
        return
    
    # Générer la pyramide d'étoiles
    for i in range(1, n + 1):
        # Calculer le nombre d'étoiles pour cette ligne
        nb_etoiles = 2 * i - 1
        # Calculer le nombre d'espaces à gauche pour centrer la ligne
        nb_espaces = n - i
        # Afficher les espaces à gauche
        print(" " * nb_espaces, end="")
        # Afficher les étoiles
        print("*" * nb_etoiles)

# Demander à l'utilisateur de saisir le nombre de lignes pour la pyramide
try:
    lignes = int(input("Entrez le nombre de lignes pour la pyramide d'étoiles : "))
    # Appeler la fonction pour afficher la pyramide
    afficher_pyramide(lignes)
except ValueError:
    print("Veuillez entrer un entier pour le nombre de lignes.")
