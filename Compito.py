# prestito.csv è un file con nome e cognome e la somma in denaro ricevuta
# Crea un modulo con due funzioni:
#  - la prima crea un file con le persone che hanno un solo nome, e la somma è aumentata del 10%
#  - la seconda crea un file cone le persone che hanno due nomi e la somma è aumentata del 20%
# Il file principale chiama entrambe le funzioni, poi stampa a schermo
# la somma del denaro del primo file e la somma del denaro del secondo

# Esempio:
#
# prestito.csv
#   Luca;Rossi;100
#   Maria Antonietta;Spadorcia;100
#
# modulo.py
#   nome_singolo(filename):
#     apri prestiti.txt
#     scrivi sul file chiamato filename quelli che hanno un solo nome
#     Risultato: Luca;Rossi;110
#
#   nome_doppio(altro_filename):
#     apri prestiti.txt
#     scrivi sul file chiamato altro_filename quelli che hanno due nomi
#     Risultato: Maria Antonietta;Spadorcia;120
#
# Compito.py
# import modulo.py
# chiama nome_singolo(nome1) e stampa la somma del file nome1
# chiama nome_doppio(nome2) e stampa la somma del file nome2
# stampa la somma di entrambi