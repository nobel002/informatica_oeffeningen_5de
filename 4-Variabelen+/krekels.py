# Invoer.
chirps_per_minute = int(input())

# berekeningen

farenheid = 50 + ((chirps_per_minute-40)/4)
celcius = 10 + ((chirps_per_minute - 40)/7)

# Uitvoer.

print("temperature (Fahrenheit):", farenheid)
print("temperature (Celcius):", celcius)
