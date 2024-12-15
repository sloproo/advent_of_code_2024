def lue(tiedosto: str) -> tuple[tuple[int, int], set, set, str]:
    
    with open(tiedosto) as f:
        seinat, laatikot = set(), set()        
        i = 0
        for r in f:
            if r == "\n":
                break
            for j in range(len(r.strip())):
                if r[j] == "#":
                    seinat.add((j, i))
                elif r[j] == "O":
                    laatikot.add((j, i))
                elif r[j] == "@":
                    robotti = (j, i)
            i += 1
        kaskyt = ""
        for r in f:
            kaskyt += r.strip()
        kaskyt = kaskyt.replace("v", "D").replace("^", "U").replace("<", "L").replace(">", "R")
        return (robotti, seinat, laatikot, kaskyt)

def summaa(eka: tuple, toka: tuple) -> tuple:
    return (eka[0] + toka[0], eka[1] + toka[1])

def gps(koord: tuple) -> int:
    return koord[1] * 100 + koord[0]

robotti, seinat, laatikot, kaskyt = lue("input.txt")

suunnat = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

def piirra(robotti: tuple =robotti, seinat:set =seinat, laatikot: set =laatikot):
    leveys = max(koord[0] for koord in seinat) + 1
    korkeus = max(koord[1] for koord in seinat) + 1
    kartta = []
    for _ in range(korkeus):
        kartta.append(["." for __ in range(leveys)])
    for seina in seinat:
        kartta[seina[1]][seina[0]] = "#"
    for laatikko in laatikot:
        kartta[laatikko[1]][laatikko[0]] = "O"
    kartta[robotti[1]][robotti[0]] = "@"
    for r in kartta:
        print("".join(r))
    pass

def liiku(suunta: str, robotti: tuple =robotti, seinat: set = seinat,
          laatikot: set = laatikot) -> tuple[tuple[int, int], set]:
    liikkuvat = [robotti]
    menoruutu = summaa(robotti, suunnat[suunta])
    while menoruutu not in seinat:
        if menoruutu in laatikot:
            liikkuvat.append(menoruutu)
            menoruutu = summaa(menoruutu, suunnat[suunta])
        else:
            if len(liikkuvat) == 1:
                return menoruutu, laatikot
            else:
                laatikot.add(menoruutu)
                laatikot.remove(liikkuvat[1])
                return liikkuvat[1], laatikot
    return robotti, laatikot

piirra(robotti, seinat, laatikot)

for suunta in kaskyt:
    robotti, laatikot = liiku(suunta, robotti, seinat, laatikot)
    # piirra(robotti, seinat, laatikot)
    # print()


gps_summa = 0
for laatikko in laatikot:
    gps_summa += gps(laatikko)

print(gps_summa)
