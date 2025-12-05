import random
#-------------------------------a---------------------------
def generer(nbr, vmin, vmax):
    tableau = [random.randint(vmin, vmax) for _ in range(nbr)]
    return tableau

def combienInferieur(table, vseuil):
    compteur = 0
    for valeur in table:
        if valeur < vseuil:
            compteur += 1
    return compteur

#---------------------b----------------------
while True:
    try:
        nb_valeurs = int(input("Combien de valeurs souhaitez-vous générer (ex: 100) ? "))
        if nb_valeurs > 0:
            break
        print("Veuillez entrer un nombre positif.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre entier.")

while True:
    try:
        vmin = int(input("Entrez la valeur minimale (vmin) de l'intervalle : "))
        vmax = int(input("Entrez la valeur maximale (vmax) de l'intervalle : "))
        if vmin <= vmax:
            break
        print("La valeur minimale doit être inférieure ou égale à la valeur maximale.")
    except ValueError:
        print("Entrée invalide. Veuillez entrer des nombres entiers.")

SEUIL_DEFAUT = 30
reponse_seuil = input("Voulez-vous préciser le seuil (Oui/O ou Non/N) ? ").strip().lower()

seuil = SEUIL_DEFAUT
if reponse_seuil in ('oui', 'o'):
    while True:
        try:
            seuil_choisi = int(input("Veuillez entrer la valeur du seuil : "))
            seuil = seuil_choisi
            break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier pour le seuil.")
else:
    print(f"Le seuil par défaut ({SEUIL_DEFAUT}) sera appliqué.")

tableau_resultat = generer(nb_valeurs, vmin, vmax)
tableau_resultat.sort()
compte_final = combienInferieur(tableau_resultat, seuil)

print("\n--- RÉSULTATS FINAUX ---")
print(f"Paramètres : {nb_valeurs} valeurs, intervalle [{vmin}, {vmax}], seuil {seuil}")
print(f"Tableau généré et trié : {tableau_resultat}")
print(f"Le nombre de valeurs inférieures à {seuil} est : {compte_final}")