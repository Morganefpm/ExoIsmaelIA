def afficher_alphabet():
    lettre_a = ord('a')
    lettre_z = ord('z')
    
    for i in range(lettre_a, lettre_z + 1):
        print(chr(i))

# Appeler la fonction pour afficher chaque lettre de l'alphabet
afficher_alphabet()
