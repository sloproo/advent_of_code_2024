import itertools
            
def sisalla(x: int, y: int, ruudukko: list) ->bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def etsi(x: int, y: int, dx: int, dy: int, sana: str, ruudukko: list):
    if not (sisalla(x+dx, y+dy, ruudukko)):
        return 0
    if ruudukko[y+dy][x+dx] == sana[1]:
        if len(sana) == 2:
            print(f"Löytyi, päätepiste {x+dx}, {y+dy}, suunta {dx}, {dy}")
            return 1
        else:
            return etsi(x+dx, y+dy, dx, dy, sana[1:], ruudukko)
    else:
        return 0

ruudukko = []
with open("alku.txt") as f:
    for r in f:
        rivi = [kirjain for kirjaimet in r.strip().split() for kirjain in kirjaimet]
        print(rivi)
        ruudukko.append(rivi)

sana = "XMAS"
sanoja_loytynyt = 0 

for y in range(len(ruudukko) - 1):
    for x in range(len(ruudukko[y]) - 1):
        if ruudukko[y][x] == sana[0]:
            suunnat = [pari for pari in itertools.product([-1, 0, 1], repeat=2)]
            suunnat.remove((0,0))
            for dx, dy in suunnat:
                sanoja_loytynyt += etsi(x, y, dx, dy, sana, ruudukko)
            

print(sanoja_loytynyt)
