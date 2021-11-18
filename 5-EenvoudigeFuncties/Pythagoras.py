from math import sqrt


a = float(input("a: "))
b = float(input("b: "))

c = sqrt(pow(a, 2) + pow(b, 2))

print(f"In een rechthoekige driehoek met rechthoekszijden a = {a:.2f} en b = {b:.2f} is de schuine zijde {c:.2f}")
