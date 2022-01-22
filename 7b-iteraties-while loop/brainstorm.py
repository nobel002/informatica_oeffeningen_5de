i = 0
from random import randint

while i < 5:
    print(i)
    i += 1

# Voorkeur
for i in range(5):
    print(i)

# Typisch voorbeeld van een while loop.
vorst_periode = 0
temperatuur = randint(-10, 1)

while temperatuur <= 0:
    vorst_periode += 1
    temperatuur = temperatuur = randint(-10, 1)
print('---')
print(vorst_periode)
