def est_nombre_armstrong(nombre):
    # Convertir le nombre en une chaîne de caractères pour pouvoir itérer sur chaque chiffre
    chiffres = str(nombre)
    
    # Initialiser la somme
    somme = 0
    
    # Calculer la somme des cubes des chiffres
    for chiffre in chiffres:
        somme += int(chiffre) ** 3
    
    # Vérifier si la somme est égale au nombre d'origine
    return somme == nombre

# Demander à l'utilisateur d'entrer un numéro
numero = int(input("Entrez un numéro : "))

# Vérifier si le numéro est un nombre d'Armstrong et afficher le résultat
if est_nombre_armstrong(numero):
    print(f"{numero} est un nombre Armstrong")
else:
    print(f"{numero} n'est pas un nombre Armstrong")
