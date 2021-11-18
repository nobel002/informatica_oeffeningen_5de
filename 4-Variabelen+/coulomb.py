# Invoer.
r = float(input('De afstand = '))

k = 8.99 * (10 ** 9)
q1 = 2.0 * (10 ** (-6))
q2 = 1.0 * (10 ** (-6))

# Berekeningen.

kracht = k * ((q1 * q2) / (r ** 2))

# Uitvoer.

print(kracht * (10 ** 4))
