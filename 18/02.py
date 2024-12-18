def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        bitit = [(int(jaettu[0]), int(jaettu[1])) for jaettu in [r.strip().split(",") for r in f.readlines()]]
        return bitit
    
bitit = lue("input.txt")
print(bitit)
print(len(bitit))
joukko = set(bitit)
print(len(joukko))


