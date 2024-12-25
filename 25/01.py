import itertools

def lue(tiedosto: str) -> tuple[list, list]:
    with open(tiedosto) as f:
        koko = -1
        avaimet = []
        lukot = []
        moykky = []
        for r in f:
            if r == "\n" and koko == -1:
                koko = len(moykky)
            if len(moykky) != koko and r != "\n":
                moykky.append([merkki for merkki in r.strip()])
            if len(moykky) == koko:
                palkit = []
                for x in range(len(moykky[0])):
                    palkit.append([moykky[y][x] for y in range(len(moykky))])

                muutoskohdat = []
                for palkki in palkit:
                    for y in range(len(palkki) - 1):
                        if palkki[y] != palkki[y+1]:
                            muutoskohdat.append(y)
                            break
                if palkki[0][0] == ".":
                    avain = [len(moykky) - muutoskohta - 2
                                for muutoskohta in muutoskohdat]
                    avaimet.append(avain)
                else:
                    lukko = [muutoskohta for muutoskohta in muutoskohdat]
                    lukot.append(lukko)
                moykky = []
    return lukot, avaimet

lukot, avaimet = lue("input.txt")

kaypia_yhdistelmia = 0
for lukko, avain in itertools.product(lukot, avaimet):
    for i in range(len(lukko)):
        if lukko[i] + avain[i] >= 6:
            break
    else:
        kaypia_yhdistelmia += 1

print(f"Käypiä lukko-avain-yhdistelmiä on {kaypia_yhdistelmia}")
