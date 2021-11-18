from math import ceil
getal = int(input("Het getal r"))

som = 0
for i in range(ceil(100/getal)+1):
    if i*getal <= 100:
        som += i * getal

print(som)
