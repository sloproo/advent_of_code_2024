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
    
sarjalla_rahaa = {}

for luku in apinoiden_alkuluvut:
    apinan_sarjat = {}
    apinan_hinnat = [luku % 10]
    for i in range(2000):
        luku = kierros(luku)
        apinan_hinnat.append((luku % 10, luku % 10 - apinan_hinnat[-1]))
        
        if i >= 3:
            sarja = (tuple([apinan_hinnat[x][1] for x in range(-4, 0)])
            if sarja not in apinan_sarjat:
                apinan_sarjat[sarja] = apinan_hinnat[-1][0]
    for sarja in apinan_sarjat:
        if sarja not in sarjalla_rahaa:
            sarjalla_rahaa[sarja] = apinan_sarjat[sarja]
        else:
            sarjalla_rahaa[sarja] += apinan_sarjat[sarja]

print(f"Apinojen hinnankehitykset ja sarjoilla saatavat rahat laskettu")
print(f"Aikaa kului {time.time() - alkuaika}")

print(f"Paras saalis on {max(sarjalla_rahaa.values())}
print(f"Aikaa kului {time.time() - alkuaika}")

pass



