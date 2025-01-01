import itertools

class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.alkusarjat = [r.strip() for r in f.readlines()]
        self.liikkeet = {
            "^": {"A": ">A", "<": "v<A", "v": "vA", "^": "A"},
            "A": {"^": "<A", ">": "vA", "A": "A"},
            "<": {"^": ">^A", "v": ">A", ">": ">>A", "<": "A"},
            "v": {"^": "^A", "<": "<A", ">": ">A", "v": "A"},
            ">": {"A": "^A", "<": "<<A", "v": "<A", ">": "A"}
        }

    def tasonnousu(self, painallukset: str) -> str:
        palautettava = ""
        for i in range(len(painallukset) - 1):
            palautettava += self.liikkeet[painallukset[i]][painallukset[i+1]]
        return palautettava
    
    def etsi_nopeimmat(self):
        lyhin = None
        for self.liikkeet["^"][">"], self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
            self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], self.liikkeet[">"]["^"] in \
            itertools.product([">vA", "v>A"], ["<v<A", "v<<A"], ["<vA", "v<A"],
            [">^>A", ">>^A"], ["^>A", ">^A"], ["<^A", "^<A"]):
            testiliikkeet = "^^>A><>v^>><<vv<vA"
            myllatty = self.tasonnousu(self.tasonnousu(self.tasonnousu(self.tasonnousu( \
                self.tasonnousu(testiliikkeet)))))
            if lyhin == None:
                lyhin = len(myllatty)
            elif len(myllatty) < lyhin:
                lyhin = len(myllatty)
                n1, n2, n3, n4, n5, n6 = self.liikkeet["^"][">"], \
                self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
                self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], \
                self.liikkeet[">"]["^"]
        
        self.liikkeet["^"][">"], self.liikkeet["A"]["<"], self.liikkeet["A"]["v"], \
        self.liikkeet["<"]["A"], self.liikkeet["v"]["A"], self.liikkeet[">"]["^"] \
        = n1, n2, n3, n4, n5, n6

    def nopein_numeronappis(self):
        # Tämmösellä liikkeelle list(set(itertools.permutations("vv>", 3))) 

ase = Avaruusasema("input.txt")
ase.etsi_nopeimmat()
pass




"""
Todo:
Seuraavalle tasolle-funktio joka yksinkertaisesti korvaa alemman tason sarja-
merkkijonosta kaiken sillä, mitä self.liikkeet sanoo. "A":sta aina lähdetään ja
liikkeet self.liikkeetin mukaan.

Siinä käyttöön 

Tässä käyttöön 
itertools.product: self.likkeet["^"][">"], self.liikkeet[jotain][muuta] in
itertools.product([ekan, vaihtoehdot], [tokan_vaihtoehdot], jne) ja ajaa siinä
for-loopissa sarjaa_seuraavalle tasolle vaikka 5 kertaa ja käskee sitä seuraamaan
ja tallentamaan aina, kun vaihtoehtojen yhdistelmällä saa kaikkein pienimmän painallusmäärän.


    def sarja_seuraavalle_tasolle(self, alempi: str) -> str:
        for vaihtoehdot 
    
    def ratkaise(self):
        kompleksisuudet = 0
        
        for sarja in self.alkusarjat:
            tokat = self.sarja_ylemmiksi_painalluksiksi(sarja, self.numeronappis)
            tokat = list(set(tokat))
            kolmannet = []
            for toka in tokat:
                kolmannet += self.sarja_ylemmiksi_painalluksiksi(toka, self.nuolinappis)
            kolmannet = list(set(kolmannet))
            pass # Tsekataan tähän väliin kolmosia
            lyhin = min(len(kol) for kol in kolmannet) 
            kolmannet = [kolmas for kolmas in kolmannet if len(kolmas) == lyhin]
            neljannet = []
            for kolmas in kolmannet:
                neljannet += self.sarja_ylemmiksi_painalluksiksi(kolmas, self.nuolinappis)
            neljannet = list(set(neljannet))
            # neljannet = [neljas for neljas in neljannet if len(neljas) == len(sorted(neljannet, key= len)[0])]
            lyhin = min([len(nelonen) for nelonen in neljannet])
            neljannet = [nel for nel in neljannet if len(nel) == lyhin]
            print(f"Sarjan {sarja} kompleksisuus on {lyhin} * {int(sarja[:-1])} = " +
            f"{lyhin * int(sarja[:-1])} ")
            kompleksisuudet += lyhin * int(sarja[:-1])
        print(f"Kompleksisuuksien summa = {kompleksisuudet}")        

    def napin_koordinaatti(self, nappi, nappaimisto: list) -> tuple[int, int]:
        for y in range(len(nappaimisto)):
            for x in range(len(nappaimisto[y])):
                if nappaimisto[y][x] == nappi:
                    return (x, y)
        raise AssertionError("Ei löytynyt haettua nappia")
    
    def sarja_ylemmiksi_painalluksiksi(self, sarja: str, nappis: str) -> list:
        delta = self.matka_deltaksi("A", sarja[0], nappis)
        permutaatiot = self.delta_permutaatioiksi(delta)
        permutaatioiden_jono = [self.putsaa_vaihtoehtolista(permutaatiot, "A", nappis)] +[["A"]]
        for i in range(len(sarja) -1):
            delta = self.matka_deltaksi(sarja[i], sarja[i+1], nappis)
            permutaatiot = self.delta_permutaatioiksi(delta)
            permutaatiot = self.putsaa_vaihtoehtolista(permutaatiot, sarja[i], nappis)
            permutaatioiden_jono.append(permutaatiot)
            permutaatioiden_jono.append(["A"])
        yhdistelmat = list(itertools.product(*permutaatioiden_jono))
        litistetyt = [''.join(yhdistelma) for yhdistelma in yhdistelmat]
        return list(set(litistetyt))
        
    def litista_permutaatiot(self, permutaatiot: list) -> list:
        eroteltuina = list(itertools.product(*permutaatiot))
        litistettyna = [''.join(eroteltu) for eroteltu in eroteltuina]
        return litistettyna

    def sarja_deltoiksi(self, sarja: str, nappis: str) -> list:
        sarja = "A" + sarja
        deltat = []
        for i in range(len(sarja) -1):
            deltat.append(self.matka_deltaksi(sarja[i], sarja[i+1], nappis))
        return deltat
    
    def matka_deltaksi(self, nappi1, nappi2, nappaimisto: list) -> tuple[int, int]:
        x1, y1 = self.napin_koordinaatti(nappi1, nappaimisto)
        x2, y2 = self.napin_koordinaatti(nappi2, nappaimisto)
        return (x2 - x1, y2 - y1)

    def delta_permutaatioiksi(self, delta: tuple[int, int]) -> list[str]:
        yhteensa = ""
        if delta[0] < 0:
            yhteensa += abs(delta[0]) * "<"
        else:
            yhteensa += delta[0] * ">"
        if delta[1] < 0:
            yhteensa += abs(delta[1]) * "^"
        else:
            yhteensa += delta[1] * "v"
        mahdolliset = list({"".join(per) for per in itertools.permutations(yhteensa)})
        return mahdolliset
    
    def putsaa_vaihtoehtolista(self, vaihtoehtolista: list,
                               lahtokohta: str, 
                               nappaimisto: list) -> list:
        palautettavat = []
        for askelsarja in vaihtoehtolista:
            olinpaikka = self.napin_koordinaatti(lahtokohta, nappaimisto)
            for askel in askelsarja:
                olinpaikka = self.koordinaatista_suuntaan(olinpaikka, askel)
                if nappaimisto[olinpaikka[1]][olinpaikka[0]] == "X":
                    break
            else:
                palautettavat.append(askelsarja)
        return palautettavat

    def koordinaatista_suuntaan(self, koord: tuple[int, int], suunta: str) -> \
    tuple[int, int]:
        if suunta == "^":
            return (koord[0], koord[1] - 1)
        elif suunta == ">":
            return (koord[0] + 1, koord[1])
        elif suunta == "v":
            return (koord[0], koord[1] + 1)
        elif suunta =="<":
            return (koord[0] - 1, koord[1])
        else:
            raise AssertionError("Nyt ei ollut kunnon suuntaa. Lipsahtiko A?")

"""
