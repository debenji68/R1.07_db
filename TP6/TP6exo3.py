def ajouter_elt(lst=[0, 1, 2], elt=3):
    lst.append(elt)
    return lst

#---------------a--------------
resultat_a = ajouter_elt()
print(resultat_a)

#---------------b------------------
resultat_b = ajouter_elt()
print(resultat_b)

print(f"ID du premier résultat: {id(resultat_a)}")
print(f"ID du deuxième résultat: {id(resultat_b)}")
#Explication: L'ID est le même. La liste par défaut est partagée et modifiée.

#-----------------c--------------------------
def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

#---------------------d-------------------------
resultat_d = ajouter_carac()
print(resultat_d)

#------------------------e-----------------------
resultat_e = ajouter_carac()
print(resultat_e)
#Résultat : abcd (identique au premier appel)