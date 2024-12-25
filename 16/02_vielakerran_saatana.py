from typing import Self

def lue(tiedosto: str) -> tuple:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([m for m in r.strip()])
    for y in range(len(kartta)):
        for x in range(len(kartta[y])):
            if kartta[y][x] == "E" or kartta[y][x] == "S":
                if kartta[y][x] == "E":
                    maali = (x, y)
                    kartta[y][x] = "."
                elif kartta[y][x] == "S":
                    alku = (x, y)
                    kartta[y][x] = "."
    return (kartta, alku, maali)


class Tila:
    def __init__(self, paikka: tuple[int, int], suunta: str, askeleita: int,
                edeltava: Self, kartta: list):
                #  edeltava: Self, kartta: list =kartta):
        self.paikka = paikka
        self.suunta = suunta
        self.askeleita = askeleita
        self.edeltava = edeltava
        self.kartta = kartta

    def __repr__(self):
        return f"{self.paikka}, {self.suunta}, {self.askeleita}, {self.edeltava.paikka_ja_suunta()}"

    def edessa(self):
        x, y = self.paikka
        if self.suunta == "N":
            vastassa = self.kartta[y-1][x]
            koord = (x, y-1)
        elif self.suunta =="E":
            vastassa = self.kartta[y][x+1]
            koord = (x+1, y)
        elif self.suunta == "S":
            vastassa = self.kartta[y+1][x]
            koord = (x, y+1)
        elif self.suunta == "W":
            vastassa = self.kartta[y][x-1]
            koord = (x-1, y)
        else:
            raise AssertionError("Nyt oli outo suunta vastassa")
        return (vastassa, koord)
    
    def astu_eteenpain(self) -> list[Self]:
        if self.edessa()[0] == "#":
            return []
        else:
            return [Tila(self.edessa()[1], self.suunta, self.askeleita + 1, self, self.kartta)]

    def kaanny_x2(self) -> list[Self]:
        uudet_suunnat = {"N": ("W", "E"), "E": ("N", "S"), "S": ("E", "W"), "W": ("S", "N")}
        kaantyneet = []
        for u_s in uudet_suunnat[self.suunta]:
            kaantynyt  = Tila(self.paikka, u_s, self.askeleita + 1000, self, self.kartta)
            if kaantynyt.edessa()[0] != "#":
                kaantyneet.append(kaantynyt)
        return kaantyneet
        
    def seuraavat(self):
        return self.astu_eteenpain() + self.kaanny_x2()
    
    def paikka_ja_suunta(self) -> tuple[tuple[int, int], str]:
        return (self.paikka, self.suunta)

    def olenko_sama_mutta_hitaampi(self, toinen_tila: Self) -> bool:
        if self.tila == toinen_tila.tila and self.suunta == toinen_tila.suunta and \
            self.askeleita > toinen_tila.askeleita:
                return True
        return False
    
    

kartta, alku, maali = (lue("input.txt"))
jonossa = [Tila(alku, "E", 0, None, kartta)]
vanhat = []
maalissa = False

while not maalissa:
    tuoreet = []
    nyt_kasitellyt = []
    jonossa = sorted(jonossa, key= lambda x: x.askeleita)
    nopein = jonossa[0].askeleita
    for tila in jonossa:
        if tila.askeleita == nopein:
            if tila.paikka != maali:
                for tuore in tila.seuraavat():
                    tuoreet.append(tuore)
            else:
                maalissa = True
            nyt_kasitellyt.append(tila)
            vanhat.append(tila)
        else:
            break

    for nyt_kasitelty in nyt_kasitellyt:
        jonossa.remove(nyt_kasitelty)
    for tuore in tuoreet:
        kelvollinen = True
        for vanha in vanhat:
            if vanha.askeleita > tuore.askeleita and kelvollinen:
                jonossa.append(tuore)
                break
            elif tuore.paikka == vanha.paikka and tuore.suunta == vanha.suunta \
                and tuore.askeleita > vanha.askeleita:
                kelvollinen = False
                break
        if kelvollinen:
            jonossa.append(tuore)
    print(jonossa[0].askeleita)
    print(f"Vanhat: {len(vanhat)}\nJonossa: {len(jonossa)}")
    print(f"")

pass
for vanha in vanhat:
    if vanha.paikka == maali:
        print(vanha)
