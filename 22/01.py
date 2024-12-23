def lue(tiedosto :str) -> list:
    with open(tiedosto) as f:
        return [int(r) for r in f.readlines()]

luvut = lue("input.txt")

def kierros(luku: int) -> int:
    pitka = 16777216
    a = (luku * 64 ^ luku) % pitka
    b = (a // 32 ^ a) % pitka
    c = (b * 2048 ^ b) % pitka
    return c

summa = 0

for luku in luvut:
    for _ in range(2000):
        luku = kierros(luku)
    summa += luku

print(summa)


