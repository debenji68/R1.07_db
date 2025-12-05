def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

lst1 = [0, 1, 2]
lst2 = ajouter_elt(lst1, len(lst1))

print("\nListe lst1")
print(f"Contenu : {lst1}")
print(f"Type : {type(lst1)}")
print(f"ID (Identifiant mémoire) : {id(lst1)}")

print("\nListe lst2")
print(f"Contenu : {lst2}")
print(f"Type : {type(lst2)}")
print(f"ID (Identifiant mémoire) : {id(lst2)}")


#Les IDs de lst1 et lst2 sont identiques.
#Les contenus de lst1 et lst2 sont égaux ([0, 1, 2, 3]).
