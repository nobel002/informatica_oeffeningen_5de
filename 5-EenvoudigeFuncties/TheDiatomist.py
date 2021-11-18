from math import floor, pi

r_lower = float(input("r: "))
r_upper = float(input("R: "))

n = floor(0.83*(pow(r_upper, 2)/pow(r_lower, 2)) - 1.9)

percent = 100 * (n * (pi * r_lower ** 2)) / (pi * r_upper ** 2)

print(f'{n} smaller circles cover {percent:.2f}% of the larger circle')
