t = float(input("T: "))
w = float(input("W: "))

w /= 3.6

wind_chill = 13.12 + 0.6215 * t + (0.3965*t - 11.37) * pow(3.6*w, 0.16)

print(wind_chill)
