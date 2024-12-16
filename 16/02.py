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
        input("Mennään eteenpäin, seinään törmäämisen olisi kai pitänyt olla estetty aiemmin. Virhe?")
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

def meneeko_mahdollisiin(tila: tuple[tuple[int, int], str, int], kaydyt: list) -> bool:
    samat_kaydyissa = [kayty for kayty in kaydyt if kayty[:2] == tila[:2]]
    if len(samat_kaydyissa) == 0:
        # input("Ei ole vielä käydyissä, voi lisätä")
        return True
    # assert len(samat_kaydyissa) <= 1
    assert tila[2] >= samat_kaydyissa[0][2]
    if tila[2] == samat_kaydyissa[0][2]:
        input("Löytyi vaihtoehtoinen reitti jo tultuun tilaan, voi lisätä")
        return True
    else:
        # input("Joo tänne ollaan tultu mutta nopeammin, ei voi lisätä")
        return False

def alusta_kartta(kartta: list) -> tuple[list, tuple, tuple]:
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            if kartta[y][x] == "E" or kartta[y][x] == "S":
                if kartta[y][x] == "E":
                    maali = (x, y)
                    kartta[y][x] = "."
                elif kartta[y][x] == "S":
                    alku = (x, y)
                    kartta[y][x] = "."
    return (kartta, alku, maali)

kartta = lue("input.txt")
kartta, alku, maali = alusta_kartta(kartta)

mahdolliset = [(alku, "E", 0, (-1, -1), "E")]
kaydyt = set()
maaliin_paasty = False

while True:
    hyodyllinen = False
    seuraavat_mahdolliset = []
    tutkittava = mahdolliset[0]
    edessa_oleva_ruutu = edessa(tutkittava[0], tutkittava[1], kartta)
    if edessa_oleva_ruutu[1] == ".":
        tila_edessa = eteenpain(tutkittava[:3], kartta)
        if meneeko_mahdollisiin(tila_edessa, kaydyt):
            seuraavat_mahdolliset.append(tuple(list(tila_edessa) + [tutkittava[0]] + [tutkittava[1]]))
            hyodyllinen = True
    kaannytyt_mahdolliset = kaanny(tutkittava[:3], kartta)
    for kaannytty in kaannytyt_mahdolliset:
        if meneeko_mahdollisiin(kaannytty, kaydyt):
            seuraavat_mahdolliset.append(tuple(list(kaannytty) + [tutkittava[0]] + [tutkittava[1]]))
            hyodyllinen = True
    if hyodyllinen:
        kaydyt.add(tutkittava)
    for s_m in seuraavat_mahdolliset:
        if s_m not in mahdolliset:
            mahdolliset.append(s_m)
    mahdolliset.pop(0)
    mahdolliset.sort(key=lambda mahdollinen: mahdollinen[2])
    # print("\x1b[2J\033[H")
    # piirra(kartta, kaydyt)
    # print(f"Askeleita edenneessä = {tutkittava[2]}")
    # time.sleep(0.2)
    pass

    if maali in [tila[0] for tila in mahdolliset]: 
        maaliin_paasty = True
        print("Jee jee")
        pass


print(f"Maali on {maali}")
for m in mahdolliset:
    if m[0] == maali:
        print(m)
        break
pass

