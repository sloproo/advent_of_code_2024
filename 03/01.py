import re

with open("input.txt") as f:
    datarivit = f.readlines()
    data = "".join(datarivit)
laskut = re.findall("mul\(\d{1,3}\,\d{1,3}\)", data)

summa = 0

for lasku in laskut:
    kerrottavat = [int(luku) for luku in re.findall("\d{1,3}", lasku)]
    summa += kerrottavat[0] * kerrottavat[1]

print(summa)
    

