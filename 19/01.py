class Kylpyla:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.pyyhkeet = f.readline().strip().split(", ")
            f.readline()
            self.asetelmat = [r.strip() for r in f]
        self.pisin = max([len(pyyhe) for pyyhe in self.pyyhkeet])
        self.vaaralliset = {vari for vari in varit 
                            if vari not in [p for p in self.pyyhkeet if len(p) == 1]}

    def vaaran_paikat(self, asetelma: str) -> list:
        paikat = []
        for vaara in self.vaaralliset:
            i = 0
            seuraava = asetelma.find(vaara, i)
            while seuraava != -1:
                paikat.append(seuraava)
                i = seuraava + 1
                seuraava = asetelma.find(vaara, i)
        return paikat


    def syvenny(self) -> int:
        mahdoton = True
        for i in range(pisin, 0, -1):
            if asetelma[-i:] in pyyhkeet:
                mahdoton = False
        if mahdoton:
            return False
        lyhyempi = min(len(asetelma), len(pyyhkeet[0]))
        for raitoja in range(lyhyempi, 0, -1):
            for pyyhe in [p for p in pyyhkeet if len(p) == raitoja]:
                if pyyhe == asetelma[:raitoja]:
                    if pyyhe == asetelma:
                        return True
                    else:
                        if syvenny(asetelma[raitoja:], pyyhkeet):
                        return True
            # print(f"Käyty läpi pituudella {raitoja}")
        return False


pyyhkeet, asetelmat = lue("input2.txt")
varit = [kirjain for kirjain in "".join(pyyhkeet)]
vaaralliset = {vari for vari in varit if vari not in [p for p in pyyhkeet if len(p) == 1]}
pyyhkeet_lajiteltu = sorted(pyyhkeet, key= lambda x: len(x), reverse= True)
pisin = len(pyyhkeet_lajiteltu[0])

riskipaikat = vaaran_paikat(vaaralliset, asetelmat[0])
pass

asetelma = asetelmat[0]
alastringit = []
for riski in riskipaikat:
    for ss_pituus in range(pisin, 1, -1):
        alastringit.append(asetelma[max(0, riski - (ss_pituus -1)):
                                    min(len(asetelma), riski + pisin)])
alastringit = list(set(alastringit))


kelvollisia = 0
i = 0
for asetelma in asetelmat:
    print(f"Käydään läpi asetelma {i}")
    if syvenny(asetelma, pyyhkeet_lajiteltu):
        kelvollisia += 1
        print(f"Löytyi kelvollinen, joita on nyt {kelvollisia}")
    else:
        print("Se ei ollut kelvollinen")
    i += 1


print(kelvollisia)

# 272 on liian matala
