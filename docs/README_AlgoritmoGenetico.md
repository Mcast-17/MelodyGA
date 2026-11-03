## Algoritmo Genetico

## Descrizione:
Il modulo "algoritmo_genetico.py" rappresenta il componente principale del progetto. Coordina tutti gli elementi dell'algoritmo genetico per generare ed evolvere melodie musicali, cercando di ottenere individui con un punteggio di fitness elevato.

## Componenti utilizzati:
L'algoritmo integra i seguenti moduli:
- Generatore: crea la popolazione iniziale di melodie casuali.
- Fitness: valuta la qualità delle melodie secondo i criteri stabiliti.
- Selezione: sceglie i genitori attraverso la selezione a torneo.
- Crossover: combina le caratteristiche di due melodie per generare nuovi individui.
- Mutazione: introduce variazioni casuali nelle note.
- Popolazione: gestisce l'insieme delle melodie appartenenti a una generazione.

## Parametri:
I parametri principali vengono importati dal modulo "config.py":
- Dimensione della popolazione: 50 individui.
- Numero di generazioni: 100.
- Probabilità di crossover: 80%.
- Probabilità di mutazione: 10% per ogni nota.

## Funzionamento:
L'algoritmo segue queste fasi:
1. Generazione della popolazione iniziale.
2. Valutazione della fitness di ogni melodia.
3. Individuazione della migliore melodia.
4. Selezione dei genitori mediante torneo.
5. Applicazione del crossover con la probabilità stabilita.
6. Applicazione della mutazione ai figli.
7. Creazione della nuova popolazione.
8. Conservazione del miglior individuo attraverso l'elitismo.
Il processo viene ripetuto per il numero di generazioni configurato.

## Elitismo:
L'algoritmo utilizza una strategia di elitismo per conservare una copia della migliore melodia trovata.
In questo modo, l'individuo con il punteggio più alto non viene perso durante le successive operazioni genetiche.
Per creare copie indipendenti degli individui viene utilizzato "deepcopy" del modulo "copy".

## Risultato:
Al termine dell'esecuzione, l'algoritmo restituisce la migliore melodia individuata e il relativo punteggio di fitness.
Il modulo permette di integrare le diverse operazioni genetiche in un unico processo evolutivo.