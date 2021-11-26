codon = input("Condon: ")

uitvoer = "gewoon"

if len(codon) == 3:
    if codon == "AUG":
        uitvoer = "start"
    elif codon == "UAG" or codon == "UGA" or codon == "UAA":
        uitvoer = "stop"
else:
    uitvoer = "ongeldig"

print(f"Het codon {codon} is een {uitvoer} codon.")
