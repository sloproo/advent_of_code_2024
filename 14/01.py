def lue(tiedosto: str) -> list:
    with open(tiedosto) as f:
        robotit = []
        for r in f:
            r = r.replace("p=", "").replace("v=", "").strip()
            paikka, suunta = r.split(" ")
            paikka = tuple([int(luku) for luku in paikka.split(",")])
            suunta = tuple([int(luku) for luku in suunta.split(",")])
            robotit.append((paikka, suunta))
        return robotit
    
def liikuta(robotti: tuple, kierroksia: int) -> tuple[int, int]:
    return ((robotti[0][0] + robotti[1][0] * kierroksia, 
             robotti[0][1] + robotti[1][1] * kierroksia))

def korjaa(sijainti: tuple, leveys: int, korkeus: int) -> tuple[int, int]:
    x, y = (sijainti[0] % leveys, sijainti[1] % korkeus)
    return (x, y)

def laske_kvadrantit(leveys: int, korkeus: int) -> list:
    eka = (0, leveys // 2 , 0, korkeus //2)
    toka = (leveys // 2 + 1, leveys, 0, korkeus // 2)
    kolmas = (0, leveys // 2, korkeus // 2 + 1, korkeus)
    neljas = (leveys // 2 + 1, leveys, korkeus // 2 + 1, korkeus)
    return [eka, toka, kolmas, neljas]

def sijoittele(paikat: list, leveys: int, korkeus: int) -> list:
    maarat = {i: 0 for i in range(4)}
    kvadrantit = laske_kvadrantit(leveys, korkeus)
    for paikka in paikat:
        for k in range(len(kvadrantit)):
            if paikka[0] in range(kvadrantit[k][0], kvadrantit[k][1]) and \
            paikka[1] in range(kvadrantit[k][2], kvadrantit[k][3]):
                maarat[k] += 1
                break
        # else:
        #     print("Robotille ei löytynyt sijoituspaikkaa :o")
    return maarat

robotit = lue("input.txt")
kierroksia = 100
leveys, korkeus = 101, 103


liikkuneet = [liikuta(robotti, kierroksia) for robotti in robotit]
korjatut = [korjaa(liikkunut, leveys, korkeus) for liikkunut in liikkuneet]
maarat = sijoittele(korjatut, leveys, korkeus)
turvallisuus = 1
for m in maarat.values():
    turvallisuus *= m

print(turvallisuus)
