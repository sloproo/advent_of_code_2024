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

    def napin_paikka(self, nappi, nappaimisto: list) -> tuple[int, int]:
        for y in range(len(nappaimisto)):
            for x in range(len(nappaimisto[y])):
                if nappaimisto[y][x] == nappi:
                    return (x, y)
        raise AssertionError("Ei löytynyt haettua nappia")
    
    def siirto_deltaksi(self, nappi1, nappi2, nappaimisto: list) -> tuple[int, int]:
        x1, y1 = self.napin_paikka(nappi1, nappaimisto)
        x2, y2 = self.napin_paikka(nappi2, nappaimisto)
        return (x2 - x1, y2 - y1)
    
    def painallus_ylatasolla(self, suunta: str) -> str:
        

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
        return list({"".join(per) for per in itertools.permutations(yhteensa)})
    
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
        palautettavat = []
        for askelsarja in vaihtoehtolista:
            olinpaikka = lahtokohta
            for askel in askelsarja:
                olinpaikka = self.koordinaatista_suuntaan(olinpaikka, askel)
                if nappaimisto[olinpaikka[1]][olinpaikka[0]] == "X":
                    break
            else:
                palautettavat.append(askelsarja)
        return palautettavat

ase = Avaruusasema("input.txt")
pass 
# 201096 liian korkea

