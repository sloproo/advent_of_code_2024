def avaa(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([ruutu for ruutu in r.strip()])
    return kartta

kartta = avaa("input.txt")
kaytetyt = []

def sisalla(x: int, y: int, ruudukko: list =kartta) -> bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def naapurit(x: int, y: int, ruudukko: list =kartta) -> list:
    return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]]

def tee_alue(x: int, y: int, kartta: list) -> tuple[list, int]:
    kirjain = kartta[y][x]
    alue = []
    uudet = [(x, y)]
    tulevat = []
    raja_aitaa = 0
    kasvoi = True
    while kasvoi:
        kasvoi = False
        for xa, ya in uudet:
            for (xn, yn) in naapurit(xa, ya, kartta):
                if not sisalla(xn, yn, kartta):
                    raja_aitaa += 1
                elif kartta[yn][xn] != kirjain:
                    raja_aitaa += 1
                elif (xn, yn) not in uudet + alue + tulevat:
                    kasvoi = True
                    tulevat.append((xn, yn))
        alue += [koord for koord in uudet]
        uudet = [koord for koord in tulevat]
        tulevat = []

    return (alue, raja_aitaa)

alueet = []
kaytetyt = []

for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        if (x, y) in kaytetyt:
            continue

        uusi_alue = tee_alue(x, y, kartta)
        alueet.append(uusi_alue)
        kaytetyt += uusi_alue[0]
        pass

hinnat = [len(alue[0]) * alue[1] for alue in alueet]
print(sum(hinnat))

