## Crossover – Algoritmo genetico

## Descrizione:
Il modulo "crossover.py" implementa l'operatore di crossover, una delle operazioni fondamentali degli algoritmi genetici.
Il suo compito è combinare due individui della popolazione, chiamati genitori, per generare nuove soluzioni, chiamate figli o discendenti.
Nel progetto, gli individui sono rappresentati da sequenze di note musicali, ovvero melodie.

## Metodo utilizzato: Single-Point Crossover:
Il progetto utilizza il crossover a punto singolo (Single-Point Crossover).
Questa tecnica prevede la scelta casuale di un punto di taglio all'interno delle due sequenze musicali.
Il procedimento si articola nelle seguenti fasi:
1. Vengono selezionate due melodie genitrici.
2. Viene individuato casualmente un punto di taglio.
3. Il primo figlio viene creato combinando la parte iniziale del primo genitore con la parte finale del secondo.
4. Il secondo figlio viene creato combinando la parte iniziale del secondo genitore con la parte finale del primo.
5. Le nuove melodie vengono restituite come risultato dell'operazione.

## Rappresentazione delle melodie:
Ogni melodia è composta da oggetti della classe "Nota".
Ogni nota contiene tre caratteristiche:
- Altezza: identifica la nota musicale.
- Ottava: indica la posizione della nota nell'estensione musicale.
- Durata: rappresenta il tempo di esecuzione della nota.
Durante il crossover vengono trasferite queste caratteristiche dai genitori ai figli.

## Vincoli implementati:
Per garantire la corretta esecuzione dell'operazione, il modulo verifica che:
- Le due melodie abbiano la stessa lunghezza.
- Entrambe contengano almeno 16 note.
- Il punto di taglio sia compreso tra la prima e l'ultima posizione della sequenza.
Questi controlli permettono di mantenere la struttura delle melodie generate.

## Struttura del modulo:
La classe "Crossover" contiene il metodo:
- "incrocia()": riceve due melodie genitrici, esegue il crossover a punto singolo e restituisce due nuovi individui.
Il metodo utilizza la libreria standard "random" per individuare casualmente il punto di taglio.

## Tecnologie utilizzate:
- Python
- Modulo standard "random"
- Classe "Nota" per la rappresentazione delle note.
- Classe "Melodia" per la gestione delle sequenze musicali.
- Modulo "config.py" per il recupero dei vincoli del progetto.

## Integrazione nell'algoritmo genetico:
Il crossover viene eseguito dopo la fase di selezione.
Le melodie selezionate vengono utilizzate come genitori per generare nuovi individui, che potranno successivamente essere sottoposti a mutazione.
I figli potranno quindi essere valutati nuovamente attraverso la funzione di fitness.
L'obiettivo è combinare caratteristiche di melodie differenti per ottenere nuove soluzioni musicali.