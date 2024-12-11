# tässä tehtävässä kivijonoon tulee uusilla kierroksilla uusia 2024:sia ja ne kehittyvät seuraavilla kierroksilla säännönmukaisesti.
# Samalla tavalla mekaanisen ennaltasäädetysti kehittyy 1.

def avaa(tiedosto: str) -> list:
    with open(tiedosto) as f:
        return f.readline().strip().split(" ")


print(avaa("alku.txt"))
