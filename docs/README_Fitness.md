# 🎯 Modulo Fitness

## Descrizione

Il modulo `fitness.py` implementa la funzione di fitness utilizzata dall'algoritmo genetico per valutare la qualità delle melodie generate.

Ogni melodia riceve un punteggio complessivo compreso tra **0 e 100**, determinato attraverso quattro criteri musicali:

- Rispetto della tonalità
- Ripetizione dei motivi musicali
- Gestione dei salti d'ottava
- Lunghezza della melodia

La fitness consente di confrontare gli individui della popolazione e guidare il processo evolutivo verso soluzioni musicalmente più valide.

---

# Criteri di Valutazione

| Criterio | Punteggio Massimo |
|-----------|-----------|
| Rispetto della tonalità | 35 |
| Ripetizione dei motivi musicali | 25 |
| Gestione dei salti d'ottava | 30 |
| Lunghezza della melodia | 10 |
| **Totale** | **100** |

---

# 1. Valutazione della Tonalità

Il metodo `valuta_tonalita()` verifica che tutte le note appartengano alla scala di **Do Maggiore**.

Le note consentite sono:

```text
Do - Re - Mi - Fa - Sol - La - Si
```

Il punteggio viene assegnato in proporzione al numero di note corrette presenti nella melodia, fino a un massimo di **35 punti**.

---

# 2. Valutazione delle Ripetizioni

Il metodo `valuta_ripetizione()` analizza la presenza di motivi musicali ricorrenti.

Un motivo musicale è definito come una sequenza di **tre note consecutive**.

L'analisi considera esclusivamente l'altezza delle note, ignorando:

- Ottava
- Durata

Per individuare le sequenze ripetute viene utilizzata la classe `Counter` del modulo `collections`.

## Sistema di punteggio

| Percentuale di ripetizione | Punteggio |
|---------------------------|-----------|
| Nessuna ripetizione | 0 |
| Fino al 10% | 25 |
| Fino al 25% | 20 |
| Fino al 40% | 15 |
| Fino al 60% | 8 |
| Oltre il 60% | 0 |

L'obiettivo è favorire una moderata ripetitività melodica senza produrre sequenze eccessivamente monotone.

---

# 3. Valutazione dei Salti d'Ottava

Il metodo `valuta_salti_ottava()` analizza gli intervalli tra note consecutive.

Per ogni nota viene calcolato un valore numerico espresso in semitoni, considerando:

- Altezza
- Ottava

Un intervallo pari o superiore a **12 semitoni** viene considerato un salto d'ottava.

Il metodo verifica:

- Numero totale di salti d'ottava.
- Numero massimo di salti consecutivi.

## Sistema di punteggio

| Condizione | Punteggio |
|------------|-----------|
| Nessun salto d'ottava | 30 |
| Da 1 a 3 salti | 25 |
| Da 4 a 6 salti | 20 |
| Oltre 6 salti | 15 |
| Più di 3 salti consecutivi | 0 |

Il superamento del limite di **tre salti consecutivi** comporta l'azzeramento del punteggio relativo a questo criterio.

---

# 4. Valutazione della Lunghezza

Il metodo `valuta_lunghezza()` verifica che la melodia contenga almeno **16 note**.

| Lunghezza melodia | Punteggio |
|-------------------|-----------|
| Almeno 16 note | 10 |
| Meno di 16 note | 0 |

---

# Calcolo della Fitness Complessiva

Il metodo `calcola_fitness()` somma i punteggi ottenuti nei quattro criteri di valutazione.

```python
fitness = (
    punteggio_tonalita
    + punteggio_ripetizione
    + punteggio_salti_ottava
    + punteggio_lunghezza
)
```

Il risultato finale viene arrotondato a due cifre decimali.

---

# Utilizzo nell'Algoritmo Genetico

La funzione di fitness viene utilizzata per:

- Confrontare le melodie della popolazione.
- Selezionare gli individui migliori.
- Individuare la migliore soluzione di ogni generazione.
- Applicare il meccanismo di elitismo.
- Guidare l'evoluzione verso melodie che rispettano i criteri musicali definiti.

In generale, una fitness più elevata indica una maggiore aderenza agli obiettivi del progetto.

---

# Considerazioni Finali

La funzione di fitness utilizza criteri euristici per valutare le caratteristiche di una melodia.

Il punteggio ottenuto non rappresenta una misura assoluta della qualità musicale, ma costituisce uno strumento efficace per orientare l'algoritmo genetico durante il processo evolutivo.

Il rispetto dei vincoli musicali viene inoltre verificato attraverso il test automatico:

```bash
python test_vincoli.py
```

Questo controllo garantisce che le melodie prodotte soddisfino tutti i requisiti progettuali definiti.
