def avaa(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([ruutu for ruutu in r.strip()])
    return kartta

kartta = avaa("alku.txt")
kaytetyt = []

def sisalla(x: int, y: int, ruudukko: list =kartta) ->bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def naapurit(x: int, y: int, ruudukko: list =kartta) -> list:
    return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)] if sisalla(xn, yn, ruudukko)]

def tee_alue(x: int, y: int, kartta: list, kaytetyt: list) -> list:
    if (x, y) in kaytetyt:
        return [[-1], -1]
    else:
        kirjain = kartta[y][x]
        alue = [(x, y)]
        vieraat_naapurit = []
        kasvoi = True
        while kasvoi:
            kasvoi = False
            for xa, ya in alue:
                for (xn, yn) in naapurit(xa, ya, kartta):
                    if kartta[yn][xn] == kirjain and (xn, yn) not in kaytetyt and (xn, yn) not in alue:
                        kasvoi = True
                        alue.append((xn, yn))
                    elif kartta[yn][xn] not in vieraat_naapurit:
                        vieraat_naapurit.append((xn, yn))
                        
        return (alue, len(vieraat_naapurit))

alueet = []
kaytetyt = []

for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        uusi_alue = tee_alue(x, y, kartta, kaytetyt)
        if uusi_alue != ([-1], -1):
            alueet.append(uusi_alue)
            kaytetyt += uusi_alue[0]

print(alueet)
