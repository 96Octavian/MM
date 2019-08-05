# prestito.csv è un file con nome e cognome e la somma in denaro ricevuta
# Crea un modulo con due funzioni:
#  - la prima crea un file con le persone che hanno un solo nome, e la somma è aumentata del 10%
#  - la seconda crea un file cone le persone che hanno due nomi e la somma è aumentata del 20%
# Il file principale chiama entrambe le funzioni, poi stampa a schermo
# la somma del denaro del primo file e la somma del denaro del secondo
def aumenta(n):
    h = n * 10 / 100
    n = n + h
    return n


def aumenta2(n):
    h = n * 20 / 100
    n = n + h
    return n


def aumenta3(n, percentuale):
    h = n * percentuale / 100
    n = n + h
    return n


def sommapercentuale():


try:
    f = open("prestito.csv", "r")
    w = open("singolo", "w")
    g = open("duenomi", "w")
except:
    Print ("file non trovato")
    return None

    for a in f:
        e = a.split(";")
        d = e[0].split(" ")
        if len(d) < 2:
            e[2] = aumenta(e[2])
            try:
                w.write(e[2])
            except:
                print("non sono riuscito a scriverlo")
        else:
            e[2] = aumenta2(e[2])
            try:
                g.write(e[2])
            except:
                print("non sono riuscito a scriverlo")
    f.close()
    w.close()
    g.close()



def creafile(nomefile):
    i = "2"
    while i != "0":
        a = input("nome?")
        b = input ("citta?")
        c = input ("cognome?")
        n = " nome: " + a + " cognome: " + b + "città: " + c
        scrivofile (nomefile , n)

        i = input("vuoi continuare?")

def scrivofile(file, n):
    f = open (file,"a")
    f.write(n)
    f.close()
    return

def contarighe(nomefile):
    f = open(nomefile, "r")
    d = 0
    for i in f:
        d = d + 1
    return d























# Esempio:
#
# prestito.csv
#   Luca;Rossi;100
#   Maria Antonietta;Spadorcia;100
#
# modulo.py
#   nome_singolo(filename):
#     apri prestito.csv
#     scrivi sul file chiamato filename quelli che hanno un solo nome
#     Risultato: Luca;Rossi;110
#
#   nome_doppio(altro_filename):
#     apri prestito.csv
#     scrivi sul file chiamato altro_filename quelli che hanno due nomi
#     Risultato: Maria Antonietta;Spadorcia;120
#
# Compito.py
# import modulo.py
# chiama nome_singolo(nome1) e stampa la somma del file nome1
# chiama nome_doppio(nome2) e stampa la somma del file nome2
# stampa la somma di entrambi












