def _germanisering(string):
    new_string = ""
    for word in string.split(" "):
        new_string += word.capitalize() + " "
    return new_string[:-1]

def germaniseer(string):
    index_spatie = string.find(" ")
    nieuwe_zin = ""
    while index_spatie > 0:
        #zin grootter
        nieuwe_zin += string[:index_spatie + 1] + string[index_spatie+1].upper()

        # zin kleinder
        string = string[index_spatie + 2:]

        index_spatie = string.find(" ")

    return nieuwe_zin + string


print(germaniseer("Test string young dagger dick"))
