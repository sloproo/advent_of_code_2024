# Tää taitaa olla oikeasti kakkososan ratkaisu

import time

def naapurit(x: int, y: int, ruudukko: list) -> list:
    palautettavat = []
    korkeus = len(ruudukko)
    leveys = len(ruudukko[0])
    for y_koord in range(y-1, y+2):
        if y_koord < 0 or y_koord >= korkeus:
            continue
        else:
            for x_koord in range(x-1, x+2):
                if x_koord < 0 or x_koord >= leveys:
                    continue
                else:
                    if not (x_koord == x and y_koord == y):
                        palautettavat.append((x_koord, y_koord))
    return palautettavat

def etsi_naapurista(x: int, y: int, ruudukko: list, sana: str) -> int:
    loytyneita = 0
    naapuriruudut = naapurit(x, y, ruudukko)
    for x1, y1 in naapuriruudut:
        print(f"Lähdetään {x}, {y}:stä liikkeelle, etsitään naapuriruudusta x = {x1}, y = {y1} seuraavaa kirjainta rimpsusta {sana}")
        if len(sana) == 1:
            return 1
        if ruudukko[y1][x1] == sana[1]:
            loytyneita += etsi_naapurista(x1, y1, ruudukko, sana[1:])
    # print(f"Palautetaan löytyneet joita oli {loytyneita}")
    return loytyneita
            
ruudukko = []
with open("alku.txt") as f:
    for r in f:
        rivi = [kirjain for kirjaimet in r.strip().split() for kirjain in kirjaimet]
        print(rivi)
        ruudukko.append(rivi)

sana = "XMAS"
sanoja_loytynyt = 0 
for y in range(len(ruudukko)):
    for x in range(len(ruudukko[y])):
        if ruudukko[y][x] == sana[0]:
            print(f"Ruudussa {x}, {y} on kirjain {sana[0]}, lähdetään siitä eteenpäin etsimään")
            uusia_osumia = etsi_naapurista(x, y, ruudukko, sana)
            print(f"Uusia osumia löytyi {uusia_osumia}")
            sanoja_loytynyt += uusia_osumia
            print(f"Tähän mennessä sanoja löytynyt {sanoja_loytynyt}")
            
print(sanoja_loytynyt)
