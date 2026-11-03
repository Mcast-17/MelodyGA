import random

from melodia import Melodia
from nota import Nota
from config import NUMERO_MINIMO_NOTE


class Crossover:

    def incrocia(self, genitore1, genitore2):

        numero_note1 = genitore1.numero_note()
        numero_note2 = genitore2.numero_note()

        if numero_note1 != numero_note2:
            raise ValueError(
                "Le melodie devono avere la stessa lunghezza"
            )

        if numero_note1 < NUMERO_MINIMO_NOTE:
            raise ValueError(
                "Le melodie non rispettano il numero minimo di note"
            )

        punto_taglio = random.randint(1, numero_note1 - 1)

        figlio1 = Melodia()
        figlio2 = Melodia()

        # Creazione del primo figlio
        for nota in genitore1.note[:punto_taglio]:
            figlio1.aggiungi_nota(
                Nota(nota.altezza, nota.ottava, nota.durata)
            )

        for nota in genitore2.note[punto_taglio:]:
            figlio1.aggiungi_nota(
                Nota(nota.altezza, nota.ottava, nota.durata)
            )

        # Creazione del secondo figlio
        for nota in genitore2.note[:punto_taglio]:
            figlio2.aggiungi_nota(
                Nota(nota.altezza, nota.ottava, nota.durata)
            )

        for nota in genitore1.note[punto_taglio:]:
            figlio2.aggiungi_nota(
                Nota(nota.altezza, nota.ottava, nota.durata)
            )

        return figlio1, figlio2
