v_stijn = float(input('v stijn: '))
v_kaat = float(input('v kaat: '))

afstand = float(input('afstand: '))

iteraties: int = 0

while afstand > 0:
    afstand -= v_stijn
    afstand -= v_kaat
    iteraties += 1

print(f"Na {iteraties} s hebben Stijn en Kaat elkaar ontmoet.")
