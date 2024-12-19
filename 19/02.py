def lue(tiedosto: str) -> tuple[list, list]:
    with open(tiedosto) as f:
        pyyhkeet = f.readline().strip().split(", ")
        f.readline()
        asetelmat = [r.strip() for r in f]
    return pyyhkeet, asetelmat

def syvenny(asetelma: str, pyyhkeet: list, loytyneita: int) -> int:
    lyhyempi = min(len(asetelma), pyyhkeet[0])
    for raitoja in range(lyhyempi, 0, -1):
        for pyyhe in [p for p in pyyhkeet if len(pyyhe) == raitoja]:
            if asetelma[:raitoja] == pyyhe:
                loytyneita += syvenny(asetelma[raitoja:], pyyhkeet, loytyneita)
    return loytyneita

pyyhkeet, asetelmat = lue("alku.txt")
pass
pyyhkeet_lajiteltu = sorted(pyyhkeet, key= lambda x: len(x), reverse= True)

for asetelma in asetelmat:
    print(syvenny)

