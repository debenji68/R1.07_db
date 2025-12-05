#-------------a-------------------
L1 = [0] * 3
print(f"Liste L1 : {L1}")
print(f"Type de L1 : {type(L1)}")
print(f"ID de L1 (adresse mémoire) : {id(L1)}\n")

#--------------b--------------------
print("Éléments \t Valeur \t Type \t\t ID (Identifiant)")
for i, element in enumerate(L1):
    print(f"L1[{i}] \t\t {element} \t\t {type(element)} \t {id(element)}")

# Remarque : Tous les éléments pointent vers le MÊME objet entier (0).
#Cela est dû à la répétition de la référence lors de '[0] * 3'.


#---------------c-------------------------
L1[1] = L1[1] + 1
print(f"Liste L1 après modification : {L1}")
print(f"Type de L1 : {type(L1)}")
print(f"Nouvel ID de L1 : {id(L1)}")

#Conclusion : L'ID de la liste L1 'a pas changé. Une liste est un objet mutable.
#La modification se fait sur le même emplacement mémoire.

#---------------d----------------------------------
print("Éléments \t Valeur \t Type \t\t ID (Identifiant)")
for i, element in enumerate(L1):
    print(f"L1[{i}] \t\t {element} \t\t {type(element)} \t {id(element)}")

#Conclusion : L'entier 1 (L1[1]) a un ID différent de l'entier 0 (L1[0] et L1[2]).
#Un entier (int) est un objet immuable. Pour passer de 0 à 1, Python a créé un nouvel objet '1'.

#---------------------e----------------------------
ma_chaine = "machaine"
print(f"Variable ma_chaine : {ma_chaine}")
print(f"Type de ma_chaine : {type(ma_chaine)}")
print(f"ID de ma_chaine : {id(ma_chaine)}\n")

print("Car. \t Valeur \t Type \t\t ID (Identifiant)")
for i, char in enumerate(ma_chaine):
    print(f"[{i}] \t {char} \t\t {type(char)} \t {id(char)}")

#Remarque : Les deux occurrences du caractère 'a' ont le même ID.
#Ceci est similaire à l'observation avec les entiers. Python optimise la mémoire en mettant en cache les objets chaînes de caractères unitaires et fréquents.