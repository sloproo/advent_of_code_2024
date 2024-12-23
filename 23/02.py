import itertools
import time

alkuaika = time.time()

def lue(tiedosto: str) -> dict:
    with open(tiedosto) as f:
        koneet = {}
        for r in f:
            eka, toka = r.strip().split("-")
            if eka in koneet:
                koneet[eka].append(toka)
            else:
                koneet[eka] = [toka]
            if toka in koneet:
                koneet[toka].append(eka)
            else:
                koneet[toka] = [eka]
        return koneet
    
koneet = lue("input.txt")



