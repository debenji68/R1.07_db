
nom1 = input("Entrez le nom de la personne 1 : ")
prenom1 = input("Entrez le prénom de la personne 1 : ")

nom2 = input("Entrez le nom de la personne 2 : ")
prenom2 = input("Entrez le prénom de la personne 2 : ")

nom1_upper = nom1.upper()
nom2_upper = nom2.upper()

prenom1_formatted = prenom1.capitalize()
prenom2_formatted = prenom2.capitalize()

output1 = f"{prenom1_formatted} {nom1_upper}"
output2 = f"{prenom2_formatted} {nom2_upper}"

if nom1 < nom2:
    resultat_ligne1 = output1
    resultat_ligne2 = output2
elif nom2 < nom1:
    resultat_ligne1 = output2
    resultat_ligne2 = output1
else:
    if prenom1 < prenom2:
        resultat_ligne1 = output1
        resultat_ligne2 = output2
    else:
        resultat_ligne1 = output2
        resultat_ligne2 = output1

print(f"Prenom NOM : {resultat_ligne1}")
print(f"Prenom NOM : {resultat_ligne2}")