## Mutazione – Algoritmo genetico

## Descrizione:
Il modulo "mutazione.py" implementa l'operatore genetico di mutazione.
La mutazione introduce modifiche casuali nelle caratteristiche delle note musicali di una melodia, contribuendo a mantenere la diversità genetica della popolazione.
Questo meccanismo permette all'algoritmo di esplorare nuove soluzioni musicali e riduce il rischio di convergere prematuramente verso soluzioni poco soddisfacenti.

## Funzionamento:
Il programma analizza tutte le note che compongono una melodia.
Per ogni nota viene generato un valore casuale, confrontato con la probabilità di mutazione definita nel file "config.py".
Se la condizione viene soddisfatta, viene selezionata casualmente una caratteristica da modificare.

## Caratteristiche modificabili:
La mutazione può intervenire su tre proprietà della classe "Nota":
- Altezza: viene scelta una nuova nota appartenente alla scala musicale definita.
- Ottava: viene assegnata casualmente un'ottava compresa tra 3 e 5.
- Durata: viene scelta una nuova durata tra quelle consentite.
Le modifiche rispettano quindi i parametri musicali definiti nella configurazione del progetto.

## Probabilità di mutazione:
Il parametro "PROBABILITA_MUTAZIONE" è definito in "config.py".
Il valore iniziale utilizzato è: "PROBABILITA_MUTAZIONE = 0.10"
Questo significa che ogni nota ha il 10% di probabilità di essere selezionata per una mutazione.
La probabilità viene applicata individualmente a ciascuna nota della melodia.

## Struttura del modulo:
La classe "Mutazione" contiene il metodo:
- "muta()": analizza le note della melodia e applica eventuali modifiche casuali alle loro caratteristiche.
Il metodo modifica direttamente la melodia ricevuta e restituisce lo stesso oggetto aggiornato.

## Tecnologie utilizzate:
- Python
- Modulo standard "random"
- Classe "Nota" per la rappresentazione delle note musicali.
- Classe "Melodia" per la gestione delle sequenze.
- Modulo "config.py" per il recupero dei parametri musicali.

## Integrazione nell'algoritmo genetico:
La mutazione viene applicata ai nuovi individui generati attraverso il crossover.
Dopo la modifica, le melodie possono essere nuovamente valutate attraverso la funzione di fitness.
Questo processo contribuisce all'evoluzione della popolazione e alla ricerca di melodie che rispettino sempre meglio i criteri musicali definiti.

## Obiettivo:
Introdurre variabilità nelle melodie generate, permettendo all'algoritmo genetico di esplorare nuove combinazioni di note, altezze e durate.