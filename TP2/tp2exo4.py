BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
nouveau_fromage = (fromage * nbConvives) / BASE
nouvelle_eau = (eau * nbConvives) / BASE
nouvel_ail = (ail * nbConvives) / BASE
nouveau_pain = (pain * nbConvives) / BASE
print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {nouveau_fromage} gr de fromage")
print(f"- {nouvelle_eau} dl d'eau")
print(f"- {nouvel_ail} gousse(s) d'ail")
print(f"- {nouveau_pain} gr de pain")