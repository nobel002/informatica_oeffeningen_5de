prijs = float(input('prijs: '))
som = 0

while prijs > 0:
    som += prijs
    prijs = float(input("prijs: "))

print(f"De totale prijs is € {som:.2f}")
