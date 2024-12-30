class Portisto:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.portit = {}
            for r in f:
                if r == "\n":
                    break
                portti = r.strip().split(": ")
                self.portit[portti[0]] = True if portti[1] == "1" else False
            self.laskutoimitukset = {}
            for r in f:
                eka, ope, toka, portti = r.strip().replace(" -> ", " ").split(" ")
                self.laskutoimitukset[portti] = (eka, toka, ope)
    
        self.suurin = 0
        for portti in self.portit:
            if portti[0] == "x":
                if int(portti[1:]) > self.suurin:
                    self.suurin = int(portti[1:])

    def nollaa_portit(self):
        for portti in self.portit:
            if portti[0] in ["x", "y", "z"]:
                self.portit[portti] = False
            
    def laske_laskut(self):
        kayttolaskut = self.laskutoimitukset.copy()
        kayttoportit = self.portit.copy()
        while len(kayttolaskut) > 0:
            poistettavat = []
            for vieras in kayttolaskut:
                if kayttolaskut[vieras][0] in kayttoportit and kayttolaskut[vieras][1] in kayttoportit:
                    eka_arvo = kayttoportit[kayttolaskut[vieras][0]]
                    toka_arvo = kayttoportit[kayttolaskut[vieras][1]]
                    if kayttolaskut[vieras][2] == "AND":
                        kayttoportit[vieras] = eka_arvo and toka_arvo
                        poistettavat.append(vieras)
                    elif kayttolaskut[vieras][2] == "OR":
                        kayttoportit[vieras] = eka_arvo or toka_arvo
                        poistettavat.append(vieras)
                    elif kayttolaskut[vieras][2] == "XOR":
                        kayttoportit[vieras] = eka_arvo != toka_arvo
                        poistettavat.append(vieras)
            for poistettava in poistettavat:
                del kayttolaskut[poistettava]
        for portti in kayttoportit:
            if portti[0] in ["x", "y", "z"]:
                self.portit[portti] = kayttoportit[portti]
                self.portit = dict(sorted(self.portit.items()))
        pass
        # return dict(sorted(self.portit.items())) # Miksi tuossa palautetaan vaan items?

    def lyh(self, kirjain: str, numero: int) -> bool:
        return self.portit[f"{kirjain}{numero:02}"]
    
    def kirjain_biniksi(self, kirjain: str) -> str:
        sana = ""
        for i in range(self.suurin + 1):
            sana += str(int(self.lyh(kirjain, i)))
        if kirjain == "z":
            sana += str(int(self.lyh(kirjain, 45)))
        return f"{sana[::-1]}"

    def tarkasta_tilanne(self):
        x_bin_strna = self.kirjain_biniksi("x")
        y_bin_strna = self.kirjain_biniksi("y")
        z_bin_strna = self.kirjain_biniksi("z")
        x_intina = int(x_bin_strna, 2)
        y_intina = int(y_bin_strna, 2)
        z_intina = int(z_bin_strna, 2)
        o_intina = x_intina + y_intina
        bittisyys = max(len(x_bin_strna), len(y_bin_strna), len(z_bin_strna))
        
        o_bin_strna = f"{o_intina:0{bittisyys}b}"
        z_bin_strna = f"{z_intina:0{bittisyys}b}"

        if x_intina + y_intina != z_intina:
            print(f"Väärin meni:")
            print(f"{x_bin_strna.zfill(46)}")
            print(f"{y_bin_strna.zfill(46)}\n")
            print(f"{z_bin_strna.zfill(46)}\n" + 
            f"{o_bin_strna.zfill(46)}")
            for i in range(len(o_bin_strna)):
                if z_bin_strna[i] != o_bin_strna[i]:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
            
        # else:
            # print(f"Oikein meni:\n{x_bin_strna.zfill(46)}\n{y_bin_strna.zfill(46)}\n{z_bin_strna.zfill(46)}\n" + 
            # f"{o_bin_strna.zfill(46)}")
            # for i in range(len(o_bin_strna)):
            #     if z_bin_strna[i] != o_bin_strna[i]:
            #         print("*", end="")
            #     else:
            #         print(" ", end="")
            # print()

    def etsi_vialliset(self):
        for i in range(self.suurin + 1):
            self.nollaa_portit()
            self.portit[f"x{i:02}"] = True
            self.laske_laskut()
            self.tarkasta_tilanne()
            pass
        pass
                

po = Portisto("input.txt")
po.etsi_vialliset()

pass



