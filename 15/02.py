def lue(tiedosto: str) -> tuple[tuple[int, int], set, set, set, str]:
    
    with open(tiedosto) as f:
        seinat, vasemmat, oikeat = set(), set(), set()
        i = 0
        for r in f:
            if r == "\n":
                break
            for j in range(len(r.strip())):
                if r[j] == "#":
                    seinat.add((j * 2, i))
                    seinat.add((j * 2 + 1, i))
                elif r[j] == "O":
                    vasemmat.add((j * 2, i))
                    oikeat.add((j * 2 + 1, i))
                elif r[j] == "@":
                    robotti = (j * 2, i)
            i += 1
        kaskyt = ""
        for r in f:
            kaskyt += r.strip()
        kaskyt = kaskyt.replace("v", "D").replace("^", "U").replace("<", "L").replace(">", "R")
        return (robotti, seinat, vasemmat, oikeat, kaskyt)

def summaa(eka: tuple, toka: tuple) -> tuple:
    return (eka[0] + toka[0], eka[1] + toka[1])

def gps(koord: tuple) -> int:
    return koord[1] * 100 + koord[0]


def piirra(robotti: tuple, seinat:set, vasemmat: set, oikeat: set):
    leveys = max(koord[0] for koord in seinat) + 1
    korkeus = max(koord[1] for koord in seinat) + 1
    kartta = []
    for _ in range(korkeus):
        kartta.append(["." for __ in range(leveys)])
    for seina in seinat:
        kartta[seina[1]][seina[0]] = "#"
    for vasen in vasemmat:
        kartta[vasen[1]][vasen[0]] = "["
    for oikea in oikeat:
        kartta[oikea[1]][oikea[0]] = "]"
    kartta[robotti[1]][robotti[0]] = "@"
    for r in kartta:
        print("".join(r))
    pass

def liiku(suunta: str, robotti: tuple, seinat: set,
          vasemmat: set, oikeat: set) -> tuple[tuple[int, int], set, set]:
    liikkuvat_vasemmat = []
    liikkuvat_oikeat = []
    seuraavat_ruudut = [summaa(robotti, suunnat[suunta])]
    if seuraavat_ruudut[0] in seinat:
        # print("Edessä on seinä, mitään ei tapahdu")
        return robotti, vasemmat, oikeat
    tyhjaa_edessa = seuraavat_ruudut[0] not in vasemmat and seuraavat_ruudut[0] not in oikeat
    while not tyhjaa_edessa:
        tyhjaa_edessa = True
        for seuraava_ruutu in seuraavat_ruudut:
            if seuraava_ruutu in seinat:
                return robotti, vasemmat, oikeat
            elif seuraava_ruutu in vasemmat:
                if seuraava_ruutu not in liikkuvat_vasemmat:
                    liikkuvat_vasemmat.append(seuraava_ruutu)
                    liikkuvat_oikeat.append((seuraava_ruutu[0]+1, seuraava_ruutu[1]))
                tyhjaa_edessa = False
            elif seuraava_ruutu in oikeat:
                if seuraava_ruutu not in liikkuvat_oikeat:
                    liikkuvat_oikeat.append(seuraava_ruutu)
                    liikkuvat_vasemmat.append((seuraava_ruutu[0]-1, seuraava_ruutu[1]))
                tyhjaa_edessa = False
            # Määritellään seuraavaksi katsottavat ruudut
        seuraavat_ruudut = [summaa(l_v, suunnat[suunta]) for l_v in liikkuvat_vasemmat
                            if summaa(l_v, suunnat[suunta]) not in liikkuvat_vasemmat + liikkuvat_oikeat] \
                            + [summaa(l_o, suunnat[suunta]) for l_o in liikkuvat_oikeat
                                if summaa(l_o, suunnat[suunta]) not in liikkuvat_vasemmat + liikkuvat_oikeat]
    # print("Ok, eli edessä pitäisi olla tyhjää ja liikkeen tapahtua")
    robotti = summaa(robotti, suunnat[suunta])
    for l_v in liikkuvat_vasemmat:
        vasemmat.remove(l_v)
    for l_o in liikkuvat_oikeat:
        oikeat.remove(l_o)
    uudet_vasemmat = set([summaa(l_v, suunnat[suunta]) for l_v in liikkuvat_vasemmat] + list(vasemmat))
    uudet_oikeat = set([summaa(l_o, suunnat[suunta]) for l_o in liikkuvat_oikeat] + list(oikeat))
    return robotti, uudet_vasemmat, uudet_oikeat

robotti, seinat, vasemmat, oikeat, kaskyt = lue("input.txt")

suunnat = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

print("Alkutilanne:")
piirra(robotti, seinat, vasemmat, oikeat)
print()
pass
for suunta in kaskyt:
    robotti, vasemmat, oikeat = liiku(suunta, robotti, seinat, vasemmat, oikeat)
    # piirra(robotti, seinat, vasemmat, oikeat)
    print()


gps_summa = 0
for laatikko in vasemmat:
    gps_summa += gps(laatikko)

print(gps_summa)
