def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        return f.readline().strip().split(" ")


print(avaa("alku.txt"))
