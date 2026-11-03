from algoritmo_genetico import AlgoritmoGenetico
from config import (
    NOTE_SCALA,
    DURATE_CONSENTITE,
    NUMERO_MINIMO_NOTE,
    MAX_SALTI_OTTAVA_CONSECUTIVI
)
from fitness import VALORI_NOTE


def verifica_melodia(melodia):

    errori = []

    # Controllo numero minimo di note
    if melodia.numero_note() < NUMERO_MINIMO_NOTE:
        errori.append("Numero di note insufficiente")

    # Controllo tonalità
    for nota in melodia.note:
        if nota.altezza not in NOTE_SCALA:
            errori.append("Nota fuori tonalità")
            break

    # Controllo durate
    for nota in melodia.note:
        if nota.durata not in DURATE_CONSENTITE:
            errori.append("Durata non consentita")
            break

    # Controllo salti d'ottava consecutivi
    salti_consecutivi = 0

    for i in range(1, len(melodia.note)):

        precedente = melodia.note[i - 1]
        corrente = melodia.note[i]

        altezza_precedente = (
            precedente.ottava * 12
            + VALORI_NOTE[precedente.altezza]
        )

        altezza_corrente = (
            corrente.ottava * 12
            + VALORI_NOTE[corrente.altezza]
        )

        intervallo = abs(
            altezza_corrente - altezza_precedente
        )

        if intervallo >= 12:
            salti_consecutivi += 1
        else:
            salti_consecutivi = 0

        if salti_consecutivi > MAX_SALTI_OTTAVA_CONSECUTIVI:
            errori.append("Troppi salti d'ottava consecutivi")
            break

    return errori


# Avvio dell'algoritmo genetico
algoritmo = AlgoritmoGenetico()
algoritmo.esegui()

# Controllo della popolazione finale
print("\n===== VERIFICA DEI VINCOLI =====")

popolazione = algoritmo.popolazione.melodie

melodie_valide = 0
melodie_non_valide = 0

for indice, melodia in enumerate(popolazione, start=1):

    errori = verifica_melodia(melodia)

    if len(errori) == 0:
        melodie_valide += 1
        print(f"Melodia {indice}: VALIDA")

    else:
        melodie_non_valide += 1
        print(f"Melodia {indice}: NON VALIDA")

        for errore in errori:
            print("  -", errore)


print("\n===== RISULTATO FINALE =====")

print("Melodie totali:", len(popolazione))
print("Melodie valide:", melodie_valide)
print("Melodie non valide:", melodie_non_valide)

if melodie_non_valide == 0:
    print("\nTUTTI I VINCOLI SONO RISPETTATI!")
else:
    print("\nSONO PRESENTI MELODIE NON VALIDE!")
