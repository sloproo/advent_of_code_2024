def avaa(tiedosto) -> tuple[list, list]:
    parit = []
    manuaalit = []
    with open(tiedosto) as f:
        for r in f:
            if "|" in r:
                sivut = tuple([int(luku) for luku in r.strip().split("|")])
                parit.append(sivut)
            else:
                break
        for r in f:
            manuaali = [int(sivu) for sivu in r.strip().split(",")]
            manuaalit.append(manuaali)

    return (parit, manuaalit)

def kelpaako(manuaali: list, parit: list) -> bool:
    for pari in parit:
        if pari[0] in manuaali and pari[1] in manuaali:
            if manuaali.index(pari[0]) < manuaali.index(pari[1]):
                continue
            else:
                return False
    else:
        return True

def vaihda(eka: int, toka: int, manuaali: list) -> list:
    manuaali[eka], manuaali[toka] = manuaali[toka], manuaali[eka]
    return manuaali

parit, manuaalit = avaa("input.txt")
vaarat = []
korjatut = []
for manuaali in manuaalit:
    if not kelpaako(manuaali, parit):
        vaarat.append(manuaali)

vaihtoja = 0

for manuaali in vaarat:
    while not kelpaako(manuaali, parit):
        for pari in parit:
            if pari[0] in manuaali and pari[1] in manuaali:
                if manuaali.index(pari[0]) > manuaali.index(pari[1]):
                    vaihda(manuaali.index(pari[0]), manuaali.index(pari[1]), manuaali)
                    vaihtoja += 1
    korjatut.append(manuaali)

korjattujen_keskikohtien_summa = 0
for manuaali in korjatut:
    korjattujen_keskikohtien_summa += manuaali[len(manuaali) // 2]

print(korjattujen_keskikohtien_summa)
print(f"Vaihtoja: {vaihtoja}")
