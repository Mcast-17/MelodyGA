from nota import Nota
from melodia import Melodia
from popolazione import Popolazione


# Creazione della popolazione
popolazione = Popolazione()

# Prima melodia
melodia1 = Melodia()
melodia1.aggiungi_nota(Nota("Do", 4, 1.0))
melodia1.aggiungi_nota(Nota("Mi", 4, 1.0))
melodia1.aggiungi_nota(Nota("Sol", 4, 1.0))

# Seconda melodia
melodia2 = Melodia()
melodia2.aggiungi_nota(Nota("Fa", 4, 1.0))
melodia2.aggiungi_nota(Nota("La", 4, 1.0))
melodia2.aggiungi_nota(Nota("Do", 5, 1.0))

# Inserimento nella popolazione
popolazione.aggiungi_melodia(melodia1)
popolazione.aggiungi_melodia(melodia2)

# Visualizzazione
print("===== POPOLAZIONE =====")

popolazione.visualizza()

print("Numero di melodie:", popolazione.numero_melodie())
