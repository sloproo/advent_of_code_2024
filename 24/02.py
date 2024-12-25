def lue(tiedosto: str) -> tuple[dict, dict]:
    with open(tiedosto) as f:
        portit = {}
        for r in f:
            if r == "\n":
                break
            portti = r.strip().split(": ")
            portit[portti[0]] = True if portti[1] == "1" else False
        laskut = {}
        for r in f:
            eka, ope, toka, portti = r.strip().replace(" -> ", " ").split(" ")
            laskut[portti] = (eka, toka, ope)
    return (portit, laskut)

def kirjain_biniksi(kirjain: str) -> int:
    arvot = [portit[portin_tunnus] for portin_tunnus in portit.keys()
             if portin_tunnus[0] == str(kirjain)]
    bini = ""
    for z in arvot:
        bini += "1" if z else "0"
    bini = bini[::-1]
    luku = int(bini, 2)
    return luku

def portin_arvoksi(kirjain: str, numero: int, arvo: int, portit: dict) -> dict:
    portit[kirjain+f"{numero:02}"] = False if arvo == 0 else True
    return portit

def nollaa_portit(portit: dict) -> dict:
    for portti in portit:
        if portti[0] in ["x", "y"]:
            portit[portti] = False
    return portit

def testaa_eka(kohta: int, portit: dict, laskut: dict) -> bool:
    kohta = 0
    portit = nollaa_portit(portit)
    portit = laske_tulos(portit, laskut)
    if portit[f"{kohta[0]}{kohta[1:]:02}"]

    
        

def laske_tulos(portit: dict, laskut: dict) -> dict:
    while len(laskut) > 0:
        poistettavat = []
        for vieras in laskut:
            if laskut[vieras][0] in portit and laskut[vieras][1] in portit:
                eka_arvo = portit[laskut[vieras][0]]
                toka_arvo = portit[laskut[vieras][1]]
                if laskut[vieras][2] == "AND":
                    portit[vieras] = eka_arvo and toka_arvo
                    poistettavat.append(vieras)
                elif laskut[vieras][2] == "OR":
                    portit[vieras] = eka_arvo or toka_arvo
                    poistettavat.append(vieras)
                elif laskut[vieras][2] == "XOR":
                    portit[vieras] = eka_arvo != toka_arvo
                    poistettavat.append(vieras)
        for poistettava in poistettavat:
            del laskut[poistettava]
    return dict(sorted(portit.items()))



portit, laskut = lue("input.txt")

portit = laske_tulos(portit, laskut)

pass



