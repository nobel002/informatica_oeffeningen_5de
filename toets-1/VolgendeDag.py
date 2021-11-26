# Invoer:
dag = int(input())
maand = int(input())
jaar = int(input())

# Bewerkingen
if dag == 31:
    if maand == 12:
        # 31 December
        dag, maand, jaar = 1, 1, jaar + 1
    else:
        dag, maand = 1, maand + 1
elif dag == 30:
    if maand < 8:
        if maand % 2 == 0:
            dag, maand = 1, maand + 1
        else:
            dag += 1
    elif maand % 2 == 1:
        dag, maand = 1, maand + 1
    else:
        dag += 1
elif dag == 29 and maand == 2:
    dag, maand = 1, 3
else:
    if maand == 2:
        # Controle 29/2/yyyy
        if jaar % 400 == 0 or (jaar % 4 == 0 and jaar % 100 != 0):
            dag += 1
        else:
            dag, maand = 1, 3
    else:
        dag += 1

# Uitvoer
print(f"{dag}/{maand}/{jaar}")
