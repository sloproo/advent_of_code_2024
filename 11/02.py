def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        # raaka = f.readline().strip().split(" ")
        return [int(kivi) for kivi in f.readline().strip().split(" ")]

def litista(lista: list) -> list:
    return [kohde for kohde in lista for kohde in lista]

def nollasta(kivi: int) -> int:
    assert kivi == 0
    return 1

def parill_pituudesta(kivi: int) -> list:
    kivi = str(kivi)
    assert len(kivi) % 2 == 0
    eka = kivi[:len(kivi) // 2]
    toka = kivi[len(kivi) // 2:]
    return [int(eka), int(toka)]

def jamasta(kivi:int) -> int:
    return kivi * 2024

def kierros(kivet: dict) -> dict:
    seuraava = {}
    for kivi in kivet:
        if kivi == 0:
            seuraava[1] = kivet[0]
        elif len(str(kivi)) % 2 == 0:
            for puolikas in parill_pituudesta(kivi):
                if puolikas in seuraava:
                    seuraava[puolikas] += kivet[kivi]
                else:
                    seuraava[puolikas] = kivet[kivi]
        else:
            if jamasta(kivi) in seuraava:
                seuraava[jamasta(kivi)] += kivet[kivi]
            else:
                seuraava[jamasta(kivi)] = kivet[kivi]

    return seuraava

kivet_lista = avaa("input.txt")
kivet = {}
for kivi in set(kivet_lista):
    kivet[kivi] = kivet_lista.count(kivi)

for i in range(75):
    kivet = kierros(kivet)
    yhteensa = sum(kivet.values())
    print(f"Se oli kierros {i+1}")
    print(f"Kiviä on yhteensä: {yhteensa}\n")
