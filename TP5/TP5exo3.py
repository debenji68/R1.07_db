def preparer_chaine(chaine):
    """
    Prépare la chaîne d'entrée en la mettant en minuscule
    et en ne gardant que les caractères alphabétiques.
    """
    chaine_lower = chaine.lower()
    chaine_epuree = ""
    for caractere in chaine_lower:
        if caractere.isalpha():
            chaine_epuree += caractere
    return chaine_epuree
def est_palindrome_recursif(chaine):
    """
    Teste si une chaîne épurée est un palindrome en utilisant la récursivité.
    """
    if len(chaine) <= 1:
        return True
    if chaine[0] == chaine[-1]:
        return est_palindrome_recursif(chaine[1:-1])
    else:
        return False

entree_utilisateur = input("Entrez un mot ou une phrase : ")
chaine_finale_test = preparer_chaine(entree_utilisateur)
if est_palindrome_recursif(chaine_finale_test):
    print("C'est un **palindrome** !")
else:
    print("Ce n'est **PAS** un palindrome.")
