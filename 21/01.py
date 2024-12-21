class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.sarjat = [r.strip() for r in f.readlines()]
        self.numeronappis = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"],
                             ["X", "0", "A"]]
        self.nuolinappis = [["X", "^", "A"], ["<", "v", ">"]]
        self.yht_kompleksisuus = 0
        for sarja in self.sarjat:
            self.pura(sarja)
        print(f"Yhteensä kompleksisuus = {self.yht_kompleksisuus}")

    def napin_paikka(self, nappi, nappaimisto: list) -> tuple[int, int]:
        for y in range(len(nappaimisto)):
            for x in range(len(nappaimisto[y])):
                if nappaimisto[y][x] == nappi:
                    return (x, y)
        raise AssertionError("Ei löytynyt haettua nappia")
    
    def napilta_toiselle(self, nappi1, nappi2, nappaimisto: list) -> str:
        x1, y1 = self.napin_paikka(nappi1, nappaimisto)
        x2, y2 = self.napin_paikka(nappi2, nappaimisto)
        dx = x2 - x1
        dy = y2 - y1
        if dx != 0 and abs(dx) / dx < 0:
            hori = "<" * abs(dx)
        else:
            hori = ">" * dx
        if dy != 0 and abs(dy) / dy < 0:
            vert = "^" * abs(dy)
        else:
            vert = "v" * dy
        if nappaimisto == self.numeronappis and nappi1 in [7, 4, 1]:
            return hori+vert
        elif nappaimisto == self.nuolinappis and nappi1 == "<":
            return hori+vert
        else:
            return vert+hori
        
    def sarja_suunniksi(self, sarja: str, nappis: list) -> str:
        suunnat = self.napilta_toiselle("A", sarja[0], nappis) + "A"
        for i in range(len(sarja) -1):
            suunnat += self.napilta_toiselle(sarja[i], sarja[i+1], nappis)
            suunnat += "A"
        return suunnat
    
    def pura(self, sarja: str) -> str:
        eka = self.sarja_suunniksi(self.sarjat[0], self.numeronappis)
        toka = self.sarja_suunniksi(eka, self.nuolinappis)
        kolmas = self.sarja_suunniksi(toka, self.nuolinappis)
        pituus = len(kolmas)
        sarja_int = int(sarja[:-1])
        print(f"Kompleksisuus vois olla {pituus} * {sarja_int} = " + 
              f"{pituus * sarja_int}")
        self.yht_kompleksisuus += pituus * sarja_int


ase = Avaruusasema("input.txt")

# 201096 liian korkea

