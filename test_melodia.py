from nota import Nota
from melodia import Melodia

melodia = Melodia()

melodia.aggiungi_nota(Nota("Do", 4, 1.0))
melodia.aggiungi_nota(Nota("Mi", 4, 0.5))
melodia.aggiungi_nota(Nota("Sol", 4, 1.0))
melodia.aggiungi_nota(Nota("Do", 5, 2.0))

print("La nostra melodia:")
melodia.visualizza()

print("\nNumero di note:", melodia.numero_note())
print("Durata totale:", melodia.durata_totale())
