turvallisia = 0

def turvallinen(suunta: str, eka: int, toka: int) -> bool:
    if suunta == "ylos":
        return 3 >= toka - eka >= 1
    elif suunta =="alas":
        return 3 >= eka - toka >= 1
    else:
        raise ValueError

def rullaa(raportti: list, suunta: str) -> bool:
    for i in range(len(raportti) -1):
        if turvallinen(suunta, raportti[i], raportti[i+1]):
            continue
        elif suoja:
            suoja = False
            if rullaa(raportti[:i] + raportti[i+1:], suunta, suoja):
                return True
            elif rullaa(raportti[:i+1] + raportti[i+2:], suunta, suoja):
                return True
        else:
            return False
    else:
        return True



with open("alku.txt") as f:
    for r in f:
        raportti = [int(luku) for luku in r.strip().split()]
        suoja = True
        
        for suunta in ["ylos", "alas"]:
            suoja = True
            if rullaa(raportti, suunta, suoja):
                turvallisia += 1
                break
            else:
                if not suoja:
                    break
                else:
                    suoja = False
            
            

print(turvallisia)

