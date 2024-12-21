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
    
    def sisalto(self, koord: tuple[int, int]) -> str:
        x, y = koord
        return self.kartta[y][x]
    
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
        return self.sisalto(koord) == "."
    
    def seuraavat_avoimet(self, koord: tuple[int, int], kaydyt: list) -> list[tuple[int, int]]:
        return [naap for naap in self.naapurit(koord) if naap not in 
                [kay[0] for kay in kaydyt] and self.sisalto(naap) == "."]

    def kartoita_askeleet(self):
        i = 1
        while self.maali not in self.matkat_alusta:
            for seur in self.naapurit(next(reversed(self.matkat_alusta.keys()))):
                if self.sisalto(seur) == "." and seur not in self.matkat_alusta:
                    self.matkat_alusta[seur] = i
                    i += 1
    
    def lisaa_timanttioikaisut(self, keskikohta: tuple[int, int]):
        x, y = keskikohta
        oikaisut = {}
        for dy in range(0, 21):
            for dx in range(0, 21 - dy):
                if (dx == 1 and dy == 0) or (dx == 0 and dy == 1):
                    continue
                if abs(dx) == 1 and abs(dy) == 1:
                    continue
                kokeiltavat = [(x - dx, y - dy), (x + dx, y - dy),
                               (x - dx, y + dy), (x + dx, y + dy)]
                for kokeiltava in kokeiltavat:
                    if self.on_sisalla(kokeiltava) and self.on_avoin(kokeiltava):
                        oikaisut[((keskikohta), (kokeiltava))] = dx + dy
        self.oikaisut.update(oikaisut)
                     
    def selvita_huijaukset(self):
        for alkupiste in self.matkat_alusta:
            self.lisaa_timanttioikaisut(alkupiste)
            
    def laske_saasto(self, oikaisu: tuple[tuple[int, int], tuple[int, int]]):
            lahto, tulo = oikaisu[0], oikaisu[1]
            pikamatka = self.oikaisut[oikaisu]
                # lahtoon_alusta = self.matkat_alusta[lahto]
            hitaampi = self.matkat_alusta[tulo] - self.matkat_alusta[lahto]
            saasto = hitaampi - pikamatka
            return saasto
                
sok = Sokkelo("input.txt")
pass

halutut_saastot = 100

saadut_saastot = 0
for oikaisu in sok.oikaisut:
    if sok.laske_saasto(oikaisu) >= halutut_saastot:
        saadut_saastot += 1

print(f"Haluttua säästöä (ainakin {halutut_saastot}) saatiin {saadut_saastot} kappaletta")

# 58719 liian matala
# 73467 liian matala
# 83615 liian matala
# 1020507 oikea 
