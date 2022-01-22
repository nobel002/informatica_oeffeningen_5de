som = 0

som += int(input())
getal = int(input())
som += getal

while som < 21 and getal != 0:
    getal = int(input())
    som += getal

uitvoer = f"Verbrand ({som})"

if som == 21:
    uitvoer = "Gewonnen!"
elif som < 21:
    uitvoer = f"Voorzichtig gespeeld ({som})"

print(uitvoer)
