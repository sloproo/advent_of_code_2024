def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        avattu = []
        for r in f:
            avattu.append([int((m)) for m in r.strip()])
    return avattu


def sisalla(x: int, y: int, ruudukko: list) -> bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    else:
        return True
    
def naapurit(x: int, y: int, ruudukko: list) -> list:
    return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)] if sisalla(xn, yn, ruudukko)]

kartta = avaa("input.txt")

nollat = []
for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        if kartta[y][x] == 0:
            nollat.append((x, y, 1))
mahdolliset = {0: nollat}

for taso in range(0, 9):
    seuraavat = []
    kaikki_seuraavat = []
    for x, y, tuloja in mahdolliset[taso]:
        for xn, yn in naapurit(x, y, kartta):
            if kartta[yn][xn] == taso+1:
                kaikki_seuraavat.append((xn, yn, tuloja))
    joukko = set((seuraava[0], seuraava[1]) for seuraava in kaikki_seuraavat)
    for xn, yn in joukko:
        kaikkiaan = 0
        for seuraava in kaikki_seuraavat:
            if seuraava[0] == xn and seuraava[1] == yn:
                kaikkiaan += seuraava[2]
        seuraavat.append((xn, yn, kaikkiaan))
    mahdolliset[taso+1] = seuraavat

print(sum([mahdollinen[2] for mahdollinen in mahdolliset[9]]))
