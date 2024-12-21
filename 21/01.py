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
    
    def delta_napilta_toiselle(self, nappi1, nappi2, nappaimisto: list) -> tuple[int, int]:
        x1, y1 = self.napin_paikka(nappi1, nappaimisto)
        x2, y2 = self.napin_paikka(nappi2, nappaimisto)
        return (x2 - x1, y2 - y1)
        
    def sarja_suunniksi(self, sarja: str, nappis: list) -> str:
        suunnat = self.napilta_toiselle("A", sarja[0], nappis) + "A"
        for i in range(len(sarja) -1):
            suunnat += self.napilta_toiselle(sarja[i], sarja[i+1], nappis)
            suunnat += "A"
        return suunnat
    
    def pura(self, sarja: str) -> str:
        sarja = "A" + sarja
        for i in range(len(sarja) - 1):
            eka_nappi = sarja[i]
            toka_nappi = sarja[i+1]
            napit = ""
            dx, dy = self.delta_napilta_toiselle(eka_nappi, toka_nappi,
                                                self.numeronappis)
            if dx < 0:
                napit += "<" * abs(dx)
            else:
                napit += ">" * dx
            if dy < 0:
                napit += "^" * abs(dy)
            else:
                napit += "v" * dy
            print(napit)
            vaihtoehtolista = list({o for o in itertools.permutations(napit, 3)})
            vaihtoehtolista = self.putsaa_vaihtoehtolista(vaihtoehtolista, 
                                                          eka_nappi, self.numeronappis)
            vaihtoehtolista = [o + ("A",) for o in vaihtoehtolista]
            pass
    
    def syvenna(self, suunnat: list) -> list:
        pass
    
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
    
    def putsaa_vaihtoehtolista(self, vaihtoehtolista: list,
                               lahtokohta: tuple[int, int], 
                               nappaimisto: list) -> list:
        pysyva_lk = lahtokohta
        palautettavat = []
        for askelsarja in vaihtoehtolista:
            lahtokohta = pysyva_lk
            for askel in askelsarja:
                lahtokohta = self.koordinaatista_suuntaan(lahtokohta, askel)
                if nappaimisto[lahtokohta[1]][lahtokohta[0]] == "X":
                    break
            else:
                palautettavat.append(askelsarja)
        return palautettavat

ase = Avaruusasema("input.txt")

# 201096 liian korkea

