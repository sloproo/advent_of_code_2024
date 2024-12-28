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

def laske_bittisyys(portit: dict) -> int:
    suurin = 0
    for portti in portit:
        if portti[0] == "x":
            if int(portti[1:]) > suurin:
                suurin = int(portti[1:])
    return suurin

def kirjain_biniksi(kirjain: str) -> int:
    arvot = [portit[portin_tunnus] for portin_tunnus in portit.keys()
             if portin_tunnus[0] == str(kirjain)]
    bini = ""
    for z in arvot:
        bini += "1" if z else "0"
    bini = bini[::-1]
    luku = int(bini, 2)
    return luku

def nollaa_portit(portit: dict) -> dict:
    for portti in portit:
        if portti[0] in ["x", "y", "z"]:
            portit[portti] = False
    return portit

def aseta_kirjaimen_luvuksi(kirjain: str, luku: str, portit: dict, bittisyys: int) -> dict:
    # binina = f"{0:0}{str(bittisyys)}{b}".format(luku)[::-1]
    binina = f"{int(luku):0{bittisyys}b}"[::-1]
    # binina = "{0:045b}".format(luku)[::-1]
    for i in range(len(binina)):
        portit[f"{kirjain}{i:02d}"] = True if binina[i] == "1" else False
    return portit

def testaa_eka(kohta: int, portit: dict, laskut: dict) -> bool:
    kohta = 0
    portit = nollaa_portit(portit)
    portit = laske_tulos(portit, laskut)
    if portit[f"{kohta[0]}{kohta[1:]:02}"]:
        pass
        
def laske_tulos(portit: dict, laskut: dict) -> dict:
    kayttolaskut = laskut.copy()
    while len(kayttolaskut) > 0:
        poistettavat = []
        for vieras in kayttolaskut:
            if kayttolaskut[vieras][0] in portit and kayttolaskut[vieras][1] in portit:
                eka_arvo = portit[kayttolaskut[vieras][0]]
                toka_arvo = portit[kayttolaskut[vieras][1]]
                if kayttolaskut[vieras][2] == "AND":
                    portit[vieras] = eka_arvo and toka_arvo
                    poistettavat.append(vieras)
                elif kayttolaskut[vieras][2] == "OR":
                    portit[vieras] = eka_arvo or toka_arvo
                    poistettavat.append(vieras)
                elif kayttolaskut[vieras][2] == "XOR":
                    portit[vieras] = eka_arvo != toka_arvo
                    poistettavat.append(vieras)
        for poistettava in poistettavat:
            del kayttolaskut[poistettava]
    return dict(sorted(portit.items()))

def z_desimaalina(portit: dict, bittisyys) -> int:
    binina = ""
    for i in range(bittisyys + 1):
        if portit[f"z{i:02}"] == True:
            binina += "1"
        else:
            binina += "0"
    binina = binina[::-1]
    return int(binina, 2)

def etsi_vialliset(portit: dict, laskut: dict):
    bittisyys = laske_bittisyys(portit)
    portit = nollaa_portit(portit)
    portit = laske_tulos(portit, laskut)
    z = z_desimaalina(portit, bittisyys)
    if z != 0:
        print(f"Väärin meni kun kaikki oli 0, z oli kuitenkin {z}")
    else:
        print(f"Oikein meni kun x ja y olivat 0, z on {z} niin kuin pitää")
    
    for i in range(bittisyys):
        portit = nollaa_portit(portit)
        aseta_kirjaimen_luvuksi("x", 2 ** i, portit, bittisyys)
        portit = laske_tulos(portit, laskut)
        z = z_desimaalina(portit, bittisyys)
        if z != 2 ** i:
            print(f"Väärin meni kun x oli {2 ** i}, pelkkä x + 0 oli {z}")
        else:
            print(f"Meni oikein kun x oli {2 ** i}, pelkkä x + 0 oli {z}")
            print("\n\n")
            pass
        
        portit = nollaa_portit(portit)
        aseta_kirjaimen_luvuksi("y", 2 ** i, portit, bittisyys)
        portit = laske_tulos(portit, laskut)
        if z != 2 ** i:
            print(f"Väärin meni kun y oli {2 ** i}, pelkkä y + 0 oli {z}")
        else:
            print(f"Meni oikein kun y oli {2 ** i}, pelkkä x + 0 oli {z}")
            print("\n\n")
            pass

        portit = nollaa_portit(portit)
        aseta_kirjaimen_luvuksi("y", 2 ** i, portit, bittisyys)
        aseta_kirjaimen_luvuksi("y", 2 ** i, portit, bittisyys)
        portit = laske_tulos(portit, laskut)
        if z != 2 ** (i+1):
            print(f"Väärin meni kun x ja y olivat {2 ** i}, x + y oli {z} eikä {2 ** (i+1)}")
        else:
            print(f"Mein oikein kun x ja y olivat {2 ** i}, x + y oli {z} eikä {2 ** (i+1)}")
            print("\n\n")
            pass
            


    

portit, laskut = lue("alku.txt")


etsi_vialliset(portit, laskut)
pass



