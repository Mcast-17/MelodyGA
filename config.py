#===Configurazione progetto===#

#Tonalità musicale: Do maggiore
TONALITA = "Do maggiore"

#Note appartenenti alla scala di Do maggiore
NOTE_SCALA = [
    "Do",
    "Re",
    "Mi",
    "Fa",
    "Sol",
    "La",
    "Si"
]

#Numero minimo di note della melodia
NUMERO_MINIMO_NOTE = 16

#Durate musicali consentite(in valori convenzionali)
DURATE_CONSENTITE = [
    0.25,#Sedicesimo
    0.5,#Ottavo
    1.0,#Quarto
    2.0,#Mezza
    4.0,#Intera
]

#Vincoli musicali
MAX_SALTI_OTTAVA_CONSECUTIVI = 3

#Parametri algoritmo genetico
DIMENSIONE_POPOLAZIONE = 50
NUMERO_GENERAZIONI = 100
PROBABILITA_MUTAZIONE = 0.10
PROBABILITA_CORSSOVER = 0.80

    
