turvallisia = 0

def turvallinen(suunta: str, eka: int, toka: int) -> bool:
    if suunta == "ylos":
        return 3 >= toka - eka >= 1
    else:
        return 3 >= eka - toka >= 1


with open("input.txt") as f:
    for r in f:
        raportti = [int(luku) for luku in r.strip().split()]
        if raportti[1] > raportti[0]:
            suunta = "ylos"
        elif raportti[1] < raportti[0]:
            suunta = "alas"
        else:
            continue
        for i in range(len(raportti) - 1):
            if not turvallinen(suunta, raportti[i], raportti[i+1]):
                break
        else:
            turvallisia += 1

print(turvallisia)

