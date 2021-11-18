aantal_getallen = int(input('het aantal getallen '))

som = 0
max = -(2 **64 - 1)     #64 bit int lim
for i in range(aantal_getallen):
    getal = int(input('getal: '))
    som += getal
    max = getal if getal > max else max

gem = som/aantal_getallen

print(f"Het grootste getal is {max} en het gemiddelde is {gem:.2f}")
