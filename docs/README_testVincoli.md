## Verifica dei Vincoli Musicali:Descrizione
Il modulo "test_vincoli.py" esegue una verifica automatica dei vincoli musicali sulle melodie appartenenti alla popolazione finale generata dall'algoritmo genetico.
L'obiettivo è controllare che tutte le melodie rispettino le caratteristiche definite nella configurazione del progetto.

## Controlli effettuati:
Il test verifica cinque aspetti principali.
1. Numero minimo di note -> Ogni melodia deve contenere almeno 16 note.
Il controllo viene effettuato attraverso il metodo "numero_note()" della classe "Melodia".

2. Rispetto della tonalità -> Viene verificato che tutte le note appartengano alla scala di Do maggiore:
- Do
- Re
- Mi
- Fa
- Sol
- La
- Si
Le note appartenenti a tonalità differenti vengono considerate non valide.

3. Durate consentite -> Ogni nota deve utilizzare una delle durate musicali definite nel file "config.py".
Il controllo impedisce la presenza di valori temporali non previsti dalla configurazione.

4. Salti d'ottava consecutivi -> Il test calcola la distanza tra due note consecutive utilizzando i rispettivi valori in semitoni.
Un intervallo pari o superiore a 12 semitoni viene considerato un salto d'ottava.
Viene monitorato il numero di salti consecutivi, verificando che non superi il limite massimo di tre.

5. Dimensione della popolazione -> Al termine dell'esecuzione viene verificato il numero totale di melodie presenti nella popolazione finale.
La dimensione prevista è di 50 individui, secondo i parametri definiti in "config.py".

## Funzionamento:
Il test esegue le seguenti operazioni:
1. Istanzia la classe "AlgoritmoGenetico".
2. Avvia il processo evolutivo.
3. Recupera la popolazione finale.
4. Analizza singolarmente ogni melodia.
5. Registra eventuali violazioni dei vincoli.
6. Mostra un riepilogo dei risultati.
Il metodo "verifica_melodia()" restituisce l'elenco degli eventuali errori individuati durante i controlli.

## Esecuzione:

- Per avviare la verifica, eseguire: python test_vincoli.py
Il programma mostra lo stato di ogni melodia, indicando se è valida oppure se presenta una o più violazioni.

## Risultato della verifica
Durante l'esecuzione di verifica effettuata, il programma ha restituito il seguente risultato:
Descrizione| Risultato
Melodie totali| 50
Melodie valide| 50
Melodie non valide| 0
Tutte le 50 melodie della popolazione finale hanno superato i controlli previsti.

## Obiettivo del modulo
Il modulo consente di verificare automaticamente la conformità delle melodie ai vincoli musicali stabiliti, fornendo un controllo indipendente rispetto al punteggio assegnato dalla funzione di fitness.