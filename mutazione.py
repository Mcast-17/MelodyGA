import random

from config import (
    NOTE_SCALA,
    DURATE_CONSENTITE,
    PROBABILITA_MUTAZIONE
)


class Mutazione:

    def muta(self, melodia):

        for nota in melodia.note:

            if random.random() < PROBABILITA_MUTAZIONE:

                caratteristica = random.choice([
                    "altezza",
                    "ottava",
                    "durata"
                ])

                if caratteristica == "altezza":
                    nota.altezza = random.choice(NOTE_SCALA)

                elif caratteristica == "ottava":
                    nota.ottava = random.randint(3, 5)

                elif caratteristica == "durata":
                    nota.durata = random.choice(DURATE_CONSENTITE)

        return melodia
