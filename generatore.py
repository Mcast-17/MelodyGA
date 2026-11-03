import random

from config import NOTE_SCALA, DURATE_CONSENTITE, NUMERO_MINIMO_NOTE
from nota import Nota
from melodia import Melodia


class Generatore:

    def genera_nota(self):
        altezza = random.choice(NOTE_SCALA)
        ottava = random.randint(3, 5)
        durata = random.choice(DURATE_CONSENTITE)

        return Nota(altezza, ottava, durata)

    def genera_melodia(self):
        melodia = Melodia()

        for i in range(NUMERO_MINIMO_NOTE):
            nota = self.genera_nota()
            melodia.aggiungi_nota(nota)

        return melodia
