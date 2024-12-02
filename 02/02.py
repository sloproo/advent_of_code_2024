def turvallinen(suunta: str, eka: int, toka: int) -> bool:
    if suunta == "ylos":
        return 3 >= toka - eka >= 1
    elif suunta =="alas":
        return 3 >= eka - toka >= 1
    else:
        raise ValueError

def rullaa(suunta: str, raportti: list) -> tuple[bool, int]:
    for i in range(len(raportti) - 1):
        if not turvallinen(suunta, raportti[i], raportti[i+1]):
            return (False, i)
    else:
        return (True, 0)

turvallisia = 0

with open("input.txt") as f:
    for r in f:
        raportti = [int(luku) for luku in r.strip().split()]
        meni = False
        for suunta in ["ylos", "alas"]:
            meni, virhekohta = rullaa(suunta, raportti)
            if meni:
                turvallisia += 1
                break
            elif rullaa(suunta, raportti[:virhekohta] + raportti [virhekohta+1:])[0]:
                turvallisia += 1
                break
            elif rullaa(suunta, raportti[:virhekohta+1] + raportti [virhekohta+2:])[0]:
                turvallisia += 1
                break

print(turvallisia)
