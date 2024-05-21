def longueur_chaine(chaine):
    compteur = 0
    for caractere in chaine:
        compteur += 1
    return compteur

# Exemple d'utilisation
chaine = "Bonjour, monde !"
longueur = longueur_chaine(chaine)
print("La longueur de la chaîne est :", longueur)
