"""
Elikkäs.
Ehkä tämän voi tehdä yksinkertaisesti kun tietää mitä tekee.
funktio sille, että muuttaa näppäimenpainallukset ylemmän tason
näppäimenpainalluksiksi. Niistä vaihtoehtoiset versiot, putsausfunktio on jo.
Kattoo niitten pituudet iteroiden ainakin sen ykköstehtävässä vaaditun kaksi
tasoa ylöspäin ja siinähän se sitten onkin.

Myöhempää varten voi katsoa vaikka just sen kaksi tasoa ylöspäin erilaisille kolmen
napinpainalluksen yhdistelmällä (10 ^3 ei kai ole paha emt?), jossa erot tulevat
näkyviin ja siitä ylöspäin varmaan kertaututuvat. Niillä sit pelaa, jos syvyyttä tulee
kovasti lisää.
"""


import itertools

class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.alkusarjat = [r.strip() for r in f.readlines()]
        self.numeronappis = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"],
                             ["X", "0", "A"]]
        self.nuolinappis = [["X", "^", "A"], ["<", "v", ">"]]
        
        kompleksisuudet = 0
        
        for sarja in self.alkusarjat:
            tokat = self.sarja_ylemmiksi_painalluksiksi(sarja, self.numeronappis)
            kolmannet = []
            for toka in tokat:
                kolmannet += self.sarja_ylemmiksi_painalluksiksi(toka, self.nuolinappis)
            neljannet = []
            for kolmas in kolmannet:
                neljannet += self.sarja_ylemmiksi_painalluksiksi(kolmas, self.nuolinappis)
            lyhin = min([len(nelonen) for nelonen in neljannet])
            print(f"Sarjan {sarja} kompleksisuus on {lyhin} * {int(sarja[:-1])} = " +
            f"{lyhin * int(sarja[:-1])} ")
            kompleksisuudet += lyhin * int(sarja[:-1])
        print(f"Kompleksisuuksien summa = {kompleksisuudet}")
        
    def kasittele_sarja(self, sarja: str, taso: int) -> list[str]:
        if taso == 1:
            nappis = self.numeronappis
        else:
            nappis = self.nuolinappis
        seuraava_taso = self.sarja_ylemmiksi_painalluksiksi(sarja, nappis)
        

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
        
        #         all_combinations = list(itertools.product(*permutaatioiden_jono))
        #         flattened_combinations = [''.join(combination) for combination in all_combinations]


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

ase = Avaruusasema("input.txt")


