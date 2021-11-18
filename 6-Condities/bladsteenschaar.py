speler_1 = input()
speler_2 = input()

if speler_2 == speler_1:
    print("onbeslist")
elif speler_2 == "blad":
    if speler_1 == "schaar":
        print("speler 1 wint")
    else:
        print("speler 2 wint")
elif speler_2 == "steen":
    if speler_1 == "blad":
        print("speler 1 wint")
    else:
        print("speler 2 wint")
else:
    if speler_1 == "steen":
        print("speler 1 wint")
    else:
        print("speler 2 wint")
