ekat = []
tokat = []
with open("input.txt") as f:
    for r in f:
        jako = [int(luku) for luku in r.strip().split()]
        ekat.append(jako[0])
        tokat.append(jako[1])

samankaltaisuus = 0

for luku in ekat:
    samankaltaisuus += luku * tokat.count(luku)

print(samankaltaisuus)
