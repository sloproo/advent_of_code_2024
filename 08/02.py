import itertools

def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        palautettava = []
        for r in f:
            palautettava.append([m for m in r.strip()])
        return palautettava

def yhdistelmat(lista: list) -> list:
    return itertools.combinations(lista, 2)

def sisalla(koordinaatit: tuple, ruudukko: list) -> bool:
    if (koordinaatit[0] < 0 or koordinaatit[1] < 0 or
        koordinaatit[1] >= len(ruudukko) or koordinaatit[0] >= len(ruudukko[y])):
        return False
    else:
        return True

ruudukko = avaa("input.txt")
antennit = {}

for y in range(len(ruudukko)):
    for x in range(len(ruudukko[y])):
        if ruudukko[y][x] != ".":
            if ruudukko[y][x] not in antennit:
                antennit[ruudukko[y][x]] = [(x, y)]
            else:
                antennit[ruudukko[y][x]].append((x, y))

antinoodit_set = set()

for antenni in antennit:
    if len(antennit[antenni]) <= 1:
        continue
    for pari in yhdistelmat(antennit[antenni]):
        x1, y1 = pari[0]
        x2, y2 = pari[1]
        xd = x2 - x1
        yd = y2 - y1
        mahd_ad_alas = pari[0]
        while sisalla(mahd_ad_alas, ruudukko):
            antinoodit_set.add(mahd_ad_alas)
            mahd_ad_alas = (mahd_ad_alas[0] - xd, mahd_ad_alas[1] - yd)
        mahd_ad_ylos = pari[1]
        while sisalla(mahd_ad_ylos, ruudukko):
            antinoodit_set.add(mahd_ad_ylos)
            mahd_ad_ylos = (mahd_ad_ylos[0] + xd, mahd_ad_ylos[1] + yd)
        
print("Antinoodit_set:")
print(antinoodit_set)
print(len(antinoodit_set))
        

        
