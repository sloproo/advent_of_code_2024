def avaa(tiedosto: str) -> list:
  with open(tiedosto) as f:
    return [merkki for r in f for merkki in r.strip()]

def sisalla(x: int, y: int, ruudukko: list) -> bool:
  if x < 0 or y < 0 or y >= len(ruudukko) or x >= len(ruudukko[y]):
    return False
  else:
    return True

def naapurit(x: int, y: int, ruudukko: list) -> list:
  return [(xn, yn) for xn, yn in [(x, y-1), (x+1, y), (x, y+1), x-1, y)] if sisalla(xn, yn, ruudukko)]

kartta = avaa("alku.txt")

