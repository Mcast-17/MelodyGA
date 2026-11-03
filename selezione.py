import random

from fitness import Fitness


class Selezione:

    def __init__(self, dimensione_torneo=3):
        self.fitness = Fitness()
        self.dimensione_torneo = dimensione_torneo

    def seleziona(self, popolazione):

        if len(popolazione.melodie) == 0:
            raise ValueError("La popolazione è vuota")

        partecipanti = random.sample(
            popolazione.melodie,
            min(self.dimensione_torneo, len(popolazione.melodie))
        )

        vincitore = max(
            partecipanti,
            key=self.fitness.calcola_fitness
        )

        return vincitore
