import re

with open("input.txt") as f:
    datarivit = f.readlines()
    data = "".join(datarivit)

data_siistitty = re.sub(r"don\'t\(\).*?do\(\)", "", data, flags=re.DOTALL)
# Kopioitu: instruction = re.sub(r"don't\(\).*?($|do\(\))", '', instruction, flags=re.DOTALL)

laskut = re.findall(r"mul\(\d{1,3}\,\d{1,3}\)", data_siistitty)

summa = 0

for lasku in laskut:
    kerrottavat = [int(luku) for luku in re.findall("\d{1,3}", lasku)]
    summa += kerrottavat[0] * kerrottavat[1]

print(data_siistitty)
print(summa)




    
# Aiemmalla tuli vastaukseksi 72147484 ja se on liian pieni
# Nyt tulee 179571322 eli se ei sensuroi mitään

# Manuaalisesti siistimällä tuli 70917760, liian pieni
# Ja sitten taas joka on liian korkea 105264641
# 105264641
# 178341598

