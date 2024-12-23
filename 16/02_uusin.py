# listaa kierrokset: jokaiselle se, mihin nyt tullaan. Kans yleinen lista kaikista käydyistä,
# ettei myöhässä tulijoita kirjata enää uudestaan mihinkään.

from typing import Self

class Kartta:
    def __init__(self, tiedosto: str):
        self.kartta = []
        with open(tiedosto) as f:
            for r in f:
                self.kartta.append([m for m in r.strip()])
        self.kasittele_kartta()
        self.tila = Tila(self.alku, "E", 0, [])

    
        
    def kasittele_kartta(self):
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[y])):
                if self.kartta[y][x] == "E" or self.kartta[y][x] == "S":
                    if self.kartta[y][x] == "E":
                        self.maali = (x, y)
                        self.kartta[y][x] = "."
                    elif self.kartta[y][x] == "S":
                        self.alku = (x, y)
                        self.kartta[y][x] = "."
    
    def etsi_reitti(self):
        pass

    def naapurit(self, koord: tuple[int, int]) -> list[tuple[int, int]]:
        pass

    def sisalla (self, koord: [tuple[int, int]]) -> bool:
        x, y = koord
        if y < 0 or x < 0 or y >= len(self.kartta) or x >= len(self.kartta[0]):
            return False
        return True


    
class Tila:
    def __init__(self, koord: tuple[int, int], suunta: str, askeleita: int,
                 edellinen: list[Self]):
        self.koord = koord
        self.suunta = suunta
        self.askeleita = askeleita
        self.edellinen = edellinen
    
    def __str__(self):
        return f"koordinaatit: {self.koord}, suunta: {self.suunta}, askeleita: " \
        + f"{self.askeleita}, edellinen oli {self.edellinen}"

self.kartta = lue("alku.txt")
self.kartta, alku, maali = kasittele_kartta(self.kartta)





pass


        
        


