def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        # raaka = f.readline().strip().split(" ")
        return [int(kivi) for kivi in f.readline().strip().split(" ")]

def litista(lista: list) -> list:
    return [kohde for kohde in lista for kohde in lista]

def nollasta(kivi: int) -> int:
    assert kivi == 0
    return 1

def parill_pituus(kivi: int) -> list:
    kivi = str(kivi)
    assert len(kivi) % 2 == 0
    eka = kivi[:len(kivi) // 2]
    toka = kivi[len(kivi) // 2:]
    return [int(eka), int(toka)]

def jama(kivi:int) -> int:
    return kivi * 2024

def kierros(kivet: list) -> list:
    seuraava = []
    for kivi in kivet:
        if kivi == 0:
            seuraava.append(nollasta(kivi))
        elif len(str(kivi)) % 2 == 0:
            seuraava += parill_pituus(kivi)
        else:
            seuraava.append(jama(kivi))
    return seuraava

    



kivet = avaa("input.txt")
print(kivet)
for i in range(25):
    kivet = kierros(kivet)
    print(len(kivet))
    
