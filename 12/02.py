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

def tee_alue(x: int, y: int, kartta: list) -> list:
    kirjain = kartta[y][x]
    alue = []
    uudet = [(x, y)]
    tulevat = []
    kasvoi = True
    while kasvoi:
        kasvoi = False
        for xa, ya in uudet:
            for (xn, yn) in naapurit(xa, ya, kartta):
                if not sisalla(xn, yn, kartta):
                    continue
                elif kartta[yn][xn] != kirjain:
                    continue
                elif (xn, yn) not in uudet + alue + tulevat:
                    kasvoi = True
                    tulevat.append((xn, yn))
        alue += [koord for koord in uudet]
        uudet = [koord for koord in tulevat]
        tulevat = []
    return (alue)

def reunat_kulmista(alue: list) -> int:
    reunoja = 0
    for x, y in alue:
        if (x-1, y) not in alue and ((x, y+1) not in alue or (x-1, y+1) in alue):
            reunoja += 1
        if (x+1, y) not in alue and ((x, y+1) not in alue or (x+1, y+1) in alue):
            reunoja += 1
        if (x, y-1) not in alue and ((x+1, y) not in alue or (x+1, y-1) in alue):
            reunoja += 1
        if (x, y+1) not in alue and ((x+1, y) not in alue or (x+1, y+1) in alue):
            reunoja += 1
    return reunoja

"""
Vasen reuna: vasemmalla ei, joko alhaalla ei tai alhaalla vasemmalla on 
Oikea reuna: oikealla ei, joko alhaalla ei tai alhaalla oikealla on
Yläreuna: ylhäällä ei, joko oikealla ei ole tai ylhäällä oikealla on
Alareuna: alhaalla ei, joko oikealla ei ole tai alhaalla oikealla on
"""

alueet = []
kaytetyt = []

for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        if (x, y) in kaytetyt:
            continue

        uusi_alue = tee_alue(x, y, kartta)
        alueet.append(uusi_alue)
        kaytetyt += uusi_alue
        pass

hinnat = sum([len(alue) * reunat_kulmista(alue) for alue in alueet])
print(hinnat)

# for alue in alueet:
#     reunoja = reunat_kulmista(alue)
#     print(f"alueella kokoa {len(alue)}, reunoja {reunoja}")
#     print(f"Hinta: {len(alue) * reunoja}")
    
