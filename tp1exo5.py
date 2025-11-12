jour=int(input("Donne moi le jour du mois"))
heure=int(input("donne moi l'heure du jour"))
minute=int(input("donne moi la minute de l'heure"))
minutepasse= (jour - 1)*24*60+heure*60+minute
print(minutepasse)