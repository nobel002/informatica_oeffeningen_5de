score_a = float(input())
score_b = float(input())

differentie = abs(score_b - score_a)

thuis, uit = 0, 0

if differentie < 10:
    winaar, verliezer = 600, 400
elif differentie < 20:
    winaar, verliezer = 700, 300
else:
    winaar, verliezer = 800, 200


if score_a - score_b >= 0:
    thuis, uit = winaar, verliezer
else:
    thuis, uit = verliezer, winaar


thuis -= 70
uit += 70

#print(f"thuisploeg: {float(thuis):.2f}")
#print(f"  uitploeg: {float(uit):.2f}")


print('{:>10}: {:.2f}\n{:>10}: {:.2f}').format('thuisploeg', thuis, 'uitploeg',uit)
