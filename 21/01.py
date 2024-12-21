def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        return [r.strip() for r in f.readlines()]

def nappaimen_paikka(nappain, nappis: list) -> tuple[int, int]:
    for y in range(len(nappis)):
        if nappain in nappis[y]:
            return (nappis[y].index(nappain), y)

def siirtymä_nappaimeen(nappain_1: int, nappain_2: int, nappis: list) -> tuple[int, int]:
    x1, y1 = nappaimen_paikka(nappain_1, nappis)
    x2, y2 = nappaimen_paikka(nappain_2, nappis)
    return (x2 -x1, y2 -y1)

def sormen_liikkeet(nappain_1, nappain_2, nappis: list) -> str:
    dx, dy = siirtymä_nappaimeen(nappain_1, nappain_2, nappis)
    if dx < 0:
        horiz = abs(dx) * "L"
    else:
        horiz = dx * "R"
    if dy < 0:
        vert = abs(dy) * "U"
    else:
        vert = dy * "D"
    if nappis == numeronappis:
        if nappain_2 in [7, 4, 1]:
            return vert+horiz
        else:
            return horiz+vert
    elif nappis == nuolinappis:
        if nappain_1 == "L":
            return horiz+vert
        else:
            return vert+horiz
    else:
        raise AssertionError("Mitään näppistä ei jäänyt kiinni!")

def liikkeet_nrosarjaan(nrosarja: str) -> str:
    liikesarja = ""
    kohdat = [99] + [int(nro) for nro in nrosarja[:-1]] + [99]
    for i in range(len(kohdat) - 1):
        liikesarja += sormen_liikkeet(kohdat[i], kohdat[i+1], numeronappis)
        liikesarja += "A"
    return liikesarja

def liikkeet_liikesarjaan(liikesarja: str) -> str:
    tekeilla = ""
    kohdat = ["A"] + [suunta for suunta in liikesarja[:-1]] + ["A"]
    for i in range(len(kohdat) - 1):
        tekeilla += sormen_liikkeet(kohdat[i], kohdat[i+1], nuolinappis)
        tekeilla += "A"
    return tekeilla

numerosarjat = lue("alku2.txt")

numeronappis = [[7, 8, 9], [4, 5, 6], [1, 2, 3], ["X", 0, 99]]
nuolinappis = [["X", "U", "A"], ["L", "D", "R"]]

yhteensa = 0

for numerosarja in numerosarjat:
    eka_sarja = liikkeet_nrosarjaan(numerosarja)
    toka_sarja = liikkeet_liikesarjaan(eka_sarja)
    kolmas_sarja = liikkeet_liikesarjaan(toka_sarja)
    kompleksisuus = len(kolmas_sarja) * int(numerosarja[:-1])
    print(f"Kompleksisuus on {len(kolmas_sarja)} * {int(numerosarja[:-1])}"
          + f" = {kompleksisuus}")
    yhteensa += kompleksisuus

print(f"Vastaus on {yhteensa}")

