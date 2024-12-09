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
            break
        palautettava += i * lista[i]
    return palautettava


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

# for m in sotkukuva:
#     print(m, end="")


pass
for i in range(len(levykuva)):
    if levykuva[i] == ".":
        vikan_i = viimeinen(levykuva)
        if vikan_i < i:
            break
        levykuva[i], levykuva[vikan_i] = levykuva[vikan_i], levykuva[i]

# print(levykuva)

print(tarkistussumma(levykuva))
