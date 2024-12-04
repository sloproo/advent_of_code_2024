import itertools
            
def sisalla(x: int, y: int, ruudukko: list) ->bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def etsi(x: int, y: int, dx: int, dy: int, sana: str, ruudukko: list):
    if not (sisalla(x+dx, y+dy, ruudukko)):
        # print(f"Tuli reuna vastaan {x+dx} {y+dy}")
        return 0
    if ruudukko[y+dy][x+dx] == sana[1]:
        if len(sana) == 2:
            print(f"Sana täyteen")
            print(f"Alkukohta x = {x-2*dx}, y = {y-2*dy}, suunta {dx}, {dy}")
            return 1
        else:
            # print(f"Löytyi kirjain {sana[1]}")
            return etsi(x+dx, y+dy, dx, dy, sana[1:], ruudukko)
    else:
        # print(f"Ei löytynyt, tuli {ruudukko[y+dy][x+dx]}")
        return 0

def lue(tiedosto: str) -> list:
    palautettava =[]
    with open(tiedosto) as f:
        for r in f:
            rivi = [kirjain for kirjaimet in r.strip().split() for kirjain in kirjaimet]
            palautettava.append(rivi)
    return palautettava

ruudukko = lue("input.txt")

sana = "XMAS"
sanoja_loytynyt = 0 

for y in range(len(ruudukko)):
    for x in range(len(ruudukko[y])):
        if ruudukko[y][x] == sana[0]:
            # print(f"Löytyi kirjain X kohdasta x = {x}, y = {y}")
            suunnat = [pari for pari in itertools.product([-1, 0, 1], repeat=2)]
            suunnat.remove((0,0))
            for dx, dy in suunnat:
                # print(f"Etsitään suunnasta dx = {dx}, dy = {dy}")
                sanoja_loytynyt += etsi(x, y, dx, dy, sana, ruudukko)
            

print(sanoja_loytynyt)
