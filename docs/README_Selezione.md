# 🏆 Modulo Selezione

## Descrizione

Il modulo `selezione.py` implementa il meccanismo di selezione degli individui all'interno dell'algoritmo genetico.

Il suo compito è individuare le melodie con i punteggi di fitness più elevati affinché possano essere utilizzate come genitori per la generazione successiva.

La selezione favorisce le soluzioni che rispettano maggiormente i criteri musicali definiti dal progetto, aumentando la probabilità che tali caratteristiche vengano mantenute e migliorate nel corso dell'evoluzione.

---

# Metodo Utilizzato: Tournament Selection

Il progetto adotta la tecnica della **selezione a torneo (Tournament Selection)**.

Questo metodo prevede il confronto tra un gruppo di individui scelti casualmente dalla popolazione, selezionando come vincitore l'individuo con la fitness più elevata.

## Procedura

1. Vengono estratte casualmente alcune melodie dalla popolazione.
2. Per ogni melodia viene calcolato il punteggio di fitness.
3. I punteggi vengono confrontati.
4. La melodia con il punteggio più elevato viene dichiarata vincitrice del torneo.
5. Il procedimento viene ripetuto fino a ottenere il numero di genitori necessario.

---

# Funzionamento

La selezione utilizza la funzione di fitness implementata nel modulo `fitness.py`.

Ogni individuo viene valutato sulla base dei criteri musicali definiti dal progetto:

- Rispetto della tonalità.
- Ripetizione equilibrata dei motivi musicali.
- Controllo dei salti d'ottava consecutivi.
- Rispetto della lunghezza minima della melodia.

La melodia con il punteggio più elevato all'interno del torneo viene scelta come genitore.

---

# Parametri Principali

Il metodo utilizza i seguenti elementi:

- **Popolazione**: insieme delle melodie candidate.
- **Dimensione del torneo**: numero di melodie confrontate durante ogni selezione.
- **Fitness**: punteggio assegnato a ciascun individuo.

La dimensione del torneo influenza direttamente la pressione selettiva dell'algoritmo.

| Dimensione torneo | Effetto |
|------------------|----------|
| Piccola | Maggiore diversità genetica |
| Grande | Maggiore pressione verso gli individui migliori |

Aumentando il numero dei partecipanti al torneo cresce la probabilità che vengano selezionate le melodie con fitness elevata.

---

# Vantaggi del Metodo

La selezione a torneo presenta numerosi vantaggi:

- Facile da implementare.
- Non richiede la normalizzazione dei punteggi di fitness.
- Consente il confronto diretto tra individui.
- Permette di controllare la pressione selettiva.
- Mantiene una buona varietà genetica all'interno della popolazione.

Per questi motivi rappresenta una delle tecniche di selezione più utilizzate negli algoritmi genetici.

---

# Integrazione nell'Algoritmo Genetico

La selezione costituisce una fase fondamentale del ciclo evolutivo.

Gli individui selezionati vengono utilizzati nelle successive operazioni genetiche:

## Crossover

Combinazione di porzioni di due melodie per generare nuovi individui.

## Mutazione

Modifica casuale di alcune caratteristiche musicali, come:

- Altezza delle note.
- Ottava.
- Durata.

Queste operazioni consentono di introdurre nuove combinazioni genetiche e aumentare l'esplorazione dello spazio delle soluzioni.

---

# Ruolo nel Processo Evolutivo

All'interno dell'algoritmo genetico la selezione svolge il compito di:

- Favorire gli individui migliori.
- Trasmettere le caratteristiche desiderabili alle generazioni successive.
- Ridurre progressivamente la presenza di soluzioni meno efficaci.
- Guidare l'evoluzione verso melodie che soddisfano i criteri musicali stabiliti.

L'efficacia della selezione influisce direttamente sulla velocità di convergenza dell'algoritmo e sulla qualità delle melodie generate.

---

# Considerazioni Finali

La selezione a torneo rappresenta un compromesso efficace tra semplicità e prestazioni.

Grazie alla sua flessibilità e alla capacità di premiare gli individui più adatti senza eliminare completamente la diversità genetica, costituisce una scelta particolarmente adatta per il problema della generazione automatica di melodie tramite algoritmi genetici.
