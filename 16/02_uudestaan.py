def lue(tiedosto: str) -> list:
    kartta = []
    with open(tiedosto) as f:
        for r in f:
            kartta.append([m for m in r.strip()])
        return kartta
    
def alusta_kartta(kartta: list) -> tuple[list, tuple, tuple]:
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
                 tulopaikka: tuple[int, int], tulosuunta: str):
        self.paikka = paikka
        self.suunta = suunta
        self.askeleita = askeleita
        self.tulopaikka = tulopaikka
        self.tulosuunta = tulosuunta

    def koord_edessa(self) -> tuple[int, int]:
        x, y = self.paikka
        if self.suunta == "N":
            koord = (x, y-1)
        elif self.suunta =="E":
            koord = (x+1, y)
        elif self.suunta == "S":
            koord = (x, y+1)
        elif self.suunta == "W":
            koord = (x-1, y)
        return koord
    
    def ruutu_edessa(self, kartta: list) -> str:
        x, y = self.koord_edessa()
        return kartta[y][x]
    
    def eteenpain(self, kartta: list) -> list:
        x, y = self.koord_edessa()
        if kartta[y][x] == ".":
            return [Tila((x, y), self.suunta, self.askeleita + 1,
                         self.paikka, self.suunta)]
        else:
            return []
    
    def kaanny(self, kartta: list) -> list:
        uudet_suunnat = {"N": ("W", "E"), "E": ("N", "S"), "S": ("E", "W"), "W": ("S", "N")}
        kaantyneet = []
        for u_s in uudet_suunnat[self.suunta]:
            kokeiltava = Tila(self.paikka, u_s, self.askeleita + 1000, 
                              self.paikka, self.suunta)
            if kokeiltava.ruutu_edessa(kartta) == ".":
                kaantyneet.append(kokeiltava)
        return kaantyneet
    
    def kaikki_mahdolliset(self, kartta: list) -> list:
        edessa = self.eteenpain(kartta)
        sivuilla = self.kaanny(kartta)
        return edessa + sivuilla

kartta = lue("alku.txt")
kartta, alku, maali = alusta_kartta(kartta)

moi = Tila((3, 7), "S", 1, (-1, -1), "N")
jou = moi.kaikki_mahdolliset(kartta)
pass
        
