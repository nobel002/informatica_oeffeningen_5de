# Invoer.

geld = int(input("bedrag in cent : "))

# Berekeningen.
euro = geld // 100
#centen %= 100
vijftig_cent = (geld - 100*euro) // 50
twintig_cent = (geld - 100*euro - 50*vijftig_cent)//20
tien_cent = (geld - 100*euro - 50*vijftig_cent - 20*twintig_cent) // 10
vijf_cent = (geld - 100*euro - 50*vijftig_cent - 20*twintig_cent - 10*tien_cent)//5
twee_cent = (geld - 100*euro - 50*vijftig_cent - 20*twintig_cent - 10*tien_cent - 5*vijf_cent)//2
een_cent = (geld - 100*euro - 50*vijftig_cent - 20*twintig_cent - 10*tien_cent - 5*vijf_cent - 2*twee_cent)

muntstukken = euro + vijftig_cent + twintig_cent + tien_cent + vijf_cent + twee_cent + een_cent
# Uitvoer.
print(f"{geld} cent kan je omwisselen in {muntstukken} muntstukken")
