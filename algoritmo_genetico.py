import random
from copy import deepcopy

from config import (
    DIMENSIONE_POPOLAZIONE,
    NUMERO_GENERAZIONI,
    PROBABILITA_CORSSOVER
)

from generatore import Generatore
from fitness import Fitness
from selezione import Selezione
from crossover import Crossover
from mutazione import Mutazione
from popolazione import Popolazione


class AlgoritmoGenetico:

    def __init__(self):

        # Parametri dell'algoritmo
        self.dimensione_popolazione = DIMENSIONE_POPOLAZIONE
        self.numero_generazioni = NUMERO_GENERAZIONI
        self.probabilita_crossover = PROBABILITA_CORSSOVER

        # Inizializzazione dei componenti
        self.generatore = Generatore()
        self.fitness = Fitness()
        self.selezione = Selezione()
        self.crossover = Crossover()
        self.mutazione = Mutazione()

        # Popolazione iniziale
        self.popolazione = Popolazione()

        # Migliore melodia trovata
        self.migliore_melodia = None
        self.migliore_fitness = float("-inf")

    def inizializza_popolazione(self):

        self.popolazione = Popolazione()

        for _ in range(self.dimensione_popolazione):
            melodia = self.generatore.genera_melodia()
            self.popolazione.aggiungi_melodia(melodia)

    def trova_migliore(self):

        if len(self.popolazione.melodie) == 0:
            return None

        migliore = max(
            self.popolazione.melodie,
            key=self.fitness.calcola_fitness
        )

        return migliore

    def aggiorna_migliore(self):

        migliore_corrente = self.trova_migliore()

        if migliore_corrente is None:
            return

        punteggio = self.fitness.calcola_fitness(
            migliore_corrente
        )

        if punteggio > self.migliore_fitness:
            self.migliore_fitness = punteggio
            self.migliore_melodia = deepcopy(
                migliore_corrente
            )

    def crea_nuova_generazione(self):

        nuova_popolazione = Popolazione()

        # Elitismo: conserviamo la migliore melodia
        elite = deepcopy(self.trova_migliore())

        if elite is not None:
            nuova_popolazione.aggiungi_melodia(elite)

        # Creazione dei nuovi individui
        while (
            len(nuova_popolazione.melodie)
            < self.dimensione_popolazione
        ):

            # Selezione dei genitori
            genitore1 = self.selezione.seleziona(
                self.popolazione
            )

            genitore2 = self.selezione.seleziona(
                self.popolazione
            )

            # Crossover oppure copia dei genitori
            if random.random() < self.probabilita_crossover:

                figlio1, figlio2 = self.crossover.incrocia(
                    genitore1,
                    genitore2
                )

            else:
                figlio1 = deepcopy(genitore1)
                figlio2 = deepcopy(genitore2)

            # Mutazione dei figli
            self.mutazione.muta(figlio1)
            self.mutazione.muta(figlio2)

            # Inserimento nella nuova popolazione
            nuova_popolazione.aggiungi_melodia(figlio1)

            if (
                len(nuova_popolazione.melodie)
                < self.dimensione_popolazione
            ):
                nuova_popolazione.aggiungi_melodia(figlio2)

        self.popolazione = nuova_popolazione

    def esegui(self):

        # Creazione della popolazione iniziale
        self.inizializza_popolazione()

        print("===== AVVIO ALGORITMO GENETICO =====")
        print(
            "Popolazione iniziale:",
            self.dimensione_popolazione
        )
        print(
            "Numero di generazioni:",
            self.numero_generazioni
        )

        # Evoluzione della popolazione
        for generazione in range(1, self.numero_generazioni + 1):

            # Aggiornamento del miglior individuo
            self.aggiorna_migliore()

            # Creazione della generazione successiva
            self.crea_nuova_generazione()

            # Visualizzazione dei progressi
            if generazione % 10 == 0:
                print(
                    f"Generazione {generazione}: "
                    f"migliore fitness = "
                    f"{self.migliore_fitness}"
                )

        # Controllo anche dell'ultima popolazione
        self.aggiorna_migliore()

        print("\n===== ALGORITMO TERMINATO =====")
        print("Migliore fitness:", self.migliore_fitness)

        return self.migliore_melodia
