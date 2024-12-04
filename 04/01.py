def naapurit(x: int, y: int, ruudukko: list) -> list:
    palautettavat = []
    korkeus = len(ruudukko)
    leveys = len(ruudukko[0])
    for y_koord in range(y-1, y+2):
        if y_koord < 0 or y_koord >= korkeus:
            continue
        else:
            for x_koord in range(x-1, x+2):
                if x_koord < 0 or x_koord >= leveys:
                    continue
                else:
                    if x_koord != x and y_koord != y:
                        palautettavat.append((x_koord, y_koord))
    return palautettavat

ruudukko = []

with open("alku.txt") as f:
    for r in f:
        rivi = [kirjain for kirjaimet in r.strip().split() for kirjain in kirjaimet]
        print(rivi)
    
print naapurit(2, 4, ruudukko)
