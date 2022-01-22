getal = int(input("Getal: "))

is_priem = True
deler = 2

while deler < getal ** 0.5 + 1:
    if getal % deler == 0:
        is_priem = False
        break
    deler += 1

if getal == 1:
    is_priem = False
if getal == 2:
    is_priem = True

if is_priem:
    uitvoer = "is een priemgetal"
else:
    uitvoer = "is geen priemgetal"
print(getal, uitvoer)


# Of Deftig

getal = int(input())
deler = getal // 2

while deler > 0 and getal % deler != 0:
    deler -= 1

if deler == 1:
    print("priem")
else:
    print("geen priem")
