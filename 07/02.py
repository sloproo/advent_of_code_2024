import itertools
import time

alkuaika = time.time()

def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        palautettava = []        
        for r in f:
            siisti = [int(luku) for luku in r.replace(":", "").strip().split(" ")]
            palautettava.append((siisti[0], siisti[1:]))
        return palautettava

def plus(eka: int, toka: int) -> int:
    return eka + toka

def kerto(eka: int, toka: int) -> int:
    return eka * toka

def yhdista(eka: int, toka: int) -> int:
    return int(str(eka) + str(toka))



laskut = avaa("input.txt")
operaattorit = ["plus", "kertaa", "yhdista"]
laske = {"plus": plus, "kertaa": kerto, "yhdista": yhdista}
kelvollisia = 0
huonoja = 0

for vastaus, nrot in laskut:
    og_nrot = [nro for nro in nrot]
    operaatiolistat = itertools.product(operaattorit, repeat=len(nrot) - 1)
    for operaatiolista in operaatiolistat:
        yli = False
        nrot = [og_nro for og_nro in og_nrot]
        for i in range(len(nrot) - 1):
            tulos = laske[operaatiolista[i]](nrot[0], nrot[1])
            if tulos > vastaus:
                yli = True
                break
            if len(nrot) >= 3:
                nrot = [tulos] + nrot[2:]
            else:
                nrot = [tulos]
        if yli:
            continue
        else:
            if nrot[0] == vastaus:
                kelvollisia += vastaus
                break

print(kelvollisia)
print(f"Aikaa kului {time.time() - alkuaika}")    
