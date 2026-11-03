from nota import Nota


class Melodia:

    def __init__(self):
        self.note = []

    # Aggiunge una nota alla melodia
    def aggiungi_nota(self, nota):
        if isinstance(nota, Nota):
            self.note.append(nota)
        else:
            raise TypeError("È possibile aggiungere solo oggetti Nota")

    # Rimuove una nota dalla melodia
    def rimuovi_nota(self, indice):
        if 0 <= indice < len(self.note):
            self.note.pop(indice)
        else:
            raise IndexError("Indice non valido")

    # Restituisce il numero di note
    def numero_note(self):
        return len(self.note)

    # Calcola la durata totale della melodia
    def durata_totale(self):
        return sum(nota.durata for nota in self.note)

    # Visualizza tutte le note
    def visualizza(self):
        for indice, nota in enumerate(self.note, start=1):
            print(f"{indice}. {nota}")

    # Restituisce una rappresentazione della melodia
    def str(self):
        return " | ".join(str(nota) for nota in self.note)
