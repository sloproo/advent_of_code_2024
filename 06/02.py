def avaa(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([merkki for merkki in r.strip()])
    return kartta

def etsi_ukko(kartta: list) -> tuple[int, int]:
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            if kartta[y][x] == "^":
                return (x, y)

def sisalla(x: int, y: int, kartta: list) -> bool:
    if x < 0 or y < 0 or y >= len(kartta) or x >= len(kartta[y]):
        return False
    else:
        return True

def liiku(x: int, y: int, suunta: str, kartta: list) -> tuple[tuple[int, int], str]:
    rotaatio = "URDL"
    ohjeet = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    seuraava = (x + ohjeet[suunta][0], y + ohjeet[suunta][1])
    if not sisalla(seuraava[0], seuraava[1], kartta):
        return ((-1, -1), suunta)
    elif kartta[seuraava[1]][seuraava[0]] == ".":
        return ((seuraava[0], seuraava[1]), suunta)
    elif kartta[seuraava[1]][seuraava[0]] == "#":
        suunta = rotaatio[(rotaatio.find(suunta) + 1) % 4]
        return ((x, y), suunta)
    else:
        raise ValueError("Nyt meni vituix kun liikkuessa ei vastaan tullut reuna, . tai #")

def kierto(tiedosto: str) -> list:
    kartta = avaa(tiedosto)
    suunta = "U"
    ukko = etsi_ukko(kartta)
    kartta[ukko[1]][ukko[0]] = "."
    kaydyt = set()

    while ukko != (-1, -1):
        kaydyt.add(ukko)
        ukko, suunta = liiku(ukko[0], ukko[1], suunta, kartta)
    return list(kaydyt)

avattava = "input.txt"
og_kartta = avaa(avattava)
og_kierto = kierto(avattava)
print(og_kierto)
luuppeja = 0

for x, y in og_kierto:
    if og_kartta[y][x] != ".":
        continue
    kartta = avaa(avattava)
    kartta[y][x] = "#"
    suunta = "U"
    ukko = etsi_ukko(kartta)
    kartta[ukko[1]][ukko[0]] = "."
    kaydyt = set()

    while ukko != (-1, -1):
        kaydyt.add((ukko, suunta))
        ukko, suunta = liiku(ukko[0], ukko[1], suunta, kartta)
        if (ukko, suunta) in kaydyt:
            luuppeja += 1
            break

print(luuppeja)
