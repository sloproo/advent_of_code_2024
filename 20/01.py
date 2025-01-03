class Sokkelo:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.kartta = []
            for r in f:
                self.kartta.append([m for m in r])
        self.alkupuhdistus()
        self.matkat_alusta = {self.alku: 0}
        self.kartoita_askeleet()
        self.oikaisut = {}
        self.selvita_huijaukset()

    
    def alkupuhdistus(self):
        for y in range(len(self.kartta)):
            for x in range(len(self.kartta[y])):
                if self.kartta[y][x] == "S":
                    self.alku = (x, y)
                    self.kartta[y][x] = "."
                elif self.kartta[y][x] == "E":
                    self.maali = (x, y)
                    self.kartta[y][x] = "."
    
    def naapurit(self, koord: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = koord
        return (paikka for paikka in [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
                if self.on_sisalla(paikka))
    
    def on_sisalla(self, koord: tuple[int, int]) -> bool:
        x, y = koord
        if x < 0 or y < 0 or y >= len(self.kartta) or x >= len(self.kartta[y]):
            return False
        else:
            return True
    
    def on_avoin(self, koord: tuple[int, int]) -> bool:
        x, y = koord
        return self.kartta[y][x] == "."
    
    def voiko_huijata(self, koord: [tuple[int, int]], suunta: str) -> bool:
        x, y = koord
        if suunta == "N" and self.on_sisalla((x, y-2)):
            return self.kartta[y-1][x] == "#" and self.kartta[y-2][x] == "."
        elif suunta == "E" and self.on_sisalla((x+2, y)):
            return self.kartta[y][x+1] == "#" and self.kartta[y][x+2] == "."
        elif suunta == "S" and self.on_sisalla((x, y+2)):
            return self.kartta[y+1][x] == "#" and self.kartta[y+2][x] == "."
        elif suunta == "W" and self.on_sisalla((x-2, y)):
            return self.kartta[y][x-1] == "#" and self.kartta[y][x-2] == "."
    
    def huijausnaapuri(self, koord: tuple[int, int], suunta: str) -> tuple[int, int]:
        x, y = koord
        return {"N": (x, y-2), "E": (x+2, y), "S": (x, y+2), "W": (x-2, y)}[suunta]
    
    def seuraavat_ruudut(self, koord: tuple[int, int], kaydyt: list) -> list[tuple[int, int]]:
        return [naap for naap in self.naapurit(koord) if naap not in 
                [kay[0] for kay in kaydyt] and self.kartta[naap[1]][naap[0]] == "."]
        
    def kartoita_askeleet(self):
        i = 1
        while self.maali not in self.matkat_alusta:
            for seur in self.naapurit(next(reversed(self.matkat_alusta.keys()))):
                if self.kartta[seur[1]][seur[0]] == "." and seur not in self.matkat_alusta:
                    self.matkat_alusta[seur] = i
                    i += 1
        
    
    def selvita_huijaukset(self):
        for kayty in self.matkat_alusta:
            for suunta in "NESW":
                if self.voiko_huijata(kayty, suunta):
                    seuraava = self.huijausnaapuri(kayty, suunta)
                    self.oikaisut[(kayty, seuraava)] = \
                    self.matkat_alusta[seuraava] - self.matkat_alusta[kayty] - 2
                
sok = Sokkelo("input.txt")

osumia = 0
for oikaisu in sok.oikaisut:
    if sok.oikaisut[oikaisu] >= 100:
        osumia += 1
print(f"Ainakin 100 ps oikaisevia huijauksia oli {osumia}")



