from generatore import Generatore
from popolazione import Popolazione
from selezione import Selezione
from fitness import Fitness


# Creazione degli oggetti
generatore = Generatore()
popolazione = Popolazione()
selezione = Selezione()
fitness = Fitness()


# Generazione di 10 melodie casuali
for i in range(10):
    melodia = generatore.genera_melodia()
    popolazione.aggiungi_melodia(melodia)


# Selezione della melodia vincitrice
vincitore = selezione.seleziona(popolazione)


# Visualizzazione dei risultati
print("===== SELEZIONE A TORNEO =====")

print("Melodie presenti:", popolazione.numero_melodie())

print("\nMelodia selezionata:")
vincitore.visualizza()

print("\nFitness della melodia selezionata:",
      fitness.calcola_fitness(vincitore))

print("===== FINE TEST =====")
