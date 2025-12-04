heures = float(input("Nombre d'heures travaillées : "))
salaire_horaire = float(input("Salaire horaire : "))
salaire = 0

if heures <= 160:
    salaire = heures * salaire_horaire
else:
    salaire = 160 * salaire_horaire
    if heures <= 200:
        salaire += (heures - 160) * salaire_horaire * 1.25
    else:
        salaire += 40 * salaire_horaire * 1.25
        salaire += (heures - 200) * salaire_horaire * 1.5

print(f"Salaire total : {salaire:.2f} €")
