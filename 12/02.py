def avaa(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([ruutu for ruutu in r.strip()])
    return kartta

kartta = avaa("alku.txt")
print(kartta)


