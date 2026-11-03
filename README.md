# 🎵 Algoritmo Genetico per la Generazione di Melodie

## Descrizione

Il progetto implementa un algoritmo genetico in Python per la generazione automatica di sequenze musicali.

L'obiettivo è individuare melodie che rispettino determinati vincoli musicali attraverso un processo evolutivo basato su selezione, crossover e mutazione.

Ogni melodia viene valutata mediante una funzione di fitness che assegna un punteggio in base alla qualità dei criteri musicali considerati.

---

## Funzionalità Principali

- Generazione casuale di melodie.
- Rappresentazione musicale tramite oggetti `Nota` e `Melodia`.
- Gestione di una popolazione di individui.
- Valutazione delle melodie mediante funzione di fitness.
- Selezione dei genitori tramite selezione a torneo.
- Crossover a punto singolo.
- Mutazione delle caratteristiche musicali.
- Elitismo per conservare la migliore soluzione.
- Verifica automatica dei vincoli musicali.

---

## Rappresentazione delle Melodie

Ogni nota è caratterizzata da:

- **Altezza**: nome della nota musicale.
- **Ottava**: registro musicale di appartenenza.
- **Durata**: valore temporale della nota.

Una melodia è rappresentata come una sequenza ordinata di oggetti `Nota`.

La tonalità di riferimento è **Do Maggiore**, composta dalle note:

`Do - Re - Mi - Fa - Sol - La - Si`

---

## Vincoli Musicali

Le melodie devono:

- Contenere almeno 16 note.
- Utilizzare esclusivamente note appartenenti alla tonalità di Do maggiore.
- Presentare ripetizioni di motivi musicali.
- Non superare tre salti consecutivi di almeno un'ottava.
- Utilizzare esclusivamente le durate consentite.

---

## Funzione di Fitness

| Criterio | Punteggio Massimo |
|-----------|-----------|
| Rispetto della tonalità | 35 |
| Ripetizione dei motivi musicali | 25 |
| Gestione dei salti d'ottava | 30 |
| Lunghezza della melodia | 10 |
| **Totale** | **100** |

La funzione di fitness utilizza criteri euristici per guidare l'evoluzione verso melodie musicalmente valide.

---

## Funzionamento dell'Algoritmo Genetico

1. Inizializzazione della popolazione.
2. Valutazione della fitness.
3. Selezione mediante torneo.
4. Crossover.
5. Mutazione.
6. Elitismo.
7. Iterazione per il numero di generazioni stabilito.

---

## Configurazione

I parametri principali sono definiti nel file `config.py`.

| Parametro | Valore |
|------------|------------|
| Dimensione popolazione | 50 |
| Numero generazioni | 100 |
| Probabilità crossover | 0.80 |
| Probabilità mutazione | 0.10 |
| Numero minimo di note | 16 |
| Numero massimo di salti consecutivi | 3 |

---

## Struttura del Progetto

```text
MelodyGA/
│
├── config.py
├── nota.py
├── melodia.py
├── popolazione.py
├── generatore.py
├── fitness.py
├── selezione.py
├── crossover.py
├── mutazione.py
├── algoritmo_genetico.py
│
├── test_fitness.py
├── test_selezione.py
├── test_crossover.py
├── test_mutazione.py
├── test_algoritmo_genetico.py
├── test_vincoli.py
│
└── docs/
    ├── README_FITNESS.md
    ├── README_SELEZIONE.md
    ├── README_CROSSOVER.md
    ├── README_MUTAZIONE.md
    ├── README_ALGORITMO.md
    └── README_testVincoli.md
```

---

## Esecuzione

### Avvio dell'algoritmo genetico

```bash
python test_algoritmo_genetico.py
```

### Verifica dei vincoli musicali

```bash
python test_vincoli.py
```

---

## Verifica dei Risultati

Il test dei vincoli controlla:

- Numero minimo di note.
- Rispetto della tonalità.
- Durate consentite.
- Limite dei salti d'ottava consecutivi.
- Dimensione della popolazione finale.

Durante l'esecuzione di verifica tutte le **50 melodie** della popolazione finale hanno superato i controlli previsti.

---

## Tecnologie Utilizzate

- Python 3
- Programmazione Orientata agli Oggetti (OOP)
- Modulo `random`
- Modulo `copy`
- Modulo `collections`

---

## Obiettivi Tecnici

Il progetto consente di approfondire:

- Algoritmi genetici.
- Intelligenza artificiale.
- Rappresentazione degli individui.
- Progettazione di funzioni di fitness.
- Implementazione di operatori genetici.
- Gestione dell'evoluzione di una popolazione artificiale.

---
