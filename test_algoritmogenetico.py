from algoritmo_genetico import AlgoritmoGenetico
from fitness import Fitness


# Creazione dell'algoritmo
algoritmo = AlgoritmoGenetico()

# Avvio dell'algoritmo genetico
migliore_melodia = algoritmo.esegui()

# Visualizzazione del risultato
print("\n===== MIGLIORE MELODIA TROVATA =====")

migliore_melodia.visualizza()

# Verifica del risultato
fitness = Fitness()

print(
    "\nFitness finale:",
    fitness.calcola_fitness(migliore_melodia)
)

print(
    "Numero di note:",
    migliore_melodia.numero_note()
)

print("\n===== FINE TEST =====")
