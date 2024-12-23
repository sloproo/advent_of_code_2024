import time

alkuaika = time.time()

class Tietokone:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.a = int(f.readline().strip().split(": ")[1])
            self.b = int(f.readline().strip().split(": ")[1])
            self.c = int(f.readline().strip().split(": ")[1])
            f.readline()
            self.ohjelma = [int(luku) for luku in f.readline().strip().split(": ")[1].split(",")]
            self.kaskyt = {0: self.nolla, 1: self.yksi, 2: self.kaksi, 3: self.kolme,
                           4: self.nelja, 5: self.viisi, 6: self.kuusi, 7: self.seitseman}
            self.lukupaa = 0
            self.palaute = []
            self.kasvava = 1

    def hae_itse_synnyttaja(self):
        while self.palaute != self.ohjelma:
            self.nollaa()
            annettu = int(input("Anna a:n arvo oktaalilukuna: "))
            print(f"Se on {int(str(annettu), 8)} desimaalilukuna")
            self.a = annettu
            
            # self.a = int(input("Anna a:n arvo: "))
            annettu = self.a
            self.aja_ohjelma()
            print(f"{self.palaute} on tuollainen verrattuna haluttuun\n" +
                  f"{self.ohjelma}\nA:lle annettu arvo oli {annettu}")
    
    def etsi_itsen_synnyttaja(self):
        while self.palaute != self.ohjelma:
            self.nollaa()
            pass
            self.aja_ohjelma()
            if len(self.palaute) < len(self.ohjelma):
                self.kasvava *= 2
                
            else:
                print(f"nyt aletaan lähestyä: palaute ei ole enää lyhyempi kuin ohjelma a:n arvolla" +
                      f"{self.a}.\nSillä siis palaute on {self.palaute}")
                # time.sleep(5)
            # print(f"a:n arvolla {self.kasvava} palaute oli {self.palaute}")
            # time.sleep(0.5)
            print(f"Kasvava on kasvanut lukuun {self.kasvava}")

        print(f"Sit löytyi. Kasvava = {self.kasvava}")
        print(f"Kesti {time.time() - alkuaika}")

    
    def nollaa(self):
        self.b = 0
        self.c = 0
        self.palaute = []
        self.lukupaa = 0

    def ota_ohjelma(self, otettava: str):
        self.ohjelma = [int(luku) for luku in otettava.split(",")]

    def aja_ohjelma(self):
        jatka = True
        while jatka:
            if self.lukupaa >= len(self.ohjelma) -1:
                print(f"Korruptoitunutta kamaa. Lukupää ulkona. a on {kompu.a}")
                break
            kasky = self.ohjelma[self.lukupaa]
            muuttuja = self.ohjelma[self.lukupaa + 1]
            self.lukupaa += 2
            self.suorita(kasky, muuttuja)
            if self.lukupaa >= len(self.ohjelma):
                jatka = False
        # if self.palaute != [0]:
        #     print(f"Ohjelman suoritus päättyi. Tuloste:\n {self.palaute}")
        
    def suorita(self, kasky: int, muuttuja: int):
        self.kaskyt[kasky](muuttuja)
    
    def kombo(self, muuttuja: int) -> int:
        # assert 0 <= muuttuja < 7
        palautuva = {0: 0, 1: 1, 2: 2, 3: 3, 4: self.a, 5: self.b, 6: self.c}
        return palautuva[muuttuja]

    def bw_xor(self, m_1: int, m_2: int) -> int:
        bin_1 = bin(m_1)[2:]
        bin_2 = bin(m_2)[2:]
        bin_1 = bin_1[::-1]
        bin_2 = bin_2[::-1]
        lyhyempi, pitempi = tuple(sorted([bin_1, bin_2], key= lambda x: len(x)))
        palautettava_str = ""
        for i in range(len(lyhyempi)):
            if lyhyempi[i] != pitempi[i]:
                palautettava_str += "1"
            else:
                palautettava_str += "0"
        for i in range(len(lyhyempi), len(pitempi)):
            if pitempi[i] == "1":
                palautettava_str += "1"
            else:
                palautettava_str += "0"
        palautettava_int = 0
        for i in range(len(palautettava_str)):
            if palautettava_str[i] == "1":
                palautettava_int += 2 ** i
        return palautettava_int
    
    def nolla(self, muuttuja: int):
        self.a = self.a // (2 ** self.kombo(muuttuja))
    
    def yksi(self, muuttuja: int):
        self.b = self.bw_xor(self.b, muuttuja)
    
    def kaksi(self, muuttuja: int):
        self.b = self.kombo(muuttuja) % 8

    def kolme(self, muuttuja: int):
        if self.a != 0:
            self.lukupaa = muuttuja
    
    def nelja(self, muuttuja: int):
        self.b = self.bw_xor(self.b, self.c)
    
    def viisi(self, muuttuja: int):
        self.palaute.append(self.kombo(muuttuja) % 8)

    def kuusi(self, muuttuja: int):
        self.b = self.a // (2 ** self.kombo(muuttuja))

    def seitseman(self, muuttuja: int):
        self.c = self.a // (2 ** self.kombo(muuttuja))
    
    def siisti_palaute(self) -> str:
        pass
        kak = ",".join([str(luku) for luku in self.palaute])
        print(kak)
        return kak

tiedosto = "input.txt"
kompu = Tietokone(tiedosto)
kompu.kasvava = 1
kompu.hae_itse_synnyttaja()

