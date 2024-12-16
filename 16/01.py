import time


def lue(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([m for m in r.strip()])
        return kartta
    
def edessa(paikka: tuple, suunta: str, kartta: list) -> tuple[str, tuple[int, int]]:
    x, y = paikka
    if suunta == "N":
        vastassa = kartta[y-1][x]
        koord = (x, y-1)
    elif suunta =="E":
        vastassa = kartta[y][x+1]
        koord = (x+1, y)
    elif suunta == "S":
        vastassa = kartta[y+1][x]
        koord = (x, y+1)
    elif suunta == "W":
        vastassa = kartta[y][x-1]
        koord = (x-1, y)
    else:
        raise AssertionError("Nyt oli outo suunta vastassa")
    return (koord, vastassa)

def eteenpain(tila: tuple, kartta: list) -> tuple[tuple[int, int], str, int]:
    (x, y), suunta, askeleet = tila
    vastassa = edessa((x, y), suunta, kartta)
    if vastassa[1] == ".":
        return (vastassa[0], suunta, askeleet + 1)
    elif vastassa[1] == "#":
        return ((-1, -1), suunta, -1)
    else:
        raise AssertionError("Nyt tuli kartalla jotain outoa vastaan")

def kaanny(tila: tuple, kartta: list) -> list[tuple[tuple[int, int], str, int]]:
    (x, y), suunta, askeleet = tila
    uudet_suunnat = {"N": ("W", "E"), "E": ("N", "S"), "S": ("E", "W"), "W": ("S", "N")}
    kaantyneet = []
    for u_s in uudet_suunnat[suunta]:
        if edessa((x, y), u_s, kartta)[1] != "#":
            kaantyneet.append(((x, y), u_s, askeleet + 1000))
    return kaantyneet

def piirra(kartta: list, kaydyt: set):
    for kayty in kaydyt:
        x, y = kayty[0]
        kartta[y][x] = "/"
    tulostettava = ""
    for r in kartta:
        tulostettava += "".join(r) + "\n"
    print(tulostettava)

kartta = lue("alku.txt")

for y in range(len(kartta)):
    for x in range(len(kartta[y])):
        if kartta[y][x] == "E" or kartta[y][x] == "S":
            if kartta[y][x] == "E":
                maali = (x, y)
                kartta[y][x] = "."
            elif kartta[y][x] == "S":
                alku = (x, y)
                kartta[y][x] = "."

mahdolliset = [(alku, "E", 0)]
kaydyt = set()

while maali not in [tila[0] for tila in mahdolliset]:
    seuraavat_mahdolliset = []
    tutkittava = mahdolliset[0]
    edessa_oleva = edessa(tutkittava[0], tutkittava[1], kartta)
    if edessa_oleva[1] == ".":
        if (edessa_oleva[0], tutkittava[1]) not in kaydyt:
            seuraavat_mahdolliset.append(eteenpain(tutkittava, kartta))

    kaannytyt_mahdolliset = kaanny(tutkittava, kartta)
    for kaannytty in kaannytyt_mahdolliset:
        if kaannytty[:2] not in kaydyt:
            seuraavat_mahdolliset.append(kaannytty)
    kaydyt.add(tutkittava[:2])
    mahdolliset.pop(0)
    mahdolliset += seuraavat_mahdolliset
    mahdolliset.sort(key=lambda tila: tila[2])
    # print("\x1b[2J\033[H")
    # piirra(kartta, kaydyt)
    # print(f"Askeleita edenneessä = {tutkittava[2]}")
    # time.sleep(0.2)
    pass


print(f"Maali on {maali}")
for m in mahdolliset:
    if m[0] == maali:
        print(m)
        break
pass

