speler_1 = []
for i in range(3):
    speler_1.append(int(input()))
speler_2 = []

for i in range(2):
    speler_2.append(int(input()))

speler_1.sort(reverse=True)
speler_2.sort(reverse=True)

aanvaller, verdediger = 0, 0


if speler_1[0] == speler_2[0]:
    aanvaller += 1

if speler_1[1] == speler_2[1]:
    aanvaller += 1

if speler_1[0] > speler_2[0]:
    verdediger += 1
elif speler_1[0] < speler_2[0]:
    aanvaller += 1

if speler_1[1] > speler_2[1]:
    verdediger += 1
if speler_1[1] < speler_2[1]:
    aanvaller += 1



legers_aanvallers = "leger" if aanvaller == 1 else "legers"
legers_verdedigers = "leger" if verdediger == 1 else "legers"

print(f"aanvaller verliest {aanvaller} {legers_aanvallers}, verdediger verliest {verdediger} {legers_verdedigers}")
