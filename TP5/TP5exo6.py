chaine = input("Entrez une chaîne de caractères : ")
taille = len(chaine)
print("Taille de la chaîne :", taille)

voyelles = "aeiouyAEIOUY"
nb_voyelles = sum(1 for c in chaine if c in voyelles)
pourcentage = (nb_voyelles / taille) * 100 if taille > 0 else 0
print(f"Pourcentage de voyelles : {pourcentage:.2f}%")

mot = "wagon"
indice = chaine.find(mot)
if indice != -1:
    print(f'Le mot "wagon" apparaît à l’indice {indice}.')
else:
    print('Le mot "wagon" n’est pas présent.')

occ = chaine.count(mot)
print(f'Nombre d’occurrences de "{mot}" : {occ}')
