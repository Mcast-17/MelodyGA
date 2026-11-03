class Nota:

    def __init__(self, altezza, ottava, durata):
        self.altezza = altezza
        self.ottava = ottava
        self.durata = durata

    def __str__(self):
        return f"{self.altezza}{self.ottava} - Durata: {self.durata}"

    def get_altezza(self):
        return self.altezza

    def get_ottava(self):
        return self.ottava

    def get_durata(self):
        return self.durata
