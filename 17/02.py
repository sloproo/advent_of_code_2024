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
            self.kasvava = 0

    def etsi_itsen_synnyttaja(self):
        while self.palaute != self.ohjelma:
            self.nollaa()
            print(f"a = {self.a}")
            self.aja_ohjelma()
            # if len(self.palaute) < len(self.ohjelma):
            #     print(f"Vielä ollaan pienissä. a oli 8 ** {self.kasvava}")
            #     print(f"{self.palaute} oli palaute")
            #     print(f"{self.ohjelma} on se mihin pyritään")
            #     self.kasvava += 1
                
        
            # print(f"nyt aletaan lähestyä: \n{self.palaute} ei ole enää lyhyempi kuin ohjelma a:n arvolla\n" +
            #         f"{self.ohjelma}\n {self.kasvava} oli kasvava")
            # if self.kasvava % 100000 == 0:
            print(f"Sillä ollaan palautteessa {self.palaute}")
            self.kasvava += 1
            
                # time.sleep(5)
            # print(f"a:n arvolla {self.kasvava} palaute oli {self.palaute}")
            # time.sleep(0.1)
            # print(f"Kasvava on kasvanut lukuun {self.kasvava}")

        print(f"Sit löytyi. Kasvava = {self.kasvava - 1}")
        print(f"Kesti {time.time() - alkuaika}")

    
    def nollaa(self):
        self.a = self.kasvava
        self.b = 0
        self.c = 0
        self.palaute = []
        self.lukupaa = 0

    def ota_ohjelma(self, otettava: str):
        self.ohjelma = [int(luku) for luku in otettava.split(",")]

    def aja_ohjelma(self):
        jatka = True
        while jatka:
            # if self.lukupaa >= len(self.ohjelma) -1:
            #     print(f"Korruptoitunutta kamaa. Lukupää ulkona. a on {kompu.a}")
            #     break
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

tiedosto = "alku2.txt"
kompu = Tietokone(tiedosto)
kompu.etsi_itsen_synnyttaja()


