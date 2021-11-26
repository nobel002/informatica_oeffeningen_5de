aantal_elektronen = int(input("#e- : "))

buitenste_schil = "Q"
# aantal_valentie_elektronen = aantal_elektronen - 124
if aantal_elektronen <= 2:
    buitenste_schil = "K"
    # aantal_valentie_elektronen = aantal_elektronen
elif aantal_elektronen <= 10:
    buitenste_schil = "L"
    # aantal_valentie_elektronen = aantal_elektronen - 2
elif aantal_elektronen <= 28:
    buitenste_schil = "M"
    # aantal_valentie_elektronen = aantal_elektronen - 10
elif aantal_elektronen <= 60:
    buitenste_schil = "N"
    # aantal_valentie_elektronen = aantal_elektronen - 28
elif aantal_elektronen <= 92:
    buitenste_schil = "O"
    # aantal_valentie_elektronen = aantal_elektronen - 60
elif aantal_elektronen <= 124:
    buitenste_schil = "P"
    # aantal_valentie_elektronen = aantal_elektronen - 92

print(f"De {buitenste_schil}-schil is de buitenste schil van een stabiel atoom met {aantal_elektronen} elektronen.")
