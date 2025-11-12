print("Donner les trois nombres entiers x1, x2 et x3 : ")
x1 = int(input("valeur de x1"))
x2 = int(input("valeur de x2"))
x3 = int(input("valeur de x3"))
condition = not(x1 == x2) and not(x1 == x2)
if(condition):
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")
condition = (x1 > x2) or (x3 < x1)
if(condition):
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")
condition = (x1 < x2) and (x2 < x3)
if(condition):
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")
condition = not((x1 > x2) and (x1 < x3))
if(condition):
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")
condition = (x1 == x2) or (x3 == x1) or (x2 == x3)
if(condition):
    print(str(condition)+" = VRAI")
else :
    print(str(condition)+" = FAUX")