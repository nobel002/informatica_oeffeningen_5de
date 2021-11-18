a_1 = int(input("aanvaller dobelsteen1: "))
a_2 = int(input("aanvaller dobelsteen2: "))
a_3 = int(input("aanvaller dobelsteen3: "))

v_1 = int(input("aanvaller dobelsteen 1: "))
v_2 = int(input("aanvaller dobelsteen 2: "))

middelste_aanvaller = max(min(a_1, a_2), min(a_1, a_3), min(a_2, a_3))

middelste_aanvaller = a_1 + a_2 + a_2 - min(a_1, a_2, a_3) - max(a_1, a_2, a_3)

verliezer_aanvaler, verlies_verdediger = 0, 0

if max(a_2, a_2, a_3) <= max(v_1, v_2):
    verliezer_aanvaler += 1
else:
    verlies_verdediger += 1

if middelste_aanvaller <= min(v_1, v_2):
    verliezer_aanvaler += 1
else:
    verlies_verdediger += 1

if verlies_verdediger == verliezer_aanvaler:
    uitvoer = "aanvaller verliest leger 1, verdediger verliest 1 leger"
else:
    uitvoer = "aanvaller verliest {} legers, verdediger veliest {} legers".format(verliezer_aanvaler, verlies_verdediger)

print(uitvoer)
