def avaa(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([ruutu for ruutu in r.strip()])
    return kartta

kartta = avaa("alku.txt")

def sisalla(x: int, y: int, ruudukko: list =kartta) ->bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def naapurit(x: int, y: int, ruudukko: list =kartta) -> list:
    return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)] if sisalla(xn, yn, ruudukko)]

print(kartta)

pass
