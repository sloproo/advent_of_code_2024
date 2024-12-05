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

parit, manuaalit = avaa("input.txt")

keskimmaiset = 0
for manuaali in manuaalit:
    for pari in parit:
        if pari[0] in manuaali and pari[1] in manuaali:
            if manuaali.index(pari[0]) < manuaali.index(pari[1]):
                continue
            else:
                break
    else:
        keskimmaiset += manuaali[len(manuaali) // 2]

print(keskimmaiset)

