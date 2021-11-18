leeftijd = int(input("Geef uj leeftijd: "))
geslacht = input("Jongen of Meisje? ")


if leeftijd >= 18:
    if geslacht == "jongen":
        print('Welkom in de nachtclub ;), toegangsprijs is €25')

    else:

        print('Welkom in de nachtclub ;), toegang is gratis')
else:
    print('Bye...')

