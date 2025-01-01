import itertools

class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.alkusarjat = [r.strip() for r in f.readlines()]
        
        self.numeronappis = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"],
            ["X", "0", "A"]]
        self.nuolinappis = [["X", "^", "A"], ["<", "v", ">"]]
        # self.liikkeet = {
        #     "^": {"A": ">A", "<": "v<A", "v": "vA", "^": "A"},
        #     "A": {"^": "<A", ">": "vA", "A": "A"},
        #     "<": {"^": ">^A", "v": ">A", ">": ">>A", "<": "A"},
        #     "v": {"^": "^A", "<": "<A", ">": ">A", "v": "A"},
        #     ">": {"A": "^A", "<": "<<A", "v": "<A", ">": "A"}
        # }
        self.liikkeet = {}
        self.nappikset_liikkeiksi()
        self.kerroksia = 26

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
                    # else:
                    #     self.liikkeet[nappi_1][nappi_2] += painallukset
        # self.liikkeet["A"]["A"].remove("A")
        # for nappi_1 in self.liikkeet:
        #     for nappi_2 in self.liikkeet[nappi_1]:
        #         if len(self.liikkeet[nappi_1][nappi_2]) == 1:
        #             self.liikkeet[nappi_1][nappi_2] = self.liikkeet[nappi_1][nappi_2][0]
        # pass
                    
    def varmista_painallukset(self, nappi_1: str, nappi_2: str, vaaka: str,
                              pysty: str) -> list:
        if nappi_1 == "<" and nappi_2 in "^A":
            return vaaka + pysty + "A"
        elif nappi_1 in "^A" and nappi_2 == "<":
            return pysty + vaaka + "A"
        elif nappi_1 in "741" and nappi_2 in "0A":
            return vaaka + pysty + "A"
        elif nappi_1 in "0A" and nappi_2 in "741":
            return pysty + vaaka + "A"
        else:
            if "<" in vaaka:
                return vaaka + pysty + "A"
            else:
                return pysty + vaaka + "A"

    def tasonnousu(self, painallukset: str) -> str:
        palautettava = self.liikkeet["A"][painallukset[0]]
        for i in range(len(painallukset) - 1):
            palautettava += self.liikkeet[painallukset[i]][painallukset[i+1]]
        return palautettava
    
    def laske_kompleksisuus(self, sarja: str) -> int:
        pohjasarja = sarja
        for _ in range(self.kerroksia):
            sarja = self.tasonnousu(sarja)
        print(f"Kompleksisuus on {len(sarja)} * {int(pohjasarja[:-1])} = {(palautus := len(sarja) * int(pohjasarja[:-1]))}")
        return palautus

    def ratkaise(self):
        yhteensa = 0
        for alkusarja in self.alkusarjat:
            yhteensa += self.laske_kompleksisuus(alkusarja)
        return yhteensa


ase = Avaruusasema("input.txt")
print(ase.ratkaise())
pass





# Todo:

# Siinä käyttöön 

# Tässä käyttöön 
# itertools.product: self.likkeet["^"][">"], self.liikkeet[jotain][muuta] in
# itertools.product([ekan, vaihtoehdot], [tokan_vaihtoehdot], jne) ja ajaa siinä
# for-loopissa sarjaa_seuraavalle tasolle vaikka 5 kertaa ja käskee sitä seuraamaan
# ja tallentamaan aina, kun vaihtoehtojen yhdistelmällä saa kaikkein pienimmän painallusmäärän.
    
    # def etsi_nopeimmat(self):
    #     lyhin = None
    #     vaihtoehtoja_sisaltavat = []
    #     for nappi_1 in self.liikkeet:
    #         for nappi_2 in self.liikkeet[nappi_1]:
    #             if len(self.liikkeet[nappi_1][nappi_2]) > 1:
    #                 vaihtoehtoja_sisaltavat.append((nappi_1, nappi_2))
    #     for i in range(len(vaihtoehtoja_sisaltavat)):
    #         pass
        
            

    #     for self.liikkeet["^"][">"], self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
    #         self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], self.liikkeet[">"]["^"] in \
    #         itertools.product([">vA", "v>A"], ["<v<A", "v<<A"], ["<vA", "v<A"],
    #         [">^>A", ">>^A"], ["^>A", ">^A"], ["<^A", "^<A"]):
    #         testiliikkeet = "^^>A><>v^>><<vv<vA"
    #         myllatty = self.tasonnousu(self.tasonnousu(self.tasonnousu(self.tasonnousu( \
    #             self.tasonnousu(testiliikkeet)))))
    #         if lyhin == None:
    #             lyhin = len(myllatty)
    #         elif len(myllatty) < lyhin:
    #             lyhin = len(myllatty)
    #             n1, n2, n3, n4, n5, n6 = self.liikkeet["^"][">"], \
    #             self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
    #             self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], \
    #             self.liikkeet[">"]["^"]
        
    #     self.liikkeet["^"][">"], self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
    #     self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], self.liikkeet[">"]["^"] \
    #     = n1, n2, n3, n4, n5, n6


#     def ratkaise(self):
#         kompleksisuudet = 0
        
#         for sarja in self.alkusarjat:
#             tokat = self.sarja_ylemmiksi_painalluksiksi(sarja, self.numeronappis)
#             tokat = list(set(tokat))
#             kolmannet = []
#             for toka in tokat:
#                 kolmannet += self.sarja_ylemmiksi_painalluksiksi(toka, self.nuolinappis)
#             kolmannet = list(set(kolmannet))
#             pass # Tsekataan tähän väliin kolmosia
#             lyhin = min(len(kol) for kol in kolmannet) 
#             kolmannet = [kolmas for kolmas in kolmannet if len(kolmas) == lyhin]
#             neljannet = []
#             for kolmas in kolmannet:
#                 neljannet += self.sarja_ylemmiksi_painalluksiksi(kolmas, self.nuolinappis)
#             neljannet = list(set(neljannet))
#             # neljannet = [neljas for neljas in neljannet if len(neljas) == len(sorted(neljannet, key= len)[0])]
#             lyhin = min([len(nelonen) for nelonen in neljannet])
#             neljannet = [nel for nel in neljannet if len(nel) == lyhin]
#             print(f"Sarjan {sarja} kompleksisuus on {lyhin} * {int(sarja[:-1])} = " +
#             f"{lyhin * int(sarja[:-1])} ")
#             kompleksisuudet += lyhin * int(sarja[:-1])
#         print(f"Kompleksisuuksien summa = {kompleksisuudet}")        

#     def napin_koordinaatti(self, nappi, nappaimisto: list) -> tuple[int, int]:
#         for y in range(len(nappaimisto)):
#             for x in range(len(nappaimisto[y])):
#                 if nappaimisto[y][x] == nappi:
#                     return (x, y)
#         raise AssertionError("Ei löytynyt haettua nappia")
    
#     def matka_deltaksi(self, nappi1, nappi2, nappaimisto: list) -> tuple[int, int]:
#         x1, y1 = self.napin_koordinaatti(nappi1, nappaimisto)
#         x2, y2 = self.napin_koordinaatti(nappi2, nappaimisto)
#         return (x2 - x1, y2 - y1)

    # def delta_permutaatioiksi(self, delta: tuple[int, int]) -> list[str]:
    #     yhteensa = ""
    #     if delta[0] < 0:
    #         yhteensa += abs(delta[0]) * "<"
    #     else:
    #         yhteensa += delta[0] * ">"
    #     if delta[1] < 0:
    #         yhteensa += abs(delta[1]) * "^"
    #     else:
    #         yhteensa += delta[1] * "v"
    #     mahdolliset = list({"".join(per) for per in itertools.permutations(yhteensa)})
    #     return mahdolliset
    
    # def putsaa_vaihtoehtolista(self, vaihtoehtolista: list,
    #                            lahtokohta: str, 
    #                            nappaimisto: list) -> list:
    #     palautettavat = []
    #     for askelsarja in vaihtoehtolista:
    #         olinpaikka = self.napin_koordinaatti(lahtokohta, nappaimisto)
    #         for askel in askelsarja:
    #             olinpaikka = self.koordinaatista_suuntaan(olinpaikka, askel)
    #             if nappaimisto[olinpaikka[1]][olinpaikka[0]] == "X":
    #                 break
    #         else:
    #             palautettavat.append(askelsarja)
    #     return palautettavat
    
#     def koordinaatista_suuntaan(self, koord: tuple[int, int], suunta: str) -> \
#     tuple[int, int]:
#         if suunta == "^":
#             return (koord[0], koord[1] - 1)
#         elif suunta == ">":
#             return (koord[0] + 1, koord[1])
#         elif suunta == "v":
#             return (koord[0], koord[1] + 1)
#         elif suunta =="<":
#             return (koord[0] - 1, koord[1])
#         else:
#             raise AssertionError("Nyt ei ollut kunnon suuntaa. Lipsahtiko A?")

# """
