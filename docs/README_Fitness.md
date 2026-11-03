## Modulo Fitness: Descrizione
Il modulo "fitness.py" implementa la funzione di fitness utilizzata dall'algoritmo genetico per valutare la qualità delle melodie generate.
Ogni melodia riceve un punteggio complessivo compreso tra 0 e 100, determinato attraverso quattro criteri musicali: rispetto della tonalità, ripetizione dei motivi, gestione dei salti d'ottava e lunghezza della sequenza.

## Criteri di valutazione
La funzione di fitness utilizza i seguenti criteri:
Criterio| Punteggio massimo
Rispetto della tonalità| 35
Ripetizione dei motivi musicali| 25
Gestione dei salti d'ottava| 30
Lunghezza della melodia| 10
Totale| 100

1. Valutazione della tonalità -> Il metodo "valuta_tonalita()" verifica che tutte le note appartengano alla scala di Do maggiore.
Le note ammesse sono:Do, Re, Mi, Fa, Sol, La, Si.
Il punteggio viene calcolato in proporzione al numero di note appartenenti alla scala, fino a un massimo di 35 punti.

2. Valutazione delle ripetizioni -> Il metodo "valuta_ripetizione()" analizza la presenza di motivi musicali ripetuti.
Un motivo è rappresentato da una sequenza di tre note consecutive. L'analisi considera le altezze delle note, senza distinguere ottava e durata.
Attraverso la classe "Counter" del modulo "collections", vengono individuate le sequenze ricorrenti.
Il punteggio dipende dalla percentuale di motivi ripetuti:
Percentuale di ripetizione| Punteggio
Nessuna ripetizione| 0
Fino al 10%| 25
Fino al 25%| 20
Fino al 40%| 15
Fino al 60%| 8
Oltre il 60%| 0
L'obiettivo è favorire una certa ripetitività melodica senza rendere la sequenza eccessivamente monotona.

3. Valutazione dei salti d'ottava -> Il metodo "valuta_salti_ottava()" analizza gli intervalli tra note consecutive.
Per effettuare il calcolo, ogni nota viene convertita in un valore numerico espresso in semitoni, considerando sia l'altezza sia l'ottava.
Un intervallo pari o superiore a 12 semitoni viene considerato un salto d'ottava.
Il metodo verifica il numero totale di salti e il numero massimo di salti consecutivi.
Condizione| Punteggio
Nessun salto d'ottava| 30
Da 1 a 3 salti| 25
Da 4 a 6 salti| 20
Oltre 6 salti| 15
Più di 3 salti consecutivi| 0
Il superamento del limite di tre salti consecutivi comporta l'azzeramento del punteggio relativo a questo criterio.

4. Valutazione della lunghezza -> Il metodo "valuta_lunghezza()" verifica che la melodia contenga almeno 16 note.
- Almeno 16 note: 10 punti.
- Meno di 16 note: 0 punti.

## Calcolo della fitness complessiva:
Il metodo "calcola_fitness()" somma i punteggi ottenuti nei quattro criteri e restituisce il risultato complessivo.
La formula utilizzata è:
fitness = (
    punteggio_tonalita
    + punteggio_ripetizione
    + punteggio_salti_ottava
    + punteggio_lunghezza
)
Il risultato viene arrotondato a due cifre decimali.
Utilizzo nell'algoritmo genetico
La funzione di fitness viene utilizzata durante il processo evolutivo per:
- Confrontare le melodie appartenenti alla popolazione.
- Selezionare gli individui con i punteggi migliori.
- Individuare la migliore melodia di ogni generazione.
- Conservare la soluzione migliore attraverso il meccanismo di elitismo.
Una fitness più elevata indica una maggiore corrispondenza ai criteri musicali definiti.

## Considerazioni:
La funzione di fitness utilizza criteri euristici per valutare le caratteristiche delle melodie. Il punteggio non rappresenta una misura oggettiva della qualità musicale, ma permette di guidare il processo evolutivo verso soluzioni che rispettano le caratteristiche desiderate.
I vincoli musicali vengono inoltre verificati attraverso il test automatico dedicato "test_vincoli.py".