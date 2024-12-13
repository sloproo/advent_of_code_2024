def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        yhtalot = []
        while True:
            ekat = tuple([int(liike[2:]) for liike in f.readline().split(":")[1].strip().split(", ")])
            tokat = tuple([int(liike[2:]) for liike in f.readline().split(":")[1].strip().split(", ")])
            maali = tuple([int(liike[2:]) for liike in f.readline().split(":")[1].strip().split(", ")])
            yhtalot.append(tuple([(ekat[i], tokat[i], maali[i]) for i in range(2)]))
            if not f.readline():
                break
        return yhtalot
    
def ratkaise(yhtalopari: tuple) -> tuple[int, int]:
    eka, toka = yhtalopari
    ekax = tuple([luku * toka[0] for luku in eka])
    tokax = tuple([luku * eka[0] for luku in toka])
    erotus = (ekax[0] - tokax[0], ekax[1] - tokax[1], ekax[2] - tokax[2])
    assert erotus[0] == 0
    if erotus[2] % erotus[1] != 0:
        print("ei ratkea tasan")
        return (0, 0)
    else:
        b = erotus[2] // erotus[1]
        if (eka[2] - eka[1] * b) % eka[0] != 0:
            print("Ei ratkea tasan")
            return (0, 0)
        else:
            return((eka[2] - eka[1] * b) // eka[0], b)

yhtalot = avaa("input.txt")

hinta = 0
for yhtalo in yhtalot:
    ratkaisu = ratkaise(yhtalo)
    if ratkaisu != (0, 0):
        hinta += 3 * ratkaisu[0] + ratkaisu[1]
    if ratkaisu[0] > 100 or ratkaisu[1] > 100:
        raise ValueError
    
print(hinta)
