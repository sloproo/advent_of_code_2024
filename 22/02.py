import itertools
import time

alkuaika = time.time()

def lue(tiedosto :str) -> list:
    with open(tiedosto) as f:
        return [int(r) for r in f.readlines()]

apinoiden_alkuluvut = lue("input.txt")

def kierros(luku: int) -> int:
    pitka = 16777216
    a = (luku * 64 ^ luku) % pitka
    b = (a // 32 ^ a) % pitka
    c = (b * 2048 ^ b) % pitka
    return c

def sopiiko_muutos(hinnat: list, muutokset: list) -> int:
    for i in range(4):
        if hinnat[-4+i] - hinnat[-5+i] != muutokset[i]:
            return -999
    else:
        return hinnat[-1]
    
hinnat = []
hinnan_muutokset = []
kaikki_jaksot = set()

for luku in apinoiden_alkuluvut:
    tyohinnat = []
    tyomuutokset = []
    nollahinta = luku % 10
    for i in range(2000):
        luku = kierros(luku)
        tyohinnat.append(luku % 10)
        if i == 0:
            tyomuutokset.append(tyohinnat[-1] - nollahinta)
        else:
            tyomuutokset.append(tyohinnat[-1] - tyohinnat[-2])
        if i >= 3:
            kaikki_jaksot.add(tuple(tyomuutokset[-4:]))
    hinnat.append(tyohinnat)
    hinnan_muutokset.append(tyomuutokset)

print(len(kaikki_jaksot))
print(f"Aikaa kului {time.time() - alkuaika}")


paras_saalis = 0
laskuri = 0

for jakso in kaikki_jaksot:
    jakson_saalis = 0
    for apina_nro in range(len(hinnat)):
        jakso_str = "".join([str(x) for x in jakso])
        muutokset_str = "".join([str(x) for x in hinnan_muutokset[apina_nro]])
        if jakso_str in muutokset_str:
            jakso_list = list(jakso)
            for i in range(len(hinnan_muutokset[apina_nro]) - 4):
                if jakso_list == hinnan_muutokset[apina_nro][i:i+4]:
                    jakson_saalis += hinnat[apina_nro][i+3]
                    break
    paras_saalis = max(paras_saalis, jakson_saalis)
    laskuri += 1
    print(laskuri)

print(paras_saalis)
print(f"Aikaa kului {time.time() - alkuaika}")

pass



