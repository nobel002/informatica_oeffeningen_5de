#Als one liner:
#print(input('geef een woord')[::-1])

woord = str(input("woord: "))
omgekeerd_woord = ""
for letter in woord:
    omgekeerd_woord = letter + omgekeerd_woord
print(omgekeerd_woord)
