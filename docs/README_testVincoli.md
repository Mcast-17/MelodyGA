# ✅ Verifica dei Vincoli Musicali

## Descrizione

Il modulo `test_vincoli.py` esegue una verifica automatica dei vincoli musicali sulle melodie appartenenti alla popolazione finale generata dall'algoritmo genetico.

L'obiettivo del test è controllare che tutte le melodie rispettino i requisiti definiti nella configurazione del progetto, fornendo una validazione indipendente rispetto al punteggio assegnato dalla funzione di fitness.

---

# Controlli Effettuati

Il test verifica cinque aspetti fondamentali.

## 1. Numero Minimo di Note

Ogni melodia deve contenere almeno **16 note**.

Il controllo viene effettuato mediante il metodo `numero_note()` della classe `Melodia`.

**Vincolo:**

```text
Numero di note ≥ 16
```

---

## 2. Rispetto della Tonalità

Il test verifica che tutte le note appartengano alla tonalità di **Do Maggiore**.

Le note consentite sono:

```text
Do - Re - Mi - Fa - Sol - La - Si
```

Eventuali note esterne alla scala vengono considerate non valide.

---

## 3. Durate Consentite

Ogni nota deve utilizzare esclusivamente le durate musicali definite nel file `config.py`.

Questo controllo impedisce la presenza di valori temporali non previsti dalla configurazione del sistema.

---

## 4. Salti d'Ottava Consecutivi

Il test calcola la distanza tra note consecutive convertendole in valori espressi in semitoni.

Un intervallo pari o superiore a **12 semitoni** viene considerato un salto d'ottava.

Per ogni melodia viene verificato che il numero di salti consecutivi non superi il limite massimo consentito.

**Vincolo:**

```text
Massimo 3 salti d'ottava consecutivi
```

---

## 5. Dimensione della Popolazione

Al termine dell'esecuzione viene verificato il numero totale di individui presenti nella popolazione finale.

Secondo la configurazione del progetto, la popolazione deve contenere:

```text
50 melodie
```

Valore definito nel file `config.py`.

---

# Funzionamento

Il test esegue automaticamente le seguenti operazioni:

1. Istanzia la classe `AlgoritmoGenetico`.
2. Avvia il processo evolutivo.
3. Recupera la popolazione finale generata.
4. Analizza ogni melodia singolarmente.
5. Registra eventuali violazioni dei vincoli.
6. Mostra un riepilogo finale dei risultati.

Il metodo `verifica_melodia()` restituisce l'elenco degli eventuali errori rilevati durante i controlli.

---

# Esecuzione

Per avviare la verifica eseguire:

```bash
python test_vincoli.py
```

Durante l'esecuzione il programma indica per ogni melodia:

- Stato della verifica.
- Eventuali violazioni riscontrate.
- Esito finale del controllo.

---

# Risultato della Verifica

L'esecuzione effettuata sul progetto ha prodotto il seguente risultato:

| Descrizione | Risultato |
|------------|-----------|
| Melodie totali | 50 |
| Melodie valide | 50 |
| Melodie non valide | 0 |

✅ Tutte le melodie della popolazione finale hanno superato i controlli previsti.

---

# Obiettivo del Modulo

Il modulo fornisce un meccanismo di validazione automatica delle melodie generate dall'algoritmo genetico.

In particolare consente di:

- Verificare il rispetto dei vincoli musicali.
- Individuare eventuali errori nella generazione delle melodie.
- Confermare la correttezza della popolazione finale.
- Garantire la conformità delle soluzioni prodotte ai requisiti del progetto.

---

# Considerazioni Finali

La funzione di fitness guida l'evoluzione delle melodie assegnando un punteggio a ciascun individuo, mentre il modulo `test_vincoli.py` svolge un ruolo di verifica indipendente.

L'utilizzo combinato di fitness e controlli automatici garantisce che le melodie finali non solo ottengano un buon punteggio evolutivo, ma rispettino anche tutti i requisiti musicali definiti dal progetto.
