import math

def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        return f.readline().strip().split(" ")

def litista(lista: list) -> list:
    return [kohde for kohde in lista for kohde in lista]

def nollasta(kivi: int) -> int:
    assert kivi == 0
    return 1

def pari_log(kivi: int) -> tuple[int, int]:
    assert len(str(kivi)) % 0
    



print(avaa("alku.txt"))
