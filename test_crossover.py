from generatore import Generatore
from crossover import Crossover
from fitness import Fitness


# Creazione degli oggetti
generatore = Generatore()
crossover = Crossover()
fitness = Fitness()


# Generazione dei due genitori
genitore1 = generatore.genera_melodia()
genitore2 = generatore.genera_melodia()


# Operazione di crossover
figlio1, figlio2 = crossover.incrocia(
    genitore1,
    genitore2
)


# Visualizzazione dei risultati
print("===== GENITORE 1 =====")
genitore1.visualizza()

print("\n===== GENITORE 2 =====")
genitore2.visualizza()

print("\n===== FIGLIO 1 =====")
figlio1.visualizza()

print("\n===== FIGLIO 2 =====")
figlio2.visualizza()


# Valutazione dei figli
print("\n===== FITNESS FIGLI =====")

print("Fitness figlio 1:",
      fitness.calcola_fitness(figlio1))

print("Fitness figlio 2:",
      fitness.calcola_fitness(figlio2))


print("\nNumero note figlio 1:", figlio1.numero_note())
print("Numero note figlio 2:", figlio2.numero_note())

print("\n===== FINE TEST =====")
