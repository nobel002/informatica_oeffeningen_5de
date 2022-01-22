dikte = int(input("Dikte v/h papier"))
afstand = int(input("Afstand: "))

afgelegde_afstand = dikte
iteraties = 0
while afstand >= afgelegde_afstand:
    afgelegde_afstand *= 2
    iteraties += 1

print(f"Na {iteraties} keer vouwen bedraagt de dikte van het papier {afgelegde_afstand} mm.")
