def nome_singolo(filename):
    f = open("prestito.csv", "r")
    output = open(filename, "w")
    lista = []
    for line in f:
        if " " not in line:
            lista.append(line)
    for elem in lista:
        riga = elem.split(";")
        somma = int(riga[2])
        somma = somma + (somma * 10 / 100)
        riga[2] = str(somma)
        output.write(";".join(riga) + '\n')
    f.close()
    output.close()


def nome_doppio(filename):
    f = open("prestito.csv", "r")
    output = open(filename, "w")
    lista = []
    for line in f:
        if " " in line:
            lista.append(line)
    for elem in lista:
        riga = elem.split(";")
        somma = int(riga[2])
        somma = somma + (somma * 20 / 100)
        riga[2] = str(somma)
        output.write(";".join(riga) + '\n')
    f.close()
    output.close()