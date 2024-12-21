class Avaruusasema:
    def __init__(self, tiedosto: str):
        with open(tiedosto) as f:
            self.sarjat = [r.strip() for r in f.readlines()]
        self.
