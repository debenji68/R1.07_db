import os.path
import datetime

def verifier_fichier(nom_fichier):
    """Vérifie l'existence, la taille, et l'heure de dernière modification d'un fichier."""
    if not os.path.isfile(nom_fichier):
        print(f"Le chemin '{nom_fichier}' n'est pas un fichier valide ou n'existe pas.")
        return None
    print(f"\n--- Informations pour {nom_fichier} ---")
    taille = os.path.getsize(nom_fichier)
    print(f"Taille : **{taille}** octets")
    timestamp_modif = os.path.getmtime(nom_fichier)
    date_modif = datetime.datetime.fromtimestamp(timestamp_modif)
    print(f"Dernière modification : **{date_modif.strftime('%Y-%m-%d %H:%M:%S')}**")
    return timestamp_modif

def comparer_fichiers(ts1, nom1, ts2, nom2):
    """Compare deux timestamps de modification et affiche le fichier le plus récent."""
    if ts1 is None and ts2 is None:
        print("\nAucun des deux fichiers spécifiés n'est valide.")
    elif ts1 is None:
        print(f"\nSeul le fichier '{nom2}' est valide.")
        print(f"Le fichier le plus récent est : **{nom2}**")
    elif ts2 is None:
        print(f"\nSeul le fichier '{nom1}' est valide.")
        print(f"Le fichier le plus récent est : **{nom1}**")
    else:
        print("\n--- Comparaison ---")
        if ts1 > ts2:
            date_recent = datetime.datetime.fromtimestamp(ts1)
            print(f"Le fichier le plus récent est : **{nom1}**")
            print(f"Date de modification : **{date_recent.strftime('%Y-%m-%d %H:%M:%S')}**")
        elif ts2 > ts1:
            date_recent = datetime.datetime.fromtimestamp(ts2)
            print(f"Le fichier le plus récent est : **{nom2}**")
            print(f"Date de modification : **{date_recent.strftime('%Y-%m-%d %H:%M:%S')}**")
        else:
            print("Les deux fichiers ont été modifiés au même instant.")


fichier1_nom = input("Entrez le nom du premier fichier (ex: f1.txt) : ")
fichier2_nom = input("Entrez le nom du second fichier (ex: f2.txt) : ")
timestamp1 = verifier_fichier(fichier1_nom)
timestamp2 = verifier_fichier(fichier2_nom)
comparer_fichiers(timestamp1, fichier1_nom, timestamp2, fichier2_nom)