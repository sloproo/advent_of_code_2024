turvallisia = 0

def turvallinen(suunta: str, eka: int, toka: int) -> bool:
    if suunta == "ylos":
        return 3 >= toka - eka >= 1
    else:
        return 3 >= eka - toka >= 1
    
def hae_suunta(raportti: list) -> str:
    if raportti[1] > raportti[0]:
        return "ylos"
    elif raportti[1] < raportti[0]:
        return "alas"
    else:
        return "rikki"


with open("input.txt") as f:
    for r in f:
        raportti = [int(luku) for luku in r.strip().split()]
        suunta = hae_suunta(raportti)
        if suunta == "rikki":
            continue
        for i in range(len(raportti) - 1):
            if not turvallinen(suunta, raportti[i], raportti[i+1]):
                break
        else:
            turvallisia += 1

print(turvallisia)

