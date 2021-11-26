# Invoer
getal_a = int(input())
getal_b = int(input())

som_a, som_b = 0, 0
# Bewerkingen

# Een deler kan maar zo groot zijn als de helft van dat getal.
for i in range(1, max(getal_a, getal_b) >> 1 + 1):
    if getal_a % i == 0 and i != getal_a:
        som_a += i
    if getal_b % i == 0 and i != getal_b:
        som_b += i

# Uitvoer
if som_a == getal_b and som_b == getal_a:
    print(f"{getal_a} en {getal_b} zijn bevriende getallen")
else:
    print(f"{getal_a} en {getal_b} zijn geen bevriende getallen")
