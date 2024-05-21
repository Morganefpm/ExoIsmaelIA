def tri_bulles_decroissant(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] < tab[j+1]:
                # Échanger les éléments si l'élément actuel est plus petit que le suivant
                tab[j], tab[j+1] = tab[j+1], tab[j]

def ranger_tableau_par_ordre_decroissant(tab):
    # Appel de la fonction de tri à bulles pour le tri décroissant
    tri_bulles_decroissant(tab)

# Exemple d'utilisation
import random

# Générer un tableau d'entiers aléatoires de plus de 15 indices
tableau = [random.randint(1, 100) for _ in range(20)]

print("Tableau avant le tri :")
print(tableau)

# Appeler la fonction pour ranger le tableau par ordre décroissant
ranger_tableau_par_ordre_decroissant(tableau)

print("\nTableau après le tri :")
print(tableau)
