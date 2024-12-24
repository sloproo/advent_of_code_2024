def lue(tiedosto: str) -> tuple[dict, dict]:
    with open(tiedosto) as f:
        portit = {}
        for r in f:
            if r == "\n":
                break
            portti = r.strip().split(": ")
            portit[portti[0]] = True if portti[1] == "1" else False
        vieraat = {}
        for r in f:
            eka, ope, toka, portti = r.strip().replace(" -> ", " ").split(" ")
            vieraat[portti] = (eka, toka, ope)
    return (portit, vieraat)

portit, vieraat = lue("input.txt")

while len(vieraat) > 0:
    poistettavat = []
    for vieras in vieraat:
        if vieraat[vieras][0] in portit and vieraat[vieras][1] in portit:
            eka_arvo = portit[vieraat[vieras][0]]
            toka_arvo = portit[vieraat[vieras][1]]
            if vieraat[vieras][2] == "AND":
                portit[vieras] = eka_arvo and toka_arvo
                poistettavat.append(vieras)
            elif vieraat[vieras][2] == "OR":
                portit[vieras] = eka_arvo or toka_arvo
                poistettavat.append(vieras)
            elif vieraat[vieras][2] == "XOR":
                portit[vieras] = eka_arvo != toka_arvo
                poistettavat.append(vieras)

    for poistettava in poistettavat:
        del vieraat[poistettava]

portit = dict(sorted(portit.items()))


zetat = [portit[z] for z in portit.keys() if z[0] == "z"]
bini = ""
for z in zetat:
    bini += "1" if z else "0"

bini = bini[::-1]

luku = int(bini, 2)
print(luku)




