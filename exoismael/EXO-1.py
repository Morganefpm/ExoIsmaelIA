def mile_to_km(distance_miles):
    # 1 mile est égal à 1.60934 kilomètres
    distance_km = distance_miles * 1.60934
    return distance_km

# Demander à l'utilisateur d'entrer la distance en miles
distance_miles = float(input("Entrez la distance en miles : "))

# Convertir la distance en km en utilisant la fonction
distance_km = mile_to_km(distance_miles)

# Afficher le résultat
print(f"{distance_miles} miles équivaut à {distance_km} kilomètres.")
