ruudukko = []

with open("alku.txt") as f:
    for r in f:
        rivi = [kirjain for kirjain in r.strip().split()]
        print(rivi)
    
