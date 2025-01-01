import itertools

class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.alkusarjat = [r.strip() for r in f.readlines()]
        
        self.numeronappis = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"],
            ["X", "0", "A"]]
        self.nuolinappis = [["X", "^", "A"], ["<", "v", ">"]]
        self.liikkeet = {}
        self.nappikset_liikkeiksi()

    def delta(self, nappi_1: str, nappi_2: str) -> tuple:
        if nappi_1 in "^<v>" or nappi_2 in "^<v>":
            nappis = self.nuolinappis
        else:
            nappis = self.numeronappis
        for y in range(len(nappis)):
            for x in range(len(nappis[y])):
                if nappis[y][x] == "X":
                    continue
                if nappis[y][x] == nappi_1:
                    koor_1 = (x, y)
                if nappis[y][x] == nappi_2:
                    koor_2 = (x, y)
        return (koor_2[0] - koor_1[0], koor_2[1] - koor_1[1])
    
    def nappikset_liikkeiksi(self):
        for nappis in [self.numeronappis, self.nuolinappis]:
            napit = [nappi for rivi in nappis for nappi in rivi if nappi != "X"]
            for nappi_1 in napit:
                if nappi_1 not in self.liikkeet:
                    self.liikkeet[nappi_1] = {}
                for nappi_2 in napit:
                    delta = self.delta(nappi_1, nappi_2)
                    vaaka = "<" * abs(delta[0]) if delta[0] < 0 else ">" * delta[0]
                    pysty = "^" * abs(delta[1]) if delta[1] < 0 else "v" * delta[1]
                    painallukset = self.varmista_painallukset(nappi_1, nappi_2,
                                                              vaaka, pysty)
                    if nappi_2 not in self.liikkeet[nappi_1]:
                        self.liikkeet[nappi_1][nappi_2] = painallukset

    def varmista_painallukset(self, nappi_1: str, nappi_2: str, vaaka: str,
                              pysty: str) -> list:
        if nappi_1 == "<" and nappi_2 in "^A":
            return "A" + vaaka + pysty + "A"
        elif nappi_1 in "^A" and nappi_2 == "<":
            return "A" + pysty + vaaka + "A"
        elif nappi_1 in "741" and nappi_2 in "0A":
            return "A" + vaaka + pysty + "A"
        elif nappi_1 in "0A" and nappi_2 in "741":
            return "A" + pysty + vaaka + "A"
        else:
            if "<" in vaaka:
                return "A" + vaaka + pysty + "A"
            else:
                return "A" + pysty + vaaka + "A"

    def tasonnousu(self,siirtymat: dict) -> dict:
        uudet_siirtymat = {}
        for siirtyma in siirtymat:
            for i in range(len(siirtyma) -1):
                if (self.liikkeet[siirtyma[i]][siirtyma[i+1]]) in uudet_siirtymat:
                    uudet_siirtymat[self.liikkeet[siirtyma[i]][siirtyma[i+1]]] += \
                    1 * siirtymat[siirtyma]
                else:
                    uudet_siirtymat[self.liikkeet[siirtyma[i]][siirtyma[i+1]]] = \
                    1 * siirtymat[siirtyma]
        return uudet_siirtymat
    
    def laske_kompleksisuus(self, pohjasarja: str) -> int:
        sarja = "A" + pohjasarja
        siirtymat = {}
        for i in range(len(sarja) - 1):
            if (self.liikkeet[sarja[i]][sarja[i+1]]) in siirtymat:
                siirtymat[self.liikkeet[sarja[i]][sarja[i+1]]] += 1
            else:
                siirtymat[self.liikkeet[sarja[i]][sarja[i+1]]] = 1
        for _ in range(self.robotteja):
            siirtymat = self.tasonnousu(siirtymat)

        pituudet = 0
        for siirtyma in siirtymat:
            pituudet += siirtymat[siirtyma] * (len(siirtyma) - 1)
        print(f"Kompleksisuus on {pituudet} * {int(pohjasarja[:-1])} = {(palautus := pituudet * int(pohjasarja[:-1]))}")
        return palautus

    def ratkaise(self):
        yhteensa = 0
        for alkusarja in self.alkusarjat:
            yhteensa += self.laske_kompleksisuus(alkusarja)
        return yhteensa


ase = Avaruusasema("input.txt")
ase.robotteja = 25
print(ase.ratkaise())
pass
