import itertools

def sisalla(x: int, y: int, ruudukko: list) ->bool:
    if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
        return False
    return True

def lue(tiedosto: str) -> list:
    palautettava =[]
    with open(tiedosto) as f:
        for r in f:
            rivi = [kirjain for kirjaimet in r.strip().split() for kirjain in kirjaimet]
            palautettava.append(rivi)
    return palautettava

def onko_risti(x: int, y: int, ruudukko: list) -> bool:
    kirjaimet = ["M", "S"]
    for x2, y2 in [pari for pari in itertools.product([-1, 1], repeat=2)]:
        if not sisalla(x + x2, y + y2, ruudukko):
            return False
    if ruudukko[y-1][x-1] == ruudukko[y-1][x+1] and ruudukko[y-1][x-1] in kirjaimet:
        kirjaimet.remove(ruudukko[y-1][x-1])
        if ruudukko[y+1][x-1] == ruudukko[y+1][x+1] and ruudukko[y+1][x-1] in kirjaimet:
            return True
    elif ruudukko[y-1][x-1] == ruudukko[y+1][x-1] and ruudukko[y-1][x-1] in kirjaimet:
        kirjaimet.remove(ruudukko[y-1][x-1])
        if ruudukko[y-1][x+1] == ruudukko[y+1][x+1] and ruudukko[y-1][x+1] in kirjaimet:
            return True
    elif ruudukko[y-1][x-1] == ruudukko[y-1][x+1] and ruudukko[y-1][x-1] in kirjaimet:
        kirjaimet.remove(ruudukko[y-1][x-1])
        if ruudukko[y+1][x-1] == ruudukko[y+1][x+1] and ruudukko[y+1][x-1] in kirjaimet:
            return True
    else:
        return False
            
ruudukko = lue("input.txt")

risteja_loytynyt = 0 
for y in range(len(ruudukko)):
    for x in range(len(ruudukko[y])):
        if ruudukko[y][x] == "A":
            print(f"Ruudussa {x}, {y} on kirjain A, lähdetään siitä eteenpäin etsimään")
                        
            if onko_risti(x, y, ruudukko):
                risteja_loytynyt += 1
                print(f"Uusi osuma löytyi, X:n keskipiste {x}, {y}")
            print(f"Tähän mennessä sanoja löytynyt {risteja_loytynyt}")
            
print(risteja_loytynyt)
