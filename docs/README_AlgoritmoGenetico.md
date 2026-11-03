# 🧬 Algoritmo Genetico

## Descrizione

Il modulo `algoritmo_genetico.py` rappresenta il componente principale del progetto.

Il suo compito è coordinare tutte le fasi dell'algoritmo genetico per generare ed evolvere melodie musicali, con l'obiettivo di individuare soluzioni che ottengano punteggi di fitness sempre più elevati.

Il modulo integra i diversi operatori genetici e gestisce l'intero processo evolutivo, dalla creazione della popolazione iniziale fino all'identificazione della migliore melodia.

---

# Componenti Utilizzati

L'algoritmo genetico integra i seguenti moduli:

| Modulo | Funzione |
|----------|----------|
| `Generatore` | Crea la popolazione iniziale di melodie casuali |
| `Fitness` | Valuta la qualità delle melodie |
| `Selezione` | Individua i genitori tramite selezione a torneo |
| `Crossover` | Combina le caratteristiche dei genitori |
| `Mutazione` | Introduce variazioni casuali nelle melodie |
| `Popolazione` | Gestisce l'insieme degli individui della generazione |

Ogni componente contribuisce all'evoluzione progressiva della popolazione.

---

# Parametri Principali

I parametri dell'algoritmo sono definiti nel file `config.py`.

| Parametro | Valore |
|------------|-----------|
| Dimensione popolazione | 50 |
| Numero di generazioni | 100 |
| Probabilità di crossover | 80% |
| Probabilità di mutazione | 10% |
| Numero minimo di note | 16 |
| Numero massimo di salti consecutivi | 3 |

Questi parametri possono essere modificati per sperimentare comportamenti evolutivi differenti.

---

# Funzionamento

L'algoritmo segue un ciclo evolutivo composto dalle seguenti fasi.

## 1. Generazione della popolazione iniziale

Viene creata una popolazione composta da melodie generate casualmente.

---

## 2. Valutazione della fitness

Ogni melodia viene analizzata dalla funzione di fitness che assegna un punteggio compreso tra 0 e 100.

---

## 3. Individuazione della migliore soluzione

Viene identificata la melodia con il punteggio più elevato della generazione corrente.

---

## 4. Selezione

I genitori vengono scelti tramite il metodo della **Tournament Selection**.

---

## 5. Crossover

Le melodie selezionate vengono combinate per generare nuovi individui.

---

## 6. Mutazione

I figli ottenuti possono subire modifiche casuali nelle loro caratteristiche musicali.

---

## 7. Creazione della nuova popolazione

I nuovi individui sostituiscono progressivamente quelli della generazione precedente.

---

## 8. Elitismo

La migliore melodia individuata viene conservata nella nuova generazione.

---

Il processo viene ripetuto per il numero di generazioni definito nella configurazione.

---

# Schema del Processo Evolutivo

```text
Popolazione Iniziale
          ↓
    Valutazione
          ↓
      Selezione
          ↓
      Crossover
          ↓
      Mutazione
          ↓
 Nuova Popolazione
          ↓
       Elitismo
          ↓
 Generazione Successiva
```

---

# Elitismo

L'algoritmo utilizza una strategia di **elitismo** per conservare la migliore soluzione individuata durante l'evoluzione.

L'individuo con la fitness più elevata viene copiato direttamente nella generazione successiva, evitando che venga perso a causa di crossover o mutazioni.

Per creare copie indipendenti delle melodie viene utilizzata la funzione:

```python
deepcopy()
```

fornita dal modulo standard `copy`.

L'elitismo garantisce che la qualità della migliore soluzione trovata non peggiori nel corso delle generazioni.

---

# Fitness delle Melodie

La valutazione viene effettuata considerando quattro criteri:

| Criterio | Punteggio massimo |
|-----------|-----------|
| Rispetto della tonalità | 35 |
| Ripetizione dei motivi musicali | 25 |
| Gestione dei salti d'ottava | 30 |
| Lunghezza della melodia | 10 |
| **Totale** | **100** |

La fitness guida il processo evolutivo favorendo gli individui più adatti.

---

# Risultato dell'Esecuzione

Al termine dell'esecuzione, l'algoritmo restituisce:

- La migliore melodia individuata.
- Il punteggio di fitness associato.
- La popolazione finale evoluta.

La soluzione ottenuta rappresenta l'individuo che meglio soddisfa i criteri musicali definiti nel progetto.

---

# Tecnologie Utilizzate

- Python 3
- Programmazione Orientata agli Oggetti (OOP)
- Modulo `random`
- Modulo `copy`
- Modulo `collections`
- Algoritmi Genetici
- Euristiche di valutazione musicale

---

# Obiettivo del Modulo

L'obiettivo principale dell'algoritmo genetico è evolvere progressivamente una popolazione di melodie musicali attraverso:

- Selezione degli individui migliori.
- Ricombinazione delle caratteristiche musicali.
- Introduzione di variazioni casuali.
- Conservazione delle soluzioni più promettenti.

Il sistema ricerca automaticamente melodie che rispettino i vincoli musicali e ottengano punteggi di fitness elevati.

---

# Considerazioni Finali

Il modulo `algoritmo_genetico.py` costituisce il cuore del progetto, coordinando tutte le operazioni necessarie all'evoluzione delle melodie.

L'integrazione di selezione, crossover, mutazione, fitness ed elitismo permette di simulare un processo evolutivo capace di migliorare progressivamente la qualità musicale degli individui generati.

Il progetto rappresenta un'applicazione pratica degli algoritmi genetici nel contesto dell'intelligenza artificiale e della generazione procedurale di contenuti musicali.
