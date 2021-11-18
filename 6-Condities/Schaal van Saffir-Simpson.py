#119-153	1
#154-177	2
#178-209	3
#210-249	4
#≥ 250	5
speed = int(input())

boodschap = "categorie 5"

if speed < 119:
    boodschap = "geen orkaan"
elif speed <= 153:
   boodschap = "categorie 1"
elif speed <= 177:
    boodschap = "categorie 2"
elif speed <= 209:
    boodschap = "categorie 3"
elif speed <= 249:
    boodschap = "categorie 4"

print(boodschap)


## IS ELEGANTER DAN GW RANDOM SHIT DOEN
