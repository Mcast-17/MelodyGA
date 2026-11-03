## Selezione – Algoritmo genetico

## Descrizione:
Il modulo "selezione.py" implementa il meccanismo di selezione degli individui all'interno dell'algoritmo genetico.
Il suo compito è individuare le melodie con i punteggi di fitness più elevati, affinché possano essere utilizzate come genitori nella creazione della generazione successiva.
La selezione permette di favorire le soluzioni che rispettano maggiormente i criteri musicali definiti nel progetto.

## Metodo utilizzato: Tournament Selection
Il progetto utilizza la tecnica della selezione a torneo.
Questo metodo prevede il confronto tra un gruppo di individui scelti casualmente dalla popolazione.
Il procedimento si articola nelle seguenti fasi:
1. Vengono estratte casualmente alcune melodie dalla popolazione.
2. Per ogni melodia viene calcolato il punteggio di fitness.
3. I punteggi vengono confrontati.
4. La melodia con il punteggio più alto viene selezionata come vincitrice del torneo.
5. Il procedimento può essere ripetuto per selezionare altri individui.

## Funzionamento
La selezione utilizza la funzione di fitness implementata nel modulo "fitness.py".
Ogni individuo viene valutato attraverso i criteri musicali previsti:

- Rispetto della tonalità.
- Ripetizione equilibrata delle sequenze musicali.
- Rispetto del limite dei salti di ottava consecutivi.
- Presenza del numero minimo di note.

La melodia con il punteggio maggiore viene scelta come genitore.

## Parametri principali
Il metodo utilizza principalmente:
- Popolazione: insieme delle melodie candidate.
- Dimensione del torneo: numero di melodie confrontate durante ogni torneo.
- Fitness: punteggio assegnato a ciascuna melodia.

La dimensione del torneo influenza il livello di selettività dell'algoritmo: aumentando il numero di partecipanti, aumenta la pressione verso gli individui con fitness elevata.

## Vantaggi del metodo
La selezione a torneo presenta diversi vantaggi:
- È semplice da implementare.
- Non richiede la normalizzazione dei punteggi di fitness.
- Permette di confrontare direttamente le melodie.
- Consente di regolare la pressione selettiva modificando la dimensione del torneo.

## Integrazione nell'algoritmo genetico
La selezione rappresenta una fase fondamentale del ciclo evolutivo.
Gli individui selezionati verranno utilizzati nelle successive operazioni genetiche:
- Crossover: combinazione di due melodie per generare nuovi individui.
- Mutazione: modifica casuale di alcune caratteristiche delle melodie.
L'obiettivo è migliorare progressivamente la qualità delle soluzioni attraverso le generazioni.