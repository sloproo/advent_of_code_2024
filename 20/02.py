class Sokkelo:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.kartta = []
            for r in f:
                self.kartta.append([m for m in r])
        self.alkupuhdistus()
        self.matkat_alusta = {self.alku: 0}
        self.kartoita_askeleet()
        self.oikaisut = []
        self.selvita_huijaukset()
        
        self.saastettava = 54
        
        self.laske_saastot()
        print(f"Täsmälleen {self.saastettava} ps nopeampia oikaisuja oli {self.satasen_saastoja}")

    
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

    def etene_seinissa(self, og_lahtopiste: tuple[int, int], 
                       nyt_lahtopiste: tuple[int, int], nyt_tulopiste: tuple[int, int],
                       ask_otettu: int, etaisyydet_lahtopisteesta: dict) -> dict:
        y, x = nyt_tulopiste
        if ask_otettu > 20:
            return {}
        etaisyydet_lahtopisteesta[nyt_tulopiste] = (ask_otettu, self.sisalto(nyt_tulopiste))
        if self.sisalto(nyt_tulopiste) == "." and ask_otettu == 1:
                return {}
        if self.sisalto(nyt_tulopiste) == ".":
                return etaisyydet_lahtopisteesta
        # kasvatettava = len(etaisyydet_lahtopisteesta)
        for naapuri in [n for n in self.naapurit(nyt_tulopiste)
                        if n not in etaisyydet_lahtopisteesta]:
            etaisyydet_lahtopisteesta.update(self.etene_seinissa(
                og_lahtopiste, nyt_tulopiste, naapuri, ask_otettu + 1,
                etaisyydet_lahtopisteesta))
        # if len(etaisyydet_lahtopisteesta) == kasvatettava:
        #     return {}
        # else:
        return etaisyydet_lahtopisteesta

    def astu_seinaan(self, og_lahtopiste: tuple[int, int]):
        oikaisut = {}
        kaydyt = {og_lahtopiste}
        nykyiset = {n for n in self.naapurit(og_lahtopiste) if self.sisalto(n) == "#"}
        for i in range(1, 19):
            tulevat = set()
            for nykyinen in nykyiset:
                for tuleva in self.naapurit(nykyinen):
                    if tuleva != og_lahtopiste and tuleva not in kaydyt \
                        and tuleva not in oikaisut:
                        if self.sisalto(tuleva) == "#":
                            tulevat.add(tuleva)
                        elif self.sisalto(tuleva) == ".":
                            oikaisut[tuleva] = i + 1
                kaydyt.add(nykyinen)
            nykyiset = tulevat
        self.oikaisut += [(og_lahtopiste, oik, oikaisut[oik]) for oik in oikaisut]

                     
    def selvita_huijaukset(self):
        for alkupiste in self.matkat_alusta:
            self.astu_seinaan(alkupiste)
            
    def laske_saastot(self):
        self.satasen_saastoja = 0
        for oikaisu in self.oikaisut:
            lahto, tulo, pikamatka = oikaisu
                # lahtoon_alusta = self.matkat_alusta[lahto]
            hitaampi = self.matkat_alusta[tulo] - self.matkat_alusta[lahto]
            saasto = hitaampi - pikamatka
            if saasto == self.saastettava:
                self.satasen_saastoja += 1
                
sok = Sokkelo("alku.txt")
pass
