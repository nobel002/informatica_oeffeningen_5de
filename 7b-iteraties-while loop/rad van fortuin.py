woord = input("Woord: ")
inzet = int(input('inzet: '))

letter = input('letter: ')
prev = ""
prijs = 0
while letter in woord and letter not in prev:
    prev += letter
    letter = input('letter: ')
    prijs += inzet

print(prijs)
