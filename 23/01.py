import itertools
import time

alkuaika = time.time()

def lue(tiedosto: str) -> dict:
    with open(tiedosto) as f:
        koneet = {}
        for r in f:
            eka, toka = r.strip().split("-")
            if eka in koneet:
                koneet[eka].append(toka)
            else:
                koneet[eka] = [toka]
            if toka in koneet:
                koneet[toka].append(eka)
            else:
                koneet[toka] = [eka]
        return koneet
    
koneet = lue("input.txt")

yhdistelmat = list(itertools.combinations(koneet, 3))
triot = []
for eka, toka, kolmas in yhdistelmat:
    if toka not in koneet[eka] or kolmas not in koneet[eka] or kolmas not in koneet[toka]:
        continue
    else:
        triot.append((eka, toka, kolmas))

t_alkuisia = 0
for trio in triot:
    potko = "".join(trio)
    if "t" in potko[::2]:
        t_alkuisia += 1

print(f"T-alkuisia on {t_alkuisia}")
print(f"Aikaa meni {time.time() - alkuaika} s")
