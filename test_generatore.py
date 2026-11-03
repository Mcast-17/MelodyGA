from generatore import Generatore


generatore = Generatore()
melodia = generatore.genera_melodia()

print("===== MELODIA GENERATA =====")
melodia.visualizza()
print("\nNumero di note:",melodia.numero_note())
print("Durata totale:",melodia.durata_totale())

print("=====FINE TEST====")

