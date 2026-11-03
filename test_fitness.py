from generatore import Generatore
from fitness import Fitness


generatore = Generatore()
fitness = Fitness()

# Generazione di una melodia casuale
melodia = generatore.genera_melodia()

# Calcolo della fitness
punteggio = fitness.calcola_fitness(melodia)

print("===== VALUTAZIONE MELODIA =====")

melodia.visualizza()

print("\nPunteggio tonalità:",
      fitness.valuta_tonalita(melodia))

print("Punteggio ripetizione:",
      fitness.valuta_ripetizione(melodia))

print("Punteggio salti di ottava:",
      fitness.valuta_salti_ottava(melodia))

print("Punteggio lunghezza:",
      fitness.valuta_lunghezza(melodia))

print("\nFITNESS TOTALE:", punteggio, "/ 100")

print("===== FINE TEST =====")
