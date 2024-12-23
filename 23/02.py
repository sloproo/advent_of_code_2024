import itertools
import time

alkuaika = time.time()

def lue(tiedosto: str) -> dict:
    with open(tiedosto) as f:
        koneet = {}
        for r in f:
            eka, toka = r.strip().split("-")
            if eka in koneet:
                koneet[eka].add(toka)
            else:
                koneet[eka] = {toka}
            if toka in koneet:
                koneet[toka].add(eka)
            else:
                koneet[toka] = {eka}
        return koneet

def puhdista(joukko: set) -> set:
    joukko_lyhennetty = {tuple(sorted(jasen)) for jasen in joukko}
    return joukko_lyhennetty

def kasvata(monikot: set) -> set:
    suurempi = set()
    for kopla in monikot:
        yhteiset = koneet[kopla[0]].intersection(*(set(koneet[muu]) for muu in kopla[1:]))
        for yhteinen in yhteiset:
            suurempi.add(kopla + (yhteinen, ))
    suurempi = puhdista(suurempi)
    return suurempi

    
koneet = lue("input.txt")
suurin_mahdollinen = max({len(yhteydet) for yhteydet in koneet.values()})
suurin_porukka = 0

parit = set()
for kone in koneet:
    for kone_2 in koneet[kone]:
        parit.add((kone, kone_2))
parit = puhdista(parit)

pass
joukot = {2: parit}

for i in range(3, suurin_mahdollinen + 1):
    joukot[i] = kasvata(joukot[i-1])

pisin = joukot[max(joukot.keys())]

vastaus = ",".join(list(pisin)[0])
print(vastaus)


print(f"Aikaa meni {time.time() - alkuaika} sek.")

