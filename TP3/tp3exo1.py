#a
N = int(input("Entrez N : "))

somme = 0
for i in range(N + 1):
    somme += i
print("Somme =", somme)

#b
valeur = 0

while valeur != 100:
    valeur = int(input("Entrez une valeur : "))
print("Fin")

#c
inf_10 = 0
entre_10_15 = 0
sup_15 = 0

for i in range(10):
    valeur = -1
    while valeur < 0 or valeur > 20:
        valeur = float(input("Entrez une valeur entre 0 et 20 : "))

    if valeur < 10:
        inf_10 += 1
    elif valeur < 15:
        entre_10_15 += 1
    else:
        sup_15 += 1

print("Inférieur à 10 :", inf_10)
print("Entre 10 et 15 :", entre_10_15)
print("Supérieur ou égal à 15 :", sup_15)

#d
X = float(input("Entrez X : "))
somme = 0
N = 0

while somme + N + 1 <= X:
    N += 1
    somme += N
print("N =", N)
print("Somme =", somme)
somme = 0
for i in range(N + 1):
    somme += i
print("Somme =", somme)