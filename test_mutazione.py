from generatore import Generatore
from mutazione import Mutazione
from fitness import Fitness


# Creazione degli oggetti
generatore = Generatore()
mutazione = Mutazione()
fitness = Fitness()


# Generazione della melodia
melodia = generatore.genera_melodia()

print("===== MELODIA ORIGINALE =====")

melodia.visualizza()

print("\nFitness originale:",
      fitness.calcola_fitness(melodia))


# Applicazione della mutazione
mutazione.muta(melodia)

print("\n===== MELODIA DOPO LA MUTAZIONE =====")

melodia.visualizza()

print("\nFitness dopo la mutazione:",
      fitness.calcola_fitness(melodia))

print("\nNumero di note:", melodia.numero_note())

print("===== FINE TEST =====")
