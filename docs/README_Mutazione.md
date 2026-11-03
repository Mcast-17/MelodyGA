# 🔄 Modulo Mutazione

## Descrizione

Il modulo `mutazione.py` implementa l'operatore genetico di **mutazione** utilizzato dall'algoritmo genetico.

La mutazione introduce modifiche casuali nelle caratteristiche delle note musicali che compongono una melodia, contribuendo a mantenere la diversità genetica della popolazione.

Questo meccanismo consente all'algoritmo di esplorare nuove soluzioni musicali e riduce il rischio di convergere prematuramente verso soluzioni subottimali.

---

# Funzionamento

Il modulo analizza tutte le note presenti in una melodia.

Per ogni nota viene generato un valore casuale che viene confrontato con la probabilità di mutazione definita nel file `config.py`.

Se la condizione viene soddisfatta, viene scelta casualmente una caratteristica della nota da modificare.

Il processo viene ripetuto indipendentemente per ogni nota della melodia.

---

# Caratteristiche Modificabili

La mutazione può intervenire su tre proprietà della classe `Nota`.

## Altezza

Viene selezionata una nuova nota appartenente alla scala musicale definita nel progetto.

Esempio:

```text
Do → Sol
Mi → La
```

---

## Ottava

Viene assegnata casualmente una nuova ottava compresa tra:

```text
3 - 5
```

Esempio:

```text
Ottava 3 → Ottava 5
```

---

## Durata

Viene selezionata una nuova durata tra quelle consentite dalla configurazione.

Esempio:

```text
1/4 → 1/2
1/8 → 1/4
```

---

# Probabilità di Mutazione

La probabilità di mutazione è definita nel file `config.py`.

```python
PROBABILITA_MUTAZIONE = 0.10
```

Ciò significa che ogni nota ha una probabilità del **10%** di essere selezionata per una modifica.

La probabilità viene applicata in modo indipendente a ciascuna nota della melodia.

---

# Struttura del Modulo

La classe `Mutazione` mette a disposizione il seguente metodo:

### `muta()`

Analizza tutte le note della melodia e applica eventuali modifiche casuali alle loro caratteristiche.

Il metodo:

- Riceve una melodia come parametro.
- Modifica direttamente l'oggetto ricevuto.
- Restituisce la melodia aggiornata.

---

# Parametri Coinvolti

Il processo di mutazione utilizza:

- La melodia da modificare.
- La probabilità di mutazione.
- Le note ammesse dalla scala musicale.
- Le ottave consentite.
- Le durate consentite.

Tali informazioni vengono recuperate dal file `config.py`.

---

# Tecnologie Utilizzate

- Python 3
- Modulo standard `random`
- Classe `Nota`
- Classe `Melodia`
- File di configurazione `config.py`

---

# Integrazione nell'Algoritmo Genetico

La mutazione viene applicata ai nuovi individui generati dalla fase di crossover.

Il ciclo generale è il seguente:

```text
Selezione
      ↓
Crossover
      ↓
Mutazione
      ↓
Valutazione Fitness
```

Dopo la mutazione, le nuove melodie vengono rivalutate attraverso la funzione di fitness per determinarne la qualità.

---

# Ruolo nel Processo Evolutivo

La mutazione svolge un ruolo fondamentale all'interno dell'algoritmo genetico:

- Introduce nuove caratteristiche nella popolazione.
- Aumenta la diversità genetica.
- Riduce il rischio di convergenza prematura.
- Favorisce l'esplorazione di nuove combinazioni musicali.
- Permette di scoprire soluzioni potenzialmente migliori.

Senza la mutazione la popolazione tenderebbe a diventare troppo simile nel corso delle generazioni, limitando la capacità di ricerca dell'algoritmo.

---

# Obiettivo del Modulo

L'obiettivo principale della mutazione è introdurre variabilità nelle melodie generate.

Attraverso modifiche casuali di:

- Altezza delle note
- Ottava
- Durata

l'algoritmo può esplorare nuove combinazioni musicali e migliorare progressivamente la qualità delle soluzioni prodotte.

---

# Considerazioni Finali

La mutazione rappresenta uno degli operatori fondamentali degli algoritmi genetici.

Nel contesto della generazione automatica di melodie, essa permette di creare nuove varianti musicali mantenendo il rispetto dei vincoli definiti dal progetto.

Combinata con selezione, crossover ed elitismo, contribuisce all'evoluzione della popolazione verso melodie sempre più aderenti ai criteri musicali stabiliti.
