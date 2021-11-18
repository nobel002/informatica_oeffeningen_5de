# Invoer.

avogadro = 6.020 * 10e22
molaire_massa_zwavel = 32.06

aantal_deeltjes_in_mol = float(input("Wat is het aantal deeltjes zwavel? "))


# Berekeningen.
aantal_deeltjes = aantal_deeltjes_in_mol * avogadro

massa = aantal_deeltjes_in_mol * molaire_massa_zwavel


# Uitvoer.
print(massa)
print(aantal_deeltjes)
