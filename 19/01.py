class Kylpyla:
    def __init__(self, tiedosto: str):
            with open(tiedosto) as f:
                self.pyyhkeet = f.readline().strip().split(", ")
                f.readline()
                self.asetelmat = [r.strip() for r in f]
            self.ratkaistut = {}
    
    def sopiiko(self, pyyhe: str, takana: str, haluttu: str) -> bool:
        return takana+pyyhe == haluttu[:len(takana+pyyhe)]
    
    def edista(self, haluttu: str, takana: str) -> int:
        osumia = 0
        for pyyhe in self.pyyhkeet:
            if self.sopiiko(pyyhe, takana, haluttu):
                if takana+pyyhe in self.ratkaistut:
                    osumia += self.ratkaistut[takana+pyyhe]
                elif takana + pyyhe == haluttu:
                    osumia += 1
                elif len(takana + pyyhe) >= len(haluttu) and takana + pyyhe != haluttu:
                    osumia += 0
                else:
                    osumia += self.edista(haluttu, takana+pyyhe)
        self.ratkaistut[takana] = osumia
        return osumia
    
    def ratkaise_kaikki(self):
        ratkeavia = 0
        for haluttu in self.asetelmat:
            self.ratkaistut = {}
            osumia = self.edista(haluttu, "")
            if osumia > 0:
                ratkeavia += 1
            print(f"{haluttu}: {osumia}")
        print(f"Yhteensä ratkenneita oli {ratkeavia}")

onsen = Kylpyla("input.txt")

onsen.ratkaise_kaikki()

pass
# 272 on liian matala
