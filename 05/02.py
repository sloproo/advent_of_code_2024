def avaa(tiedosto) -> tuple[list, list]:
    parit = []
    with open(tiedosto) as f:
        for r in f:
            if "|" in r:
                sivut = tuple([int(luku) for luku in r.strip().split("|")])
                parit.append(sivut)
    return parit


print(avaa("alku.txt"))
