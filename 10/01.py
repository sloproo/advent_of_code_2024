def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        avattu = []
        for r in f:
            avattu.append([int((m)) for m in r.strip()])
    return avattu

kartta = avaa("input.txt")

def sisalla(x: int, y: int, ruudukko: list =kartta) -> bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    else:
        return True
    
def naapurit(x: int, y: int, ruudukko: list =kartta) -> list:
    return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)] if sisalla(xn, yn, ruudukko)]


nollat = []
for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        if kartta[y][x] == 0:
            nollat.append((x, y))
mahdolliset = {0: nollat}

reitteja = 0

for x, y in nollat:
    nykyiset = [(x, y)]
    for taso in range(9):
        seuraavat = []
        for xn, yn in nykyiset:
            for xs, ys in naapurit(xn, yn):
                if kartta[ys][xs] == taso + 1:
                    seuraavat.append((xs, ys))
        seuraavat = list(set(seuraavat))
        nykyiset = seuraavat.copy()
    reitteja += len(seuraavat)


print(reitteja)

