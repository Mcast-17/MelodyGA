# 🔀 Modulo Crossover

## Descrizione

Il modulo `crossover.py` implementa l'operatore genetico di **crossover**, una delle componenti fondamentali degli algoritmi genetici.

Il suo obiettivo è combinare le caratteristiche di due individui della popolazione, chiamati **genitori**, per generare nuove soluzioni, chiamate **figli** o **discendenti**.

Nel progetto, ogni individuo è rappresentato da una melodia composta da una sequenza ordinata di note musicali. Il crossover consente di creare nuove melodie combinando porzioni delle melodie dei genitori.

---

# Metodo Utilizzato: Single-Point Crossover

Il progetto utilizza la tecnica del **crossover a punto singolo** (*Single-Point Crossover*).

Questo metodo prevede la scelta casuale di un punto di taglio all'interno delle due melodie genitrici.

## Procedura

1. Vengono selezionate due melodie genitrici.
2. Viene individuato casualmente un punto di taglio.
3. Il primo figlio viene creato combinando:
   - la parte iniziale del primo genitore;
   - la parte finale del secondo genitore.
4. Il secondo figlio viene creato combinando:
   - la parte iniziale del secondo genitore;
   - la parte finale del primo genitore.
5. Le nuove melodie vengono restituite come risultato dell'operazione.

---

# Esempio

## Genitore 1

```text
Do Re Mi | Fa Sol La Si
```

## Genitore 2

```text
La Sol Fa | Mi Re Do Si
```

## Punto di taglio

```text
           ↑
```

## Figlio 1

```text
Do Re Mi | Mi Re Do Si
```

## Figlio 2

```text
La Sol Fa | Fa Sol La Si
```

In questo modo i figli ereditano caratteristiche da entrambi i genitori.

---

# Rappresentazione delle Melodie

Ogni melodia è composta da oggetti della classe `Nota`.

Ogni nota possiede tre proprietà fondamentali:

- **Altezza**: identifica la nota musicale.
- **Ottava**: indica il registro musicale della nota.
- **Durata**: rappresenta il tempo di esecuzione della nota.

Durante il crossover queste informazioni vengono trasferite dai genitori ai nuovi individui.

---

# Vincoli Implementati

Per garantire la corretta esecuzione dell'operazione, il modulo verifica che:

- Le due melodie abbiano la stessa lunghezza.
- Entrambe contengano almeno 16 note.
- Il punto di taglio sia compreso tra il primo e l'ultimo elemento della sequenza.

Questi controlli consentono di mantenere la coerenza strutturale delle melodie generate.

---

# Struttura del Modulo

La classe `Crossover` mette a disposizione il seguente metodo:

### `incrocia()`

Riceve due melodie genitrici, esegue il crossover a punto singolo e restituisce due nuove melodie figlie.

Il metodo utilizza il modulo standard `random` per determinare casualmente il punto di taglio.

---

# Parametri Coinvolti

L'operazione utilizza:

- Primo genitore.
- Secondo genitore.
- Punto di crossover.
- Lunghezza delle melodie.
- Vincoli definiti nel file `config.py`.

---

# Tecnologie Utilizzate

- Python 3
- Modulo standard `random`
- Classe `Nota`
- Classe `Melodia`
- File di configurazione `config.py`

---

# Integrazione nell'Algoritmo Genetico

Il crossover viene eseguito immediatamente dopo la fase di selezione.

Il flusso generale dell'algoritmo è il seguente:

```text
Selezione
      ↓
Crossover
      ↓
Mutazione
      ↓
Valutazione Fitness
```

Le melodie selezionate come genitori vengono combinate per generare nuovi individui che successivamente possono essere sottoposti a mutazione.

Una volta modificati, i figli vengono valutati nuovamente tramite la funzione di fitness.

---

# Ruolo nel Processo Evolutivo

Il crossover svolge un ruolo fondamentale perché:

- Combina le caratteristiche di individui differenti.
- Favorisce la produzione di nuove soluzioni.
- Incrementa la variabilità della popolazione.
- Permette la trasmissione dei tratti migliori alle generazioni successive.
- Contribuisce alla ricerca di melodie con fitness più elevata.

Senza crossover, l'evoluzione sarebbe limitata alle sole modifiche introdotte dalla mutazione.

---

# Obiettivo del Modulo

L'obiettivo principale è generare nuove melodie combinando caratteristiche provenienti da individui differenti.

Attraverso il crossover, l'algoritmo può:

- Riutilizzare sequenze musicali promettenti.
- Creare nuove combinazioni di note.
- Esplorare regioni diverse dello spazio delle soluzioni.
- Migliorare progressivamente la qualità della popolazione.

---

# Considerazioni Finali

Il crossover rappresenta il principale meccanismo di ricombinazione genetica dell'algoritmo.

Nel contesto della generazione automatica di melodie, consente di unire frammenti musicali provenienti da individui diversi per produrre nuove sequenze potenzialmente più efficaci rispetto ai genitori.

Combinato con selezione, mutazione ed elitismo, contribuisce all'evoluzione della popolazione verso melodie che soddisfano sempre meglio i criteri musicali definiti dal progetto.
