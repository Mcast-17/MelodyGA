from melodia import Melodia

class Popolazione:

    def __init__(self):
        self.melodie = []

    def aggiungi_melodia(self,melodia):
        if isinstance(melodia,Melodia):
            self.melodie.append(melodia)

        else:
            raise TypeError("E' possibile aggiungere solo oggetti Melodia")

    def numero_melodie(self):
        return len(self.melodie)

    def visualizza(self):
        for indice,melodia in enumerate(self.melodie,start=1):
            print(f"Melodia{indice}:")
            melodia.visualizza()

print("------------------")
