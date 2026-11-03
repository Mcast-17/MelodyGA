from collections import Counter

from config import NOTE_SCALA, NUMERO_MINIMO_NOTE


# Valore delle note musicali espresso in semitoni
VALORI_NOTE = {
    "Do": 0,
    "Re": 2,
    "Mi": 4,
    "Fa": 5,
    "Sol": 7,
    "La": 9,
    "Si": 11
}


class Fitness:

    # Valutazione della tonalità (35 punti)
    def valuta_tonalita(self, melodia):

        if melodia.numero_note() == 0:
            return 0

        note_corrette = sum(
            1 for nota in melodia.note
            if nota.altezza in NOTE_SCALA
        )

        percentuale = (
            note_corrette / melodia.numero_note()
        )

        return round(percentuale * 35, 2)

    # Valutazione della ripetizione melodica (25 punti)
    def valuta_ripetizione(self, melodia):

        if melodia.numero_note() < 3:
            return 0

        motivi = []

        for i in range(len(melodia.note) - 2):

            motivo = tuple(
                nota.altezza
                for nota in melodia.note[i:i + 3]
            )

            motivi.append(motivo)

        conteggi = Counter(motivi)

        ripetizioni = sum(
            conteggio - 1
            for conteggio in conteggi.values()
        )

        totale_motivi = len(motivi)

        rapporto = ripetizioni / totale_motivi

        if rapporto == 0:
            punteggio = 0
        elif rapporto <= 0.10:
            punteggio = 25
        elif rapporto <= 0.25:
            punteggio = 20
        elif rapporto <= 0.40:
            punteggio = 15
        elif rapporto <= 0.60:
            punteggio = 8
        else:
            punteggio = 0

        return punteggio

    # Valutazione dei salti d'ottava (30 punti)
    def valuta_salti_ottava(self, melodia):

        salti_consecutivi = 0
        massimo_salti = 0
        numero_salti = 0

        for i in range(1, len(melodia.note)):

            nota_precedente = melodia.note[i - 1]
            nota_corrente = melodia.note[i]

            altezza_precedente = (
                nota_precedente.ottava * 12
                + VALORI_NOTE[nota_precedente.altezza]
            )

            altezza_corrente = (
                nota_corrente.ottava * 12
                + VALORI_NOTE[nota_corrente.altezza]
            )

            intervallo = abs(
                altezza_corrente - altezza_precedente
            )

            if intervallo >= 12:
                salti_consecutivi += 1
                numero_salti += 1
            else:
                salti_consecutivi = 0

            massimo_salti = max(
                massimo_salti,
                salti_consecutivi
            )

        # Penalità se vengono superati tre salti consecutivi
        if massimo_salti > 3:
            return 0

        # Premiamo melodie con pochi salti e senza sequenze eccessive
        if numero_salti == 0:
            return 30
        elif numero_salti <= 3:
            return 25
        elif numero_salti <= 6:
            return 20
        else:
            return 15

    # Valutazione della lunghezza (10 punti)
    def valuta_lunghezza(self, melodia):

        if melodia.numero_note() >= NUMERO_MINIMO_NOTE:
            return 10

        return 0

    # Calcolo del punteggio complessivo
    def calcola_fitness(self, melodia):

        punteggio = (
            self.valuta_tonalita(melodia)
            + self.valuta_ripetizione(melodia)
            + self.valuta_salti_ottava(melodia)
            + self.valuta_lunghezza(melodia)
        )

        return round(punteggio, 2)