try:
    somme = int(input("Entrez la somme d'argent entière à décomposer (en euros) : "))
except ValueError:
    print("Erreur : Veuillez entrer une valeur numérique entière.")
    exit()

valeurs_disponibles = [100, 50, 10, 2, 1]
decomposition_resultat = []
somme_restante = somme
for valeur in valeurs_disponibles:
    nombre_unites = somme_restante // valeur
    if nombre_unites > 0:
        if valeur >= 10:
            libelle = "billets"
        else:
            libelle = "pièces"
        decomposition_resultat.append(f"{nombre_unites} {libelle} de {valeur}")
    somme_restante = somme_restante % valeur

if not decomposition_resultat:
    message_decomposition = "aucune unité de monnaie."
elif len(decomposition_resultat) == 1:
    message_decomposition = decomposition_resultat[0] + "."
else:
    dernier_element = decomposition_resultat.pop()
    message_decomposition = ", ".join(decomposition_resultat) + f" et {dernier_element}."

print(f"La décomposition de {somme} euros est : {message_decomposition}")