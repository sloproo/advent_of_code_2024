class Kartta:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.bitit = [(int(jaettu[0]), int(jaettu[1])) for jaettu in [r.strip().split(",") for r in f.readlines()]]
            self.leveys = max(luku for luku in{pari[0] for pari in self.bitit}.union({pari[0] for pari in self.bitit}))
            self.korruptoituneet = []
            self.kierros = 0
            self.alku = (0, 0)
            self.maali = (self.leveys, self.leveys)
            self.kaydyt = {}
            self.saavutetut_ajassa = {}

    def sisalla(self, pari: tuple[int, int]) -> bool:
        x, y = pari
        if x < 0 or y < 0 or x > self.leveys or y > self.leveys:
            return False
        else:
            return True
    
    def naapurit(self, ruutu: tuple[int, int]) -> list[tuple[int, int]]:
        x, y = ruutu
        return {pari for pari in {(x-1, y), (x, y-1), (x+1, y), (x, y+1)} 
                if self.sisalla(pari)}
    
    def luo_tarjokkaat(self, ruutu: tuple[int, int]) -> list[tuple[int, int]]:
        return [naapuri for naapuri in self.naapurit(ruutu) 
                if naapuri not in self.korruptoituneet]

    def alusta(self):
        self.tarjokkaat = {self.alku: self.kierros}

    def kay_kierros(self):
        seuraavat = []        
        self.saavutetut_ajassa[self.kierros] = []
        for tarjokas in self.tarjokkaat:
            if tarjokas not in self.kaydyt and tarjokas not in self.korruptoituneet:
                self.kaydyt[tarjokas] = self.kierros
                self.saavutetut_ajassa[self.kierros] += tarjokas
                seuraavat += self.luo_tarjokkaat(tarjokas)
        self.tarjokkaat = list(set(seuraavat))
        self.kierros += 1
    
    def mene_maaliin(self):
        self.alusta()
        while self.maali not in self.kaydyt:
            
            self.kay_kierros()
        print(f"Maalissa {self.maali} ollaan ajassa {self.kaydyt[self.maali]}")
        

kartta = Kartta("input.txt")
kartta.korruptoituneet = kartta.bitit[:1024]
kartta.mene_maaliin()

    



