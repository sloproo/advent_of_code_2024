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
            self.kasvava = 35184373000000 # Käyty luvut 443739658 - 1670000000 ja se tais mennä yli eli liian isosta aloitettiin
            # Kokeillaan sit pienimmästä 10-numeroisesta oktaaliluvusta eli 134217728:stä ylöspäin

    def etsi_itsen_synnyttaja(self):
        while self.palaute != self.ohjelma:
            self.nollaa()
            self.aja_ohjelma()
            if self.kasvava % 1000000 == 0:
                print(f"Mennään numerossa {self.kasvava}")
                print(self.palaute)
                print(f"{self.ohjelma} \n")
            self.kasvava += 1
    
        print(f"Sit löytyi. Kasvava = {self.kasvava - 1}")
        print(f"Kesti {time.time() - alkuaika}")
    

    '''
    Tätä alla olevaa on muokkailtu kesken tekemisen. Siitä oli sellainen versio,
    jonne manuaalisesti naputellaan sarjaa ja etsitään alkupään numeroita kuntoon.
    Sillä löytyi tuo 4532305133267 ja sen jälkeen sit muokkasin koodia niin, että
    se brute forcettaa viimeiset kolme lukua.

    Siis se perusluuppi oli while self.palaute != self.ohjelma ja inputilla otettiin
    while True. Alla ChatGPT:n tarjoama ohjelma moiseen DDDX
    
        syote = input("Anna syöte: ")
        if syote == "exit":
            break
        desimaalina = 0
        self.nollaa()
        if "8" in syote or "9" in syote:
            print("Syötteessä ei saa olla numeroita 8 tai 9.")
            continue
        for i in range(len(syote)):
            desimaalina += int(syote[i]) * 8 ** (15 - i)
        self.a = desimaalina
        self.aja_ohjelma()
        print(f"Saatiin:  {str(self.palaute): >65}")
        print(f"Halutaan: {str(self.ohjelma): >65}")
    '''

    def testaa_manuaalisesti(self):
        voittavat = []
        for i in range(1000):
            desimaalina = 0
            self.nollaa()
            syote = str(4532305133267) + f"{i:02d}"
            print(f"Syöte on {syote}")
            if "8" in syote or "9" in syote:
                continue
            for i in range(len(syote)):
                desimaalina += int(syote[i]) * 8 ** (15 - i)
            self.a = desimaalina
            self.aja_ohjelma()
            print(f"Saatiin:  {str(self.palaute): >65}")
            print(f"Halutaan: {str(self.ohjelma): >65}")
            if self.palaute == self.ohjelma:
                voittavat.append(desimaalina)
        print(f"Voittava luku oli 10-kantaisena {desimaalina}")
        print(f"Voittavat: {sorted(voittavat)}")

    
    def nollaa(self):
        self.a = self.kasvava
        self.b = 0
        self.c = 0
        self.palaute = []
        self.lukupaa = 0

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

tiedosto = "input.txt"
kompu = Tietokone(tiedosto)
# kompu.etsi_itsen_synnyttaja()
kompu.testaa_manuaalisesti()

