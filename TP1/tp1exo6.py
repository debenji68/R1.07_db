minute=int(input("donne moi les minutes"))
jour=minute/1440
minute=minute%1440
heure=minute/60
minute=minute%60
print(f"on est le jour {jour:.0f}, et il est {heure:.0f}h{minute:.0f}")