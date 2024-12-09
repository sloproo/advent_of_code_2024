def lue(tiedosto: str) -> str:
    with open(tiedosto) as f:
        return f.readline().strip()
    
def viimeinen(lista: list) -> int:
    for i in range(len(lista) -1, -1, -1):
        if lista[i] != ".":
            return i
        
def tarkistussumma(lista: list) -> int:
    palautettava = 0
    for i in range(len(lista)):
        if lista[i] == ".":
            continue
        palautettava += i * lista[i]
    return palautettava

def tulosta(lista: list) -> None:
    for m in levykuva:
        print(m, end="")
    print()

def tulosta_ruju(lista: list) -> None:
    for m in levykuva:
        if m != ".":
            print("X", end="")
        else:
            print(m, end="")
    print()

levy = lue("input.txt")

sekaisin = []
tyhjia = []

for i in range(len(levy)):
    if i % 2 == 0:
        sekaisin.append(int(levy[i]))
    else:
        tyhjia.append(int(levy[i]))

levykuva = []

for i in range(len(sekaisin)):
    for _ in range(sekaisin[i]):
        levykuva.append(i)
    if i < len(tyhjia):
        for _ in range(tyhjia[i]):
            levykuva.append(".")

haussa = len(sekaisin) -1
aloituskohta = len(levykuva) - 1
while haussa > 0:
    loytyi = False
    for i in range(aloituskohta, -1, -1):
        if not loytyi:
            if levykuva[i] == haussa:
                loytyi = True
                loppu = i
        else:
            if levykuva[i] != haussa:
                alku = i + 1
                break
    pituus = loppu - alku + 1

    for i in range(alku - (pituus - 1)): # Tästä puuttui sulut pituus - 1 :n ympäriltä ja se kusi
        if levykuva[i:i+pituus] == ["."] * pituus:
            levykuva[i:i+pituus], levykuva[alku:loppu+1] = levykuva[alku:loppu+1], levykuva[i:i+pituus]
            # tulosta(levykuva)
            break
        else:
            continue
    haussa -= 1
    aloituskohta = alku
    if haussa % 500 == 0:
        print(f"haussa = {haussa}")

# print(levykuva)


print(tarkistussumma(levykuva))

# liian korkea = 6239783431260
