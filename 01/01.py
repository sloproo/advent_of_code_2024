ekat = []
tokat = []
with open("input.txt") as f:
    for r in f:
        jako = [int(luku) for luku in r.strip().split()]
        ekat.append(jako[0])
        tokat.append(jako[1])

ekat.sort()
tokat.sort()

etaisyydet = 0

for i in range(len(ekat)):
    etaisyydet += abs(ekat[i] - tokat[i])

print(etaisyydet)
